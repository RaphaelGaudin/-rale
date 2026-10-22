// Accueil, test de niveau adaptatif et choix de l'objectif quotidien.
import { h } from '../util.js';
import { LEVELS, LEVEL_INFO } from '../content.js';
import { PlacementTest, QUESTIONS_PER_LEVEL } from '../placement.js';
import * as store from '../store.js';
import { play } from '../sound.js';
import { logo } from './components.js';
import { exerciseView } from './exerciseView.js';

export function onboardingView({ onDone }) {
  const root = h('div', { class: 'onboarding' });

  function welcome() {
    root.replaceChildren(
      h('div', { class: 'welcome' },
        h('div', { class: 'welcome-logo pop' }, logo(150)),
        h('h1', { class: 'brand' }, 'Órale'),
        h('p', { class: 'tagline' }, 'L\'espagnol du Mexique,', h('br'), 'cinq minutes par jour.'),
        h('ul', { class: 'perks' },
          h('li', {}, '🌮 32 thèmes de la vie au Mexique'),
          h('li', {}, '🔊 Une voix à l\'accent mexicain'),
          h('li', {}, '🧠 Répétition espacée pour ne rien oublier')),
        h('div', { class: 'actions stack' },
          h('button', { class: 'btn btn-primary', onclick: test }, 'Faire le test de niveau'),
          h('button', { class: 'btn btn-ghost', onclick: () => result('A1', true) }, 'Je débute complètement'))));
  }

  function test() {
    const placement = new PlacementTest();
    const ask = () => {
      const ex = placement.question;
      const levelBadges = h('div', { class: 'level-steps' },
        LEVELS.map((l, i) => h('span', { class: i < placement.levelIndex ? 'done' : i === placement.levelIndex ? 'current' : '' }, l)));
      const dots = h('div', { class: 'q-dots' },
        Array.from({ length: QUESTIONS_PER_LEVEL }, (_, i) => h('i', { class: i < placement.index ? 'done' : i === placement.index ? 'current' : '' })));
      const view = exerciseView(ex, (correct) => {
        placement.answer(correct);
        play(correct ? 'correct' : 'wrong');
        setTimeout(() => {
          if (placement.advance()) result(placement.result, false, placement.scores);
          else ask();
        }, correct ? 800 : 1500);
      });
      view.classList.add('card-enter');
      root.replaceChildren(
        h('div', { class: 'placement' },
          h('div', { class: 'placement-head' },
            h('button', { class: 'link', onclick: welcome }, 'Annuler'),
            h('span', { class: 'muted' }, `Niveau ${placement.level} · question ${placement.index + 1}/${QUESTIONS_PER_LEVEL}`)),
          levelBadges, dots, view));
    };
    ask();
  }

  function result(level, skipped, scores = {}) {
    let goal = store.state.dailyGoal;
    const goals = [5, 10, 15, 20];
    const goalButtons = goals.map((g) =>
      h('button', {
        class: `goal-chip ${g === goal ? 'on' : ''}`,
        onclick: (e) => {
          goal = g;
          goalButtons.forEach((b) => b.classList.remove('on'));
          e.currentTarget.classList.add('on');
        },
      }, h('strong', {}, `${g} min`), h('span', {}, g === 5 ? 'Tranquilo' : g === 10 ? 'Régulier' : g === 15 ? 'Sérieux' : 'Intense')));
    const info = LEVEL_INFO[level];
    root.replaceChildren(
      h('div', { class: 'result' },
        h('div', { class: 'big-emoji pop' }, info.emoji),
        h('p', { class: 'muted' }, skipped ? 'On commence par les bases' : 'Ton niveau'),
        h('h1', { class: 'level-title' }, level, h('span', {}, ` · ${info.name}`)),
        h('p', {}, info.blurb),
        !skipped
          ? h('div', { class: 'scores' }, Object.entries(scores).map(([l, s]) => h('span', { class: s >= 3 ? 'ok' : 'ko' }, `${l} : ${s}/4`)))
          : null,
        h('h3', {}, 'Ton objectif quotidien'),
        h('div', { class: 'goal-chips' }, goalButtons),
        h('div', { class: 'actions' },
          h('button', {
            class: 'btn btn-primary',
            onclick: () => {
              store.update({ onboarded: true, level, placement: skipped ? null : level, dailyGoal: goal });
              play('complete');
              onDone();
            },
          }, '¡Vámonos!'))));
  }

  welcome();
  return root;
}
