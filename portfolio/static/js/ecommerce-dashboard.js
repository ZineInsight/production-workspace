// ====================================
//   🚀 E-COMMERCE DASHBOARD JAVASCRIPT
//   Fonctionnalités interactives Power BI style
// ====================================

// Configuration des données (basées sur data_ecommerce.py)
const ECOMMERCE_DATA = {
    mainMetrics: {
        ca: { value: 574, growth: 14.8 },
        marge: { value: 60.72, percentage: 10.58 },
        commandes: { value: 1247, growth: 12.3 },
        clients: { value: 892, growth: 8.7 }
    },
    
    monthlyData: [
        { month: 'Jan', revenue: 78.5, orders: 167 },
        { month: 'Fév', revenue: 65.2, orders: 142 },
        { month: 'Mar', revenue: 71.8, orders: 155 },
        { month: 'Avr', revenue: 82.3, orders: 178 },
        { month: 'Mai', revenue: 89.1, orders: 192 },
        { month: 'Jun', revenue: 94.7, orders: 201 },
        { month: 'Jul', revenue: 67.4, orders: 145 },
        { month: 'Aoû', revenue: 42.1, orders: 98 },
        { month: 'Sep', revenue: 76.9, orders: 163 },
        { month: 'Oct', revenue: 85.4, orders: 181 },
        { month: 'Nov', revenue: 91.8, orders: 195 },
        { month: 'Déc', revenue: 88.2, orders: 189 }
    ],
    
    categories: [
        { name: 'Électronique', revenue: 289.73, percentage: 50.4, color: '#004B87' },
        { name: 'Smartphones', revenue: 153.28, percentage: 26.7, color: '#00BCF2' },
        { name: 'Informatique', revenue: 89.67, percentage: 15.6, color: '#F2C811' },
        { name: 'Santé', revenue: 42.24, percentage: 7.3, color: '#FFB900' }
    ],
    
    topProducts: [
        { name: 'Casques Audio', revenue: 202.45, color: '#107C10' },
        { name: 'iPhone 15', revenue: 153.28, color: '#0078D4' },
        { name: 'Laptops', revenue: 89.67, color: '#D83B01' },
        { name: 'Montres', revenue: 67.82, color: '#00BCF2' },
        { name: 'Suppléments', revenue: 45.33, color: '#FFB900' }
    ]
};

// Couleurs Power BI authentiques
const POWERBI_COLORS = {
    primary: '#004B87',
    secondary: '#00BCF2', 
    accent: '#F2C811',
    success: '#107C10',
    warning: '#FFB900',
    error: '#D83B01',
    background: '#F8F8F8'
};

// ===== INITIALIZATION ===== 
function initEcommerceDashboard() {
    console.log('🚀 Initialisation Dashboard E-commerce Power BI Style');
    
    // Initialize charts
    initTemporalChart();
    initCategoriesChart();
    initProductsChart();
    initKPIGauges();
    
    // Setup interactions
    setupDashboardInteractions();
    
    console.log('✅ Dashboard initialisé avec succès');
}

// ===== TEMPORAL EVOLUTION CHART =====
function initTemporalChart() {
    const ctx = document.getElementById('temporal-chart');
    if (!ctx) return;
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ECOMMERCE_DATA.monthlyData.map(d => d.month),
            datasets: [{
                label: 'CA (K€)',
                data: ECOMMERCE_DATA.monthlyData.map(d => d.revenue),
                borderColor: POWERBI_COLORS.primary,
                backgroundColor: POWERBI_COLORS.primary + '20',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: POWERBI_COLORS.accent,
                pointBorderColor: POWERBI_COLORS.primary,
                pointBorderWidth: 2,
                pointRadius: 6,
                pointHoverRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: POWERBI_COLORS.primary,
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: POWERBI_COLORS.accent,
                    borderWidth: 1,
                    cornerRadius: 8,
                    displayColors: false,
                    callbacks: {
                        label: function(context) {
                            return `CA: ${context.parsed.y}K€`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        color: '#E1E1E1',
                        lineWidth: 1
                    },
                    ticks: {
                        color: '#323130',
                        font: {
                            size: 11
                        }
                    }
                },
                y: {
                    grid: {
                        color: '#E1E1E1',
                        lineWidth: 1
                    },
                    ticks: {
                        color: '#323130',
                        font: {
                            size: 11
                        },
                        callback: function(value) {
                            return value + 'K€';
                        }
                    }
                }
            },
            elements: {
                point: {
                    hoverBorderWidth: 3
                }
            },
            interaction: {
                intersect: false,
                mode: 'index'
            }
        }
    });
}

