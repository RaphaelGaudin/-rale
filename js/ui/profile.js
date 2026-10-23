// Onglet « Profil » : statistiques, réglages, sauvegarde de la progression.
import { h, addDays, dayKey, startOfDay, weekdayShort, plural } from '../util.js';
import { LEVELS, LEVEL_INFO } from '../content.js';
import * as store from '../store.js';
import { speak, voiceDescription, mexicanVoice, hasRecordedVoices, allClipUrls } from '../speech.js';
import { art, header, logo, toast } from './components.js';

export function profileView(ctx) {
  const s = store.state;
  const root = h('div', { class: 'screen profile' });

  const render = () => {
    const week = Array.from({ length: 7 }, (_, i) => {
      const d = addDays(startOfDay(), i - 6);
      return { d, minutes: Math.round((s.secondsByDay[dayKey(d)] || 0) / 60) };
    });
    const max = Math.max(s.dailyGoal, ...week.map((w) => w.minutes));
    const learned = store.learnedItems().length;

    root.replaceChildren(
      header('Profil'),
      h('section', { class: 'profile-hero' },
        logo(64),
        h('div', {},
          h('h2', {}, `Contenu ${s.level} · ${LEVEL_INFO[s.level].name}`),
          h('p', { class: 'muted' }, s.placement ? `Niveau estimé au test : ${s.placement}` : 'Parcours depuis le début'))),
      h('div', { class: 'mini-stats four' },
        h('div', {}, h('strong', {}, art('ui-flame', 'inline'), store.currentStreak()), h('span', {}, 'série')),
        h('div', {}, h('strong', {}, art('ui-trophy', 'inline'), s.bestStreak), h('span', {}, 'record')),
        h('div', {}, h('strong', {}, art('ui-star', 'inline'), s.xp), h('span', {}, 'XP')),
        h('div', {}, h('strong', {}, art('ui-book', 'inline'), learned), h('span', {}, 'appris'))),
      h('section', { class: 'card' },
        h('h3', {}, 'Minutes par jour'),
        h('div', { class: 'forecast week' },
          week.map((w, i) =>
            h('div', { class: `bar-col ${i === 6 ? 'today' : ''} ${w.minutes >= s.dailyGoal ? 'goal' : ''}` },
              h('span', { class: 'bar-value' }, w.minutes || ''),
              h('div', { class: 'bar-track' },
                h('div', { class: 'goal-line', style: { bottom: `${(s.dailyGoal / max) * 100}%` } }),
                h('div', { class: 'bar', style: { height: `${(w.minutes / max) * 100}%` } })),
              h('span', { class: 'bar-label' }, i === 6 ? 'Auj.' : weekdayShort(w.d)))))),

      h('section', { class: 'card settings' },
        h('h3', {}, 'Réglages'),
        settingRow('Objectif quotidien',
          h('div', { class: 'segmented small' },
            [5, 10, 15, 20].map((g) => h('button', { class: g === s.dailyGoal ? 'on' : '', onclick: () => { store.update({ dailyGoal: g }); render(); } }, `${g}′`)))),
        settingRow('Mon niveau',
          h('div', { class: 'segmented small' },
            LEVELS.map((l) => h('button', { class: l === s.level ? 'on' : '', onclick: () => { store.update({ level: l }); render(); } }, l)))),
        settingRow('Vitesse de la voix',
          h('div', { class: 'rate' },
            h('input', {
              type: 'range', min: '0.6', max: '1.2', step: '0.05', value: String(s.speechRate),
              oninput: (e) => store.update({ speechRate: Number(e.target.value) }),
              onchange: () => speak('¡Órale! ¿Qué onda?'),
            }),
            h('button', { class: 'btn btn-ghost small', onclick: () => speak('Hola, ¿cómo estás? Bienvenido a México.') }, '▶︎ Tester'))),
        toggleRow('Sons', 'sound', render),
        toggleRow('Vibrations', 'haptics', render),
        hasRecordedVoices()
          ? settingRow('Voix',
            h('div', { class: 'segmented small' },
              [['recorded', 'Enregistrée'], ['device', 'iPhone']].map(([v, label]) =>
                h('button', { class: (s.voice || 'recorded') === v ? 'on' : '', onclick: () => { store.update({ voice: v }); render(); speak('¡Hola! ¿Cómo estás?'); } }, label))))
          : null,
        h('p', { class: 'muted small voice-info' }, voiceDescription()),
        hasRecordedVoices() && s.voice !== 'device'
          ? h('button', { class: 'btn btn-ghost small', onclick: (e) => downloadVoices(e.currentTarget) }, 'Télécharger les voix pour le mode hors-ligne')
          : !mexicanVoice()
            ? h('p', { class: 'muted small' }, 'Pour une voix mexicaine plus naturelle sur iPhone : Réglages › Accessibilité › Contenu énoncé › Voix › Espagnol (Mexique), puis télécharge « Paulina » ou « Juan » (version améliorée).')
            : h('p', { class: 'muted small' }, 'Astuce : la version « améliorée » de la voix (Réglages › Accessibilité › Contenu énoncé › Voix) est bien plus naturelle.'),
        h('p', { class: 'muted small' }, 'Pas de son ? Monte le volume avec les boutons latéraux de l\'iPhone. Sur les iOS plus anciens que la version 17, désactive aussi le mode silencieux.')),

      h('section', { class: 'card settings' },
        h('h3', {}, 'Ma progression'),
        h('p', { class: 'muted small' }, `Ta progression est enregistrée sur ce téléphone (${plural(s.sessions, 'session')} jouée${s.sessions > 1 ? 's' : ''}). Exporte-la de temps en temps pour la garder en sécurité.`),
        h('div', { class: 'button-row' },
          h('button', { class: 'btn btn-ghost small', onclick: exportProgress }, 'Exporter'),
          h('button', { class: 'btn btn-ghost small', onclick: () => importProgress(render) }, 'Importer')),
        h('div', { class: 'button-row' },
          h('button', { class: 'btn btn-ghost small', onclick: () => { store.update({ onboarded: false }); ctx.refresh(); } }, 'Refaire le test de niveau'),
          h('button', {
            class: 'btn btn-danger small',
            onclick: () => {
              if (confirm('Effacer toute ta progression ? Cette action est irréversible.')) {
                store.reset();
                ctx.refresh();
              }
            },
          }, 'Tout effacer'))),
      h('p', { class: 'muted small center' }, 'Órale · hecho con amor y mucho chile'));
  };
  render();
  return root;
}

