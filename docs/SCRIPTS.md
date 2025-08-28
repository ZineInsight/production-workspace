# 🚀 Scripts de Lancement - Revolutionary Platform

## � **Nouvelle Organisation (Plus Propre !)**

Tous les scripts sont maintenant organisés dans `/scripts/` avec des liens symboliques à la racine.

```bash
# Utilisation simple depuis la racine
./start full        # = ./scripts/start.sh full
./go               # = ./scripts/go.sh
```

## �📋 Scripts Disponibles (Optimisés)

### **🎯 start** - Script Principal (RECOMMANDÉ)

Script maître pour lancer ton système d'authentification complet

```bash
./start             # Backend JWT + PaywallManager
./start full        # Backend + Frontend dev (port 3000)
./start stop        # Arrêter tout
./start status      # Voir le statut
./start test        # Tester les APIs auth
```

### **🌐 go** - Frontend Seul

Lance uniquement le frontend Revolutionary

```bash
./go           # Frontend sur port 3000 (lien vers scripts/go.sh)
# Ou directement: ./scripts/go.sh
```

### **⚡ optimize.sh** - Optimisations

Optimise les performances du système

```bash
./optimize.sh  # Cache Python + Service Worker + Performance
```

### **🏭 production-mode.sh** - Switch Dev/Prod

Bascule entre mode développement et production

```bash
./production-mode.sh dev      # Mode développement
./production-mode.sh prod     # Mode production (systemd)
./production-mode.sh status   # Voir le mode actuel
```

---

## 🎯 Usage Recommandé

### **Pour développer/tester :**

```bash
./start.sh full     # Système complet
# Puis aller sur https://localhost:8443/auth.html
```

### **Pour la production :**

```bash
./production-mode.sh prod    # Activer systemd
# Ton site sera disponible automatiquement
```

### **Pour optimiser :**

```bash
./optimize.sh       # Optimisations performance
```

---

## 🗑️ Scripts Supprimés (Redondants)

- ❌ **super.sh** → Remplacé par `start.sh full`
- ❌ **launch-your-site.sh** → Obsolète (cherchait dans UNUSED_BACKUP)
- ❌ **restart-revolutionary.sh** → Remplacé par `start.sh restart`
- ❌ **redis-cache-optimizer.sh** → Intégré dans `optimize.sh`
- ❌ **revolutionary.sh** → Remplacé par `start.sh`

---

## ✅ Système Final

Tu as maintenant **4 scripts optimaux** qui couvrent tous tes besoins :

1. **start.sh** → Lancement système auth complet
2. **go.sh** → Frontend seul
3. **optimize.sh** → Performance
4. **production-mode.sh** → Dev/Prod switch

**Plus de redondance, plus de confusion !** 🎉
