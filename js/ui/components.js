// Composants d'interface réutilisables.
import { h } from '../util.js';
import { speak } from '../speech.js';
import { MASTERED_STAGE } from '../srs.js';

const SVG_NS = 'http://www.w3.org/2000/svg';

export function svg(markup, className = '') {
  const wrapper = document.createElement('span');
  wrapper.className = `svg ${className}`;
  wrapper.innerHTML = markup;
  return wrapper;
}

let logoCount = 0;
/** Le logo Órale : une bulle de BD contenant le drapeau mexicain. */
export function logo(size = 64) {
  const id = `bubble-${logoCount++}`;
  const bubble = 'M28 6H92A22 22 0 0 1 114 28V62A22 22 0 0 1 92 84H54L26 106L32 84H28A22 22 0 0 1 6 62V28A22 22 0 0 1 28 6Z';
  return svg(
    `<svg xmlns="${SVG_NS}" viewBox="0 0 120 112" width="${size}" height="${size * 112 / 120}" role="img" aria-label="Órale">
      <defs><clipPath id="${id}"><path d="${bubble}"/></clipPath></defs>
      <g clip-path="url(#${id})">
        <rect x="0" y="0" width="42" height="112" fill="#006847"/>
        <rect x="42" y="0" width="36" height="112" fill="#FFFFFF"/>
        <rect x="78" y="0" width="42" height="112" fill="#CE1126"/>
        <path d="M47.5 49A12.5 12.5 0 0 0 72.5 49" fill="none" stroke="#3E7B27" stroke-width="2.6" stroke-linecap="round"/>
        <ellipse cx="60" cy="51" rx="4" ry="2" fill="#3E7B27"/>
        <path d="M56 41L47 33L50 42L57 46ZM64 41L73 33L70 42L63 46Z" fill="#8B5A2B"/>
        <ellipse cx="60" cy="43" rx="5" ry="7" fill="#8B5A2B"/>
        <circle cx="60" cy="34" r="3" fill="#8B5A2B"/>
      </g>
      <path d="${bubble}" fill="none" stroke="#1B1B1F" stroke-width="5" stroke-linejoin="round"/>
    </svg>`,
    'logo',
  );
}

export const ICONS = {
  learn: '<svg viewBox="0 0 24 24"><path d="M12 3 2 8l10 5 8-4v6h2V8L12 3Zm-6 9.2V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-3.8l-6 3-6-3Z"/></svg>',
  review: '<svg viewBox="0 0 24 24"><path d="M12 4a8 8 0 0 1 7.4 5H17v2h6V5h-2v2.5A10 10 0 0 0 2.1 11h2A8 8 0 0 1 12 4Zm7.9 9A8 8 0 0 1 4.6 15H7v-2H1v6h2v-2.5A10 10 0 0 0 21.9 13h-2Z"/></svg>',
  discover: '<svg viewBox="0 0 24 24"><path d="M4 5h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Zm6 3v8l6-4-6-4Z"/></svg>',
  profile: '<svg viewBox="0 0 24 24"><path d="M12 12a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9Zm0 2c-4.4 0-8 2.2-8 5v2h16v-2c0-2.8-3.6-5-8-5Z"/></svg>',
  speaker: '<svg viewBox="0 0 24 24"><path d="M4 9v6h4l5 5V4L8 9H4Zm12.5 3a4.5 4.5 0 0 0-2.5-4v8a4.5 4.5 0 0 0 2.5-4ZM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6Z"/></svg>',
  close: '<svg viewBox="0 0 24 24"><path d="M18.3 5.7 12 12l6.3 6.3-1.4 1.4L10.6 13.4 4.3 19.7l-1.4-1.4L9.2 12 2.9 5.7l1.4-1.4 6.3 6.3 6.3-6.3 1.4 1.4Z" transform="translate(1 0)"/></svg>',
  back: '<svg viewBox="0 0 24 24"><path d="M15.4 4.6 8 12l7.4 7.4-1.4 1.4L5.2 12 14 3.2l1.4 1.4Z"/></svg>',
  star: '<svg viewBox="0 0 24 24"><path d="m12 2 3 6.6 7.2.7-5.4 4.8 1.6 7.1L12 17.5l-6.4 3.7 1.6-7.1L1.8 9.3 9 8.6 12 2Z"/></svg>',
  check: '<svg viewBox="0 0 24 24"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2Z"/></svg>',
  play: '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7L8 5Z"/></svg>',
  backspace: '<svg viewBox="0 0 24 24"><path d="M22 5H8l-6 7 6 7h14V5Zm-3.6 10.6-1.4 1.4-3-3-3 3-1.4-1.4 3-3-3-3L11 8.2l3 3 3-3 1.4 1.4-3 3 3 3Z"/></svg>',
};

