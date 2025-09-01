# 🚀 BIGQUERY ➜ POWER BI PREP

## 📋 **Purpose**

Ce dossier prépare vos données BigQuery pour Power BI.
**Plus de Plotly, plus de serveurs, plus de galères !**

## 📊 **Fichiers utiles**

### **🎯 Export Power BI**

- `export_for_powerbi.py` ➜ **Script principal** - Export CSV optimisé pour Power BI
- `.env` ➜ **Credentials** BigQuery (à garder secret !)

### **🔍 Analyse & Debug**

- `business_analysis.py` ➜ Analyses business avancées
- `explore_data.py` ➜ Exploration des données BigQuery
- `test_connection.py` ➜ Test de connexion BigQuery

### **📂 Données**

- `data/powerbi_exports/` ➜ **Fichiers CSV** pour Power BI
- `requirements.txt` ➜ Dépendances Python (si besoin)

## 🚀 **Usage**

### **1. Export pour Power BI**

```bash
cd /var/www/production-workspace/bigquery-powerbi-prep
python3 export_for_powerbi.py
```

### **2. Télécharger sur Mac**

```bash
scp -r user@server:/path/to/data/powerbi_exports/ ~/Downloads/
```

### **3. Import dans Power BI**

- Power BI Service ➜ Obtenir des données ➜ CSV
- Drag & drop vos graphiques !

## 💡 **Workflow Freelance**

1. **Serveur Linux** ➜ Prépare les données (ce dossier)
2. **Mac** ➜ Power BI pour le rendu client
3. **Facturation** ➜ Dashboard pro sans galères techniques !

---
**✅ Fini Plotly ! Vive Power BI ! 🎉**
