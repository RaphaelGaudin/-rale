// Voix en espagnol : clips audio enregistrés (js/data/audio.js) quand ils existent,
// sinon synthèse vocale du téléphone (es-MX de préférence).
import { state } from './store.js';
import { AUDIO } from './data/audio.js';

const SILENT_MP3 = 'data:audio/mpeg;base64,SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjYwLjE2LjEwMAAAAAAAAAAAAAAA//NwwAAAAAAAAAAAAEluZm8AAAAPAAAABAAAAlgAenp6enp6enp6enp6enp6enp6enp6enp6pqampqampqampqampqampqampqampqamptPT09PT09PT09PT09PT09PT09PT09PT09P/////////////////////////////////AAAAAExhdmM2MC4zMQAAAAAAAAAAAAAAACQCcQAAAAAAAAJY+/rsqgAAAAAAAAAAAAAAAAD/80DEAAAAA0gAAAAATEFNRTMuMTAwVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/zQsRbAAADSAAAAABVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/zQMSkAAADSAAAAABVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//NCxKMAAANIAAAAAFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV';

// ── Clips enregistrés ──

const player = typeof Audio !== 'undefined' ? new Audio() : null;
if (player) {
  player.preload = 'auto';
  player.setAttribute('playsinline', '');
}
let playToken = 0;

function clipUrl(text) {
  const file = AUDIO.clips[text.trim()];
  return file ? `./audio/${file}` : null;
}

export function hasRecordedVoices() {
  return Object.keys(AUDIO.clips).length > 0;
}

function useClips() {
  return state.voice !== 'device' && hasRecordedVoices();
}

function playClip(url, token) {
  return new Promise((resolve) => {
    if (!player) return resolve();
    let done = false;
    const finish = () => {
      if (done) return;
      done = true;
      player.removeEventListener('ended', finish);
      player.removeEventListener('error', finish);
      resolve();
    };
    player.addEventListener('ended', finish);
    player.addEventListener('error', finish);
    player.src = url;
    player.playbackRate = Math.min(1, Math.max(0.6, state.speechRate || 0.9) + 0.1);
    player.preservesPitch = true;
    player.webkitPreservesPitch = true;
    const p = player.play();
    if (p && p.catch) p.catch(finish);
    // Sécurité si l'événement « ended » n'arrive jamais.
    setTimeout(() => token === playToken && finish(), 15000);
  });
}

// ── Synthèse vocale de l'appareil ──

const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
let voices = [];

function loadVoices() {
  if (!synth) return;
  const score = (v) => {
    const lang = v.lang.replace('_', '-').toLowerCase();
    let s = 0;
    if (lang === 'es-mx') s += 100;
    else if (lang === 'es-us') s += 60;
    else if (lang.startsWith('es-419')) s += 50;
    else if (lang.startsWith('es')) s += 10;
    else return -1;
    if (/premium|enhanced|mejorad|natural/i.test(v.name)) s += 20;
    if (v.localService) s += 1;
    return s;
  };
  voices = synth.getVoices().filter((v) => score(v) >= 0).sort((a, b) => score(b) - score(a));
}

if (synth) {
  loadVoices();
  synth.addEventListener?.('voiceschanged', loadVoices);
}

export function mexicanVoice() {
  return voices.find((v) => v.lang.replace('_', '-').toLowerCase() === 'es-mx') || null;
}

export function voiceDescription() {
  if (useClips()) return 'Voix enregistrées (synthèse neuronale), disponibles hors-ligne.';
  if (!synth) return 'Synthèse vocale indisponible sur cet appareil.';
  if (!voices.length) loadVoices();
  const mx = mexicanVoice();
  if (mx) return `Voix de l'iPhone : ${mx.name} (espagnol du Mexique)`;
  if (voices[0]) return `Pas de voix mexicaine installée, utilisation de « ${voices[0].name} » (${voices[0].lang}).`;
  return 'Aucune voix espagnole trouvée sur cet appareil.';
}

function voiceFor(speakerIndex) {
  const mx = voices.filter((v) => v.lang.replace('_', '-').toLowerCase() === 'es-mx');
  const pool = mx.length ? mx : voices;
  return pool.length ? pool[speakerIndex % pool.length] : null;
}

function utter(text, { speaker = 0 } = {}) {
  return new Promise((resolve) => {
    if (!synth) return resolve();
    if (!voices.length) loadVoices();
    const u = new SpeechSynthesisUtterance(text);
    const voice = voiceFor(speaker);
    if (voice) u.voice = voice;
    u.lang = voice?.lang || 'es-MX';
    u.rate = state.speechRate || 0.9;
    const distinctVoices = new Set(voices.filter((v) => v.lang === u.lang).map((v) => v.name)).size;
    u.pitch = distinctVoices > 1 ? 1 : [1, 1.25, 0.85][speaker % 3];
    let done = false;
    const finish = () => {
      if (done) return;
      done = true;
      resolve();
    };
    u.onend = finish;
    u.onerror = finish;
    setTimeout(finish, 1500 + text.length * 120);
    synth.speak(u);
  });
}

/** iOS ignore parfois une phrase demandée juste après cancel() : on attend un court instant. */
async function cancelSynth() {
  if (!synth) return;
  if (synth.speaking || synth.pending) {
    synth.cancel();
    await new Promise((r) => setTimeout(r, 80));
  }
}

// ── API ──

/** Lit un texte en espagnol (interrompt la lecture en cours). */
export async function speak(text, options = {}) {
  const token = ++playToken;
  player?.pause();
  await cancelSynth();
  if (token !== playToken) return;
  const url = useClips() && clipUrl(text);
  if (url) return playClip(url, token);
  return utter(text, options);
}

/** Lit un dialogue réplique par réplique. `onLine(i)` est appelé avant chaque réplique. */
export async function speakLines(lines, onLine) {
  const token = ++playToken;
  player?.pause();
  await cancelSynth();
  const speakers = [...new Set(lines.map((l) => l.speaker))];
  for (let i = 0; i < lines.length; i++) {
    if (token !== playToken) return;
    onLine?.(i);
    const url = useClips() && clipUrl(lines[i].es);
    if (url) await playClip(url, token);
    else await utter(lines[i].es, { speaker: speakers.indexOf(lines[i].speaker) });
    await new Promise((r) => setTimeout(r, 250));
  }
  if (token === playToken) onLine?.(-1);
}

export function stop() {
  playToken++;
  player?.pause();
  synth?.cancel();
}

/** Liste des fichiers audio (pour le téléchargement hors-ligne). */
export function allClipUrls() {
  return [...new Set(Object.values(AUDIO.clips))].map((f) => `./audio/${f}`);
}

/**
 * iOS n'autorise le son qu'après un geste de l'utilisateur : au premier toucher,
 * on « bénit » le lecteur audio et on amorce la synthèse vocale.
 */
export function unlockSpeech() {
  if (player) {
    player.src = SILENT_MP3;
    const p = player.play();
    if (p && p.catch) p.catch(() => {});
  }
  if (synth) {
    try {
      const u = new SpeechSynthesisUtterance(' ');
      u.volume = 0;
      synth.speak(u);
    } catch (e) { /* rien */ }
  }
}

export function isSupported() {
  return !!synth || hasRecordedVoices();
}