/** Met en cache tous les fichiers audio pour pouvoir réviser sans réseau. */
async function downloadVoices(button) {
  const urls = allClipUrls();
  let done = 0;
  button.disabled = true;
  const cache = 'caches' in window ? await caches.open('orale-audio') : null;
  for (let i = 0; i < urls.length; i += 8) {
    await Promise.all(urls.slice(i, i + 8).map(async (url) => {
      try {
        if (cache && !(await cache.match(url))) await cache.add(url);
      } catch { /* on réessaiera plus tard */ }
      done++;
    }));
    button.textContent = `Téléchargement… ${Math.round((done / urls.length) * 100)} %`;
  }
  button.textContent = 'Voix disponibles hors-ligne ✓';
}

function settingRow(label, control) {
  return h('div', { class: 'setting' }, h('span', {}, label), control);
}

function toggleRow(label, key, render) {
  return settingRow(label,
    h('button', {
      class: `switch ${store.state[key] ? 'on' : ''}`,
      role: 'switch',
      'aria-checked': String(!!store.state[key]),
      onclick: () => { store.update({ [key]: !store.state[key] }); render(); },
    }, h('i')));
}

async function exportProgress() {
  const data = store.exportData();
  const file = new File([data], `orale-progression-${dayKey()}.json`, { type: 'application/json' });
  try {
    if (navigator.canShare?.({ files: [file] })) {
      await navigator.share({ files: [file], title: 'Progression Órale' });
      return;
    }
  } catch (e) {
    if (e.name === 'AbortError') return;
  }
  const url = URL.createObjectURL(file);
  const a = h('a', { href: url, download: file.name });
  document.body.append(a);
  a.click();
  a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function importProgress(render) {
  const input = h('input', { type: 'file', accept: 'application/json,.json' });
  input.addEventListener('change', async () => {
    const file = input.files?.[0];
    if (!file) return;
    try {
      store.importData(await file.text());
      toast('Progression importée ✓');
      render();
    } catch {
      toast('Fichier invalide');
    }
  });
  input.click();
}
