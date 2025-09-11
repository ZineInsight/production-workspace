// Création d'un script pour analyser les traductions manquantes
const fs = require('fs');

// Extraire toutes les clés data-i18n du HTML
const htmlContent = `<!-- Copiez votre contenu HTML ici -->`;
const dataI18nRegex = /data-i18n="([^"]+)"/g;
const htmlKeys = [];
let match;

while ((match = dataI18nRegex.exec(htmlContent)) !== null) {
    htmlKeys.push(match[1]);
}

// Traductions existantes (structure simplifiée)
const existingTranslations = {
    "nav.brand": true,
    "nav.tagline": true,
    "nav.dashboards": true,
    // ... (à compléter avec toutes les traductions existantes)
};

// Trouver les clés manquantes
const missingKeys = htmlKeys.filter(key => !existingTranslations[key]);

console.log('Clés manquantes:', missingKeys);
