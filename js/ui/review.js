// Onglet « Révisions » : ce qui est à revoir aujourd'hui et la prévision sur 7 jours.
import { h, plural, weekdayShort } from '../util.js';
import { themesById } from '../content.js';
import * as store from '../store.js';
import { MASTERED_STAGE, INTERVALS } from '../srs.js';
import { speak } from '../speech.js';
import { header, stageDots } from './components.js';

export function reviewView(ctx) {
  const due = store.dueItems();
  const forecast = store.forecast(7);
  const max = Math.max(1, ...forecast.map((d) => d.count));
  const learned = store.learnedItems();
  const mastered = learned.filter((i) => store.stageOf(i.id) >= MASTERED_STAGE).length;

  const chart = h('div', { class: 'forecast' },
    forecast.map((d, i) =>
      h('div', { class: `bar-col ${i === 0 ? 'today' : ''}` },
        h('span', { class: 'bar-value' }, d.count || ''),
        h('div', { class: 'bar-track' }, h('div', { class: 'bar', style: { height: `${(d.count / max) * 100}%` } })),
        h('span', { class: 'bar-label' }, i === 0 ? 'Auj.' : i === 1 ? 'Dem.' : weekdayShort(d.date)))));

  // Éléments du jour, regroupés par thème.
  const groups = new Map();
  for (const item of due) {
    if (!groups.has(item.themeId)) groups.set(item.themeId, []);
    groups.get(item.themeId).push(item);
  }

  const dueList = due.length
    ? [...groups.entries()].map(([themeId, items]) => {
      const theme = themesById.get(themeId);
      return h('section', { class: 'due-group', style: { '--theme': theme.color } },
        h('h3', {}, h('span', { class: 'emoji' }, theme.emoji), ` ${theme.titleEs}`, h('span', { class: 'muted small' }, ` · ${items.length}`)),
        h('div', { class: 'item-list' }, items.map((item) =>
          h('div', { class: 'item-row', role: 'button', tabindex: '0', onclick: () => item.kind !== 'dialogue' && item.kind !== 'grammar' && speak(item.es) },
            h('span', { class: 'emoji' }, item.emoji),
            h('span', { class: 'item-text' },
              h('strong', {}, item.kind === 'grammar' || item.kind === 'dialogue' ? item.fr : item.es),
              h('small', {}, item.kind === 'grammar' || item.kind === 'dialogue' ? item.es : item.fr)),
            stageDots(store.stageOf(item.id))))));
    })
    : h('div', { class: 'empty' },
      h('div', { class: 'big-emoji' }, learned.length ? '😎' : '🌱'),
      h('p', {}, learned.length ? 'Rien à réviser aujourd\'hui. ¡Qué chido!' : 'Apprends tes premiers mots : ils apparaîtront ici quand il sera temps de les revoir.'));

  return h('div', { class: 'screen review' },
    header('Révisions'),
    h('section', { class: 'review-hero' },
      h('div', { class: 'due-count' }, h('strong', {}, due.length), h('span', {}, due.length > 1 ? 'éléments à revoir aujourd\'hui' : 'élément à revoir aujourd\'hui')),
      h('button', { class: 'btn btn-primary', disabled: !due.length, onclick: () => ctx.startLesson({ mode: 'review' }) }, due.length ? 'Réviser maintenant' : 'À jour ✓')),
    h('section', { class: 'card' },
      h('h3', {}, 'Les 7 prochains jours'),
      chart,
      h('p', { class: 'muted small' }, `Chaque élément revient après ${INTERVALS.slice(0, 5).join(', ')} jours… Une erreur le fait redescendre d'une étape.`)),
    h('div', { class: 'mini-stats' },
      h('div', {}, h('strong', {}, learned.length), h('span', {}, 'appris')),
      h('div', {}, h('strong', {}, mastered), h('span', {}, 'maîtrisés')),
      h('div', {}, h('strong', {}, forecast.slice(1).reduce((n, d) => n + d.count, 0)), h('span', {}, 'cette semaine'))),
    due.length ? h('h2', { class: 'section-title' }, `Aujourd'hui · ${plural(due.length, 'élément')}`) : null,
    dueList);
}
