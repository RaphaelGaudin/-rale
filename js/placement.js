// Test de niveau adaptatif : 4 questions par niveau, on monte tant qu'on en réussit au moins 3.
import { LEVELS, themesForLevel } from './content.js';
import { makeExercise } from './exercises.js';
import { shuffle } from './util.js';

export const QUESTIONS_PER_LEVEL = 4;
export const PASS_MARK = 3;

function questionsFor(level) {
  const themes = shuffle(themesForLevel(level));
  const ofKind = (theme, kind) => shuffle(theme.items.filter((i) => i.kind === kind))[0];
  return [
    makeExercise(ofKind(themes[0], 'word'), 1, true), // choisir le mot espagnol
    makeExercise(ofKind(themes[1], 'phrase'), 0), // comprendre une phrase
    makeExercise(ofKind(themes[2], 'phrase'), 1), // retrouver une phrase
    makeExercise(ofKind(themes[3], 'grammar'), 2), // grammaire sans indice
  ];
}

export class PlacementTest {
  constructor() {
    this.levelIndex = 0;
    this.index = 0;
    this.correct = 0;
    this.scores = {};
    this.result = null;
    this.questions = questionsFor(LEVELS[0]);
  }

  get level() {
    return LEVELS[this.levelIndex];
  }

  get question() {
    return this.questions[this.index];
  }

  answer(correct) {
    if (correct) this.correct++;
  }

  /** Passe à la question suivante. Renvoie true si le test est terminé. */
  advance() {
    this.index++;
    if (this.index < QUESTIONS_PER_LEVEL) return false;
    this.scores[this.level] = this.correct;
    const passed = this.correct >= PASS_MARK;
    if (passed && this.levelIndex < LEVELS.length - 1) {
      this.levelIndex++;
      this.index = 0;
      this.correct = 0;
      this.questions = questionsFor(this.level);
      return false;
    }
    // Échec : on commence à ce niveau. Réussite du B2 : on reste en B2.
    this.result = this.level;
    return true;
  }
}
