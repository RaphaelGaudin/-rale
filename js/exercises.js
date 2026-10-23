// Fabrique d'exercices. La difficulté (0 à 3) suit la maîtrise de l'élément :
// 0 reconnaître · 1 choisir le mot · 2 épeler / reconstruire · 3 écrire / comprendre à l'oral.
import { itemsForLevel, themeOf } from './content.js';
import { normalizeAnswer, pick, removeAccents, sample, shuffle, stripArticle, stripPunctuation, tokenize } from './util.js';

export function distractors(item, count, key) {
  const theme = themeOf(item);
  const same = theme.items.filter((i) => i.kind === item.kind && i.id !== item.id);
  const wider = itemsForLevel(item.level).filter((i) => i.kind === item.kind && i.themeId !== item.themeId);
  const seen = new Set([key(item)]);
  const result = [];
  for (const candidate of [...shuffle(same), ...shuffle(wider)]) {
    const k = key(candidate);
    if (seen.has(k)) continue;
    seen.add(k);
    result.push(candidate);
    if (result.length === count) break;
  }
  return result;
}

function mcq(base, correct, others) {
  return {
    ...base,
    type: 'mcq',
    choices: shuffle([{ ...correct, correct: true }, ...others.map((o) => ({ ...o, correct: false }))]),
  };
}

const LETTER_POOL = 'aeioulnrstcdmpb';

function spellExercise(base, word) {
  const target = stripPunctuation(stripArticle(word)).toLowerCase();
  const article = word.length !== stripArticle(word).length ? word.slice(0, word.length - stripArticle(word).length).trim() : '';
  const letters = [...target].filter((ch) => ch !== ' ');
  const extra = letters.length > 12 ? 0 : 2;
  const distractorLetters = [];
  while (distractorLetters.length < extra) {
    const l = pick([...LETTER_POOL]);
    if (!letters.includes(l)) distractorLetters.push(l);
  }
  return {
    ...base,
    type: 'spell',
    article,
    target: [...target],
    tiles: shuffle([...letters, ...distractorLetters]).map((letter, i) => ({ id: i, letter })),
  };
}

/** Mots d'une phrase, sans majuscule initiale : sinon elle trahirait le premier mot. */
function tileTokens(sentence) {
  const tokens = tokenize(sentence);
  if (tokens[0] && tokens[0] !== tokens[0].toUpperCase()) tokens[0] = tokens[0][0].toLowerCase() + tokens[0].slice(1);
  return tokens;
}

function buildExercise(base, sentence, item) {
  const tokens = tileTokens(sentence);
  const pool = itemsForLevel(item.level)
    .filter((i) => i.kind === 'phrase' && i.es !== sentence)
    .flatMap((i) => tileTokens(i.es))
    .filter((t) => !tokens.some((x) => x.toLowerCase() === t.toLowerCase()));
  const extras = tokens.length > 9 ? sample(pool, 1) : sample([...new Set(pool)], 2);
  return {
    ...base,
    type: 'build',
    tokens,
    tiles: shuffle([...tokens, ...extras]).map((word, i) => ({ id: i, word })),
  };
}

// ── Mots ──

/** Vrai ou faux : l'image correspond-elle au mot ? */
function trueFalse(item, base) {
  const truth = Math.random() < 0.5;
  const other = truth ? item : distractors(item, 1, (i) => i.es)[0] || item;
  const isTrue = other === item;
  return {
    ...base,
    type: 'mcq',
    label: 'Vrai ou faux ?',
    prompt: { art: item.art, caption: item.fr, text: `¿Es «${other.es}»?`, audio: other.es, autoplay: true },
    choiceStyle: 'tf',
    choices: [{ label: 'Sí', correct: isTrue, tf: 'yes' }, { label: 'No', correct: !isTrue, tf: 'no' }],
  };
}

function dictation(item, base, label = 'Écoute et écris') {
  return { ...base, type: 'write', label, prompt: { audio: item.es, autoplay: true, listenOnly: true }, accept: [item.es] };
}