// ===== CATEGORIES PERFORMANCE CHART =====
function initCategoriesChart() {
    const ctx = document.getElementById('categories-chart');
    if (!ctx) return;
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ECOMMERCE_DATA.categories.map(d => d.name),
            datasets: [{
                data: ECOMMERCE_DATA.categories.map(d => d.percentage),
                backgroundColor: ECOMMERCE_DATA.categories.map(d => d.color),
                borderColor: '#ffffff',
                borderWidth: 3,
                hoverBorderWidth: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '60%',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: POWERBI_COLORS.primary,
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: POWERBI_COLORS.accent,
                    borderWidth: 1,
                    cornerRadius: 8,
                    displayColors: true,
                    callbacks: {
                        label: function(context) {
                            const category = ECOMMERCE_DATA.categories[context.dataIndex];
                            return `${category.name}: ${category.percentage}% (${category.revenue}K€)`;
                        }
                    }
                }
            },
            elements: {
                arc: {
                    hoverBorderWidth: 4
                }
            }
        }
    });
}

// ===== TOP PRODUCTS CHART =====
function initProductsChart() {
    const ctx = document.getElementById('products-chart');
    if (!ctx) return;
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ECOMMERCE_DATA.topProducts.map(d => d.name),
            datasets: [{
                label: 'CA (K€)',
                data: ECOMMERCE_DATA.topProducts.map(d => d.revenue),
                backgroundColor: ECOMMERCE_DATA.topProducts.map(d => d.color),
                borderColor: ECOMMERCE_DATA.topProducts.map(d => d.color),
                borderWidth: 1,
                borderRadius: 4,
                borderSkipped: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: POWERBI_COLORS.primary,
                    titleColor: '#fff',
                    bodyColor: '#fff',
                    borderColor: POWERBI_COLORS.accent,
                    borderWidth: 1,
                    cornerRadius: 8,
                    displayColors: false,
                    callbacks: {
                        label: function(context) {
                            return `CA: ${context.parsed.x}K€`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        color: '#E1E1E1',
                        lineWidth: 1
                    },
                    ticks: {
                        color: '#323130',
                        font: {
                            size: 11
                        },
                        callback: function(value) {
                            return value + 'K€';
                        }
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#323130',
                        font: {
                            size: 11
                        }
                    }
                }
            },
            elements: {
                bar: {
                    borderRadius: 4
                }
            }
        }
    });
}

// ===== KPI GAUGES =====
function initKPIGauges() {
    initRevenueGauge();
    initMarginGauge();
}

function initRevenueGauge() {
    const ctx = document.getElementById('revenue-gauge');
    if (!ctx) return;
    
    const current = 574;
    const target = 650;
    const percentage = Math.round((current / target) * 100);
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [percentage, 100 - percentage],
                backgroundColor: [POWERBI_COLORS.success, '#E1E1E1'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            cutout: '75%',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: false
                }
            },
            elements: {
                arc: {
                    borderRadius: 8
                }
            }
        },
        plugins: [{
            id: 'gaugeText',
            afterDatasetsDraw: function(chart) {
                const ctx = chart.ctx;
                const centerX = chart.width / 2;
                const centerY = chart.height / 2;
                
                ctx.save();
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.font = 'bold 16px Inter';
                ctx.fillStyle = POWERBI_COLORS.primary;
                ctx.fillText(percentage + '%', centerX, centerY);
                ctx.restore();
            }
        }]
    });
}

function initMarginGauge() {
    const ctx = document.getElementById('margin-gauge');
    if (!ctx) return;
    
    const current = 10.6;
    const target = 12;
    const percentage = Math.round((current / target) * 100);
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [percentage, 100 - percentage],
                backgroundColor: [POWERBI_COLORS.warning, '#E1E1E1'],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            cutout: '75%',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: false
                }
            },
            elements: {
                arc: {
                    borderRadius: 8
                }
            }
        },
        plugins: [{
            id: 'gaugeText',
            afterDatasetsDraw: function(chart) {
                const ctx = chart.ctx;
                const centerX = chart.width / 2;
                const centerY = chart.height / 2;
                
                ctx.save();
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.font = 'bold 16px Inter';
                ctx.fillStyle = POWERBI_COLORS.primary;
                ctx.fillText(percentage + '%', centerX, centerY);
                ctx.restore();
            }
        }]
    });
}

