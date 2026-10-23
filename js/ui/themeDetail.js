// Fiche d'un thème : contenu, maîtrise de chaque élément, lancement d'une leçon.
import { h } from '../util.js';
import { KIND_LABEL, LEVEL_INFO } from '../content.js';
import * as store from '../store.js';
import { speak } from '../speech.js';
import { art, header, ring, sheet, speakerButton, stageDots } from './components.js';
import { itemCardContent } from './cards.js';
import { ITEMS_PER_LESSON } from '../lesson.js';

const KINDS = [
  ['word', 'Mots'],
  ['phrase', 'Phrases'],
  ['grammar', 'Grammaire'],
  ['dialogue', 'Dialogue'],
];

export function themeDetailView(theme, ctx) {
  const p = store.themeProgress(theme);
  const remaining = p.total - p.learned;
  const lessons = Math.ceil(p.total / ITEMS_PER_LESSON);
  const lessonNo = Math.min(lessons, Math.floor(p.learned / ITEMS_PER_LESSON) + 1);

  const sections = KINDS.map(([kind, title]) => {
    const items = theme.items.filter((i) => i.kind === kind);
    return h('section', { class: 'item-section' },
      h('h3', {}, title),
      h('div', { class: 'item-list' }, items.map((item) => itemRow(item))));
  });

  return h('div', { class: 'screen theme-detail', style: { '--theme': theme.color } },
    header('', { onBack: ctx.back }),
    h('div', { class: 'theme-hero' },
      ring(p.ratio, { size: 110, stroke: 8, color: '#fff', track: 'rgba(255,255,255,.25)', content: art(theme.art, 'theme-hero-art') }),
      h('h1', {}, theme.titleEs),
      h('p', {}, theme.titleFr),
      h('p', { class: 'small' }, `${theme.level} · ${LEVEL_INFO[theme.level].name} · ${p.learned}/${p.total} appris`),
      h('div', { class: 'theme-actions' },
        remaining
          ? h('button', { class: 'btn btn-light', onclick: () => ctx.startLesson({ mode: 'theme', theme }) }, `Leçon ${lessonNo}/${lessons}`)
          : h('p', { class: 'small' }, 'Tout est appris ✓'),
        p.learned >= 4
          ? h('button', { class: 'btn btn-ghost-light', onclick: () => ctx.startLesson({ mode: 'practice', theme }) }, 'S\'entraîner')
          : null)),
    sections);
}

function itemRow(item) {
  const stage = store.stageOf(item.id);
  const label = item.kind === 'grammar' || item.kind === 'dialogue' ? item.fr : item.es;
  const sub = item.kind === 'grammar' ? item.es : item.kind === 'dialogue' ? item.es : item.fr;
  return h('div', {
    class: `item-row ${stage ? '' : 'unlearned'}`,
    role: 'button',
    tabindex: '0',
    onclick: () => {
      if (item.kind === 'word' || item.kind === 'phrase') speak(item.es);
      sheet(h('div', { class: `present present-${item.kind} in-sheet` }, itemCardContent(item)), { title: KIND_LABEL[item.kind] });
    },
  },
  art(item.art, 'row-art'),
  h('span', { class: 'item-text' }, h('strong', {}, label), h('small', {}, sub)),
  stageDots(stage),
  item.kind === 'word' || item.kind === 'phrase' ? speakerButton(item.es) : null);
}