function wordExercise(item, difficulty, showCaption) {
  const base = { item, difficulty, showCaption, answer: item.es, answerFr: item.fr, speakOnReveal: item.es };
  const r = Math.random();
  switch (difficulty) {
    case 0:
      if (r < 0.35) return trueFalse(item, base);
      return mcq(
        { ...base, label: 'Quelle image correspond ?', prompt: { text: item.es, audio: item.es, autoplay: true }, choiceStyle: 'image' },
        { art: item.art, label: item.fr, id: item.id },
        distractors(item, 3, (i) => i.art).map((d) => ({ art: d.art, label: d.fr, id: d.id })),
      );
    case 1:
      if (r < 0.35) {
        return mcq(
          { ...base, label: 'Écoute et choisis l\'image', prompt: { audio: item.es, autoplay: true, listenOnly: true }, choiceStyle: 'image' },
          { art: item.art, label: item.fr, id: item.id },
          distractors(item, 3, (i) => i.art).map((d) => ({ art: d.art, label: d.fr, id: d.id })),
        );
      }
      return mcq(
        { ...base, label: 'Quel est le mot ?', prompt: { art: item.art, caption: item.fr }, choiceStyle: 'text' },
        { label: item.es, id: item.id },
        distractors(item, 3, (i) => i.es).map((d) => ({ label: d.es, id: d.id })),
      );
    case 2:
      if (r < 0.25) return trueFalse(item, base);
      return spellExercise({ ...base, label: 'Épelle le mot', prompt: { art: item.art, caption: item.fr } }, item.es);
    default:
      if (r < 0.34) return { ...base, type: 'write', label: 'Écris en espagnol', prompt: { art: item.art, caption: item.fr, forceCaption: true } };
      if (r < 0.67) return dictation(item, base, 'Écoute et écris le mot');
      return mcq(
        { ...base, label: 'Écoute : que signifie ce mot ?', prompt: { audio: item.es, autoplay: true, listenOnly: true }, choiceStyle: 'text' },
        { label: item.fr, id: item.id },
        distractors(item, 3, (i) => i.fr).map((d) => ({ label: d.fr, id: d.id })),
      );
  }
}

// ── Phrases ──

/** Phrase à trou : on retire un mot et on le fait retrouver parmi d'autres. */
function phraseGap(item, base) {
  const words = item.es.split(' ');
  const candidates = words.map((w, i) => ({ w, i, clean: stripPunctuation(w) })).filter((x) => x.clean.length >= 3);
  if (words.length < 3 || !candidates.length) return null;
  const hole = pick(candidates);
  const others = shuffle([...new Set(itemsForLevel(item.level)
    .filter((i) => i.kind === 'phrase' && i.id !== item.id)
    .flatMap((i) => tokenize(i.es))
    .filter((t) => t.length >= 3 && t.toLowerCase() !== hole.clean.toLowerCase()))]).slice(0, 3);
  if (others.length < 3) return null;
  const prompt = words.map((w, i) => (i === hole.i ? w.replace(hole.clean, '___') : w)).join(' ');
  return {
    ...base,
    type: 'mcq',
    label: 'Complète la phrase',
    prompt: { text: prompt, blank: true, caption: item.fr },
    choiceStyle: 'text',
    choices: shuffle([{ label: hole.clean, correct: true }, ...others.map((o) => ({ label: o, correct: false }))]),
  };
}

