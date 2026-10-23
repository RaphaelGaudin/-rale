// Moteur d'une session de 5 minutes. Mélange les nouveautés d'un thème
// et les révisions d'autres thèmes. Aucune manipulation du DOM ici.
import * as store from './store.js';
import { difficultyForStage, showCaptionForStage } from './srs.js';
import { makeExercise, makePairs } from './exercises.js';
import { itemsById } from './content.js';
import { play } from './sound.js';
import { shuffle } from './util.js';

export const SESSION_SECONDS = 5 * 60;
const NEW_PER_BATCH = 4;
const RETRIEVALS_TO_LEARN = 3;
const COMBO_MILESTONES = [3, 5, 10, 15, 20, 30, 50];
const PAIRS_XP = 20;
/** Nombre d'éléments nouveaux vus en une leçon, pour annoncer « Leçon X/Y ». */
export const ITEMS_PER_LESSON = 8;

/** Ordre d'introduction dans un thème : on intercale phrases, points de grammaire et dialogues entre les mots. */
function introductionOrder(items) {
  let w = 0, p = 0, g = 0, d = 0;
  const slot = (item) => {
    if (item.kind === 'word') return w++;
    if (item.kind === 'phrase') return 2.5 + 3 * p++;
    if (item.kind === 'grammar') return 5.5 + 12 * g++;
    return 9.5 + 12 * d++;
  };
  return items.map((item) => ({ item, s: slot(item) })).sort((a, b) => a.s - b.s).map((x) => x.item);
}

export class Lesson {
  /**
   * @param {{mode: 'theme'|'review'|'practice', theme?: object, onChange: Function}} options
   * « practice » : entraînement libre sur les éléments déjà appris d'un thème (une erreur compte pour la révision).
   */
  constructor({ mode, theme = null, onChange }) {
    this.mode = mode;
    this.theme = theme;
    this.onChange = onChange || (() => {});
    this.queue = [];
    this.sessionCorrect = {};
    this.presented = new Set();
    this.current = null;
    this.feedback = null;
    this.combo = 0;
    this.bestCombo = 0;
    this.xp = 0;
    this.correctCount = 0;
    this.answerCount = 0;
    this.learnedIds = [];
    this.reviewedIds = new Set();
    this.finished = false;
    this.summary = null;
    this.timeUp = false;
    this.startTime = Date.now();

    if (mode === 'theme') {
      this.newPool = introductionOrder(theme.items.filter((i) => !store.isLearned(i.id)));
      const due = store.dueItems();
      // On met en avant les révisions des autres thèmes.
      const others = due.filter((i) => i.themeId !== theme.id);
      const same = due.filter((i) => i.themeId === theme.id);
      this.reviewPool = [...others, ...same].map((i) => ({ type: 'review', id: i.id }));
      if (others.length < 3) {
        const dueIds = new Set(due.map((i) => i.id));
        const practice = store
          .learnedItems()
          .filter((i) => i.themeId !== theme.id && !dueIds.has(i.id))
          .sort((a, b) => store.stageOf(a.id) - store.stageOf(b.id) || (store.itemState(a.id).last < store.itemState(b.id).last ? -1 : 1))
          .slice(0, 3 - others.length)
          .map((i) => ({ type: 'practice', id: i.id }));
        this.reviewPool.push(...practice);
      }
    } else if (mode === 'practice') {
      this.newPool = [];
      const learned = theme.items.filter((i) => store.isLearned(i.id));
      // Les éléments les moins solides d'abord, puis le reste au hasard.
      const weak = learned.filter((i) => store.stageOf(i.id) <= 2);
      const strong = learned.filter((i) => store.stageOf(i.id) > 2);
      this.reviewPool = [...shuffle(weak), ...shuffle(strong)].map((i) => ({ type: 'practice', id: i.id, harder: true }));
    } else {
      this.newPool = [];
      this.reviewPool = store.dueItems().map((i) => ({ type: 'review', id: i.id }));
    }
    this.isEmpty = this.newPool.length === 0 && this.reviewPool.length === 0;
  }

  get elapsed() {
    return (Date.now() - this.startTime) / 1000;
  }

  get remaining() {
    return Math.max(0, SESSION_SECONDS - this.elapsed);
  }

  start() {
    if (this.isEmpty) return;
    this.appendBatch();
    this.next();
  }

  /** Ajoute un lot : jusqu'à 4 nouveautés, chacune présentée puis retrouvée 3 fois, entrecoupées de révisions. */
  appendBatch() {
    const fresh = this.newPool.splice(0, NEW_PER_BATCH);
    const reviews = this.reviewPool.splice(0, fresh.length ? 5 : 10);
    const steps = [];
    const remaining = new Map(fresh.map((i) => [i.id, RETRIEVALS_TO_LEARN]));
    const learn = (item) => {
      steps.push({ type: 'learn', id: item.id });
      remaining.set(item.id, remaining.get(item.id) - 1);
    };
    fresh.forEach((item, idx) => {
      steps.push({ type: 'present', id: item.id });
      learn(item);
      if (idx >= 1) learn(fresh[idx - 1]);
      if (idx >= 2) learn(fresh[idx - 2]);
      if (reviews.length) steps.push(reviews.shift());
    });
    while ([...remaining.values()].some((n) => n > 0)) {
      for (const item of fresh) if (remaining.get(item.id) > 0) learn(item);
      if (reviews.length) steps.push(reviews.shift());
    }
    steps.push(...reviews);
    // Petit jeu des paires en fin de lot (bonus d'XP, sans effet sur les révisions).
    const pairs = this.pairsCandidates(fresh);
    if (pairs.length >= 4) steps.push({ type: 'pairs', id: pairs[0].id, ids: pairs.map((i) => i.id) });
    this.queue.push(...steps);
    return steps.length;
  }

