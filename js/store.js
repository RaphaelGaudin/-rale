// Progression de l'utilisateur, sauvegardée dans le stockage local du téléphone.
import { addDays, dayKey, daysBetween, shuffle, startOfDay } from './util.js';
import * as SRS from './srs.js';
import { itemsById, itemsForLevel, LEVELS, themesForLevel } from './content.js';

const STORAGE_KEY = 'orale.progress.v1';

const DEFAULTS = {
  onboarded: false,
  level: 'A1',
  placement: null,
  items: {}, // id → { stage, due, correct, wrong, last, learnedAt }
  xp: 0,
  streak: 0,
  bestStreak: 0,
  lastPracticeDay: null,
  dailyGoal: 5, // minutes
  secondsByDay: {},
  bestCombo: 0,
  sessions: 0,
  sound: true,
  haptics: true,
  speechRate: 0.9,
  voice: 'recorded', // 'recorded' (clips audio) ou 'device' (synthèse de l'iPhone)
  levelUpNotice: null,
};

function load() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return { ...structuredClone(DEFAULTS), ...JSON.parse(raw) };
  } catch (e) {
    console.warn('Progression illisible, on repart de zéro.', e);
  }
  return structuredClone(DEFAULTS);
}

const listeners = new Set();
export const state = load();

export function save() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (e) {
    console.warn('Sauvegarde impossible', e);
  }
  listeners.forEach((fn) => fn(state));
}

export function subscribe(fn) {
  listeners.add(fn);
  return () => listeners.delete(fn);
}

export function update(changes) {
  Object.assign(state, changes);
  save();
}

// ── Éléments ──

export function itemState(id) {
  return state.items[id];
}

export function stageOf(id) {
  return state.items[id]?.stage || 0;
}

export function isLearned(id) {
  return SRS.isLearned(state.items[id]);
}

export function markLearned(id) {
  state.items[id] = SRS.learned(state.items[id] || {});
  save();
}

export function recordReview(id, correct) {
  const current = state.items[id];
  if (!SRS.isLearned(current)) return;
  state.items[id] = SRS.reviewed(current, correct);
  save();
}

/** Éléments à revoir aujourd'hui (y compris en retard), du plus en retard au moins en retard. */
export function dueItems(today = dayKey()) {
  return Object.entries(state.items)
    .filter(([id, s]) => itemsById.has(id) && SRS.isDue(s, today))
    .sort((a, b) => (a[1].due < b[1].due ? -1 : a[1].due > b[1].due ? 1 : a[1].stage - b[1].stage))
    .map(([id]) => itemsById.get(id));
}

/** Nombre d'éléments à revoir pour chacun des `days` prochains jours (le jour 0 inclut le retard). */
export function forecast(days = 7) {
  const today = startOfDay();
  const counts = Array.from({ length: days }, (_, i) => ({ date: addDays(today, i), count: 0 }));
  for (const [id, s] of Object.entries(state.items)) {
    if (!itemsById.has(id) || !SRS.isLearned(s)) continue;
    const offset = Math.max(0, daysBetween(today, new Date(s.due + 'T00:00:00')));
    if (offset < days) counts[offset].count++;
  }
  return counts;
}

export function learnedItems() {
  return Object.entries(state.items)
    .filter(([id, s]) => itemsById.has(id) && SRS.isLearned(s))
    .map(([id]) => itemsById.get(id));
}

export function themeProgress(theme) {
  const learned = theme.items.filter((i) => isLearned(i.id)).length;
  return { learned, total: theme.items.length, ratio: learned / theme.items.length };
}

export function levelProgress(level) {
  const items = itemsForLevel(level);
  const learned = items.filter((i) => isLearned(i.id)).length;
  return { learned, total: items.length, ratio: items.length ? learned / items.length : 0 };
}

// ── Temps de pratique, série et objectif ──

export function todaySeconds() {
  return state.secondsByDay[dayKey()] || 0;
}

export function goalRatio() {
  return Math.min(1, todaySeconds() / (state.dailyGoal * 60));
}

/** La série affichée : elle tombe à 0 si on a sauté un jour. */
export function currentStreak() {
  if (!state.lastPracticeDay) return 0;
  const gap = daysBetween(new Date(state.lastPracticeDay + 'T00:00:00'), new Date());
  return gap <= 1 ? state.streak : 0;
}

export function practicedToday() {
  return state.lastPracticeDay === dayKey();
}

/** À appeler à la fin de chaque session. Renvoie des infos pour l'écran de bilan. */
export function recordSession({ seconds, xp, bestCombo }) {
  const today = dayKey();
  const goalBefore = goalRatio() >= 1;
  state.secondsByDay[today] = (state.secondsByDay[today] || 0) + Math.round(seconds);
  state.xp += xp;
  state.sessions += 1;
  state.bestCombo = Math.max(state.bestCombo, bestCombo);

  let streakExtended = false;
  if (state.lastPracticeDay !== today) {
    const gap = state.lastPracticeDay
      ? daysBetween(new Date(state.lastPracticeDay + 'T00:00:00'), new Date())
      : Infinity;
    state.streak = gap === 1 ? state.streak + 1 : 1;
    state.lastPracticeDay = today;
    streakExtended = true;
  }
  state.bestStreak = Math.max(state.bestStreak, state.streak);
  const levelUp = checkLevelUp();
  save();
  return { streakExtended, goalJustReached: !goalBefore && goalRatio() >= 1, levelUp };
}

/** On passe au niveau suivant quand 80 % du niveau actuel est appris. */
function checkLevelUp() {
  const idx = LEVELS.indexOf(state.level);
  if (idx < LEVELS.length - 1 && levelProgress(state.level).ratio >= 0.8) {
    state.level = LEVELS[idx + 1];
    return state.level;
  }
  return null;
}

/** Le thème conseillé pour la leçon du jour : le premier thème non terminé du niveau. */
export function suggestedTheme() {
  const startIdx = LEVELS.indexOf(state.level);
  const order = [...LEVELS.slice(startIdx), ...LEVELS.slice(0, startIdx).reverse()];
  for (const level of order) {
    const theme = themesForLevel(level).find((t) => t.items.some((i) => !isLearned(i.id)));
    if (theme) return theme;
  }
  return null;
}

/**
 * Après le test de niveau : les éléments des niveaux réussis sont considérés comme connus
 * (étape 2) et reviennent en révision, étalés sur `days` jours, pour confirmer les acquis.
 * Une erreur les fera redescendre comme n'importe quel élément.
 */
export function seedKnownLevels(levels, days = 21) {
  const today = startOfDay();
  const items = shuffle(levels.flatMap((l) => itemsForLevel(l)).filter((i) => !isLearned(i.id)));
  items.forEach((item, i) => {
    state.items[item.id] = {
      stage: 2,
      due: dayKey(addDays(today, 1 + (i % days))),
      learnedAt: dayKey(today),
      seeded: true,
      last: new Date().toISOString(),
    };
  });
  save();
  return items.length;
}

export function exportData() {
  return JSON.stringify(state, null, 1);
}

export function importData(json) {
  const data = JSON.parse(json);
  if (typeof data !== 'object' || !data.items) throw new Error('Fichier invalide');
  Object.keys(state).forEach((k) => delete state[k]);
  Object.assign(state, structuredClone(DEFAULTS), data);
  save();
}

export function reset() {
  Object.keys(state).forEach((k) => delete state[k]);
  Object.assign(state, structuredClone(DEFAULTS));
  save();
}
