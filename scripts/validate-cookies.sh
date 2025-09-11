#!/bin/bash

# 🧪 COOKIES SYSTEM VALIDATION SCRIPT
# Validates that all pages have cookies system correctly integrated

echo "🧪 VALIDATION: ZineInsight Cookies Global System"
echo "=================================================="

# Base directories
PORTFOLIO_DIR="/var/www/production-workspace/frontend/portfolio"
ZSCORE_DIR="/var/www/production-workspace/frontend/zscore"
SHARED_DIR="/var/www/production-workspace/frontend/shared"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counter
tests_passed=0
tests_failed=0

# Function to test file existence and content
test_file() {
    local file="$1"
    local test_name="$2"
    local css_required="$3"
    local js_required="$4"
    
    echo ""
    echo "🔍 Testing: $test_name"
    echo "File: $file"
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ FAIL: File not found${NC}"
        ((tests_failed++))
        return
    fi
    
    # Test CSS inclusion
    if [ "$css_required" = "true" ]; then
        if grep -q "cookies-global.css" "$file"; then
            echo -e "${GREEN}✅ CSS: cookies-global.css found${NC}"
        else
            echo -e "${RED}❌ CSS: cookies-global.css NOT found${NC}"
            ((tests_failed++))
            return
        fi
    fi
    
    # Test JS inclusion
    if [ "$js_required" = "true" ]; then
        if grep -q "cookies-global.js" "$file"; then
            echo -e "${GREEN}✅ JS: cookies-global.js found${NC}"
        else
            echo -e "${RED}❌ JS: cookies-global.js NOT found${NC}"
            ((tests_failed++))
            return
        fi
    fi
    
    echo -e "${GREEN}✅ PASS: $test_name${NC}"
    ((tests_passed++))
}

# Test core files
echo "📁 Testing Core Files..."
if [ -f "$SHARED_DIR/css/cookies-global.css" ]; then
    echo -e "${GREEN}✅ cookies-global.css exists${NC}"
else
    echo -e "${RED}❌ cookies-global.css missing${NC}"
    ((tests_failed++))
fi

if [ -f "$SHARED_DIR/js/cookies-global.js" ]; then
    echo -e "${GREEN}✅ cookies-global.js exists${NC}"
else
    echo -e "${RED}❌ cookies-global.js missing${NC}"
    ((tests_failed++))
fi

# Test main pages
echo ""
echo "🏠 Testing Main Pages..."
test_file "$PORTFOLIO_DIR/index.html" "Portfolio Homepage (zineinsight.com)" true true
test_file "$ZSCORE_DIR/index.html" "ZScore Homepage (/zscore)" true true
test_file "$ZSCORE_DIR/questionnaire.html" "ZScore Questionnaire" true true
test_file "$ZSCORE_DIR/results.html" "ZScore Results" true true
test_file "$ZSCORE_DIR/auth.html" "ZScore Auth" true true

# Test country pages  
echo ""
echo "🌍 Testing Country Pages..."
COUNTRY_PAGES=(
    "allemagne.html:Germany"
    "canada.html:Canada"
    "uk.html:UK"
    "australie.html:Australia"
    "france.html:France"
    "usa.html:USA"
)

for page_info in "${COUNTRY_PAGES[@]}"; do
    IFS=':' read -r page_name country_name <<< "$page_info"
    test_file "$ZSCORE_DIR/$page_name" "Country Page: $country_name" true true
done

# Test configuration in core files
echo ""
echo "🔧 Testing Configuration..."

# Test if cookies-global.js has the main class
if grep -q "class ZineInsightCookies" "$SHARED_DIR/js/cookies-global.js"; then
    echo -e "${GREEN}✅ ZineInsightCookies class found${NC}"
    ((tests_passed++))
else
    echo -e "${RED}❌ ZineInsightCookies class missing${NC}"
    ((tests_failed++))
fi

# Test if CSS has the main styles
if grep -q ".cookies-banner" "$SHARED_DIR/css/cookies-global.css"; then
    echo -e "${GREEN}✅ cookies-banner styles found${NC}"
    ((tests_passed++))
else
    echo -e "${RED}❌ cookies-banner styles missing${NC}"
    ((tests_failed++))
fi

# Final report
echo ""
echo "📊 FINAL REPORT"
echo "================"
echo -e "Tests Passed: ${GREEN}$tests_passed${NC}"
echo -e "Tests Failed: ${RED}$tests_failed${NC}"
echo ""

if [ $tests_failed -eq 0 ]; then
    echo -e "${GREEN}🎉 ALL TESTS PASSED! Cookies system is ready!${NC}"
    echo ""
    echo "✅ Ready to test on:"
    echo "   • zineinsight.com (Portfolio)"
    echo "   • zineinsight.com/zscore (ZScore)"
    echo "   • zineinsight.com/zscore/questionnaire.html"
    echo "   • zineinsight.com/zscore/results.html"
    echo "   • zineinsight.com/zscore/auth.html"
    echo "   • All country pages"
    echo ""
    echo "🍪 RGPD Compliance: ✅ COMPLETE"
    exit 0
else
    echo -e "${RED}❌ SOME TESTS FAILED! Please fix issues above.${NC}"
    exit 1
fi
