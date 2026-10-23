// Index du contenu pédagogique (généré dans js/data/content.js).
import { THEMES, RECOMMENDATIONS, PLACEMENT } from './data/content.js';

export const LEVELS = ['A1', 'A2', 'B1', 'B2'];

export const LEVEL_INFO = {
  A1: { name: 'Débutant', art: 'ui-sprout', blurb: 'Se présenter, commander des tacos, compter ses pesos.' },
  A2: { name: 'Élémentaire', art: 'nopal', blurb: 'Se déplacer en ville, voyager, raconter sa journée.' },
  B1: { name: 'Intermédiaire', art: 'chile', blurb: 'Travailler, louer un appart, parler comme un chilango.' },
  B2: { name: 'Avancé', art: 'aguila', blurb: 'Débattre, comprendre l\'actualité, l\'histoire et l\'argot.' },
};

export const KIND_LABEL = {
  word: 'Mot',
  phrase: 'Phrase',
  grammar: 'Grammaire',
  dialogue: 'Dialogue',
};

export { THEMES, RECOMMENDATIONS, PLACEMENT };

export const themesById = new Map(THEMES.map((t) => [t.id, t]));
export const itemsById = new Map();
for (const theme of THEMES) {
  for (const item of theme.items) {
    item.themeId = theme.id;
    item.level = theme.level;
    itemsById.set(item.id, item);
  }
}

export function themesForLevel(level) {
  return THEMES.filter((t) => t.level === level);
}

export function itemsForLevel(level) {
  return themesForLevel(level).flatMap((t) => t.items);
}

export function themeOf(item) {
  return themesById.get(item.themeId);
}

export function levelIndex(level) {
  return LEVELS.indexOf(level);
}
