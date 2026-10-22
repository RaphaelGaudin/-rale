// Test de niveau adaptatif. À chaque niveau (A1 → B2), 8 questions couvrant
// vocabulaire, compréhension écrite et orale, grammaire et dialogue — une par thème.
// On passe au niveau suivant avec au moins 6 bonnes réponses sur 8 ; dès que ce score
// devient impossible, on s'arrête : c'est le niveau où commencer.
import { LEVELS, themesForLevel } from './content.js';
import { distractors } from './exercises.js';
import { pick, shuffle } from './util.js';

export const QUESTIONS_PER_LEVEL = 8;
export const PASS_MARK = 6;

export const SKILLS = {
  vocab: 'Vocabulaire',
  reading: 'Compréhension écrite',
  listening: 'Compréhension orale',
  grammar: 'Grammaire',
};

function choicesFrom(correct, others) {
  return shuffle([{ label: correct, correct: true }, ...others.map((label) => ({ label, correct: false }))]);
}

function quizSentence(q) {
  return q.prompt.replace('___', q.answer).replace(/\s*\([^)]*\)\s*$/, '');
}

const BUILDERS = {
  // « Que signifie jitomate ? » — le mot espagnol, sans image (elle donnerait la réponse).
  wordToFr(theme) {
    const item = pick(theme.items.filter((i) => i.kind === 'word'));
    return {
      skill: 'vocab', item, type: 'mcq', choiceStyle: 'text',
      label: 'Que signifie ce mot ?',
      prompt: { text: item.es, audio: item.es },
      choices: choicesFrom(item.fr, distractors(item, 3, (i) => i.fr).map((d) => d.fr)),
      answer: item.es, answerFr: item.fr,
    };
  },
  frToWord(theme) {
    const item = pick(theme.items.filter((i) => i.kind === 'word'));
    return {
      skill: 'vocab', item, type: 'mcq', choiceStyle: 'text',
      label: 'Comment dit-on… ?',
      prompt: { text: item.fr, lang: 'fr' },
      choices: choicesFrom(item.es, distractors(item, 3, (i) => i.es).map((d) => d.es)),
      answer: item.es, answerFr: item.fr,
    };
  },
  reading(theme) {
    const item = pick(theme.items.filter((i) => i.kind === 'phrase'));
    return {
      skill: 'reading', item, type: 'mcq', choiceStyle: 'text',
      label: 'Que signifie cette phrase ?',
      prompt: { text: item.es },
      choices: choicesFrom(item.fr, distractors(item, 3, (i) => i.fr).map((d) => d.fr)),
      answer: item.es, answerFr: item.fr,
    };
  },
  // Phrase entendue seulement, sans le texte.
  listening(theme) {
    const item = pick(theme.items.filter((i) => i.kind === 'phrase'));
    return {
      skill: 'listening', item, type: 'mcq', choiceStyle: 'text',
      label: 'Écoute : que signifie cette phrase ?',
      prompt: { audio: item.es, autoplay: true, listenOnly: true },
      choices: choicesFrom(item.fr, distractors(item, 3, (i) => i.fr).map((d) => d.fr)),
      answer: item.es, answerFr: item.fr,
    };
  },
  grammar(theme) {
    const item = theme.items.find((i) => i.kind === 'grammar');
    const q = item.quiz;
    return {
      skill: 'grammar', item, type: 'mcq', choiceStyle: 'text',
      label: 'Complète la phrase',
      prompt: { text: q.prompt, blank: true },
      choices: shuffle(q.options.map((o) => ({ label: o, correct: o === q.answer }))),
      answer: quizSentence(q), answerFr: q.translation,
    };
  },
  dialogue(theme) {
    const item = theme.items.find((i) => i.kind === 'dialogue');
    const q = item.question;
    return {
      skill: 'reading', item, type: 'mcq', choiceStyle: 'text',
      label: 'Lis le dialogue et réponds',
      prompt: { dialogue: item.lines, question: q.prompt },
      choices: shuffle(q.options.map((o) => ({ label: o, correct: o === q.answer }))),
      answer: q.answer, answerFr: null,
    };
  },
};

// Du plus simple au plus exigeant ; chaque question vient d'un thème différent.
const PLAN = ['wordToFr', 'frToWord', 'reading', 'grammar', 'wordToFr', 'listening', 'grammar', 'dialogue'];

function questionsFor(level) {
  const themes = shuffle(themesForLevel(level));
  return PLAN.map((kind, i) => ({ ...BUILDERS[kind](themes[i % themes.length]), uid: `${level}-${i}` }));
}

export class PlacementTest {
  constructor() {
    this.levelIndex = 0;
    this.index = 0;
    this.correct = 0;
    this.wrong = 0;
    this.scores = {}; // niveau → { correct, asked }
    this.skills = Object.fromEntries(Object.keys(SKILLS).map((k) => [k, { correct: 0, asked: 0 }]));
    this.passed = [];
    this.result = null;
    this.questions = questionsFor(LEVELS[0]);
  }

  get level() {
    return LEVELS[this.levelIndex];
  }

  get question() {
    return this.questions[this.index];
  }

  /** Nombre total de questions posées jusqu'ici (pour la barre de progression). */
  get asked() {
    return Object.values(this.scores).reduce((n, s) => n + s.asked, 0) + this.index;
  }

  answer(correct) {
    const skill = this.skills[this.question.skill];
    skill.asked++;
    if (correct) {
      this.correct++;
      skill.correct++;
    } else {
      this.wrong++;
    }
  }

  /** Passe à la question suivante. Renvoie true si le test est terminé. */
  advance() {
    this.index++;
    const failed = this.wrong > QUESTIONS_PER_LEVEL - PASS_MARK;
    if (this.index < QUESTIONS_PER_LEVEL && !failed) return false;

    this.scores[this.level] = { correct: this.correct, asked: this.index };
    if (!failed) this.passed.push(this.level);
    if (!failed && this.levelIndex < LEVELS.length - 1) {
      this.levelIndex++;
      this.index = 0;
      this.correct = 0;
      this.wrong = 0;
      this.questions = questionsFor(this.level);
      return false;
    }
    // Échec : on commence à ce niveau. Réussite du B2 : on reste en B2.
    this.result = this.level;
    return true;
  }
}
