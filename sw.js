// Service worker : l'app fonctionne hors-ligne, et se met à jour dès qu'il y a du réseau.
const CACHE = 'orale-v2';
const AUDIO_CACHE = 'orale-audio';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './css/app.css',
  './js/app.js',
  './js/util.js',
  './js/srs.js',
  './js/store.js',
  './js/content.js',
  './js/data/content.js',
  './js/data/art.js',
  './js/data/audio.js',
  './js/speech.js',
  './js/sound.js',
  './js/exercises.js',
  './js/lesson.js',
  './js/placement.js',
  './js/ui/components.js',
  './js/ui/cards.js',
  './js/ui/exerciseView.js',
  './js/ui/lessonView.js',
  './js/ui/onboarding.js',
  './js/ui/learn.js',
  './js/ui/themeDetail.js',
  './js/ui/review.js',
  './js/ui/discover.js',
  './js/ui/profile.js',
  './icons/apple-touch-icon.png',
  './icons/icon-192.png',
  './icons/icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE && k !== AUDIO_CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

// Réseau d'abord (avec délai max), sinon cache.
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  if (request.method !== 'GET' || url.origin !== self.location.origin) return;
  // Les fichiers audio ne changent jamais (nom = empreinte du texte) : cache d'abord.
  if (url.pathname.includes('/audio/')) {
    event.respondWith((async () => {
      const cache = await caches.open(AUDIO_CACHE);
      const key = url.origin + url.pathname;
      let response = await cache.match(key);
      if (!response) {
        response = await fetch(key);
        if (!response.ok) return response;
        await cache.put(key, response.clone());
      }
      return rangeResponse(request, response);
    })());
    return;
  }
  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    try {
      const response = await Promise.race([
        fetch(request),
        new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 3500)),
      ]);
      if (response.ok) cache.put(request, response.clone());
      return response;
    } catch {
      const cached = await cache.match(request, { ignoreSearch: true });
      return cached || (request.mode === 'navigate' ? cache.match('./index.html') : Response.error());
    }
  })());
});

/** Safari lit l'audio par morceaux (en-tête Range) : il faut répondre en 206. */
async function rangeResponse(request, response) {
  const range = request.headers.get('range');
  if (!range) return response;
  const buffer = await response.arrayBuffer();
  const [, startStr, endStr] = /bytes=(\d*)-(\d*)/.exec(range) || [];
  const start = Number(startStr) || 0;
  const end = endStr ? Math.min(Number(endStr), buffer.byteLength - 1) : buffer.byteLength - 1;
  return new Response(buffer.slice(start, end + 1), {
    status: 206,
    headers: {
      'Content-Type': response.headers.get('Content-Type') || 'audio/mpeg',
      'Content-Range': `bytes ${start}-${end}/${buffer.byteLength}`,
      'Content-Length': String(end - start + 1),
      'Accept-Ranges': 'bytes',
    },
  });
}
