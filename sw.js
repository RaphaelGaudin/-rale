// Service worker : l'app fonctionne hors-ligne, et se met à jour dès qu'il y a du réseau.
const CACHE = 'orale-v1';
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
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

// Réseau d'abord (avec délai max), sinon cache.
self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET' || new URL(request.url).origin !== self.location.origin) return;
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
