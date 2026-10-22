// Onglet « Découvrir » : films, séries, livres et podcasts adaptés au niveau.
import { h } from '../util.js';
import { LEVELS, LEVEL_INFO, RECOMMENDATIONS } from '../content.js';
import * as store from '../store.js';
import { art, header } from './components.js';

const TYPES = [
  ['all', 'Tout', 'ui-star'],
  ['film', 'Films', 'ui-film'],
  ['series', 'Séries', 'ui-series'],
  ['book', 'Livres', 'ui-book'],
  ['podcast', 'Podcasts', 'ui-podcast'],
];
const TYPE_LABEL = { film: 'Film', series: 'Série', book: 'Livre', podcast: 'Podcast / vidéo' };
const TYPE_COLOR = { film: '#E4007C', series: '#1E88E5', book: '#00A86B', podcast: '#FF6B1A' };

let selectedLevel = null;
let selectedType = 'all';

export function discoverView() {
  if (!selectedLevel) selectedLevel = store.state.level;
  const root = h('div', { class: 'screen discover' });

  const render = () => {
    const items = RECOMMENDATIONS.filter((r) => r.level === selectedLevel && (selectedType === 'all' || r.type === selectedType));
    root.replaceChildren(
      header('Découvrir'),
      h('p', { class: 'intro' }, 'Du contenu authentique pour t\'immerger dans l\'espagnol du Mexique, choisi pour ton niveau.'),
      h('div', { class: 'segmented' },
        LEVELS.map((l) =>
          h('button', { class: l === selectedLevel ? 'on' : '', onclick: () => { selectedLevel = l; render(); } },
            l, l === store.state.level ? h('i', { class: 'dot' }) : null))),
      h('p', { class: 'muted small level-blurb' }, art(LEVEL_INFO[selectedLevel].art, 'inline'), `${LEVEL_INFO[selectedLevel].name} — ${LEVEL_INFO[selectedLevel].blurb}`),
      h('div', { class: 'filter-chips' },
        TYPES.map(([type, label, key]) =>
          h('button', { class: `chip ${type === selectedType ? 'on' : ''}`, onclick: () => { selectedType = type; render(); } }, art(key, 'inline'), label))),
      items.length
        ? h('div', { class: 'reco-list' }, items.map(recoCard))
        : h('div', { class: 'empty' }, h('p', {}, 'Rien dans cette catégorie pour ce niveau. Essaie un autre filtre !')));
  };
  render();
  return root;
}

function recoCard(r) {
  return h('article', { class: 'reco', style: { '--theme': TYPE_COLOR[r.type] } },
    h('div', { class: 'reco-poster' }, art(r.art)),
    h('div', { class: 'reco-body' },
      h('span', { class: 'reco-type' }, TYPE_LABEL[r.type]),
      h('h3', {}, r.title),
      h('p', { class: 'reco-meta' }, `${r.creator} · ${r.year}`),
      h('p', {}, r.description),
      h('p', { class: 'reco-tip' }, art('ui-bulb', 'inline'), r.tip)));
}
