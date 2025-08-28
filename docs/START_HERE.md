# ✨ Revolutionary Platform - Organisation Améliorée

## 🎯 **USAGE RAPIDE (Commandes Principales)**

```bash
# Démarrer le système complet (recommandé)
./start full

# Tester les APIs d'authentification
./start test

# Voir le statut
./start status

# Frontend seul (développement)
./go
```

## 📁 **Nouvelle Organisation (Plus Propre)**

Les scripts sont maintenant organisés dans `/scripts/` pour garder la racine propre :

```
/var/www/Revolutionnary/
├── start -> scripts/start.sh     # 🚀 Script principal
├── go -> scripts/go.sh          # 🌐 Frontend dev
├── scripts/                     # 📁 Tous les scripts
│   ├── start.sh                 # Script maître
│   ├── go.sh                    # Frontend seul
│   ├── optimize.sh              # Optimisations
│   ├── production-mode.sh       # Switch dev/prod
│   └── README.md               # Doc détaillée
├── SCRIPTS.md                   # Guide des scripts
├── ROADMAP.md                   # Feuille de route
└── ...
```

## 🔗 **Liens Symboliques**

Des liens symboliques permettent l'utilisation directe depuis la racine :

- `./start` → `scripts/start.sh`
- `./go` → `scripts/go.sh`

## 📋 **Documentation**

- **`SCRIPTS.md`** : Guide complet des scripts
- **`scripts/README.md`** : Documentation technique détaillée
- **`ROADMAP.md`** : Prochaines étapes et objectifs

---

**🎉 Résultat : Racine propre + Organisation professionnelle !**
