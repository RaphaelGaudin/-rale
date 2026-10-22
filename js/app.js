// Point d'entrée : navigation entre onglets, fiches de thème et leçons.
import { h } from './util.js';
import * as store from './store.js';
import { unlockOnFirstGesture } from './sound.js';
import { stop } from './speech.js';
import { icon } from './ui/components.js';
import { onboardingView } from './ui/onboarding.js';
import { learnView } from './ui/learn.js';
import { themeDetailView } from './ui/themeDetail.js';
import { reviewView } from './ui/review.js';
import { discoverView } from './ui/discover.js';
import { profileView } from './ui/profile.js';
import { lessonView } from './ui/lessonView.js';

const app = document.getElementById('app');
const TABS = [
  ['learn', 'Apprendre'],
  ['review', 'Révisions'],
  ['discover', 'Découvrir'],
  ['profile', 'Profil'],
];

const nav = {
  tab: 'learn',
  theme: null, // fiche de thème ouverte
  lesson: null, // { mode, theme }
};
const scrollByTab = {};

const ctx = {
  openTheme(theme) {
    scrollByTab[nav.tab] = window.scrollY;
    nav.theme = theme;
    render({ scrollTop: true });
  },
  back() {
    nav.theme = null;
    render();
  },
  startLesson(opts) {
    if (!nav.theme) scrollByTab[nav.tab] = window.scrollY;
    nav.lesson = opts;
    render({ scrollTop: true });
  },
  refresh() {
    render();
  },
};

function tabBar() {
  const due = store.dueItems().length;
  return h('nav', { class: 'tabbar' },
    TABS.map(([id, label]) =>
      h('button', {
        class: `tab ${nav.tab === id ? 'on' : ''}`,
        onclick: () => {
          stop();
          if (nav.tab === id && !nav.theme) return window.scrollTo({ top: 0, behavior: 'smooth' });
          scrollByTab[nav.tab] = window.scrollY;
          nav.tab = id;
          nav.theme = null;
          render();
        },
      },
      h('span', { class: 'tab-icon' }, icon(id), id === 'review' && due ? h('span', { class: 'badge' }, due > 99 ? '99+' : due) : null),
      h('span', { class: 'tab-label' }, label))));
}

function render({ scrollTop = false } = {}) {
  document.body.classList.toggle('in-lesson', !!nav.lesson);

  if (!store.state.onboarded) {
    nav.lesson = null;
    nav.theme = null;
    app.replaceChildren(onboardingView({ onDone: () => { nav.tab = 'learn'; render({ scrollTop: true }); } }));
    window.scrollTo(0, 0);
    return;
  }

  if (nav.lesson) {
    const { mode, theme } = nav.lesson;
    app.replaceChildren(lessonView({
      mode,
      theme,
      onExit: () => {
        nav.lesson = null;
        render();
      },
    }));
    window.scrollTo(0, 0);
    return;
  }

  let screen;
  if (nav.theme) screen = themeDetailView(nav.theme, ctx);
  else if (nav.tab === 'learn') screen = learnView(ctx);
  else if (nav.tab === 'review') screen = reviewView(ctx);
  else if (nav.tab === 'discover') screen = discoverView(ctx);
  else screen = profileView(ctx);

  app.replaceChildren(h('main', { class: 'main' }, screen), tabBar());
  window.scrollTo(0, scrollTop || nav.theme ? 0 : scrollByTab[nav.tab] || 0);
}

// Quand on revient sur l'app un autre jour, on rafraîchit (révisions du jour, série).
let lastDay = new Date().toDateString();
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible' && new Date().toDateString() !== lastDay && !nav.lesson) {
    lastDay = new Date().toDateString();
    render();
  }
});

unlockOnFirstGesture();
render();

if ('serviceWorker' in navigator && location.protocol !== 'file:') {
  navigator.serviceWorker.register('./sw.js').catch((e) => console.warn('Service worker non enregistré', e));
}
