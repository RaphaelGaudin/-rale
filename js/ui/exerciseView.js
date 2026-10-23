// Affichage des exercices : QCM, épellation, phrase à reconstruire, écriture.
import { h } from '../util.js';
import { speak, speakLines, stop } from '../speech.js';
import { buzz, play } from '../sound.js';
import { checkBuilt, checkWritten } from '../exercises.js';
import { art, icon, speakerButton, withBlank } from './components.js';

function promptView(ex) {
  const p = ex.prompt;
  const parts = [];

  if (p.dialogue) {
    parts.push(dialoguePrompt(p));
    return h('div', { class: 'prompt prompt-dialogue' }, parts);
  }

  if (p.listenOnly) {
    parts.push(h('div', { class: 'listen-zone' }, speakerButton(p.audio, { big: true, label: 'Réécouter' }), h('p', { class: 'muted' }, 'Touche pour réécouter')));
  }

  if (p.art) {
    const showCaption = ex.showCaption || p.forceCaption;
    const caption = h('div', { class: `caption ${showCaption ? '' : 'hidden-caption'}` }, showCaption ? p.caption : 'Touche l\'image pour un indice');
    const tile = h('button', {
      class: 'art',
      'aria-label': 'Illustration',
      onclick: () => {
        if (!showCaption) {
          caption.textContent = p.caption;
          caption.classList.remove('hidden-caption');
        }
      },
    }, art(p.art));
    parts.push(tile, caption);
  }

  if (p.text) {
    parts.push(
      h('div', { class: 'prompt-text-row' },
        h('p', { class: `prompt-text ${p.lang === 'fr' ? 'fr' : 'es'} ${p.text.length > 40 ? 'long' : ''}` },
          p.speaker ? h('span', { class: 'speaker-name' }, `${p.speaker} : `) : null,
          p.blank ? withBlank(p.text) : p.text),
        p.audio ? speakerButton(p.audio) : null),
    );
    if (p.caption && !p.art) parts.push(h('p', { class: 'hint' }, p.caption));
  }

  if (p.passage) parts.push(h('div', { class: 'passage', lang: 'es' }, p.passage));
  if (p.question) parts.push(h('p', { class: 'question' }, p.question));

  if (p.autoplay && p.audio) setTimeout(() => speak(p.audio), 350);
  return h('div', { class: 'prompt' }, parts);
}

function dialoguePrompt(p) {
  const speakers = [...new Set(p.dialogue.map((l) => l.speaker))];
  const bubbles = p.dialogue.map((line) =>
    h('div', { class: `bubble ${speakers.indexOf(line.speaker) % 2 ? 'right' : 'left'}` },
      h('span', { class: 'who' }, line.speaker), h('span', {}, line.es)));
  const transcript = h('div', { class: `transcript ${p.listenOnly ? 'concealed' : ''}` }, bubbles);
  const playBtn = h('button', {
    class: 'btn btn-ghost play-dialogue',
    onclick: () => playAll(),
  }, icon('play'), p.listenOnly ? ' Écouter le dialogue' : ' Écouter');
  const playAll = () => {
    playBtn.classList.add('playing');
    speakLines(p.dialogue, (i) => {
      bubbles.forEach((b, j) => b.classList.toggle('active', j === i));
      if (i === -1) playBtn.classList.remove('playing');
    });
  };
  if (p.autoplayDialogue) setTimeout(playAll, 400);
  const reveal = p.listenOnly
    ? h('button', { class: 'link', onclick: (e) => { transcript.classList.remove('concealed'); e.currentTarget.remove(); } }, 'Afficher le texte')
    : null;
  return [playBtn, transcript, reveal, h('p', { class: 'question' }, p.question)];
}

// ── QCM ──

function mcqView(ex, onAnswer) {
  let answered = false;
  const buttons = ex.choices.map((choice) => {
    const btn = h(
      'button',
      {
        class: `choice ${ex.choiceStyle === 'image' ? 'choice-image' : 'choice-text'} ${choice.tf ? `choice-${choice.tf}` : ''}`,
        onclick: () => {
          if (answered) return;
          answered = true;
          btn.classList.add(choice.correct ? 'correct' : 'wrong');
          buttons.forEach((b, i) => {
            if (ex.choices[i].correct) b.classList.add('correct');
            else if (b !== btn) b.classList.add('dim');
          });
          onAnswer(choice.correct);
        },
      },
      choice.art ? art(choice.art) : null,
      ex.choiceStyle === 'image'
        ? (ex.showCaption ? h('span', { class: 'choice-caption' }, choice.label) : null)
        : h('span', {}, choice.label),
    );
    return btn;
  });
  const layout = ex.choiceStyle === 'image' ? 'grid' : ex.choiceStyle === 'tf' ? 'tf' : 'list';
  return h('div', { class: `choices ${layout}` }, buttons);
}

