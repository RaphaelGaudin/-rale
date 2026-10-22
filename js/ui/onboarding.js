// Accueil, test de niveau adaptatif et choix de l'objectif quotidien.
import { h, plural } from '../util.js';
import { itemsForLevel } from '../content.js';
import { LEVELS, LEVEL_INFO } from '../content.js';
import { PlacementTest, QUESTIONS_PER_LEVEL, PASS_MARK, SKILLS } from '../placement.js';
import * as store from '../store.js';
import { play } from '../sound.js';
import { art, logo } from './components.js';
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
          h('li', {}, art('taco'), '32 thèmes de la vie au Mexique'),
          h('li', {}, art('ui-speaker'), 'Des voix en espagnol à chaque mot'),
          h('li', {}, art('ui-brain'), 'Répétition espacée pour ne rien oublier')),
        h('div', { class: 'actions stack' },
          h('button', { class: 'btn btn-primary', onclick: intro }, 'Faire le test de niveau'),
          h('button', { class: 'btn btn-ghost', onclick: () => result('A1', true) }, 'Je débute complètement'))));
  }

  function intro() {
    root.replaceChildren(
      h('div', { class: 'result test-intro' },
        art('ui-brain', 'big-art pop'),
        h('h1', { class: 'level-title small-title' }, 'Test de niveau'),
        h('ul', { class: 'perks' },
          h('li', {}, art('ui-calendar'), `${QUESTIONS_PER_LEVEL} questions par niveau, de A1 à B2 : vocabulaire, grammaire, lecture et écoute.`),
          h('li', {}, art('ui-trophy'), `Avec ${PASS_MARK} bonnes réponses sur ${QUESTIONS_PER_LEVEL}, tu passes au niveau suivant.`),
          h('li', {}, art('ui-bulb'), 'Tu ne sais pas ? Touche « Je ne sais pas » plutôt que de deviner : le résultat sera plus juste.')),
        h('p', { class: 'muted small' }, 'Entre 3 et 10 minutes. Monte le son pour les questions d\'écoute.'),
        h('div', { class: 'actions stack' },
          h('button', { class: 'btn btn-primary', onclick: test }, 'C\'est parti'),
          h('button', { class: 'btn btn-ghost', onclick: welcome }, 'Retour'))));
  }

  function test() {
    const placement = new PlacementTest();
    root.placement = placement; // accès pour les tests automatisés

    const next = (delay) => setTimeout(() => {
      const previousLevel = placement.level;
      if (placement.advance()) return result(placement.result, false, placement);
      if (placement.level !== previousLevel) return levelPassed(previousLevel, placement, ask);
      ask();
    }, delay);

    const ask = () => {
      const ex = placement.question;
      let answered = false;
      const levelBadges = h('div', { class: 'level-steps' },
        LEVELS.map((l, i) => h('span', { class: i < placement.levelIndex ? 'done' : i === placement.levelIndex ? 'current' : '' }, l)));
      const dots = h('div', { class: 'q-dots' },
        Array.from({ length: QUESTIONS_PER_LEVEL }, (_, i) => h('i', { class: i < placement.index ? 'done' : i === placement.index ? 'current' : '' })));
      const view = exerciseView(ex, (correct) => {
        if (answered) return;
        answered = true;
        skip.remove();
        placement.answer(correct);
        play(correct ? 'correct' : 'wrong');
        next(correct ? 700 : 1500);
      });
      const skip = h('button', {
        class: 'btn btn-ghost small dont-know',
        onclick: () => {
          if (answered) return;
          answered = true;
          skip.remove();
          // On montre la bonne réponse, sans pénalité sonore.
          view.querySelectorAll('.choice').forEach((b, i) => b.classList.add(ex.choices[i].correct ? 'correct' : 'dim'));
          view.classList.add('locked');
          placement.answer(false);
          next(1400);
        },
      }, 'Je ne sais pas');
      view.classList.add('card-enter');
      root.replaceChildren(
        h('div', { class: 'placement' },
          h('div', { class: 'placement-head' },
            h('button', { class: 'link', onclick: welcome }, 'Annuler'),
            h('span', { class: 'muted' }, `Niveau ${placement.level} · ${placement.index + 1}/${QUESTIONS_PER_LEVEL}`)),
          levelBadges, dots, view, h('div', { class: 'actions' }, skip)));
    };
    ask();
  }

  function levelPassed(level, placement, then) {
    const s = placement.scores[level];
    play('learned');
    root.replaceChildren(
      h('div', { class: 'result level-passed' },
        art('ui-trophy', 'big-art pop'),
        h('h1', { class: 'level-title small-title' }, `${level} validé !`),
        h('p', { class: 'muted' }, `${s.correct}/${s.asked} bonnes réponses. On passe au niveau ${placement.level}.`)));
    setTimeout(then, 1600);
  }

  function result(level, skipped, placement = null) {
    let goal = store.state.dailyGoal;
    let seed = true;
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
    const passed = placement?.passed || [];
    const seedCount = passed.reduce((n, l) => n + itemsForLevel(l).length, 0);

    const levelRows = placement
      ? h('div', { class: 'score-table' },
        LEVELS.filter((l) => placement.scores[l]).map((l) => {
          const sc = placement.scores[l];
          const ok = passed.includes(l);
          return h('div', { class: `score-row ${ok ? 'ok' : 'ko'}` },
            h('strong', {}, l),
            h('div', { class: 'score-bar' }, h('i', { style: { width: `${(sc.correct / QUESTIONS_PER_LEVEL) * 100}%` } })),
            h('span', {}, `${sc.correct}/${sc.asked}`, ok ? ' ✓' : ''));
        }))
      : null;
    const skillRows = placement
      ? h('div', { class: 'skill-grid' },
        Object.entries(SKILLS).filter(([k]) => placement.skills[k].asked).map(([k, label]) => {
          const sk = placement.skills[k];
          return h('div', { class: 'skill' }, h('strong', {}, `${Math.round((sk.correct / sk.asked) * 100)} %`), h('span', {}, label));
        }))
      : null;
    const seedSwitch = passed.length
      ? h('div', { class: 'setting seed-setting' },
        h('span', {}, `Ajouter ${passed.join(' et ')} à mes révisions`, h('small', {}, `${plural(seedCount, 'élément')}, étalés sur 3 semaines, pour confirmer tes acquis.`)),
        h('button', {
          class: 'switch on', role: 'switch', 'aria-checked': 'true',
          onclick: (e) => { seed = !seed; e.currentTarget.classList.toggle('on', seed); e.currentTarget.setAttribute('aria-checked', String(seed)); },
        }, h('i')))
      : null;

    root.replaceChildren(
      h('div', { class: 'result' },
        art(info.art, 'big-art pop'),
        h('p', { class: 'muted' }, skipped ? 'On commence par les bases' : 'Ton niveau'),
        h('h1', { class: 'level-title' }, level, h('span', {}, ` · ${info.name}`)),
        h('p', {}, info.blurb),
        levelRows,
        skillRows,
        seedSwitch,
        h('h3', {}, 'Ton objectif quotidien'),
        h('div', { class: 'goal-chips' }, goalButtons),
        h('div', { class: 'actions' },
          h('button', {
            class: 'btn btn-primary',
            onclick: () => {
              store.update({ onboarded: true, level, placement: skipped ? null : level, dailyGoal: goal });
              if (seed && passed.length) store.seedKnownLevels(passed);
              play('complete');
              onDone();
            },
          }, '¡Vámonos!'))));
    window.scrollTo(0, 0);
  }

  welcome();
  return root;
}
