// Écran de leçon : chrono de 5 minutes, exercices, retours, combos et bilan.
import { h, formatDuration, plural } from '../util.js';
import { Lesson, SESSION_SECONDS } from '../lesson.js';
import { itemsById, LEVEL_INFO } from '../content.js';
import * as store from '../store.js';
import { speak, stop } from '../speech.js';
import { art, icon, ring } from './components.js';
import { exerciseView } from './exerciseView.js';
import { presentationView } from './cards.js';

const PRAISE = ['¡Muy bien!', '¡Órale!', '¡Excelente!', '¡Qué padre!', '¡Bien hecho!', '¡Eso!', '¡Chido!'];
const OOPS = ['Casi…', '¡Ups!', 'No pasa nada'];

export function lessonView({ mode, theme, onExit }) {
  const color = theme?.color || '#7B2CBF';
  const root = h('div', { class: 'lesson', style: { '--theme': color } });
  let timer = null;
  let autoAdvance = null;
  let shownCurrent = null;

  const exit = () => {
    clearInterval(timer);
    clearTimeout(autoAdvance);
    stop();
    onExit();
  };

  const lesson = new Lesson({ mode, theme, onChange: () => update() });
  root.lesson = lesson; // accès pour les tests automatisés

  if (lesson.isEmpty) {
    root.append(
      h('div', { class: 'lesson-empty' },
        art(mode === 'review' ? 'chido' : 'ui-trophy', 'big-art'),
        h('h2', {}, mode === 'review' ? 'Rien à réviser aujourd\'hui' : 'Thème terminé !'),
        h('p', { class: 'muted' }, mode === 'review'
          ? 'Tout est à jour. Reviens demain, ou apprends de nouveaux mots.'
          : 'Tu as appris tous les éléments de ce thème. Ils reviendront dans tes révisions.'),
        h('button', { class: 'btn btn-primary', onclick: exit }, 'Retour')),
    );
    return root;
  }

  // ── Barre du haut ──
  const bar = h('div', { class: 'time-bar' }, h('div', { class: 'time-fill' }));
  const clock = h('span', { class: 'clock' }, formatDuration(SESSION_SECONDS));
  const comboChip = h('span', { class: 'combo-chip' });
  const quit = () => {
    if (lesson.answerCount > 0 && !lesson.finished && !confirm('Quitter la leçon ? Ce que tu as appris est conservé.')) return;
    lesson.quit();
    exit();
  };
  const top = h('div', { class: 'lesson-top' },
    h('button', { class: 'icon-btn', onclick: quit, 'aria-label': 'Quitter' }, icon('close')),
    bar, clock, comboChip);
  const stage = h('div', { class: 'lesson-stage' });
  const feedbackZone = h('div', { class: 'feedback-zone' });
  const comboBurst = h('div', { class: 'combo-burst' });
  root.append(top, stage, feedbackZone, comboBurst);

  const tick = () => {
    const ratio = lesson.elapsed / SESSION_SECONDS;
    bar.firstChild.style.width = `${Math.min(100, ratio * 100)}%`;
    clock.textContent = lesson.remaining > 0 ? formatDuration(lesson.remaining) : 'Fin !';
    root.classList.toggle('overtime', lesson.remaining <= 0);
  };

  function renderCombo() {
    comboChip.replaceChildren(...(lesson.combo >= 2 ? [icon('flame'), ` ${lesson.combo}`] : []));
    comboChip.classList.toggle('on', lesson.combo >= 2);
  }

  function showCurrent() {
    const { item, exercise } = lesson.current;
    const view = exercise
      ? exerciseView(exercise, (correct, note) => lesson.answer(correct, note))
      : presentationView(item, () => lesson.next());
    view.classList.add('card-enter');
    stage.replaceChildren(view);
    stage.scrollTop = 0;
  }

  function showFeedback(fb) {
    const good = fb.correct;
    const title = good ? PRAISE[Math.floor(Math.random() * PRAISE.length)] : OOPS[Math.floor(Math.random() * OOPS.length)];
    const extra = [];
    if (fb.justLearned) extra.push(h('p', { class: 'fb-learned' }, art('ui-star', 'inline'), 'Appris ! Il reviendra demain en révision.'));
    if (fb.note) extra.push(h('p', { class: 'fb-note' }, fb.note));
    const banner = h('div', { class: `feedback ${good ? 'good' : 'bad'}` },
      h('div', { class: 'fb-head' }, h('strong', {}, title), good ? icon('check') : null),
      !good || fb.note ? h('div', { class: 'fb-answer' }, h('p', { class: 'es' }, fb.answer), fb.answerFr ? h('p', { class: 'fr' }, fb.answerFr) : null) : null,
      extra,
      h('button', { class: `btn ${good ? 'btn-light' : 'btn-primary'}`, onclick: () => advance() }, 'Continuer'));
    feedbackZone.replaceChildren(banner);
    requestAnimationFrame(() => banner.classList.add('show'));
    if (fb.speak) setTimeout(() => speak(fb.speak), good ? 150 : 300);

    if (fb.comboMilestone) {
      comboBurst.replaceChildren(h('span', {}, art('ui-flame', 'inline'), `Combo ×${fb.comboMilestone}`));
      comboBurst.classList.remove('show');
      void comboBurst.offsetWidth;
      comboBurst.classList.add('show');
    }
    if (good) {
      const delay = fb.justLearned || fb.comboMilestone || fb.note ? 1800 : 1100;
      autoAdvance = setTimeout(advance, delay);
    }
  }

  function advance() {
    clearTimeout(autoAdvance);
    if (!lesson.feedback) return;
    feedbackZone.replaceChildren();
    lesson.next();
  }

  function update() {
    renderCombo();
    if (lesson.finished) {
      clearInterval(timer);
      clearTimeout(autoAdvance);
      if (!lesson.summary) return exit();
      root.replaceChildren(summaryView(lesson, exit));
      return;
    }
    if (lesson.current && lesson.current !== shownCurrent) {
      shownCurrent = lesson.current;
      showCurrent();
    }
    if (lesson.feedback && !feedbackZone.firstChild) showFeedback(lesson.feedback);
  }

  timer = setInterval(tick, 250);
  tick();
  lesson.start();
  return root;
}

