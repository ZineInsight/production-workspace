#!/bin/bash

# 🚀 ZineInsight Production Deployment Script
# =============================================

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🚀 ZineInsight Production Deployment${NC}"
echo "======================================"

# 1. Backup current configuration
echo -e "${YELLOW}📋 Creating backup...${NC}"
sudo cp /etc/nginx/sites-available/zineinsight.conf /etc/nginx/sites-available/zineinsight.conf.backup.$(date +%Y%m%d_%H%M%S)

# 2. Update nginx configuration
echo -e "${YELLOW}🔧 Updating nginx configuration...${NC}"
sudo cp nginx/nginx-unified.conf /etc/nginx/sites-available/zineinsight.conf

# 3. Update nginx to point to production workspace
echo -e "${YELLOW}📁 Updating file paths...${NC}"
sudo sed -i 's|/var/www/Revolutionnary/platform/frontend|/var/www/production-workspace/frontend|g' /etc/nginx/sites-available/zineinsight.conf

# 4. Test nginx configuration
echo -e "${YELLOW}✅ Testing nginx configuration...${NC}"
sudo nginx -t

# 5. Reload nginx
echo -e "${YELLOW}🔄 Reloading nginx...${NC}"
sudo systemctl reload nginx

# 6. Update backend path (if needed)
echo -e "${YELLOW}⚙️ Backend update available in backend/ directory${NC}"

echo ""
echo -e "${GREEN}✅ Deployment completed successfully!${NC}"
echo ""
echo -e "${BLUE}🌍 Live URLs:${NC}"
echo "   - Homepage: https://zineinsight.com/"
echo "   - ZScore: https://zineinsight.com/zscore/"
echo "   - How it works: https://zineinsight.com/geo-intelligence/"
echo ""
echo -e "${BLUE}📁 Production paths:${NC}"
echo "   - Frontend: /var/www/production-workspace/frontend/"
echo "   - Backend: /var/www/production-workspace/backend/"
echo "   - Nginx: /var/www/production-workspace/nginx/"

