#!/usr/bin/env python3
"""Génère les voix (audio/*.mp3) et js/data/audio.js avec le modèle Supertonic 3 (sherpa-onnx).

Prérequis :
  pip install sherpa-onnx soundfile numpy num2words
  ffmpeg (encodage MP3)
  Modèle Supertonic 3 converti pour sherpa-onnx, dans un dossier contenant :
  duration_predictor.onnx, text_encoder.onnx, vector_estimator.onnx, vocoder.onnx,
  tts.json, unicode_indexer.bin, voice.bin

Usage : python3 tools/build_audio.py --model chemin/vers/le/modele [--only-missing]
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "audio")
MANIFEST = os.path.join(ROOT, "js", "data", "audio.js")

# Genre des personnages des dialogues (pour choisir une voix féminine ou masculine).
FEMALE = {"Lupita", "Ana", "Claire", "Marie", "Rosa", "Vendedora", "Julia", "Señora", "Recepcionista", "Emma", "Karla",
          "Doctora", "Inés", "Léa", "Chloé", "Abuela", "Sarah", "Licenciada", "Casera", "Nina", "Margaux", "Camille",
          "Lisa", "Andrea", "Valeria", "Élodie", "Manon", "Maestra", "Mariana", "Pauline", "Regina", "Juliette", "Inès"}

# Phrases lues ailleurs dans l'app (réglages).
EXTRA_TEXTS = ["¡Órale! ¿Qué onda?", "Hola, ¿cómo estás? Bienvenido a México.", "¡Hola! ¿Cómo estás?"]


def load_export(name):
    """Lit un « export const NAME = … ; » de js/data/content.js (JSON)."""
    src = open(os.path.join(ROOT, "js", "data", "content.js"), encoding="utf-8").read()
    body = src.split(f"export const {name} = ", 1)[1]
    return json.loads(body.split(";\n\nexport const ", 1)[0].rstrip().rstrip(";"))


def load_content():
    return load_export("THEMES")


def quiz_sentence(q):
    """Même calcul que grammarQuiz() dans js/exercises.js."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", q["prompt"].replace("___", q["answer"], 1))


def collect(themes):
    """Renvoie [(texte, genre_voix, rang_voix)] : rang = 0 voix principale, 1 seconde voix du même genre."""
    clips = {}
    for t in themes:
        for item in t["items"]:
            if item["kind"] in ("word", "phrase"):
                clips.setdefault(item["es"], ("F", 0))
            elif item["kind"] == "grammar":
                for ex in item["examples"]:
                    clips.setdefault(ex["es"], ("F", 0))
                clips.setdefault(quiz_sentence(item["quiz"]), ("F", 0))
            else:
                seen = {}
                for line in item["lines"]:
                    g = "F" if line["speaker"] in FEMALE else "M"
                    if line["speaker"] not in seen:
                        seen[line["speaker"]] = (g, sum(1 for v in seen.values() if v[0] == g))
                    clips.setdefault(line["es"], seen[line["speaker"]])
    # Questions d'écoute du test de niveau.
    for questions in load_export("PLACEMENT")["bank"].values():
        for q in questions:
            if q.get("audio"):
                clips.setdefault(q["audio"], ("M", 0))
    for text in EXTRA_TEXTS:
        clips.setdefault(text, ("F", 0))
    return clips


def for_tts(text):
    """Texte envoyé au modèle : chiffres en toutes lettres, symboles nettoyés."""
    from num2words import num2words
    s = text
    if "=" in s:
        s = s.split("=", 1)[1]
    s = s.replace("→", ", ").replace("«", "").replace("»", "").replace("—", " ").replace("…", ".")
    s = re.sub(r"(\d)\s(\d{3})", r"\1\2", s)  # 12 000 → 12000
    s = re.sub(r"\d+", lambda m: num2words(int(m.group()), lang="es"), s)
    return re.sub(r"\s+", " ", s).strip()