export function icon(name, className = '') {
  if (name === 'flame') return h('span', { class: `icon emoji-icon ${className}` }, '🔥');
  return svg(ICONS[name], `icon ${className}`);
}

export function speakerButton(text, { label = 'Écouter', big = false, onClick } = {}) {
  return h(
    'button',
    {
      class: `speaker ${big ? 'speaker-big' : ''}`,
      'aria-label': label,
      onclick: (e) => {
        e.stopPropagation();
        const btn = e.currentTarget;
        btn.classList.add('playing');
        (onClick ? onClick() : speak(text)).finally(() => btn.classList.remove('playing'));
      },
    },
    icon('speaker'),
  );
}

/** Anneau de progression SVG. */
export function ring(ratio, { size = 56, stroke = 6, color = 'var(--accent)', track = 'rgba(255,255,255,.15)', content = null } = {}) {
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  const el = h('div', { class: 'ring', style: { width: `${size}px`, height: `${size}px` } });
  el.innerHTML = `<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">
    <circle cx="${size / 2}" cy="${size / 2}" r="${r}" fill="none" stroke="${track}" stroke-width="${stroke}"/>
    <circle cx="${size / 2}" cy="${size / 2}" r="${r}" fill="none" stroke="${color}" stroke-width="${stroke}"
      stroke-linecap="round" stroke-dasharray="${c}" stroke-dashoffset="${c * (1 - Math.min(1, Math.max(0, ratio)))}"
      transform="rotate(-90 ${size / 2} ${size / 2})"/></svg>`;
  if (content) el.append(h('div', { class: 'ring-content' }, content));
  return el;
}

/** Barre de maîtrise : 5 pastilles (étapes 1 à 5 de la répétition espacée). */
export function stageDots(stage) {
  return h(
    'span',
    { class: 'stage-dots', title: stage ? `Étape ${stage}` : 'Pas encore appris' },
    Array.from({ length: MASTERED_STAGE }, (_, i) => h('i', { class: i < stage ? 'on' : '' })),
  );
}

export function header(title, { onBack, right } = {}) {
  return h(
    'header',
    { class: 'topbar' },
    onBack ? h('button', { class: 'icon-btn', onclick: onBack, 'aria-label': 'Retour' }, icon('back')) : h('span', { class: 'icon-btn-spacer' }),
    h('h1', {}, title),
    right || h('span', { class: 'icon-btn-spacer' }),
  );
}

export function toast(message) {
  const el = h('div', { class: 'toast' }, message);
  document.body.append(el);
  requestAnimationFrame(() => el.classList.add('show'));
  setTimeout(() => {
    el.classList.remove('show');
    setTimeout(() => el.remove(), 400);
  }, 2200);
}

/** Feuille modale qui monte du bas de l'écran. */
export function sheet(content, { title } = {}) {
  const close = () => {
    overlay.classList.remove('show');
    setTimeout(() => overlay.remove(), 300);
  };
  const overlay = h(
    'div',
    { class: 'sheet-overlay', onclick: (e) => e.target === overlay && close() },
    h(
      'div',
      { class: 'sheet' },
      h('div', { class: 'sheet-head' }, h('span', { class: 'sheet-grip' }), title ? h('h2', {}, title) : null,
        h('button', { class: 'icon-btn sheet-close', onclick: close, 'aria-label': 'Fermer' }, icon('close'))),
      h('div', { class: 'sheet-body' }, content),
    ),
  );
  document.body.append(overlay);
  requestAnimationFrame(() => overlay.classList.add('show'));
  return close;
}

/** Remplace « ___ » par une case vide stylée. */
export function withBlank(text, filled = null) {
  const parts = text.split('___');
  if (parts.length === 1) return text;
  return [parts[0], h('span', { class: `blank ${filled ? 'filled' : ''}` }, filled || ' '), parts.slice(1).join('___')];
}
