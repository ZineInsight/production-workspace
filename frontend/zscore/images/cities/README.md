# 🖼️ Images des Villes - Revolutionary

## 📁 Structure

```
images/cities/
├── agadir.webp          ← Format WebP (recommandé)
├── casablanca.jpg       ← Format JPG (accepté)
├── ouarzazate.png       ← Format PNG (accepté)
├── rabat.jpeg           ← Format JPEG (accepté)
└── ... (autres villes)
```

## 🖼️ Formats supportés

### ✅ **Tous formats acceptés :**

- **`.webp`** → Recommandé (meilleure compression)
- **`.jpg`** → Standard (très répandu)
- **`.jpeg`** → Standard (même que JPG)
- **`.png`** → Bonne qualité (avec transparence)
- **`.gif`** → Supporté (animations possibles)

### 🏆 **Recommandation par priorité :**

1. **WebP** → Poids léger, qualité excellente
2. **JPG/JPEG** → Bon compromis poids/qualité
3. **PNG** → Si besoin de transparence
4. **GIF** → Si animation nécessaire

## 🎯 Comment ajouter une nouvelle photo

### 1. Préparer l'image

- **Formats acceptés** : WebP, JPG, JPEG, PNG, GIF
- **Dimensions** : 800x400px minimum
- **Poids** : < 200KB recommandé (< 500KB max)
- **Qualité** : Photo panoramique ou vue emblématique

### 2. Nommer le fichier

- **Exemples valides** :
  - `casablanca.jpg` ✅
  - `agadir.webp` ✅
  - `fes.png` ✅
  - `rabat.jpeg` ✅

## 🎯 Comment ajouter une nouvelle photo

### 1. Préparer l'image

- **Format recommandé** : WebP (meilleure compression)
- **Dimensions** : 800x400px minimum
- **Poids** : < 200KB recommandé
- **Qualité** : Photo panoramique ou vue emblématique de la ville

### 2. Nommer le fichier

- **Format** : `nomville.webp` (tout en minuscules)
- **Exemples** :
  - Casablanca → `casablanca.webp`
  - Fès → `fes.webp`
  - Laâyoune → `laayoune.webp`

### 3. Ajouter au mapping JavaScript

Éditer `/js/results.js` ligne ~10 :

```javascript
const CITY_IMAGES = {
    // Ajouter la nouvelle ville
    'Nouvelle Ville': 'images/cities/nouvelleville.webp',
    // ...
};
```

### 4. Tester

- Lancer l'application
- Si la ville est #1 dans les résultats → l'image s'affiche
- Si pas d'image → placeholder avec "Image à venir..."

## 🔧 Outils de conversion

### Convertir en WebP (Linux/Mac)

```bash
# Installer webp
apt install webp  # Ubuntu
brew install webp  # Mac

# Convertir
cwebp input.jpg -q 80 -o output.webp
```

### Redimensionner

```bash
# Avec ImageMagick
convert input.jpg -resize 800x400^ -gravity center -crop 800x400+0+0 output.jpg
```

## 📊 Status des images

- ✅ **Agadir** : agadir.webp
- ✅ **Casablanca** : casablanca.webp
- ✅ **Ouarzazate** : ouarzazate.webp
- ❌ **Rabat** : À ajouter
- ❌ **Marrakech** : À ajouter
- ❌ **Fès** : À ajouter

*Mise à jour au fur et à mesure...*