def pitch(samples, sr):
    """Fréquence fondamentale moyenne (Hz) par autocorrélation, pour reconnaître voix aiguë / grave."""
    x = samples[: sr * 2].astype(np.float64)
    x -= x.mean()
    lo, hi = sr // 400, sr // 70
    frames = [x[i:i + 2048] for i in range(0, len(x) - 2048, 1024)]
    f0 = []
    for f in frames:
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        ac = np.correlate(f, f, "full")[len(f) - 1:]
        lag = lo + int(np.argmax(ac[lo:hi]))
        f0.append(sr / lag)
    return float(np.median(f0)) if f0 else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--only-missing", action="store_true")
    ap.add_argument("--steps", type=int, default=8)
    args = ap.parse_args()

    import sherpa_onnx
    import soundfile as sf

    m = args.model.rstrip("/") + "/"
    tts = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            supertonic=sherpa_onnx.OfflineTtsSupertonicModelConfig(
                duration_predictor=m + "duration_predictor.onnx", text_encoder=m + "text_encoder.onnx",
                vector_estimator=m + "vector_estimator.onnx", vocoder=m + "vocoder.onnx", tts_json=m + "tts.json",
                unicode_indexer=m + "unicode_indexer.bin", voice_style=m + "voice.bin"),
            num_threads=os.cpu_count() or 4)))

    def generate(text, sid):
        g = sherpa_onnx.GenerationConfig()
        g.sid = sid
        g.num_steps = args.steps
        g.speed = 1.0
        g.extra = {"lang": "es"}
        a = tts.generate(for_tts(text), g)
        return np.asarray(a.samples, dtype=np.float32), a.sample_rate

    # Classement des voix du modèle en féminines / masculines selon la hauteur.
    # On réutilise le classement déjà enregistré pour que les noms de fichiers restent stables.
    previous = None
    if os.path.exists(MANIFEST):
        try:
            previous = json.loads(open(MANIFEST, encoding="utf-8").read().split("export const AUDIO = ", 1)[1].rstrip().rstrip(";"))["voices"]
        except (IndexError, KeyError, ValueError):
            previous = None
    n = tts.num_speakers or 1
    if previous and previous.get("F") and previous.get("M"):
        voices = {"F": previous["F"], "M": previous["M"]}
        print("Voix reprises du manifeste :", voices)
    else:
        probe = [(sid, pitch(*generate("Hola, ¿cómo estás? Me llamo Lupita y vivo en México.", sid))) for sid in range(n)]
        probe.sort(key=lambda p: -p[1])
        half = max(1, n // 2)
        voices = {"F": [sid for sid, _ in probe[:half]], "M": [sid for sid, _ in probe[half:]] or [probe[-1][0]]}
        print("Voix (sid, Hz) :", [(s, round(f)) for s, f in probe], "→", voices)

    os.makedirs(OUT_DIR, exist_ok=True)
    clips = collect(load_content())
    manifest = {}
    for i, (text, (gender, rank)) in enumerate(sorted(clips.items())):
        sid = voices[gender][rank % len(voices[gender])]
        name = hashlib.sha1(f"{sid}|{text}".encode()).hexdigest()[:12] + ".mp3"
        manifest[text] = name
        dest = os.path.join(OUT_DIR, name)
        if args.only_missing and os.path.exists(dest):
            continue
        samples, sr = generate(text, sid)
        with tempfile.NamedTemporaryFile(suffix=".wav") as wav:
            sf.write(wav.name, samples, sr)
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", wav.name,
                            "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
                                   "silenceremove=start_periods=1:start_threshold=-50dB,areverse,adelay=60,apad=pad_dur=0.12",
                            "-ac", "1", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "48k", dest], check=True)
        if i % 50 == 0:
            print(f"{i}/{len(clips)} {text}")

    # Supprime les fichiers qui ne servent plus.
    used = set(manifest.values())
    for f in os.listdir(OUT_DIR):
        if f.endswith(".mp3") and f not in used:
            os.remove(os.path.join(OUT_DIR, f))

    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write("// Fichier généré par tools/build_audio.py — ne pas modifier à la main.\n")
        f.write("export const AUDIO = ")
        json.dump({"voices": {"model": "Supertonic 3", **voices}, "clips": manifest}, f, ensure_ascii=False, indent=0)
        f.write(";\n")
    size = sum(os.path.getsize(os.path.join(OUT_DIR, x)) for x in used)
    print(f"{len(manifest)} clips, {size // 1024} Ko → {OUT_DIR}")


if __name__ == "__main__":
    sys.exit(main())
