# 🚀 NGINX CONFIGURATIONS - ZineInsight Revolutionary

## 📁 Structure des configurations Nginx

### ✅ **CONFIGURATION ACTIVE**

- **Serveur** : `/etc/nginx/sites-available/zineinsight-spa-simple.conf`
- **Status** : 🟢 En production depuis Aug 22, 2025
- **Fonction** : Configuration ultra-simple et efficace

```nginx
# API Proxy simplifié
location ~ ^/api/(.*)$ {
    proxy_pass http://127.0.0.1:8000/api/$1$is_args$args;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### 📚 **CONFIGURATIONS DE RÉFÉRENCE**

#### `nginx-api-proxy-reference.conf`

- **Usage** : Configuration de base pour proxy API
- **Avantage** : Headers CORS complets, timeouts configurés
- **Status** : 📖 Documentation/référence

#### `nginx-auth.conf` (ARCHIVÉ)

- **Usage** : Anciennes règles d'authentification
- **Status** : 🗄️ Archivé (historique)

### 🛠️ **CONFIGURATIONS WORKSPACE**

#### `/nginx-api-proxy.conf`

- **Status** : 📖 Référence active
- **Usage** : Template de base pour nouvelles installations

#### `/nginx-unified.conf`

- **Status** : 🗄️ Configuration complexe (backup)
- **Usage** : Version complète avec toutes les optimisations

## 🔧 **COMMANDES UTILES**

### Tester configuration

```bash
sudo nginx -t
```

### Recharger configuration

```bash
sudo systemctl reload nginx
```

### Voir configuration active

```bash
sudo nginx -T | grep -A 20 "server_name zineinsight.com"
```

### Backup configuration

```bash
sudo cp /etc/nginx/sites-available/zineinsight-spa-simple.conf \
       /var/www/Revolutionnary/docs/nginx/backup-$(date +%Y%m%d).conf
```

## 📊 **HISTORIQUE**

- **Aug 22, 2025** : Résolution problème API proxy avec configuration simple
- **Aug 21, 2025** : Configurations complexes avec multiples règles
- **Aug 19, 2025** : Configuration initiale auth

## 🎯 **NOTES IMPORTANTES**

1. **Ne pas modifier** la configuration active sans backup
2. **Tester toujours** avec `nginx -t` avant reload
3. **Backend doit tourner** sur port 8000 pour que le proxy fonctionne
4. **Certificats SSL** gérés par Let's Encrypt automatiquement