// ── Épeler ──

function spellView(ex, onAnswer) {
  let pos = 0;
  let mistakes = 0;
  let done = false;
  const slots = ex.target.map((ch) => h('span', { class: ch === ' ' ? 'slot space' : 'slot' }, ''));
  const skipSpaces = () => {
    while (pos < ex.target.length && ex.target[pos] === ' ') pos++;
  };
  skipSpaces();
  const mark = () => slots.forEach((s, i) => s.classList.toggle('cursor', i === pos && !done));

  const finish = (correct) => {
    done = true;
    mark();
    tiles.forEach((t) => (t.disabled = true));
    onAnswer(correct);
  };

  const tiles = ex.tiles.map((tile) => {
    const btn = h('button', {
      class: 'tile',
      onclick: () => {
        if (done || btn.classList.contains('used')) return;
        if (tile.letter === ex.target[pos]) {
          slots[pos].textContent = tile.letter;
          slots[pos].classList.add('filled');
          btn.classList.add('used');
          play('tap');
          pos++;
          skipSpaces();
          mark();
          if (pos >= ex.target.length) finish(mistakes === 0);
        } else {
          mistakes++;
          buzz(40);
          btn.classList.remove('shake');
          void btn.offsetWidth;
          btn.classList.add('shake');
          if (mistakes >= 3) {
            slots.forEach((s, i) => {
              if (!s.textContent && ex.target[i] !== ' ') {
                s.textContent = ex.target[i];
                s.classList.add('revealed');
              }
            });
            finish(false);
          }
        }
      },
    }, tile.letter);
    return btn;
  });
  mark();
  return h('div', { class: 'spell' },
    h('div', { class: 'slots' }, ex.article ? h('span', { class: 'article' }, ex.article) : null, slots),
    h('div', { class: 'tiles' }, tiles));
}

// ── Reconstruire une phrase ──

function buildView(ex, onAnswer) {
  const placed = []; // indices des tuiles posées
  let done = false;
  const answerZone = h('div', { class: 'answer-zone' });
  const bank = h('div', { class: 'tiles word-tiles' });
  const check = h('button', { class: 'btn btn-primary', disabled: true }, 'Vérifier');

  const tileButtons = ex.tiles.map((tile) =>
    h('button', {
      class: 'tile word',
      onclick: () => {
        if (done) return;
        const idx = placed.indexOf(tile.id);
        if (idx >= 0) placed.splice(idx, 1);
        else placed.push(tile.id);
        play('tap');
        render();
      },
    }, tile.word));

  const render = () => {
    answerZone.replaceChildren(...placed.map((id) => tileButtons[id]));
    bank.replaceChildren(...ex.tiles.map((t) => (placed.includes(t.id) ? h('span', { class: 'tile ghost' }, t.word) : tileButtons[t.id])));
    check.disabled = placed.length === 0;
  };

  check.addEventListener('click', () => {
    if (done) return;
    done = true;
    const words = placed.map((id) => ex.tiles[id].word);
    const correct = checkBuilt(words, ex.tokens);
    answerZone.classList.add(correct ? 'correct' : 'wrong');
    check.remove();
    onAnswer(correct);
  });
  render();
  return h('div', { class: 'build' }, answerZone, bank, h('div', { class: 'actions' }, check));
}

// ── Écrire ──

const SPECIAL_KEYS = ['á', 'é', 'í', 'ó', 'ú', 'ñ', 'ü', '¿', '¡'];

