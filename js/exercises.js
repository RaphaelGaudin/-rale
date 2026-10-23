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

function wordExercise(item, difficulty, showCaption) {
  const base = { item, difficulty, showCaption, answer: item.es, answerFr: item.fr, speakOnReveal: item.es };
  switch (difficulty) {
    case 0:
      return mcq(
        { ...base, label: 'Quelle image correspond ?', prompt: { text: item.es, audio: item.es, autoplay: true }, choiceStyle: 'image' },
        { art: item.art, label: item.fr, id: item.id },
        distractors(item, 3, (i) => i.art).map((d) => ({ art: d.art, label: d.fr, id: d.id })),
      );
    case 1:
      return mcq(
        { ...base, label: 'Quel est le mot ?', prompt: { art: item.art, caption: item.fr }, choiceStyle: 'text' },
        { label: item.es, id: item.id },
        distractors(item, 3, (i) => i.es).map((d) => ({ label: d.es, id: d.id })),
      );
    case 2:
      return spellExercise(
        { ...base, label: 'Épelle le mot', prompt: { art: item.art, caption: item.fr } },
        item.es,
      );
    default:
      if (Math.random() < 0.5) {
        return {
          ...base,
          type: 'write',
          label: 'Écris en espagnol',
          prompt: { art: item.art, caption: item.fr, forceCaption: true },
        };
      }
      return mcq(
        { ...base, label: 'Écoute : que signifie ce mot ?', prompt: { audio: item.es, autoplay: true, listenOnly: true }, choiceStyle: 'text' },
        { label: item.fr, id: item.id },
        distractors(item, 3, (i) => i.fr).map((d) => ({ label: d.fr, id: d.id })),
      );
  }
}

// ── Phrases ──

function phraseExercise(item, difficulty) {
  const base = { item, difficulty, showCaption: false, answer: item.es, answerFr: item.fr, speakOnReveal: item.es };
  switch (difficulty) {
    case 0:
      return mcq(
        { ...base, label: 'Que signifie cette phrase ?', prompt: { text: item.es, audio: item.es, autoplay: true }, choiceStyle: 'text' },
        { label: item.fr, id: item.id },
        distractors(item, 3, (i) => i.fr).map((d) => ({ label: d.fr, id: d.id })),
      );
    case 1:
      return mcq(
        { ...base, label: 'Comment dit-on… ?', prompt: { text: item.fr, lang: 'fr' }, choiceStyle: 'text' },
        { label: item.es, id: item.id },
        distractors(item, 3, (i) => i.es).map((d) => ({ label: d.es, id: d.id })),
      );
    case 2:
      return buildExercise({ ...base, label: 'Traduis en espagnol', prompt: { text: item.fr, lang: 'fr' } }, item.es, item);
    default:
      return buildExercise(
        { ...base, label: 'Écoute et reconstitue la phrase', prompt: { audio: item.es, autoplay: true, listenOnly: true } },
        item.es,
        item,
      );
  }
}

// ── Grammaire ──

function grammarQuiz(item, withHint) {
  const q = item.quiz;
  const full = q.prompt.replace('___', q.answer).replace(/\s*\([^)]*\)\s*$/, '');
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

function grammarExercise(item, difficulty) {
  const buildFromExample = () => {
    const ex = pick(item.examples);
    return buildExercise(
      { item, label: 'Traduis en espagnol', prompt: { text: ex.fr, lang: 'fr' }, answer: ex.es, answerFr: ex.fr, speakOnReveal: ex.es },
      ex.es,
      item,
    );
  };
  if (difficulty === 0) return grammarQuiz(item, true);
  if (difficulty === 1) return buildFromExample();
  if (difficulty === 2) return grammarQuiz(item, false);
  return Math.random() < 0.5 ? grammarQuiz(item, false) : buildFromExample();
}

// ── Dialogues ──

function dialogueExercise(item, difficulty) {
  const q = item.question;
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
  if (difficulty === 2) {
    const shortLines = item.lines.filter((l) => tokenize(l.es).length <= 10);
    const line = pick(shortLines.length ? shortLines : item.lines);
    return buildExercise(
      { item, label: `Traduis la réplique de ${line.speaker}`, prompt: { text: line.fr, lang: 'fr' }, answer: line.es, answerFr: line.fr, speakOnReveal: line.es },
      line.es,
      item,
    );
  }
  const listenOnly = difficulty >= 3;
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