function summaryView(lesson, onClose) {
  const accuracy = lesson.answerCount ? Math.round((lesson.correctCount / lesson.answerCount) * 100) : 0;
  const learned = lesson.learnedIds.map((id) => itemsById.get(id));
  const { streakExtended, goalJustReached, levelUp } = lesson.summary;
  const streak = store.currentStreak();
  const minutes = Math.round(store.todaySeconds() / 60);

  return h('div', { class: 'summary' },
    art(accuracy >= 80 ? 'ui-trophy' : 'padre', 'big-art pop'),
    h('h2', {}, accuracy >= 80 ? '¡Órale, qué bien!' : '¡Buen trabajo!'),
    h('p', { class: 'muted' }, 'Session terminée'),
    h('div', { class: 'stats-grid' },
      stat(`+${lesson.xp}`, 'XP'),
      stat(`${accuracy} %`, 'Précision'),
      stat(`×${lesson.bestCombo}`, 'Meilleur combo'),
      stat(formatDuration(Math.min(lesson.elapsed, SESSION_SECONDS)), 'Temps')),
    levelUp ? h('div', { class: 'level-up' }, art(LEVEL_INFO[levelUp].art, 'inline'), `Nouveau niveau : ${levelUp} · ${LEVEL_INFO[levelUp].name} !`) : null,
    h('div', { class: 'summary-row' },
      h('div', { class: `streak-box ${streakExtended ? 'extended' : ''}` },
        icon('flame', 'flame'),
        h('div', {}, h('strong', {}, plural(streak, 'jour')), h('span', {}, streakExtended ? 'Série prolongée' : 'de série'))),
      h('div', { class: 'goal-box' },
        ring(store.goalRatio(), { size: 52, stroke: 6, color: '#F5B700', content: store.goalRatio() >= 1 ? '✓' : `${minutes}′` }),
        h('div', {}, h('strong', {}, goalJustReached ? 'Objectif atteint !' : `${minutes} / ${store.state.dailyGoal} min`), h('span', {}, 'aujourd\'hui')))),
    learned.length
      ? h('div', { class: 'learned-list' },
        h('h3', {}, `${plural(learned.length, 'élément appris', 'éléments appris')}`),
        h('div', { class: 'chips' }, learned.map((i) => h('span', { class: 'chip' }, art(i.art, 'inline'), i.kind === 'word' || i.kind === 'phrase' ? i.es : i.fr))))
      : null,
    lesson.reviewedIds.size ? h('p', { class: 'muted' }, `${plural(lesson.reviewedIds.size, 'révision')} effectuée${lesson.reviewedIds.size > 1 ? 's' : ''}`) : null,
    h('div', { class: 'actions' }, h('button', { class: 'btn btn-primary', onclick: onClose }, 'Terminer')));
}

function stat(value, label) {
  return h('div', { class: 'stat' }, h('strong', {}, value), h('span', {}, label));
}