function writeView(ex, onAnswer) {
  let done = false;
  const input = h('input', {
    class: 'write-input',
    type: 'text',
    autocomplete: 'off',
    autocorrect: 'off',
    autocapitalize: 'none',
    spellcheck: 'false',
    lang: 'es',
    placeholder: 'Écris ici…',
    enterkeyhint: 'done',
  });
  const submit = () => {
    if (done || !input.value.trim()) return;
    done = true;
    input.blur();
    const { correct, note } = checkWritten(input.value, ex.accept || ex.answer);
    input.classList.add(correct ? 'correct' : 'wrong');
    input.disabled = true;
    onAnswer(correct, note);
  };
  input.addEventListener('keydown', (e) => e.key === 'Enter' && submit());
  const keys = SPECIAL_KEYS.map((k) =>
    h('button', {
      class: 'key',
      onpointerdown: (e) => e.preventDefault(), // garde le clavier ouvert
      onclick: () => {
        const start = input.selectionStart ?? input.value.length;
        const end = input.selectionEnd ?? input.value.length;
        input.value = input.value.slice(0, start) + k + input.value.slice(end);
        input.setSelectionRange(start + 1, start + 1);
        input.focus();
      },
    }, k));
  setTimeout(() => input.focus(), 400);
  return h('div', { class: 'write' }, input, h('div', { class: 'keys' }, keys),
    h('div', { class: 'actions' }, h('button', { class: 'btn btn-primary', onclick: submit }, 'Vérifier')));
}

// ── Jeu des paires ──

function pairsView(ex, onAnswer) {
  let selected = null; // { side, id, el }
  let mistakes = 0;
  let found = 0;
  const byId = Object.fromEntries(ex.pairs.map((p) => [p.id, p]));
  const make = (side, id) => {
    const p = byId[id];
    const content = side === 'left' ? h('span', {}, p.es) : p.art ? art(p.art) : h('span', {}, p.fr);
    const el = h('button', { class: `pair-tile ${side} ${side === 'right' && p.art ? 'has-art' : ''}`, onclick: () => tap(side, id, el) }, content);
    return el;
  };
  const tap = (side, id, el) => {
    if (el.classList.contains('matched')) return;
    if (side === 'left') speak(byId[id].es);
    if (!selected || selected.side === side) {
      selected?.el.classList.remove('selected');
      selected = { side, id, el };
      el.classList.add('selected');
      return;
    }
    if (selected.id === id) {
      [selected.el, el].forEach((x) => { x.classList.remove('selected'); x.classList.add('matched'); });
      play('tap');
      found++;
      selected = null;
      if (found === ex.pairs.length) onAnswer(mistakes <= 1);
    } else {
      mistakes++;
      buzz(40);
      [selected.el, el].forEach((x) => { x.classList.remove('shake'); void x.offsetWidth; x.classList.add('shake'); });
      selected.el.classList.remove('selected');
      selected = null;
    }
  };
  return h('div', { class: 'pairs' },
    h('div', { class: 'pair-col' }, ex.left.map((id) => make('left', id))),
    h('div', { class: 'pair-col' }, ex.right.map((id) => make('right', id))));
}

// ── Remettre un dialogue dans l'ordre ──

function orderView(ex, onAnswer) {
  let next = 0;
  let mistakes = 0;
  const done = h('div', { class: 'order-done transcript' });
  const speakers = [...new Set(ex.lines.map((l) => l.speaker))];
  const pool = h('div', { class: 'order-pool' }, ex.order.map((i) => {
    const line = ex.lines[i];
    const el = h('button', {
      class: 'order-line',
      onclick: () => {
        if (i === next) {
          el.remove();
          done.append(h('div', { class: `bubble ${speakers.indexOf(line.speaker) % 2 ? 'right' : 'left'} card-enter` },
            h('span', { class: 'who' }, line.speaker), h('span', {}, line.es)));
          speak(line.es, { speaker: speakers.indexOf(line.speaker) });
          next++;
          if (next === ex.lines.length) onAnswer(mistakes <= 1);
        } else {
          mistakes++;
          buzz(40);
          el.classList.remove('shake');
          void el.offsetWidth;
          el.classList.add('shake');
        }
      },
    }, h('span', { class: 'who' }, line.speaker), h('span', {}, line.es));
    return el;
  }));
  return h('div', { class: 'order' }, done, pool);
}

/** Construit la vue d'un exercice. `onAnswer(correct, note)` est appelé une seule fois. */
export function exerciseView(ex, onAnswer) {
  stop();
  let answered = false;
  const once = (correct, note) => {
    if (answered) return;
    answered = true;
    onAnswer(correct, note);
  };
  const body =
    ex.type === 'pairs' ? pairsView(ex, once)
      : ex.type === 'order' ? orderView(ex, once)
      : ex.type === 'spell' ? spellView(ex, once)
      : ex.type === 'build' ? buildView(ex, once)
        : ex.type === 'write' ? writeView(ex, once)
          : mcqView(ex, once);
  const prompt = ex.prompt ? promptView(ex) : null;
  return h('div', { class: `exercise ex-${ex.type}` }, h('p', { class: 'ex-label' }, ex.label), prompt, body);
}
