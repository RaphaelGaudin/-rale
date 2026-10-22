#!/usr/bin/env python3
"""Génère js/data/art.js (illustrations SVG) à partir de tools/art/*.py.

Usage : python3 tools/build_art.py [--preview fichier.html]
"""
import importlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

MODULES = ["art.a1", "art.a2", "art.b1", "art.b2", "art.ui"]


def collect():
    art = {}
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError as e:
            if e.name == name:
                continue
            raise
        for key in mod.ART:
            assert key not in art, f"illustration en double : {key}"
        art.update(mod.ART)
    return art


def main():
    art = collect()
    out = os.path.join(ROOT, "js", "data", "art.js")
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Fichier généré par tools/build_art.py — ne pas modifier à la main.\n")
        f.write("export const ART = ")
        json.dump(art, f, ensure_ascii=False, indent=0)
        f.write(";\n")
    print(f"{len(art)} illustrations → {out} ({os.path.getsize(out) // 1024} Ko)")
    if "--preview" in sys.argv:
        dest = sys.argv[sys.argv.index("--preview") + 1]
        cells = "".join(f'<figure><div class="tile">{svg}</div><figcaption>{k}</figcaption></figure>' for k, svg in art.items())
        with open(dest, "w", encoding="utf-8") as f:
            f.write(f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;background:#16121F;font-family:sans-serif;color:#ccc;display:flex;flex-wrap:wrap;gap:8px;padding:8px}}
figure{{margin:0;width:118px;text-align:center;font-size:11px}}
.tile{{width:118px;height:118px;background:#FFF7EA;border-radius:22px;padding:10px;box-sizing:border-box}}
svg{{width:100%;height:100%}}</style>{cells}""")


if __name__ == "__main__":
    main()
