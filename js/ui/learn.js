// Onglet « Apprendre » : objectif du jour, série, leçon conseillée et thèmes par niveau.
import { h, plural } from '../util.js';
import { LEVELS, LEVEL_INFO, themesForLevel } from '../content.js';
import * as store from '../store.js';
import { art, icon, logo, ring } from './components.js';

export function learnView(ctx) {
  const s = store.state;
  const streak = store.currentStreak();
  const minutes = Math.floor(store.todaySeconds() / 60);
  const due = store.dueItems().length;
  const suggested = store.suggestedTheme();

  const hero = h('section', { class: 'hero', style: { '--theme': suggested?.color || '#E4007C' } },
    h('div', { class: 'hero-goal' },
      ring(store.goalRatio(), { size: 84, stroke: 9, color: '#FFFFFF', track: 'rgba(255,255,255,.25)', content: store.goalRatio() >= 1 ? '✓' : `${minutes}′` }),
      h('div', {},
        h('p', { class: 'hero-label' }, store.goalRatio() >= 1 ? 'Objectif du jour atteint !' : 'Objectif du jour'),
        h('p', { class: 'hero-value' }, `${minutes} / ${s.dailyGoal} min`))),
    suggested
      ? h('button', { class: 'btn btn-light hero-cta', onclick: () => ctx.startLesson({ mode: 'theme', theme: suggested }) },
        art(suggested.art, 'cta-art'),
        h('span', {}, h('strong', {}, 'Leçon de 5 min'), h('small', {}, suggested.titleEs)))
      : h('p', {}, 'Tu as tout appris ! Continue tes révisions.'));

  const reviewCard = due
    ? h('button', { class: 'review-banner', onclick: () => ctx.startLesson({ mode: 'review' }) },
      art('ui-review', 'banner-art'),
      h('span', {}, h('strong', {}, plural(due, 'élément'), ' à réviser'), h('small', {}, 'Ne laisse pas tes mots s\'envoler !')),
      icon('play'))
    : null;

  const levels = LEVELS.map((level) => {
    const progress = store.levelProgress(level);
    const isCurrent = level === s.level;
    return h('section', { class: `level-section ${isCurrent ? 'current' : ''}` },
      h('div', { class: 'level-head' },
        h('h2', {}, h('span', { class: 'level-badge' }, level), ` ${LEVEL_INFO[level].name}`),
        isCurrent ? h('span', { class: 'pill' }, 'Ton niveau') : null,
        h('span', { class: 'muted small' }, `${Math.round(progress.ratio * 100)} %`)),
      h('div', { class: 'progress-line' }, h('i', { style: { width: `${progress.ratio * 100}%` } })),
      h('div', { class: 'theme-grid' }, themesForLevel(level).map((theme) => themeCard(theme, ctx))));
  });

  return h('div', { class: 'screen learn' },
    h('header', { class: 'home-head' },
      h('div', { class: 'brand-row' }, logo(40), h('span', { class: 'brand' }, 'Órale')),
      h('div', { class: 'counters' },
        h('span', { class: `counter streak ${streak ? 'on' : ''}`, title: 'Série de jours' }, icon('flame'), ` ${streak}`),
        h('span', { class: 'counter xp', title: 'Points d\'expérience' }, icon('star'), ` ${s.xp}`))),
    hero,
    reviewCard,
    levels);
}

function themeCard(theme, ctx) {
  const p = store.themeProgress(theme);
  return h('button', { class: 'theme-card', style: { '--theme': theme.color }, onclick: () => ctx.openTheme(theme) },
    h('div', { class: 'theme-art' },
      ring(p.ratio, { size: 64, stroke: 5, color: '#fff', track: 'rgba(255,255,255,.25)', content: art(theme.art, 'theme-art-svg') })),
    h('strong', {}, theme.titleEs),
    h('small', {}, theme.titleFr),
    p.learned === p.total ? h('span', { class: 'done-badge' }, '✓') : null);
}
