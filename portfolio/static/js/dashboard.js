// Dashboard Charts JavaScript

// Chart.js default configuration
Chart.defaults.font.family = 'Inter, sans-serif';
Chart.defaults.color = '#64748b';
Chart.defaults.elements.bar.borderRadius = 6;
Chart.defaults.elements.line.borderWidth = 3;
Chart.defaults.elements.point.radius = 5;
Chart.defaults.elements.point.hoverRadius = 8;

// Color palette
const colors = {
    primary: '#2563eb',
    success: '#10b981',
    warning: '#f59e0b',
    danger: '#ef4444',
    info: '#0ea5e9',
    secondary: '#64748b',
    light: '#f8fafc'
};

// MRR Evolution Chart
function createMRRChart(data) {
    const ctx = document.getElementById('mrrChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'MRR (€)',
                data: data.data,
                borderColor: colors.primary,
                backgroundColor: colors.primary + '20',
                fill: true,
                tension: 0.4
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
                    callbacks: {
                        label: function(context) {
                            return 'MRR: €' + context.parsed.y.toLocaleString();
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    ticks: {
                        callback: function(value) {
                            return '€' + (value / 1000) + 'K';
                        }
                    },
                    grid: {
                        color: '#f1f5f9'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            },
            elements: {
                point: {
                    backgroundColor: colors.primary,
                    borderColor: '#fff',
                    borderWidth: 2
                }
            }
        }
    });
}

// Churn Evolution Chart
function createChurnChart(data) {
    const ctx = document.getElementById('churnChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Churn Rate (%)',
                data: data.data,
                borderColor: colors.danger,
                backgroundColor: colors.danger + '20',
                fill: true,
                tension: 0.4
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
                    callbacks: {
                        label: function(context) {
                            return 'Churn: ' + context.parsed.y + '%';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 15,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: '#f1f5f9'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            },
            elements: {
                point: {
                    backgroundColor: colors.danger,
                    borderColor: '#fff',
                    borderWidth: 2
                }
            }
        }
    });
}

// Customer Segment Charts
function createSegmentCharts(data) {
    // Revenue by Segment
    const revenueCtx = document.getElementById('revenueSegmentChart');
    if (revenueCtx) {
        new Chart(revenueCtx, {
            type: 'doughnut',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.revenue,
                    backgroundColor: [colors.primary, colors.success, colors.warning],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 20,
                            usePointStyle: true
                        }
                    },
                    title: {
                        display: true,
                        text: 'Revenue par Segment',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    }
                }
            }
        });
    }

    // Churn by Segment
    const churnCtx = document.getElementById('churnSegmentChart');
    if (churnCtx) {
        new Chart(churnCtx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Churn %',
                    data: data.churn,
                    backgroundColor: [colors.danger + '80', colors.warning + '80', colors.success + '80'],
                    borderColor: [colors.danger, colors.warning, colors.success],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    title: {
                        display: true,
                        text: 'Churn par Segment',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return value + '%';
                            }
                        }
                    }
                }
            }
        });
    }

    // LTV by Segment
    const ltvCtx = document.getElementById('ltvSegmentChart');
    if (ltvCtx) {
        new Chart(ltvCtx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'LTV €',
                    data: data.ltv,
                    backgroundColor: [colors.info + '80', colors.primary + '80', colors.success + '80'],
                    borderColor: [colors.info, colors.primary, colors.success],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    title: {
                        display: true,
                        text: 'LTV par Segment',
                        font: {
                            size: 14,
                            weight: '600'
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return '€' + value.toLocaleString();
                            }
                        }
                    }
                }
            }
        });
    }
}

// Conversion Evolution Chart (Fashion case)
function createConversionChart(data) {
    const ctx = document.getElementById('conversionChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Desktop',
                data: data.desktop,
                borderColor: colors.secondary,
                backgroundColor: colors.secondary + '20',
                fill: false,
                tension: 0.4
            }, {
                label: 'Mobile',
                data: data.mobile,
                borderColor: colors.primary,
                backgroundColor: colors.primary + '20',
                fill: false,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        usePointStyle: true,
                        padding: 20
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.dataset.label + ': ' + context.parsed.y + '%';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    },
                    grid: {
                        color: '#f1f5f9'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            },
            elements: {
                point: {
                    borderColor: '#fff',
                    borderWidth: 2
                }
            }
        }
    });
}

// Utility functions
function formatCurrency(value) {
    return new Intl.NumberFormat('fr-FR', {
        style: 'currency',
        currency: 'EUR'
    }).format(value);
}

function formatPercentage(value) {
    return value.toFixed(1) + '%';
}

// Animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
});