// ===== DASHBOARD INTERACTIONS =====
function setupDashboardInteractions() {
    // Toolbar buttons functionality
    const refreshBtn = document.querySelector('[title="Actualiser"]');
    const exportBtn = document.querySelector('[title="Exporter"]');
    const shareBtn = document.querySelector('[title="Partager"]');
    
    if (refreshBtn) {
        refreshBtn.addEventListener('click', function() {
            this.style.animation = 'spin 1s linear';
            setTimeout(() => {
                this.style.animation = '';
                showNotification('Dashboard actualisé !', 'success');
                updateLastRefresh();
            }, 1000);
        });
    }
    
    if (exportBtn) {
        exportBtn.addEventListener('click', function() {
            showNotification('Export PDF en cours...', 'info');
            // Simulate export
            setTimeout(() => {
                showNotification('Export terminé !', 'success');
            }, 2000);
        });
    }
    
    if (shareBtn) {
        shareBtn.addEventListener('click', function() {
            if (navigator.share) {
                navigator.share({
                    title: 'Dashboard E-commerce - ZineInsight',
                    text: 'Découvrez notre dashboard Power BI professionnel',
                    url: window.location.href
                });
            } else {
                navigator.clipboard.writeText(window.location.href);
                showNotification('Lien copié !', 'success');
            }
        });
    }
    
    // Dashboard CTA interaction
    const dashboardCTA = document.querySelector('.dashboard-cta');
    if (dashboardCTA) {
        dashboardCTA.addEventListener('click', function() {
            showDashboardModal();
        });
    }
}

// ===== UTILITY FUNCTIONS =====
function updateLastRefresh() {
    const refreshElement = document.querySelector('.last-refresh');
    if (refreshElement) {
        refreshElement.textContent = 'Dernière actualisation: maintenant';
        
        setTimeout(() => {
            refreshElement.textContent = 'Dernière actualisation: il y a 1min';
        }, 60000);
    }
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `dashboard-notification ${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <div class="notification-icon">
                ${type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️'}
            </div>
            <div class="notification-message">${message}</div>
        </div>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 24px;
        background: ${type === 'success' ? '#107C10' : type === 'error' ? '#D83B01' : '#0078D4'};
        color: white;
        padding: 16px 24px;
        border-radius: 8px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        z-index: 10000;
        font-family: Inter, sans-serif;
        font-size: 14px;
        font-weight: 500;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    // Add to DOM
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after delay
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

function showDashboardModal() {
    // Create modal overlay
    const modal = document.createElement('div');
    modal.className = 'dashboard-modal-overlay';
    modal.innerHTML = `
        <div class="dashboard-modal">
            <div class="modal-header">
                <h3>🚀 Dashboard Interactif</h3>
                <button class="modal-close">&times;</button>
            </div>
            <div class="modal-content">
                <p>Ce dashboard complet inclut :</p>
                <ul>
                    <li>📊 Analyses temps réel</li>
                    <li>🎯 KPIs personnalisés</li>
                    <li>📈 Prévisions automatisées</li>
                    <li>🚨 Alertes intelligentes</li>
                    <li>📱 Version mobile</li>
                    <li>🔄 Synchronisation automatique</li>
                </ul>
                <div class="modal-cta">
                    <a href="mailto:otmane@zineinsight.com?subject=Dashboard%20E-commerce%20Demo" 
                       class="btn-modal-primary">
                        📧 Demander une démo
                    </a>
                </div>
            </div>
        </div>
    `;
    
    // Add styles
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    `;
    
    // Add to DOM
    document.body.appendChild(modal);
    
    // Close functionality
    const closeBtn = modal.querySelector('.modal-close');
    closeBtn.addEventListener('click', () => {
        document.body.removeChild(modal);
    });
    
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            document.body.removeChild(modal);
        }
    });
}

// ===== CSS ANIMATIONS =====
const style = document.createElement('style');
style.textContent = `
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .dashboard-modal .dashboard-modal {
        background: white;
        border-radius: 16px;
        padding: 32px;
        max-width: 500px;
        width: 90%;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .dashboard-modal .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 1px solid #E1E1E1;
    }
    
    .dashboard-modal .modal-header h3 {
        color: #004B87;
        font-size: 24px;
        font-weight: 700;
        margin: 0;
    }
    
    .dashboard-modal .modal-close {
        background: none;
        border: none;
        font-size: 24px;
        color: #666;
        cursor: pointer;
        padding: 8px;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background 0.2s ease;
    }
    
    .dashboard-modal .modal-close:hover {
        background: #f5f5f5;
    }
    
    .dashboard-modal .modal-content p {
        color: #323130;
        margin-bottom: 16px;
        font-size: 16px;
    }
    
    .dashboard-modal .modal-content ul {
        color: #323130;
        margin-bottom: 24px;
        padding-left: 20px;
    }
    
    .dashboard-modal .modal-content li {
        margin-bottom: 8px;
        font-size: 14px;
    }
    
    .dashboard-modal .modal-cta {
        text-align: center;
    }
    
    .dashboard-modal .btn-modal-primary {
        background: linear-gradient(135deg, #004B87 0%, #00BCF2 100%);
        color: white;
        padding: 16px 32px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        display: inline-block;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 12px rgba(0,75,135,0.3);
    }
    
    .dashboard-modal .btn-modal-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,75,135,0.4);
    }
`;
document.head.appendChild(style);

// Export function for global access
window.initEcommerceDashboard = initEcommerceDashboard;