function phraseExercise(item, difficulty) {
  const base = { item, difficulty, showCaption: false, answer: item.es, answerFr: item.fr, speakOnReveal: item.es };
  const r = Math.random();
  switch (difficulty) {
    case 0:
      return mcq(
        { ...base, label: 'Que signifie cette phrase ?', prompt: { text: item.es, audio: item.es, autoplay: true }, choiceStyle: 'text' },
        { label: item.fr, id: item.id },
        distractors(item, 3, (i) => i.fr).map((d) => ({ label: d.fr, id: d.id })),
      );
    case 1:
      if (r < 0.5) {
        const gap = phraseGap(item, base);
        if (gap) return gap;
      }
      return mcq(
        { ...base, label: 'Comment dit-on… ?', prompt: { text: item.fr, lang: 'fr' }, choiceStyle: 'text' },
        { label: item.es, id: item.id },
        distractors(item, 3, (i) => i.es).map((d) => ({ label: d.es, id: d.id })),
      );
    case 2:
      return buildExercise({ ...base, label: 'Traduis en espagnol', prompt: { text: item.fr, lang: 'fr' } }, item.es, item);
    default:
      if (r < 0.4 && tokenize(item.es).length <= 8) return dictation(item, base, 'Écoute et écris la phrase');
      return buildExercise(
        { ...base, label: 'Écoute et reconstitue la phrase', prompt: { audio: item.es, autoplay: true, listenOnly: true } },
        item.es,
        item,
      );
  }
}

// ── Grammaire ──

function quizSentence(q) {
  return q.prompt.replace('___', q.answer).replace(/\s*\([^)]*\)\s*$/, '');
}

const quizzesOf = (item) => item.quizzes || [item.quiz];
const questionsOf = (item) => item.questions || [item.question];

function grammarQuiz(item, withHint, q = pick(quizzesOf(item))) {
  const full = quizSentence(q);
  return {
    item,
    type: 'mcq',
    label: 'Complète la phrase',
    prompt: { text: q.prompt, blank: true, caption: withHint ? q.translation : null },
    choiceStyle: 'text',
    choices: shuffle(q.options.map((o) => ({ label: o, correct: o === q.answer }))),
    answer: full,
    answerFr: q.translation,
    speakOnReveal: full,
  };
}

/** Le trou est à écrire au clavier (seulement pour les réponses courtes et simples). */
function grammarTyped(item) {
  const typable = quizzesOf(item).filter((q) => !/[…/]/.test(q.answer) && q.answer.length <= 16);
  if (!typable.length) return null;
  const q = pick(typable);
  const full = quizSentence(q);
  return {
    item,
    type: 'write',
    label: 'Écris le mot qui manque',
    prompt: { text: q.prompt, blank: true, caption: q.translation },
    accept: [q.answer],
    answer: full,
    answerFr: q.translation,
    speakOnReveal: full,
  };
}

function grammarExercise(item, difficulty) {
  const buildFromExample = () => {
    const ex = pick(item.examples);
    return buildExercise(
      { item, label: 'Traduis en espagnol', prompt: { text: ex.fr, lang: 'fr' }, answer: ex.es, answerFr: ex.fr, speakOnReveal: ex.es },
      ex.es,
      item,
    );
  };
  const r = Math.random();
  if (difficulty === 0) return grammarQuiz(item, true);
  if (difficulty === 1) return r < 0.5 ? buildFromExample() : grammarQuiz(item, true);
  if (difficulty === 2) return grammarQuiz(item, false);
  if (r < 0.5) return grammarTyped(item) || grammarQuiz(item, false);
  return r < 0.75 ? buildFromExample() : grammarQuiz(item, false);
}

// ── Dialogues ──

function dialogueQuestion(item, listenOnly) {
  const q = pick(questionsOf(item));
  return {
    item,
    type: 'mcq',
    label: listenOnly ? 'Écoute le dialogue et réponds' : 'Lis le dialogue et réponds',
    prompt: { dialogue: item.lines, listenOnly, question: q.prompt, autoplayDialogue: listenOnly },
    choiceStyle: 'text',
    choices: shuffle(q.options.map((o) => ({ label: o, correct: o === q.answer }))),
    answer: q.answer,
    answerFr: null,
  };
}

