// Cartes de présentation d'un élément (nouveau mot, phrase, grammaire, dialogue).
import { h } from '../util.js';
import { speak, speakLines } from '../speech.js';
import { icon, speakerButton } from './components.js';

function wordCard(item) {
  return [
    h('div', { class: 'art art-big' }, h('span', { class: 'emoji' }, item.emoji)),
    h('div', { class: 'term-row' }, h('h2', { class: 'term' }, item.es), speakerButton(item.es)),
    h('p', { class: 'translation' }, item.fr),
    item.note ? h('p', { class: 'note' }, '💡 ', item.note) : null,
  ];
}

function phraseCard(item) {
  return [
    h('div', { class: 'term-row' }, h('h2', { class: 'term phrase' }, item.es), speakerButton(item.es)),
    h('p', { class: 'translation' }, item.fr),
    item.note ? h('p', { class: 'note' }, '💡 ', item.note) : null,
  ];
}

function grammarCard(item) {
  return [
    h('h2', { class: 'grammar-title' }, item.fr),
    h('p', { class: 'grammar-es' }, item.es),
    h('p', { class: 'explanation' }, item.explanation),
    h('div', { class: 'examples' },
      item.examples.map((ex) =>
        h('div', { class: 'example' },
          h('div', {}, h('p', { class: 'es' }, ex.es), h('p', { class: 'fr' }, ex.fr)),
          speakerButton(ex.es)))),
  ];
}

function dialogueCard(item) {
  const speakers = [...new Set(item.lines.map((l) => l.speaker))];
  const bubbles = item.lines.map((line) =>
    h('button', {
      class: `bubble ${speakers.indexOf(line.speaker) % 2 ? 'right' : 'left'}`,
      onclick: () => speak(line.es, { speaker: speakers.indexOf(line.speaker) }),
    },
    h('span', { class: 'who' }, line.speaker),
    h('span', { class: 'es' }, line.es),
    h('span', { class: 'fr' }, line.fr)));
  const playBtn = h('button', {
    class: 'btn btn-ghost play-dialogue',
    onclick: () => {
      playBtn.classList.add('playing');
      speakLines(item.lines, (i) => {
        bubbles.forEach((b, j) => b.classList.toggle('active', j === i));
        if (i >= 0) bubbles[i].scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        else playBtn.classList.remove('playing');
      });
    },
  }, icon('play'), ' Écouter le dialogue');
  return [
    h('h2', { class: 'grammar-title' }, item.es),
    h('p', { class: 'grammar-es' }, item.fr),
    playBtn,
    h('div', { class: 'transcript' }, bubbles),
  ];
}

const TAGS = { word: 'Nouveau mot', phrase: 'Nouvelle phrase', grammar: 'Point de grammaire', dialogue: 'Dialogue' };

/** Contenu d'une carte de présentation pour un élément. */
export function itemCardContent(item) {
  if (item.kind === 'word') return wordCard(item);
  if (item.kind === 'phrase') return phraseCard(item);
  if (item.kind === 'grammar') return grammarCard(item);
  return dialogueCard(item);
}

/** Carte affichée dans une leçon quand un élément est présenté pour la première fois. */
export function presentationView(item, onContinue) {
  if (item.kind === 'word' || item.kind === 'phrase') setTimeout(() => speak(item.es), 350);
  return h('div', { class: `present present-${item.kind}` },
    h('span', { class: 'tag' }, TAGS[item.kind]),
    h('div', { class: 'present-body' }, itemCardContent(item)),
    h('div', { class: 'actions' }, h('button', { class: 'btn btn-primary', onclick: onContinue }, item.kind === 'grammar' ? 'J\'ai compris' : 'C\'est noté !')));
}
