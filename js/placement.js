// Test de niveau adaptatif, avec une banque de questions dédiée (tools/placement_bank.py).
// À chaque niveau (A1 → B2), 10 questions : réponses à écrire, grammaire, vocabulaire,
// lecture d'un texte et écoute. On passe au niveau suivant avec au moins 8/10 ;
// dès que ce score devient impossible, le test s'arrête.
// Le niveau estimé est le dernier niveau réussi ; on commence par le contenu du niveau suivant.
import { LEVELS, PLACEMENT } from './content.js';
import { shuffle } from './util.js';

export const QUESTIONS_PER_LEVEL = Object.values(PLACEMENT.plan).reduce((a, b) => a + b, 0);
export const PASS_MARK = 8;

export const SKILLS = {
  write: 'Expression écrite',
  grammar: 'Grammaire',
  vocab: 'Vocabulaire',
  reading: 'Compréhension écrite',
  listening: 'Compréhension orale',
};

const LABELS = {
  write: 'Écris la réponse',
  grammar: 'Complète la phrase',
  vocab: 'Choisis la bonne réponse',
  reading: 'Lis et réponds',
  listening: 'Écoute et réponds',
};

function toExercise(q, uid) {
  const base = { uid, skill: q.skill, label: LABELS[q.skill], item: null };
  if (q.skill === 'write') {
    return {
      ...base,
      type: 'write',
      prompt: { text: q.prompt, blank: q.prompt.includes('___'), lang: q.prompt.includes('___') ? 'es' : 'fr' },
      accept: q.accept,
      answer: q.accept[0],
      answerFr: null,
    };
  }
  const prompt = q.skill === 'reading' ? { passage: q.text, question: q.question }
    : q.skill === 'listening' ? { audio: q.audio, autoplay: true, listenOnly: true, question: q.question }
      : { text: q.prompt, blank: q.prompt.includes('___'), lang: q.prompt.includes('___') ? 'es' : 'fr' };
  return {
    ...base,
    type: 'mcq',
    choiceStyle: 'text',
    prompt,
    choices: shuffle(q.options.map((o) => ({ label: o, correct: o === q.answer }))),
    answer: q.answer,
    answerFr: null,
  };
}

/** 10 questions d'un niveau, tirées au hasard selon la répartition prévue, dans un ordre de difficulté croissante. */
function questionsFor(level) {
  const bank = PLACEMENT.bank[level];
  const order = ['vocab', 'grammar', 'reading', 'write', 'listening'];
  const picked = [];
  for (const skill of order) {
    picked.push(...shuffle(bank.filter((q) => q.skill === skill)).slice(0, PLACEMENT.plan[skill] || 0));
  }
  return picked.map((q, i) => toExercise(q, `${level}-${i}`));
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

  /** Dernier niveau réussi (null si aucun). */
  get estimated() {
    return this.passed[this.passed.length - 1] || null;
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
    // On commence par le niveau échoué (ou B2 si tout est réussi).
    this.result = this.level;
    return true;
  }
}
