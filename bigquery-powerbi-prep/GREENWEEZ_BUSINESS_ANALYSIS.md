# 🌱 TOPO GREENWEEZ - Business Model & Opportunités Géographiques

## 📊 **PROFILE ENTREPRISE**

### **Histoire & Positionnement**
- **Création** : 2008 par Romain Roy
- **Vision** : Rendre les produits bio et éco-responsables accessibles partout en France
- **Evolution** : De 15 000 → 180 000 produits (marketplace)
- **Équipe** : +200 salariés
- **Siège** : Saint-Jorioz, Lac d'Annecy (Haute-Savoie)

### **Business Model Actuel**
- **Marketplace éco-responsable** (pas juste épicerie bio)
- **B2C principal** + espaces B2B (entreprises/fournisseurs)
- **Omnicanal** : Site web + App mobile + Marketplace vendeurs
- **Société à mission** depuis 2021 (objectifs sociaux/environnementaux)

---

## 🛒 **CATALOGUE & CATEGORIES**

### **Univers Produits** (cohérent avec votre dataset)
1. **Alimentation** (Bio/Sans gluten/Régimes spéciaux)
2. **Bébé & Enfant** (Couches bio/Alimentation bébé)
3. **Beauté & Hygiène** (Cosmétiques naturels)
4. **Santé & Bien-être** (Compléments alimentaires)
5. **Entretien** (Lessive écologique)
6. **Maison & Extérieur** (Mobilier/Literie/Décoration)
7. **Mode** (Vêtements éco-responsables)
8. **Sport & Outdoor** (Team Sport Greenweez)
9. **Électroménager** (Produits durables)
10. **Seconde main** (Reconditionnés)

### **Prix & Positionnement**
- **"Petits prix toute l'année"** (segment accessible)
- **Labels premium** mais prix justes
- **Segments** : Économique, Standard, Premium ✅ (match dataset)

---

## 🚚 **LOGISTIQUE & GÉOGRAPHIE**

### **Couverture Actuelle**
- **Livraison partout en France** ✅
- **Point relais** : Livraison offerte dès 39€
- **Délai** : 2-3 jours ouvrés
- **Prix** : À partir de 1€
- **Plateformes** : France + Espagne

### **Infrastructure**
- **Siège** : Saint-Jorioz (74)
- **Entrepôts** : Plusieurs plateformes françaises
- **Expansion** : Espagne (international en cours)

---

## 🎯 **OPPORTUNITÉS GÉOGRAPHIQUES RÉALISTES**

### **Granularité Régionale (Recommandée)**
```
FRANCE MÉTROPOLITAINE (13 régions)
├── Île-de-France (35% CA - Paris, banlieue CSP+)
├── Auvergne-Rhône-Alpes (15% CA - Lyon, Annecy siège)
├── Provence-Alpes-Côte d'Azur (12% CA - Nice, Marseille)
├── Nouvelle-Aquitaine (8% CA - Bordeaux, bio traditionnel)
├── Occitanie (7% CA - Toulouse, Montpellier)
├── Hauts-de-France (5% CA - Lille, densité urbaine)
├── Grand Est (5% CA - Strasbourg, transfrontalier)
├── Pays de la Loire (4% CA - Nantes, agriculture bio)
├── Bretagne (3% CA - Rennes, terroir bio)
├── Normandie (3% CA - Caen, agriculture)
├── Bourgogne-Franche-Comté (2% CA - Dijon)
├── Centre-Val de Loire (1% CA - Orléans)
└── Corse (0.5% CA - Ajaccio, niche)
```

### **Granularité Départementale (Avancée)**
```
TOP DÉPARTEMENTS BIO (basé sur réalité marché)
├── 75 - Paris (25% CA)
├── 69 - Rhône (8% CA) 
├── 13 - Bouches-du-Rhône (6% CA)
├── 31 - Haute-Garonne (4% CA)
├── 74 - Haute-Savoie (3% CA - siège)
├── 44 - Loire-Atlantique (3% CA)
├── 33 - Gironde (3% CA)
└── ... (autres départements)
```

### **Granularité Villes (Ultra-réaliste)**
```
TOP 15 VILLES GREENWEEZ (estimé cohérent)
├── Paris (20% CA)
├── Lyon (6% CA)
├── Marseille (4% CA) 
├── Toulouse (3% CA)
├── Nice (2.5% CA)
├── Nantes (2% CA)
├── Strasbourg (2% CA)
├── Montpellier (2% CA)
├── Bordeaux (2% CA)
├── Lille (1.5% CA)
├── Rennes (1.5% CA)
├── Annecy (1% CA - proximité siège)
├── Grenoble (1% CA - Alpes, éco-conscient)
├── Aix-en-Provence (1% CA)
└── Tours (0.5% CA)
```

---

## 📈 **PROFIL CLIENT GÉOGRAPHIQUE**

### **Typologie par Zone**
- **Urbain dense** (Paris, Lyon) : Premium, convenience
- **Métropoles régionales** : Standard/Premium équilibré  
- **Villes moyennes** : Économique dominant
- **Rural/Périurbain** : Livraison point relais, bulk orders

### **Saisonnalité Régionale**
- **Sud** : Pic été (cosmétiques bio, sport outdoor)
- **Montagne** : Hiver (compléments, bien-être)
- **Ouest** : Automne (produits terroir, conserves bio)

---

## 🎨 **RECOMMANDATIONS DATASET GÉOGRAPHIQUE**

### **Option 1 : Régions (Simple & Impactant)**
- 13 régions françaises
- Distribution réaliste basée sur PIB/population urbaine
- Cartes Power BI natives excellentes
- **Facile à expliquer aux clients**

### **Option 2 : Départements (Détaillé)**
- Top 20 départements français
- Permet analyse fine zones rurales/urbaines
- **Parfait pour dashboard avancé**

### **Option 3 : Villes (Ultra-précis)**
- Top 50 villes françaises
- Permet géomarketing précis
- **Impressionnant en démo client**

### **Variables Géo à Ajouter**
```sql
-- Structure recommandée pour enrichissement
ALTER TABLE green_sales ADD COLUMN region_name STRING;
ALTER TABLE green_sales ADD COLUMN departement_code STRING;  
ALTER TABLE green_sales ADD COLUMN ville_name STRING;
ALTER TABLE green_sales ADD COLUMN population_density STRING; -- Dense/Moyen/Rural
ALTER TABLE green_sales ADD COLUMN zone_climatique STRING; -- Nord/Sud/Montagne
```

---

## 🏆 **AVANTAGES BUSINESS POUR DASHBOARD**

### **Insights Géographiques Possibles**
- **Top régions** par CA/croissance
- **Saisonnalité** par zone climatique  
- **Pénétration marché** urbain/rural
- **Optimisation logistique** (coûts livraison)
- **Expansion commerciale** (zones sous-performantes)

### **Visualisations Power BI**
- **Cartes choroplèthes** (régions colorées par CA)
- **Cartes à bulles** (villes par volume)
- **Heatmaps temporelles** (évolution géographique)
- **Analyses corridor** (axes commerciaux)

**🎯 Ma recommandation : Commencer par les RÉGIONS (Option 1) - Impact visuel maximum, complexité minimum, parfait pour portfolio !**

Quelle approche géographique vous intéresse le plus ?