function dialogueOrder(item) {
  return {
    item,
    type: 'order',
    label: 'Remets le dialogue dans l\'ordre',
    lines: item.lines,
    order: shuffle(item.lines.map((_, i) => i)),
    answer: item.lines.map((l) => l.es).join(' / '),
    answerFr: null,
  };
}

function dialogueExercise(item, difficulty) {
  const r = Math.random();
  if (difficulty === 0) {
    const line = pick(item.lines);
    const others = item.lines.filter((l) => l !== line).slice(0, 3);
    return {
      item,
      type: 'mcq',
      label: 'Que veut dire cette réplique ?',
      prompt: { text: line.es, audio: line.es, autoplay: true, speaker: line.speaker },
      choiceStyle: 'text',
      choices: shuffle([{ label: line.fr, correct: true }, ...others.map((l) => ({ label: l.fr, correct: false }))]),
      answer: line.es,
      answerFr: line.fr,
      speakOnReveal: line.es,
    };
  }
  if (difficulty === 1) return r < 0.4 && item.lines.length >= 4 ? dialogueOrder(item) : dialogueQuestion(item, false);
  if (difficulty === 2) {
    if (r < 0.3) return dialogueOrder(item);
    const shortLines = item.lines.filter((l) => tokenize(l.es).length <= 10);
    const line = pick(shortLines.length ? shortLines : item.lines);
    return buildExercise(
      { item, label: `Traduis la réplique de ${line.speaker}`, prompt: { text: line.fr, lang: 'fr' }, answer: line.es, answerFr: line.fr, speakOnReveal: line.es },
      line.es,
      item,
    );
  }
  return dialogueQuestion(item, true);
}

/**
 * Crée un exercice pour `item`.
 * @param {number} difficulty 0 à 3
 * @param {boolean} showCaption afficher la légende française sous les images
 */
export function makeExercise(item, difficulty, showCaption = true) {
  const d = Math.max(0, Math.min(3, difficulty));
  let ex;
  if (item.kind === 'word') ex = wordExercise(item, d, showCaption);
  else if (item.kind === 'phrase') ex = phraseExercise(item, d);
  else if (item.kind === 'grammar') ex = grammarExercise(item, d);
  else ex = dialogueExercise(item, d);
  return { showCaption, difficulty: d, ...ex, uid: Math.random().toString(36).slice(2) };
}

/** Jeu des paires : associer 4 à 5 éléments espagnols à leur sens (dessin ou traduction). */
export function makePairs(items) {
  const chosen = sample(items.filter((i) => i.kind === 'word' || i.kind === 'phrase'), 5);
  if (chosen.length < 3) return null;
  const withArt = chosen.every((i) => i.kind === 'word');
  return {
    type: 'pairs',
    label: 'Associe les paires',
    item: null,
    pairs: chosen.map((i) => ({ id: i.id, es: i.es, fr: i.fr, art: withArt ? i.art : null })),
    left: shuffle(chosen.map((i) => i.id)),
    right: shuffle(chosen.map((i) => i.id)),
    answer: null,
    answerFr: null,
    uid: Math.random().toString(36).slice(2),
  };
}

/** Vérifie une réponse écrite (une ou plusieurs réponses acceptées). Renvoie { correct, note }. Les accents oubliés sont tolérés. */
export function checkWritten(input, expected) {
  const a = normalizeAnswer(input);
  if (!a) return { correct: false };
  const accepted = Array.isArray(expected) ? expected : [expected];
  if (accepted.some((e) => normalizeAnswer(e) === a)) return { correct: true };
  const close = accepted.find((e) => removeAccents(normalizeAnswer(e)) === removeAccents(a));
  if (close) return { correct: true, note: `Attention aux accents : ${close}` };
  return { correct: false };
}

/** Vérifie une phrase reconstruite (sans tenir compte de la casse). */
export function checkBuilt(words, expectedTokens) {
  return words.length === expectedTokens.length && words.every((w, i) => w.toLowerCase() === expectedTokens[i].toLowerCase());
}
