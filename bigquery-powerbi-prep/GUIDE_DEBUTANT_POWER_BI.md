# 🚀 GUIDE DÉBUTANT POWER BI - DASHBOARD COURSE_GREEN
## ÉTAPE PAR ÉTAPE POUR VOTRE PREMIER DASHBOARD

---

## 🎯 **ÉTAPE 1: TÉLÉCHARGER LES DONNÉES**

### Sur votre serveur Linux:
```bash
# Compresser les fichiers CSV pour téléchargement facile
cd /var/www/production-workspace/bigquery-powerbi-prep/data/powerbi_exports
tar -czf course_green_powerbi.tar.gz *.csv
```

### Sur votre Mac:
```bash
# Télécharger l'archive (remplacez par vos infos serveur)
scp user@votre-serveur:/var/www/production-workspace/bigquery-powerbi-prep/data/powerbi_exports/course_green_powerbi.tar.gz ~/Downloads/

# Décompresser
cd ~/Downloads
tar -xzf course_green_powerbi.tar.gz
```

---

## 🎯 **ÉTAPE 2: OUVRIR POWER BI DESKTOP**

1. **Lancer Power BI Desktop** sur votre Mac
2. Cliquer sur **"Blank report"** (Rapport vide)

---

## 🎯 **ÉTAPE 3: IMPORTER LES DONNÉES (CRUCIAL!)**

### **Import du fichier principal:**
1. **Ruban "Home"** → **"Get Data"** → **"Text/CSV"**
2. Sélectionner: **`course_green_overview.csv`** (LE PLUS IMPORTANT)
3. **Preview** → Vérifier que les colonnes sont bien détectées
4. **"Load"** (Charger)

### **Import des fichiers de référence** (optionnel pour démarrer):
Répéter pour:
- `kpis_globaux.csv` (pour les cartes KPI)
- `category_analysis.csv` (pour les analyses catégories)

---

## 🎯 **ÉTAPE 4: VOTRE PREMIÈRE VISUALISATION - CARTE KPI**

### **Créer une carte "Chiffre d'Affaires Total":**
1. **Panneau "Visualizations"** → Cliquer sur **"Card"** (icône rectangle)
2. **Panneau "Fields"** → Glisser **"chiffre_affaires"** dans **"Fields"**
3. 🎉 **BOOM!** Votre première visualisation!

### **Formatage de la carte:**
1. Cliquer sur votre carte → **Panneau "Format"** (rouleau de peinture)
2. **"Data label"** → **"Display units"** → **"Thousands"** ou **"Auto"**
3. **"Title"** → Changer pour **"Chiffre d'Affaires Total"**

---

## 🎯 **ÉTAPE 5: GRAPHIQUE EN BARRES - TOP PRODUITS**

### **Créer un graphique en barres:**
1. Cliquer dans un espace vide du canvas
2. **Visualizations** → **"Clustered bar chart"**
3. **Glisser les champs:**
   - **Axis (Y):** `pdt_name` (nom des produits)
   - **Values (X):** `chiffre_affaires` (CA)
4. **Votre graphique apparaît!** 📊

### **Améliorer le graphique:**
1. **Clic droit** sur le graphique → **"Sort by"** → **"chiffre_affaires"**
2. **Format** → **"X-Axis"** → **"Display units"** → **"Thousands"**
3. **Titre:** "Top Produits par Chiffre d'Affaires"

---

## 🎯 **ÉTAPE 6: GRAPHIQUE DONUT - RÉPARTITION CATÉGORIES**

### **Créer un donut:**
1. Nouvelle zone vide → **"Donut chart"**
2. **Glisser les champs:**
   - **Legend:** `category_1` (catégorie principale)
   - **Values:** `chiffre_affaires`
3. **Magic!** Répartition par catégorie 🍩

---

## 🎯 **ÉTAPE 7: SCATTER PLOT - PRIX VS QUANTITÉ**

### **Relation Prix/Quantité:**
1. **"Scatter chart"**
2. **Champs:**
   - **X Axis:** `ps_cat` (prix standard)
   - **Y Axis:** `qty` (quantité)
   - **Size:** `chiffre_affaires`
   - **Legend:** `category_1`
3. **Tendances visibles!** 📈

---

## 🎯 **ÉTAPE 8: FILTRES INTERACTIFS (SLICER)**

### **Ajouter un filtre catégorie:**
1. **"Slicer"** visualization
2. **Field:** `category_1`
3. **Positionnez en haut de votre dashboard**
4. **Testez!** Cliquez sur une catégorie → Toutes vos visualisations se filtrent automatiquement! ✨

---

## 🎯 **ÉTAPE 9: MISE EN PAGE ET DESIGN**

### **Organisation:**
1. **Redimensionnez** vos visualisations
2. **Alignez** les éléments (guides automatiques)
3. **Espacez** harmonieusement

### **Thème professionnel:**
1. **View** → **Themes** → Choisir un thème (ex: "Executive")
2. **Instant professional look!** 🎨

---

## 🎯 **ÉTAPE 10: TITRE ET FINALISATION**

### **Ajouter un titre principal:**
1. **Insert** → **Text box**
2. Taper: **"Dashboard Course Green - Analyse E-commerce"**
3. **Formatage:** Police grande, couleur thème

### **Sauvegarder:**
1. **File** → **Save As**
2. Nom: **"Dashboard_Course_Green_v1.pbix"**

---

## 🎉 **FÉLICITATIONS!**

**Vous venez de créer votre premier dashboard Power BI professionnel!**

### **Ce que vous avez accompli:**
✅ Import de données CSV  
✅ Cartes KPI  
✅ Graphiques en barres  
✅ Graphique donut  
✅ Scatter plot  
✅ Filtres interactifs  
✅ Design professionnel  

---

## 🚀 **PROCHAINES ÉTAPES AVANCÉES:**

1. **Ajouter des pages** (onglets) pour les 6 slides recommandés
2. **Créer des mesures DAX** pour des calculs avancés
3. **Relations entre tables** pour des analyses croisées
4. **Formatage conditionnel** pour des alertes visuelles

---

## ⚠️ **CONSEILS PREMIÈRE FOIS:**

### **Si ça ne marche pas:**
1. **Vérifiez les types de colonnes** (Text, Number, Date)
2. **Format** → **Data type** pour corriger
3. **N'hésitez pas** à expérimenter!

### **Bonnes pratiques:**
- **Sauvegardez souvent** (Ctrl+S)
- **Nommez vos visualisations** clairement
- **Testez les filtres** régulièrement
- **Gardez un design cohérent**

---

**🎯 Vous êtes maintenant prêt(e) pour créer votre showcase Power BI!**
