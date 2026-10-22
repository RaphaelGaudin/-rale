// Voix à l'accent mexicain grâce à la synthèse vocale du téléphone (es-MX).
import { state } from './store.js';

const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
let voices = [];
let sequenceToken = 0;

function loadVoices() {
  if (!synth) return;
  const all = synth.getVoices();
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
  voices = all.filter((v) => score(v) >= 0).sort((a, b) => score(b) - score(a));
}

if (synth) {
  loadVoices();
  synth.addEventListener?.('voiceschanged', loadVoices);
}

export function isSupported() {
  return !!synth;
}

export function mexicanVoice() {
  return voices.find((v) => v.lang.replace('_', '-').toLowerCase() === 'es-mx') || null;
}

export function voiceDescription() {
  if (!synth) return 'Synthèse vocale indisponible sur cet appareil.';
  if (!voices.length) loadVoices();
  const mx = mexicanVoice();
  if (mx) return `Voix mexicaine : ${mx.name}`;
  if (voices[0]) return `Pas de voix mexicaine installée, utilisation de « ${voices[0].name} » (${voices[0].lang}).`;
  return 'Aucune voix espagnole trouvée.';
}

/** Voix d'un personnage : on alterne les voix mexicaines disponibles et la hauteur. */
function voiceFor(speakerIndex) {
  const mx = voices.filter((v) => v.lang.replace('_', '-').toLowerCase() === 'es-mx');
  const pool = mx.length ? mx : voices;
  return pool.length ? pool[speakerIndex % pool.length] : null;
}

function utter(text, { speaker = 0, rate = 1 } = {}) {
  return new Promise((resolve) => {
    if (!synth) return resolve();
    if (!voices.length) loadVoices();
    const u = new SpeechSynthesisUtterance(text);
    const voice = voiceFor(speaker);
    if (voice) u.voice = voice;
    u.lang = voice?.lang || 'es-MX';
    u.rate = (state.speechRate || 0.9) * rate;
    // Si une seule voix est disponible, on varie la hauteur selon le personnage.
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
    // Sécurité : certains navigateurs n'envoient jamais « onend ».
    setTimeout(finish, 1500 + text.length * 120);
    synth.speak(u);
  });
}

/** Lit un texte en espagnol (interrompt la lecture en cours). */
export function speak(text, options = {}) {
  if (!synth) return Promise.resolve();
  sequenceToken++;
  synth.cancel();
  return utter(text, options);
}

/** Lit un dialogue réplique par réplique. `onLine(i)` est appelé avant chaque réplique. */
export async function speakLines(lines, onLine) {
  if (!synth) return;
  const token = ++sequenceToken;
  synth.cancel();
  const speakers = [...new Set(lines.map((l) => l.speaker))];
  for (let i = 0; i < lines.length; i++) {
    if (token !== sequenceToken) return;
    onLine?.(i);
    await utter(lines[i].es, { speaker: speakers.indexOf(lines[i].speaker) });
    await new Promise((r) => setTimeout(r, 250));
  }
  if (token === sequenceToken) onLine?.(-1);
}

export function stop() {
  sequenceToken++;
  synth?.cancel();
}
