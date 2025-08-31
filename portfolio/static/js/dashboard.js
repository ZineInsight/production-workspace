// Dashboard JavaScript functionality

class Dashboard {
    constructor() {
        this.charts = {};
        this.updateInterval = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.initializeAnimations();
    }

    setupEventListeners() {
        // Timeframe selector for visitors chart
        const visitorsTimeframe = document.getElementById('visitorsTimeframe');
        if (visitorsTimeframe) {
            visitorsTimeframe.addEventListener('change', (e) => {
                this.updateVisitorsChart(e.target.value);
            });
        }

        // Chart controls
        document.querySelectorAll('.chart-controls .btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                this.toggleChartDataset(e.target);
            });
        });

        // Refresh button
        const refreshBtn = document.querySelector('[onclick="refreshData()"]');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.refreshDashboardData();
            });
        }

        // Export button
        const exportBtn = document.querySelector('[onclick="exportData()"]');
        if (exportBtn) {
            exportBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.exportDashboardData();
            });
        }
    }

    initializeAnimations() {
        // Animate metric cards on load
        const metricCards = document.querySelectorAll('.metric-card');
        metricCards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';

            setTimeout(() => {
                card.style.transition = 'all 0.6s ease';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 200);
        });

        // Animate progress bars
        setTimeout(() => {
            this.animateProgressBars();
        }, 1000);

        // Animate skill bars
        this.animateSkillBars();
    }

    animateProgressBars() {
        const progressBars = document.querySelectorAll('.progress-fill, .skill-progress, .page-progress');
        progressBars.forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0%';

            setTimeout(() => {
                bar.style.transition = 'width 1.5s ease-in-out';
                bar.style.width = width;
            }, Math.random() * 500);
        });
    }

    animateSkillBars() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const skillBars = entry.target.querySelectorAll('.skill-progress');
                    skillBars.forEach((bar, index) => {
                        const width = bar.style.width;
                        bar.style.width = '0%';

                        setTimeout(() => {
                            bar.style.transition = 'width 1.5s ease-in-out';
                            bar.style.width = width;
                        }, index * 200);
                    });
                }
            });
        });

        const skillsSection = document.querySelector('.skills');
        if (skillsSection) {
            observer.observe(skillsSection);
        }
    }

    updateVisitorsChart(timeframe) {
        // This would typically make an API call to get new data
        console.log(`Updating visitors chart for ${timeframe} days`);

        // For demo purposes, just show a loading state
        const chartContainer = document.querySelector('#visitorsChart').closest('.chart-container');
        chartContainer.style.opacity = '0.6';

        setTimeout(() => {
            chartContainer.style.opacity = '1';
            this.showNotification('Chart updated successfully', 'success');
        }, 1000);
    }

    toggleChartDataset(button) {
        // Toggle active state
        document.querySelectorAll('.chart-controls .btn').forEach(btn => {
            btn.classList.remove('active');
        });
        button.classList.add('active');

        const dataset = button.textContent.toLowerCase().replace(' ', '');
        console.log(`Toggling dataset: ${dataset}`);

        this.showNotification(`Showing ${button.textContent} data`, 'info');
    }

    refreshDashboardData() {
        this.showNotification('Refreshing dashboard data...', 'info');

        // Simulate API call
        setTimeout(() => {
            location.reload();
        }, 1500);
    }

    exportDashboardData() {
        this.showNotification('Preparing export...', 'info');

        // Get analytics data from the page
        const analyticsData = window.analyticsData || {};
        const exportData = {
            timestamp: new Date().toISOString(),
            data: analyticsData,
            metadata: {
                exported_by: 'Dashboard Export Tool',
                version: '1.0.0'
            }
        };

        // Create and download file
        const dataStr = JSON.stringify(exportData, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);

        const exportFileDefaultName = `dashboard-export-${new Date().toISOString().split('T')[0]}.json`;

        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportFileDefaultName);
        linkElement.click();

        this.showNotification('Data exported successfully', 'success');
    }

    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <i class="fas fa-${this.getNotificationIcon(type)}"></i>
            <span>${message}</span>
        `;

        // Add styles
        Object.assign(notification.style, {
            position: 'fixed',
            top: '20px',
            right: '20px',
            background: type === 'success' ? '#10B981' : type === 'error' ? '#EF4444' : '#3B82F6',
            color: 'white',
            padding: '12px 20px',
            borderRadius: '8px',
            boxShadow: '0 4px 12px rgba(0,0,0,0.2)',
            zIndex: '9999',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            fontSize: '14px',
            fontWeight: '500',
            transform: 'translateX(100%)',
            transition: 'transform 0.3s ease'
        });

        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);

        // Remove after 3 seconds
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }

    getNotificationIcon(type) {
        switch (type) {
            case 'success': return 'check-circle';
            case 'error': return 'exclamation-circle';
            case 'warning': return 'exclamation-triangle';
            default: return 'info-circle';
        }
    }

    startRealTimeUpdates() {
        // Update activity feed every 30 seconds
        this.updateInterval = setInterval(() => {
            this.addRandomActivity();
            this.updateMetrics();
        }, 30000);
    }

    stopRealTimeUpdates() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
            this.updateInterval = null;
        }
    }

    addRandomActivity() {
        const activities = [
            { icon: 'fas fa-user-plus', text: 'New visitor from Germany', time: 'Just now' },
            { icon: 'fas fa-project-diagram', text: 'Project viewed: Real-time Dashboard Suite', time: 'Just now' },
            { icon: 'fas fa-eye', text: 'Services page viewed', time: 'Just now' },
            { icon: 'fas fa-download', text: 'Portfolio PDF downloaded', time: 'Just now' },
            { icon: 'fas fa-envelope', text: 'Contact form submitted', time: 'Just now' },
            { icon: 'fas fa-chart-bar', text: 'Analytics dashboard accessed', time: 'Just now' }
        ];

        const randomActivity = activities[Math.floor(Math.random() * activities.length)];
        const activityFeed = document.getElementById('activityFeed');

        if (!activityFeed) return;

        const activityItem = document.createElement('div');
        activityItem.className = 'activity-item new-activity';
        activityItem.innerHTML = `
            <div class="activity-icon">
                <i class="${randomActivity.icon}"></i>
            </div>
            <div class="activity-content">
                <p><strong>${randomActivity.text}</strong></p>
                <span class="activity-time">${randomActivity.time}</span>
            </div>
        `;

        // Add to top of feed
        activityFeed.insertBefore(activityItem, activityFeed.firstChild);

        // Remove old activities (keep only 10)
        while (activityFeed.children.length > 10) {
            activityFeed.removeChild(activityFeed.lastChild);
        }

        // Remove new-activity class after animation
        setTimeout(() => {
            activityItem.classList.remove('new-activity');
        }, 1000);
    }

    updateMetrics() {
        // Simulate small changes in metrics
        const metricCards = document.querySelectorAll('.metric-card h3');
        metricCards.forEach(metric => {
            const currentValue = parseInt(metric.textContent.replace(/,/g, ''));
            if (!isNaN(currentValue)) {
                // Small random change (±1-5)
                const change = Math.floor(Math.random() * 10) - 5;
                const newValue = Math.max(0, currentValue + change);
                metric.textContent = newValue.toLocaleString();
            }
        });
    }
}

// Chart utilities
class ChartUtils {
    static createGradient(ctx, color1, color2) {
        const gradient = ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, color1);
        gradient.addColorStop(1, color2);
        return gradient;
    }

    static getResponsiveOptions() {
        return {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0,0,0,0.1)',
                        drawBorder: false
                    },
                    ticks: {
                        color: '#666'
                    }
                },
                x: {
                    grid: {
                        display: false,
                        drawBorder: false
                    },
                    ticks: {
                        color: '#666'
                    }
                }
            }
        };
    }
}

// Initialize dashboard when DOM is loaded
document.addEventListener('DOMContentLoaded', function () {
    const dashboard = new Dashboard();

    // Make dashboard available globally
    window.dashboard = dashboard;

    // Start real-time updates if on dashboard page
    if (document.querySelector('.dashboard-body')) {
        dashboard.startRealTimeUpdates();
    }
});

// Cleanup on page unload
window.addEventListener('beforeunload', function () {
    if (window.dashboard) {
        window.dashboard.stopRealTimeUpdates();
    }
});

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Portfolio-specific functionality
if (document.querySelector('#contactForm')) {
    document.getElementById('contactForm').addEventListener('submit', async function (e) {
        e.preventDefault();

        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;

        // Show loading state
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;

        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            message: document.getElementById('message').value
        };

        try {
            const response = await fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (result.status === 'success') {
                if (window.dashboard) {
                    window.dashboard.showNotification('Thank you for your message! We\'ll get back to you soon.', 'success');
                } else {
                    alert('Thank you for your message! We\'ll get back to you soon.');
                }
                this.reset();
            } else {
                throw new Error('Failed to send message');
            }
        } catch (error) {
            if (window.dashboard) {
                window.dashboard.showNotification('There was an error sending your message. Please try again.', 'error');
            } else {
                alert('There was an error sending your message. Please try again.');
            }
        } finally {
            // Restore button state
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

// Mobile navigation toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', function () {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function (e) {
        if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
}

// Active navigation highlighting
window.addEventListener('scroll', function () {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.clientHeight;

        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
        }
    });
});