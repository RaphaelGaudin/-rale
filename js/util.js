// Petits utilitaires partagés : DOM, aléatoire, dates, texte.

/** Crée un élément DOM : h('div', {class: 'x', onclick: fn}, enfant1, 'texte', …) */
export function h(tag, props = {}, ...children) {
  const el = document.createElement(tag);
  for (const [key, value] of Object.entries(props || {})) {
    if (value === undefined || value === null || value === false) continue;
    if (key === 'class') el.className = value;
    else if (key === 'style' && typeof value === 'object') Object.assign(el.style, value);
    else if (key.startsWith('on') && typeof value === 'function') el.addEventListener(key.slice(2), value);
    else if (key === 'html') el.innerHTML = value;
    else el.setAttribute(key, value === true ? '' : value);
  }
  appendChildren(el, children);
  return el;
}

function appendChildren(el, children) {
  for (const child of children) {
    if (child === null || child === undefined || child === false) continue;
    if (Array.isArray(child)) appendChildren(el, child);
    else el.append(child instanceof Node ? child : document.createTextNode(String(child)));
  }
}

export function shuffle(array) {
  const a = [...array];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function sample(array, n) {
  return shuffle(array).slice(0, n);
}

export function pick(array) {
  return array[Math.floor(Math.random() * array.length)];
}

// ── Dates (jours calendaires locaux) ──

const DAY_MS = 24 * 60 * 60 * 1000;

export function startOfDay(date = new Date()) {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  return d;
}

export function addDays(date, days) {
  const d = new Date(date);
  d.setDate(d.getDate() + days);
  return d;
}

/** Clé « AAAA-MM-JJ » en heure locale. */
export function dayKey(date = new Date()) {
  const d = new Date(date);
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${d.getFullYear()}-${m}-${day}`;
}

/** Nombre de jours calendaires entre deux dates (b - a). */
export function daysBetween(a, b) {
  return Math.round((startOfDay(b) - startOfDay(a)) / DAY_MS);
}

const WEEKDAYS = ['dim.', 'lun.', 'mar.', 'mer.', 'jeu.', 'ven.', 'sam.'];
export function weekdayShort(date) {
  return WEEKDAYS[new Date(date).getDay()];
}

// ── Texte ──

const ARTICLES = /^(el|la|los|las|un|una|unos|unas)\s+/i;

/** « el mango » → « mango » */
export function stripArticle(text) {
  return text.replace(ARTICLES, '');
}

/** Retire la ponctuation espagnole et française. */
export function stripPunctuation(text) {
  return text.replace(/[¿?¡!.,;:«»"—–…()]/g, '').replace(/\s+/g, ' ').trim();
}

export function removeAccents(text) {
  // On garde le ñ, qui est une vraie lettre en espagnol.
  return text
    .replace(/ñ/g, '\u0000').replace(/Ñ/g, '\u0001')
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/\u0000/g, 'ñ').replace(/\u0001/g, 'Ñ');
}

export function normalizeAnswer(text) {
  return stripPunctuation(stripArticle(text.trim().toLowerCase()));
}

/** Découpe une phrase en mots sans ponctuation : « ¿Cómo estás? » → ['Cómo', 'estás'] */
export function tokenize(sentence) {
  return stripPunctuation(sentence).split(' ').filter(Boolean);
}

export function formatDuration(seconds) {
  const s = Math.max(0, Math.round(seconds));
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}

export function plural(n, singular, pluralForm = singular + 's') {
  return `${n} ${n > 1 ? pluralForm : singular}`;
}

export const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
