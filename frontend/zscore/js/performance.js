/**
 * 🚀 OPTIMISATIONS PERFORMANCE - ZineInsight Revolutionary
 */

// Pre-loading intelligent
document.addEventListener('DOMContentLoaded', function() {
    // Lazy loading des images
    if ('IntersectionObserver' in window) {
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        images.forEach(img => imageObserver.observe(img));
    }
    
    // Cache des appels API
    if (!window.apiCache) {
        window.apiCache = new Map();
    }
    
    // Préchargement des ressources critiques
    const criticalResources = [
        '/js/simple-config.js',
        '/js/simple-api.js',
        '/js/zineinsight-core.js'
    ];
    
    criticalResources.forEach(resource => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = resource;
        document.head.appendChild(link);
    });
    
    console.log('⚡ Performance optimizations loaded');
});

// Service Worker pour mise en cache (optionnel)
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(() => {
        console.log('Service worker not available, running without cache');
    });
}