  /** Éléments pour le jeu des paires : ceux du lot, complétés par des éléments déjà appris du thème. */
  pairsCandidates(fresh) {
    const pairable = (i) => i.kind === 'word' || i.kind === 'phrase';
    const ids = new Set();
    const out = [];
    const add = (i) => { if (i && pairable(i) && !ids.has(i.id)) { ids.add(i.id); out.push(i); } };
    fresh.forEach(add);
    if (this.mode === 'review') return [];
    if (this.theme) shuffle(this.theme.items.filter((i) => store.isLearned(i.id))).forEach(add);
    // Toujours le même type d'élément (que des mots ou que des phrases) pour que les paires restent lisibles.
    const words = out.filter((i) => i.kind === 'word');
    const chosen = words.length >= 4 ? words : out.filter((i) => i.kind === 'phrase');
    return chosen.slice(0, 5);
  }

  next() {
    this.feedback = null;
    if (this.remaining <= 0) this.timeUp = true;
    for (;;) {
      if (!this.queue.length) {
        if (!this.timeUp && this.appendBatch() > 0) continue;
        this.finish();
        return;
      }
      const step = this.queue.shift();
      const item = itemsById.get(step.id);
      if (!item) continue;
      // Quand le temps est écoulé, on termine seulement les éléments déjà présentés.
      if (this.timeUp && step.type !== 'learn') continue;
      if (step.type === 'learn' && (!this.presented.has(step.id) || (this.sessionCorrect[step.id] || 0) >= RETRIEVALS_TO_LEARN)) continue;

      if (step.type === 'present') {
        this.presented.add(step.id);
        this.current = { step, item };
        play('newItem');
      } else if (step.type === 'pairs') {
        const exercise = makePairs(step.ids.map((id) => itemsById.get(id)).filter(Boolean));
        if (!exercise) continue;
        this.current = { step, item, exercise };
      } else {
        this.current = { step, item, exercise: this.exerciseFor(step, item) };
      }
      this.onChange();
      return;
    }
  }

  exerciseFor(step, item) {
    if (step.type === 'learn') return makeExercise(item, this.sessionCorrect[item.id] || 0, true);
    const stage = store.stageOf(item.id);
    const difficulty = difficultyForStage(stage);
    if (step.type === 'retry') return makeExercise(item, Math.max(0, difficulty - 1), true);
    if (step.harder) return makeExercise(item, Math.max(difficulty, 2), showCaptionForStage(stage));
    return makeExercise(item, difficulty, showCaptionForStage(stage));
  }

  /** Réponse de l'utilisateur à l'exercice en cours. */
  answer(correct, note = null) {
    if (!this.current?.exercise || this.feedback) return;
    const { step, item, exercise } = this.current;
    this.answerCount++;
    let comboMilestone = null;
    let justLearned = false;

    if (correct) {
      this.correctCount++;
      this.combo++;
      this.bestCombo = Math.max(this.bestCombo, this.combo);
      this.xp += 10 + (this.combo >= 3 ? 5 : 0);
      if (COMBO_MILESTONES.includes(this.combo)) comboMilestone = this.combo;
    } else {
      this.combo = 0;
    }

    if (step.type === 'pairs') {
      if (correct) this.xp += PAIRS_XP;
    } else if (step.type === 'learn') {
      if (correct) {
        this.sessionCorrect[item.id] = (this.sessionCorrect[item.id] || 0) + 1;
        if (this.sessionCorrect[item.id] === RETRIEVALS_TO_LEARN) {
          store.markLearned(item.id);
          this.learnedIds.push(item.id);
          justLearned = true;
        }
      } else {
        this.queue.splice(Math.min(2, this.queue.length), 0, { type: 'learn', id: item.id });
      }
    } else if (step.type === 'review' || step.type === 'practice') {
      if (step.type === 'review' || !correct) store.recordReview(item.id, correct);
      this.reviewedIds.add(item.id);
      if (!correct) this.queue.splice(Math.min(3, this.queue.length), 0, { type: 'retry', id: item.id });
    }

    play(correct ? (comboMilestone ? 'combo' : justLearned ? 'learned' : 'correct') : 'wrong');
    this.feedback = {
      correct,
      note,
      answer: exercise.answer,
      answerFr: exercise.answerFr,
      justLearned,
      comboMilestone,
      speak: exercise.speakOnReveal,
    };
    this.onChange();
  }

  finish() {
    if (this.finished) return;
    this.finished = true;
    this.current = null;
    if (this.answerCount > 0) {
      this.summary = store.recordSession({
        seconds: Math.min(this.elapsed, SESSION_SECONDS + 60),
        xp: this.xp,
        bestCombo: this.bestCombo,
      });
      play('complete');
    }
    this.onChange();
  }

  /** L'utilisateur quitte en cours de route : on garde ce qui a été fait. */
  quit() {
    if (this.finished) return;
    this.finished = true;
    if (this.answerCount > 0) {
      store.recordSession({ seconds: this.elapsed, xp: this.xp, bestCombo: this.bestCombo });
    }
  }
}
