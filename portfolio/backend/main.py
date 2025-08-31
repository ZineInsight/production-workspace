from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
import random

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Sample portfolio data
portfolio_data = {
    'profile': {
        'name': 'ZineInsight',
        'title': 'Data Analytics & Intelligence Platform',
        'description': 'Advanced analytics solutions for modern businesses',
        'location': 'Global',
        'experience_years': 5,
        'projects_completed': 150,
        'clients_served': 50
    },
    'skills': [
        {'name': 'Python', 'level': 95, 'category': 'Backend'},
        {'name': 'Flask/Django', 'level': 90, 'category': 'Backend'},
        {'name': 'JavaScript', 'level': 88, 'category': 'Frontend'},
        {'name': 'React', 'level': 85, 'category': 'Frontend'},
        {'name': 'Data Analysis', 'level': 98, 'category': 'Analytics'},
        {'name': 'Machine Learning', 'level': 92, 'category': 'AI/ML'},
        {'name': 'SQL/NoSQL', 'level': 94, 'category': 'Database'},
        {'name': 'AWS/Cloud', 'level': 87, 'category': 'Infrastructure'}
    ],
    'projects': [
        {
            'id': 1,
            'title': 'Geo-Intelligence Platform',
            'description': 'Advanced geospatial analytics for location-based insights',
            'technologies': ['Python', 'Flask', 'PostgreSQL', 'Leaflet.js'],
            'status': 'Production',
            'completion': 100,
            'impact': 'Increased location accuracy by 40%'
        },
        {
            'id': 2,
            'title': 'Multi-Country Analytics Engine',
            'description': 'Scalable analytics engine supporting 12+ countries',
            'technologies': ['Python', 'Redis', 'Docker', 'Nginx'],
            'status': 'Production',
            'completion': 100,
            'impact': 'Serves 10K+ users daily'
        },
        {
            'id': 3,
            'title': 'Real-time Dashboard Suite',
            'description': 'Interactive dashboards with live data visualization',
            'technologies': ['JavaScript', 'Chart.js', 'WebSocket', 'Node.js'],
            'status': 'Development',
            'completion': 75,
            'impact': 'Real-time insights for decision making'
        },
        {
            'id': 4,
            'title': 'AI-Powered Recommendations',
            'description': 'Machine learning algorithms for personalized recommendations',
            'technologies': ['Python', 'TensorFlow', 'scikit-learn', 'FastAPI'],
            'status': 'Testing',
            'completion': 85,
            'impact': 'Improved user engagement by 60%'
        }
    ],
    'services': [
        {
            'name': 'Data Analytics',
            'description': 'Transform raw data into actionable insights',
            'icon': '📊',
            'features': ['Custom Dashboards', 'Real-time Monitoring', 'Predictive Analytics']
        },
        {
            'name': 'Web Development',
            'description': 'Modern, scalable web applications',
            'icon': '🌐',
            'features': ['Responsive Design', 'API Development', 'Performance Optimization']
        },
        {
            'name': 'Machine Learning',
            'description': 'AI-powered solutions for complex problems',
            'icon': '🤖',
            'features': ['Predictive Models', 'Natural Language Processing', 'Computer Vision']
        },
        {
            'name': 'Cloud Infrastructure',
            'description': 'Scalable and secure cloud solutions',
            'icon': '☁️',
            'features': ['Auto-scaling', 'Monitoring', 'Security Implementation']
        }
    ]
}

# Generate sample analytics data
def generate_analytics_data():
    """Generate sample analytics data for the dashboard"""
    now = datetime.now()

    # Generate daily stats for the last 30 days
    daily_stats = []
    for i in range(30):
        date = now - timedelta(days=i)
        daily_stats.append({
            'date': date.strftime('%Y-%m-%d'),
            'visitors': random.randint(50, 200),
            'pageviews': random.randint(100, 500),
            'projects_viewed': random.randint(10, 50),
            'contact_inquiries': random.randint(1, 10)
        })

    return {
        'daily_stats': list(reversed(daily_stats)),
        'total_visitors': sum([day['visitors'] for day in daily_stats]),
        'total_pageviews': sum([day['pageviews'] for day in daily_stats]),
        'avg_session_duration': '2m 34s',
        'bounce_rate': '34%',
        'top_pages': [
            {'page': '/portfolio', 'views': 1234},
            {'page': '/services', 'views': 890},
            {'page': '/projects', 'views': 567},
            {'page': '/contact', 'views': 234}
        ],
        'traffic_sources': [
            {'source': 'Direct', 'percentage': 45},
            {'source': 'Google', 'percentage': 30},
            {'source': 'Social Media', 'percentage': 15},
            {'source': 'Referrals', 'percentage': 10}
        ]
    }

@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html', data=portfolio_data)

@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    analytics = generate_analytics_data()
    return render_template('dashboard.html', analytics=analytics, portfolio=portfolio_data)

@app.route('/api/portfolio')
def api_portfolio():
    """API endpoint for portfolio data"""
    return jsonify(portfolio_data)

@app.route('/api/analytics')
def api_analytics():
    """API endpoint for analytics data"""
    return jsonify(generate_analytics_data())

@app.route('/api/projects')
def api_projects():
    """API endpoint for projects data"""
    return jsonify(portfolio_data['projects'])

@app.route('/api/skills')
def api_skills():
    """API endpoint for skills data"""
    return jsonify(portfolio_data['skills'])

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    data = request.get_json()

    # In a real application, you'd save this to a database or send an email
    contact_data = {
        'name': data.get('name'),
        'email': data.get('email'),
        'message': data.get('message'),
        'timestamp': datetime.now().isoformat()
    }

    # Save to JSON file for demo purposes
    contact_file = os.path.join(os.path.dirname(__file__), '..', 'contact_messages.json')
    try:
        if os.path.exists(contact_file):
            with open(contact_file, 'r') as f:
                contacts = json.load(f)
        else:
            contacts = []

        contacts.append(contact_data)

        with open(contact_file, 'w') as f:
            json.dump(contacts, f, indent=2)

        return jsonify({'status': 'success', 'message': 'Thank you for your message!'})

    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Failed to save message'}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)