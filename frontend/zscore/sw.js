/**
 * 🚀 SERVICE WORKER - ZineInsight Revolutionary
 * Cache intelligent pour de meilleures performances
 */

const CACHE_NAME = 'zineinsight-revolutionary-v1';
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/js/simple-config.js',
    '/js/simple-api.js',
    '/js/zineinsight-core.js',
    '/css/revolutionary.css'
];

// Installation du service worker
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('🗄️ Cache initialized');
                return cache.addAll(STATIC_ASSETS);
            })
            .catch(() => {
                console.log('Cache not available, continuing without');
            })
    );
});

// Stratégie de cache : Cache First pour les assets statiques
self.addEventListener('fetch', (event) => {
    // Ignorer les appels à ton site production (port 8000)
    if (event.request.url.includes(':8000')) {
        return;
    }
    
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                return response || fetch(event.request);
            })
    );
});
