// Répétition espacée : chaque élément appris a une « étape » (stage).
// Étape 1 → revient dans 1 jour, étape 2 → 3 jours, puis 7, 14, 30…
// Une bonne réponse fait monter d'une étape, une erreur fait redescendre.
import { addDays, dayKey, startOfDay } from './util.js';

export const INTERVALS = [1, 3, 7, 14, 30, 60, 120, 240];
export const MAX_STAGE = INTERVALS.length;
/** À partir de cette étape (intervalle ≥ 30 jours), l'élément est « maîtrisé ». */
export const MASTERED_STAGE = 5;

export function intervalForStage(stage) {
  return INTERVALS[Math.min(Math.max(stage, 1), MAX_STAGE) - 1];
}

function dueFrom(now, days) {
  return dayKey(addDays(startOfDay(now), days));
}

/** Un nouvel élément vient d'être appris (retrouvé 3 fois dans la session). */
export function learned(state, now = new Date()) {
  return {
    ...state,
    stage: 1,
    due: dueFrom(now, intervalForStage(1)),
    learnedAt: dayKey(now),
    last: now.toISOString(),
  };
}

/** Résultat d'une révision : on monte d'une étape, ou on redescend après une erreur. */
export function reviewed(state, correct, now = new Date()) {
  const stage = correct ? Math.min(state.stage + 1, MAX_STAGE) : Math.max(state.stage - 1, 1);
  // Après une erreur, l'élément revient dès le lendemain.
  const days = correct ? intervalForStage(stage) : 1;
  return {
    ...state,
    stage,
    due: dueFrom(now, days),
    correct: (state.correct || 0) + (correct ? 1 : 0),
    wrong: (state.wrong || 0) + (correct ? 0 : 1),
    last: now.toISOString(),
  };
}

export function isLearned(state) {
  return !!state && state.stage >= 1;
}

export function isDue(state, today = dayKey()) {
  return isLearned(state) && state.due <= today;
}

/**
 * Niveau de difficulté de l'exercice selon la maîtrise :
 * 0 reconnaître l'image · 1 choisir le mot · 2 épeler · 3 écrire / comprendre à l'oral.
 */
export function difficultyForStage(stage) {
  if (stage <= 1) return 1;
  if (stage === 2) return 2;
  if (stage === 3) return Math.random() < 0.5 ? 2 : 3;
  return 3;
}

/** La légende française sous les images disparaît à partir de l'étape 2. */
export function showCaptionForStage(stage) {
  return stage <= 1;
}
