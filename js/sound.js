// Sons de validation synthétisés avec Web Audio (aucun fichier à télécharger).
import { state } from './store.js';
import { unlockSpeech } from './speech.js';

// iOS 17+ : le son est joué même quand le bouton « silencieux » est activé.
try {
  if (navigator.audioSession) navigator.audioSession.type = 'playback';
} catch (e) { /* non pris en charge */ }

let ctx = null;

function audio() {
  if (!ctx) {
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return null;
    ctx = new AC();
  }
  if (ctx.state === 'suspended') ctx.resume();
  return ctx;
}

// iOS n'autorise l'audio qu'après un geste de l'utilisateur : on « déverrouille » au premier toucher.
export function unlockOnFirstGesture() {
  const unlock = () => {
    const c = audio();
    if (c) {
      const buffer = c.createBuffer(1, 1, 22050);
      const src = c.createBufferSource();
      src.buffer = buffer;
      src.connect(c.destination);
      src.start(0);
    }
    unlockSpeech();
    window.removeEventListener('touchend', unlock, true);
    window.removeEventListener('click', unlock, true);
  };
  window.addEventListener('touchend', unlock, { capture: true, passive: true });
  window.addEventListener('click', unlock, true);
  // Au retour dans l'app, iOS suspend parfois le contexte audio.
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && ctx?.state !== 'running') ctx?.resume();
  });
}

function tone(c, { freq, start, duration, type = 'sine', gain = 0.18, slideTo }) {
  const osc = c.createOscillator();
  const g = c.createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, start);
  if (slideTo) osc.frequency.exponentialRampToValueAtTime(slideTo, start + duration);
  g.gain.setValueAtTime(0.0001, start);
  g.gain.exponentialRampToValueAtTime(gain, start + 0.012);
  g.gain.exponentialRampToValueAtTime(0.0001, start + duration);
  osc.connect(g).connect(c.destination);
  osc.start(start);
  osc.stop(start + duration + 0.05);
}

function bell(c, freq, start, duration = 0.35, gain = 0.16) {
  tone(c, { freq, start, duration, gain });
  tone(c, { freq: freq * 2, start, duration: duration * 0.6, gain: gain * 0.25 });
}

const SOUNDS = {
  tap(c, t) {
    tone(c, { freq: 660, start: t, duration: 0.06, type: 'triangle', gain: 0.08 });
  },
  correct(c, t) {
    bell(c, 784, t, 0.18); // sol
    bell(c, 1175, t + 0.09, 0.35); // ré
  },
  wrong(c, t) {
    tone(c, { freq: 220, start: t, duration: 0.25, type: 'triangle', gain: 0.16, slideTo: 150 });
  },
  combo(c, t) {
    [784, 988, 1175, 1568].forEach((f, i) => bell(c, f, t + i * 0.07, 0.25, 0.12));
  },
  learned(c, t) {
    [523, 659, 784].forEach((f, i) => bell(c, f, t + i * 0.08, 0.3, 0.12));
  },
  complete(c, t) {
    const notes = [523, 659, 784, 1047, 784, 1047];
    notes.forEach((f, i) => bell(c, f, t + i * 0.11, i === notes.length - 1 ? 0.7 : 0.22, 0.13));
  },
  newItem(c, t) {
    tone(c, { freq: 880, start: t, duration: 0.12, gain: 0.08 });
    tone(c, { freq: 1320, start: t + 0.06, duration: 0.18, gain: 0.06 });
  },
};

export function play(name) {
  if (!state.sound) return;
  const c = audio();
  if (!c || !SOUNDS[name]) return;
  SOUNDS[name](c, c.currentTime + 0.01);
}

/** Petite vibration (Android ; ignorée sur iPhone qui ne la permet pas depuis le web). */
export function buzz(pattern = 15) {
  if (state.haptics && navigator.vibrate) navigator.vibrate(pattern);
}
