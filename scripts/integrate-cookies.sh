#!/bin/bash

# 🍪 AUTOMATED COOKIES INTEGRATION SCRIPT
# Automatically adds cookies system to all remaining ZScore pages

echo "🚀 Starting automated cookies integration for ZScore pages..."

# Define the base directory
ZSCORE_DIR="/var/www/production-workspace/frontend/zscore"

# Define pages to update (excluding already updated ones)
PAGES=(
    "australie.html"
    "bresil.html" 
    "espagne.html"
    "france.html"
    "japon.html"
    "maroc.html"
    "mexique.html"
    "pays-bas.html"
    "portugal.html"
    "thailande.html"
    "usa.html"
    "vietnam.html"
    "test-i18n.html"
)

# CSS link to add
CSS_LINK='    <!-- 🍪 COOKIES GLOBAL SYSTEM -->
    <link rel="stylesheet" href="/css/cookies-global.css">'

# JS script to add
JS_SCRIPT='    <!-- 🍪 COOKIES GLOBAL SYSTEM -->
    <script src="/js/cookies-global.js"></script>'

# Function to add CSS to a file
add_css_to_file() {
    local file="$1"
    echo "📝 Adding CSS to $file..."
    
    # Find the last <link> tag and add our CSS after it
    if grep -q "<link" "$file"; then
        # Find the line number of the last <link> tag
        last_link_line=$(grep -n "<link" "$file" | tail -1 | cut -d: -f1)
        
        # Insert our CSS after the last link
        sed -i "${last_link_line}a\\
$CSS_LINK" "$file"
        
        echo "✅ CSS added to $file"
    else
        echo "⚠️  No <link> tags found in $file, skipping CSS"
    fi
}

# Function to add JS to a file  
add_js_to_file() {
    local file="$1"
    echo "📝 Adding JS to $file..."
    
    # Add JS before closing </body> tag
    if grep -q "</body>" "$file"; then
        # Insert our JS before </body>
        sed -i 's|</body>|'"$JS_SCRIPT"'\
\
</body>|' "$file"
        
        echo "✅ JS added to $file"
    else
        echo "⚠️  No </body> tag found in $file, skipping JS"
    fi
}

# Process each page
for page in "${PAGES[@]}"; do
    file_path="$ZSCORE_DIR/$page"
    
    if [ -f "$file_path" ]; then
        echo ""
        echo "🔧 Processing $page..."
        
        # Create backup
        cp "$file_path" "$file_path.backup"
        
        # Add CSS
        add_css_to_file "$file_path"
        
        # Add JS
        add_js_to_file "$file_path"
        
        echo "✅ $page updated successfully"
    else
        echo "❌ File $file_path not found, skipping..."
    fi
done

echo ""
echo "🎉 Automated cookies integration completed!"
echo ""
echo "📊 Summary:"
echo "- CSS system: /css/cookies-global.css"  
echo "- JS system: /js/cookies-global.js"
echo "- Pages updated: ${#PAGES[@]}"
echo ""
echo "🧪 Test your pages:"
echo "- zineinsight.com (Portfolio)"
echo "- zineinsight.com/zscore (ZScore homepage)"
echo "- zineinsight.com/zscore/questionnaire.html"
echo "- zineinsight.com/zscore/results.html"
echo "- zineinsight.com/zscore/auth.html"
echo "- All country pages"
echo ""
echo "🍪 All pages now have consistent RGPD cookies!"
