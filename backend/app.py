# AfiYor Enhanced Features - app.py
# User accounts, conversation history, personalization, and shareability
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import random
import os
import hashlib
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

class AfiYorDatabase:
    """Enhanced database for user accounts and features"""
    
    def __init__(self, db_path="afiyor.sqlite"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize enhanced database schema"""
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    email TEXT UNIQUE,
                    name TEXT,
                    country TEXT,
                    industry TEXT,
                    business_stage TEXT,
                    created_at INTEGER,
                    last_active INTEGER,
                    total_queries INTEGER DEFAULT 0,
                    subscription_tier TEXT DEFAULT 'free'
                );
                
                CREATE TABLE IF NOT EXISTS conversations (
                    id TEXT PRIMARY KEY,
                    user_id TEXT,
                    session_id TEXT,
                    query TEXT,
                    response TEXT,
                    confidence REAL,
                    created_at INTEGER,
                    country TEXT,
                    industry_relevant BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                );
                
                CREATE TABLE IF NOT EXISTS user_preferences (
                    user_id TEXT PRIMARY KEY,
                    preferred_topics TEXT,
                    communication_style TEXT,
                    business_goals TEXT,
                    updated_at INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                );
                
                CREATE TABLE IF NOT EXISTS shared_conversations (
                    share_id TEXT PRIMARY KEY,
                    conversation_id TEXT,
                    user_id TEXT,
                    title TEXT,
                    created_at INTEGER,
                    views INTEGER DEFAULT 0,
                    expires_at INTEGER,
                    FOREIGN KEY (conversation_id) REFERENCES conversations (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                );
                
                CREATE TABLE IF NOT EXISTS user_industries (
                    industry TEXT PRIMARY KEY,
                    description TEXT,
                    key_topics TEXT,
                    relevant_sectors TEXT
                );
                
                -- Insert industry data
                INSERT OR REPLACE INTO user_industries VALUES 
                ('fintech', 'Financial technology and mobile money', 'payments,banking,loans,savings', 'finance,technology'),
                ('agriculture', 'Farming and agribusiness', 'farming,crops,livestock,supply_chain', 'agriculture,food'),
                ('technology', 'Software and tech solutions', 'software,apps,platforms,innovation', 'technology,digital'),
                ('retail', 'Commerce and trading', 'sales,marketing,customers,inventory', 'commerce,trade'),
                ('manufacturing', 'Production and industrial', 'production,supply_chain,quality,export', 'industry,manufacturing'),
                ('services', 'Professional and business services', 'consulting,professional,service_delivery', 'services,business'),
                ('healthcare', 'Health and medical services', 'health,medical,wellness,telemedicine', 'health,medical'),
                ('education', 'Educational services and edtech', 'learning,training,education,skills', 'education,training'),
                ('logistics', 'Transportation and logistics', 'transport,delivery,supply_chain,logistics', 'transport,logistics');
            """)

class EnhancedAfiYor:
    """Enhanced AfiYor with personalization and user features"""
    
    def __init__(self):
        self.db = AfiYorDatabase()
        self.response_memory = {}
        
        # Industry-specific response modifiers
        self.industry_contexts = {
            'fintech': {
                'focus_areas': ['mobile money', 'payments', 'banking', 'financial inclusion'],
                'key_challenges': ['regulation', 'trust', 'security', 'financial literacy'],
                'opportunities': ['unbanked population', 'mobile adoption', 'cross-border payments']
            },
            'agriculture': {
                'focus_areas': ['supply chain', 'market access', 'weather', 'financing'],
                'key_challenges': ['climate change', 'pricing', 'storage', 'transportation'],
                'opportunities': ['food security', 'export markets', 'value addition']
            },
            'technology': {
                'focus_areas': ['innovation', 'talent', 'infrastructure', 'market fit'],
                'key_challenges': ['funding', 'skills gap', 'infrastructure', 'market education'],
                'opportunities': ['digital transformation', 'mobile first', 'AI adoption']
            },
            'retail': {
                'focus_areas': ['customer experience', 'inventory', 'location', 'pricing'],
                'key_challenges': ['competition', 'margins', 'customer retention', 'supply chain'],
                'opportunities': ['e-commerce growth', 'mobile payments', 'customer data']
            }
        }
        
        # Base response templates (enhanced from previous version)
        self.base_responses = {
            "business_startup": {
                "ghana": [
                    "Akwaaba! Starting a business in Ghana requires understanding our Akan cultural values and modern market dynamics. For {industry} ventures, focus on: building relationships with local suppliers and customers, registering with Ghana Investment Promotion Centre, understanding sector-specific regulations, and integrating mobile payments through {mobile_money}. Ghana's strengths in {sectors} create opportunities, especially in {focus_areas}. Consider joining {business_hubs} for networking and mentorship.",
                    
                    "In Ghana, successful {industry} entrepreneurs balance traditional business wisdom with innovation. Key strategies: Research your target market thoroughly in Accra or Kumasi, build partnerships with established local businesses, ensure your solution addresses real community needs, and leverage Ghana's competitive advantages in {sectors}. The {business_hubs} ecosystem provides valuable support. Mobile money adoption through {mobile_money} is essential for customer reach.",
                    
                    "Ghanaian business culture emphasizes patience, relationships, and community benefit. For {industry} startups: Spend time understanding local customs and market dynamics, engage with traditional and modern business networks, focus on sectors where Ghana excels like {sectors}, and implement mobile payment solutions using {mobile_money}. Community support and cultural sensitivity are crucial for long-term success in Ghana's market.",
                ]
            }
        }
        
        # Country data (inherited from previous version)
        self.country_data = {
            "ghana": {
                "greeting": "Akwaaba!",
                "mobile_money": ["MTN MoMo", "AirtelTigo Money", "Vodafone Cash", "Zeepay"],
                "business_hubs": ["Accra Digital Centre", "MEST Africa", "Impact Hub Accra", "Ghana Tech Lab"],
                "key_sectors": ["cocoa", "gold", "oil", "fintech", "agriculture", "tourism"],
                "cultural_values": ["Akan respect systems", "communal decision-making", "extended family support"],
                "languages": ["English", "Twi", "Ga", "Ewe", "Fante"]
            }
        }
    
    def create_user_account(self, user_data):
        """Create new user account with personalization"""
        user_id = hashlib.md5(f"{user_data['email']}{time.time()}".encode()).hexdigest()[:12]
        
        with sqlite3.connect(self.db.db_path) as conn:
            conn.execute("""
                INSERT INTO users (id, email, name, country, industry, business_stage, created_at, last_active)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id, user_data['email'], user_data['name'], 
                user_data['country'], user_data.get('industry', 'general'),
                user_data.get('business_stage', 'idea'), int(time.time()), int(time.time())
            ))
            
            # Create default preferences
            conn.execute("""
                INSERT INTO user_preferences (user_id, preferred_topics, communication_style, business_goals, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """, (
                user_id, json.dumps([user_data.get('industry', 'general')]),
                'detailed', user_data.get('business_goals', ''), int(time.time())
            ))
        
        return user_id
    
    def get_user_profile(self, user_id):
        """Get complete user profile with preferences"""
        with sqlite3.connect(self.db.db_path) as conn:
            user_row = conn.execute("""
                SELECT u.*, p.preferred_topics, p.communication_style, p.business_goals
                FROM users u
                LEFT JOIN user_preferences p ON u.id = p.user_id
                WHERE u.id = ?
            """, (user_id,)).fetchone()
            
            if user_row:
                return {
                    'id': user_row[0], 'email': user_row[1], 'name': user_row[2],
                    'country': user_row[3], 'industry': user_row[4], 'business_stage': user_row[5],
                    'total_queries': user_row[8], 'subscription_tier': user_row[9],
                    'preferred_topics': json.loads(user_row[10] or '[]'),
                    'communication_style': user_row[11], 'business_goals': user_row[12]
                }
        return None
    
    def save_conversation(self, user_id, query, response, confidence, country, session_id):
        """Save conversation with enhanced metadata"""
        conv_id = hashlib.md5(f"{user_id}{query}{time.time()}".encode()).hexdigest()[:16]
        
        # Determine if industry relevant
        user_profile = self.get_user_profile(user_id) if user_id != 'anonymous' else None
        industry_relevant = False
        
        if user_profile and user_profile['industry'] in self.industry_contexts:
            industry_context = self.industry_contexts[user_profile['industry']]
            industry_relevant = any(
                focus in query.lower() 
                for focus in industry_context['focus_areas']
            )
        
        with sqlite3.connect(self.db.db_path) as conn:
            conn.execute("""
                INSERT INTO conversations (id, user_id, session_id, query, response, confidence, created_at, country, industry_relevant)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (conv_id, user_id, session_id, query, response, confidence, int(time.time()), country, industry_relevant))
            
            # Update user query count
            if user_id != 'anonymous':
                conn.execute("""
                    UPDATE users SET total_queries = total_queries + 1, last_active = ?
                    WHERE id = ?
                """, (int(time.time()), user_id))
        
        return conv_id
    
    def get_user_conversations(self, user_id, limit=50):
        """Get user's conversation history"""
        with sqlite3.connect(self.db.db_path) as conn:
            rows = conn.execute("""
                SELECT id, query, response, confidence, created_at, country, industry_relevant
                FROM conversations 
                WHERE user_id = ?
                ORDER BY created_at DESC
                LIMIT ?
            """, (user_id, limit)).fetchall()
            
            return [{
                'id': row[0], 'query': row[1], 'response': row[2],
                'confidence': row[3], 'created_at': row[4], 'country': row[5],
                'industry_relevant': bool(row[6])
            } for row in rows]
    
    def generate_personalized_response(self, message, country, user_id="anonymous"):
        """Generate response with personalization"""
        
        # Get user profile for personalization
        user_profile = self.get_user_profile(user_id) if user_id != 'anonymous' else None
        
        # Base response generation (using previous logic)
        base_response = self.generate_base_response(message, country, user_profile)
        
        # Add personalization if user profile exists
        if user_profile:
            personalized_response = self.add_personalization(base_response, user_profile, message)
            return personalized_response
        
        return base_response
    
    def generate_base_response(self, message, country, user_profile=None):
        """Generate base response using existing logic"""
        country_info = self.country_data.get(country.lower(), self.country_data["ghana"])
        
        # Determine industry context
        industry = user_profile['industry'] if user_profile else 'general'
        industry_context = self.industry_contexts.get(industry, {})
        
        # Select appropriate template
        templates = self.base_responses["business_startup"][country.lower()]
        template = random.choice(templates)
        
        # Fill template with data
        response = template.format(
            industry=industry,
            sectors=", ".join(random.sample(country_info["key_sectors"], 3)),
            mobile_money=", ".join(random.sample(country_info["mobile_money"], 2)),
            business_hubs=random.choice(country_info["business_hubs"]),
            focus_areas=", ".join(industry_context.get('focus_areas', ['market research', 'customer validation'])[:2])
        )
        
        return response
    
    def add_personalization(self, base_response, user_profile, message):
        """Add personalized touches to response"""
        
        personalized_response = base_response
        
        # Add industry-specific insights
        if user_profile['industry'] in self.industry_contexts:
            industry_context = self.industry_contexts[user_profile['industry']]
            
            # Add relevant challenges or opportunities
            if any(word in message.lower() for word in ['challenge', 'problem', 'difficult']):
                challenges = industry_context.get('key_challenges', [])
                if challenges:
                    personalized_response += f"\n\nCommon {user_profile['industry']} challenges include: {', '.join(challenges[:2])}. Focus on addressing these systematically."
            
            elif any(word in message.lower() for word in ['opportunity', 'potential', 'growth']):
                opportunities = industry_context.get('opportunities', [])
                if opportunities:
                    personalized_response += f"\n\nKey opportunities in {user_profile['industry']} include: {', '.join(opportunities[:2])}. Consider how your business can capitalize on these trends."
        
        # Add business stage context
        if user_profile.get('business_stage'):
            if user_profile['business_stage'] == 'idea':
                personalized_response += f"\n\nSince you're in the idea stage, focus on market validation and customer discovery first."
            elif user_profile['business_stage'] == 'startup':
                personalized_response += f"\n\nAs a startup, prioritize finding product-market fit and sustainable customer acquisition."
            elif user_profile['business_stage'] == 'growth':
                personalized_response += f"\n\nFor growth stage, focus on scaling operations and expanding market reach systematically."
        
        # Add Ubuntu wisdom
        ubuntu_wisdom = [
            f"Ubuntu reminder for {user_profile['industry']}: your success should lift the entire {user_profile['industry']} ecosystem",
            "Individual success comes from community prosperity - build partnerships that benefit everyone",
            "In Ubuntu thinking, your business succeeds when your community succeeds"
        ]
        
        personalized_response += f"\n\n🤝 {random.choice(ubuntu_wisdom)}!"
        
        return personalized_response
    
    def create_shareable_link(self, conversation_id, user_id, title=None):
        """Create shareable link for conversation"""
        share_id = hashlib.md5(f"{conversation_id}{time.time()}".encode()).hexdigest()[:12]
        expires_at = int(time.time()) + (30 * 24 * 3600)  # 30 days
        
        with sqlite3.connect(self.db.db_path) as conn:
            conn.execute("""
                INSERT INTO shared_conversations (share_id, conversation_id, user_id, title, created_at, expires_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (share_id, conversation_id, user_id, title or "AfiYor Conversation", int(time.time()), expires_at))
        
        return share_id
    
    def get_shared_conversation(self, share_id):
        """Get shared conversation by share_id"""
        with sqlite3.connect(self.db.db_path) as conn:
            # Update view count
            conn.execute("UPDATE shared_conversations SET views = views + 1 WHERE share_id = ?", (share_id,))
            
            # Get conversation data
            row = conn.execute("""
                SELECT c.query, c.response, c.confidence, c.created_at, c.country,
                       s.title, s.views, u.name, u.country as user_country
                FROM shared_conversations s
                JOIN conversations c ON s.conversation_id = c.id
                LEFT JOIN users u ON s.user_id = u.id
                WHERE s.share_id = ? AND s.expires_at > ?
            """, (share_id, int(time.time()))).fetchone()
            
            if row:
                return {
                    'query': row[0], 'response': row[1], 'confidence': row[2],
                    'created_at': row[3], 'country': row[4], 'title': row[5],
                    'views': row[6], 'author_name': row[7], 'author_country': row[8]
                }
        return None

# Initialize enhanced AfiYor
afiyor = EnhancedAfiYor()

@app.route('/')
def home():
    return jsonify({
        "name": "AfiYor API",
        "version": "3.0.0",
        "description": "African AI Assistant with User Accounts & Personalization",
        "ubuntu": "I am because we are 🌍",
        "creator": "Built with love for African entrepreneurs",
        "features": [
            "User accounts and personalization",
            "Conversation history",
            "Industry-specific insights", 
            "Shareable conversations",
            "Enhanced Ubuntu philosophy integration"
        ],
        "endpoints": {
            "chat": "/chat",
            "register": "/register",
            "login": "/login",
            "history": "/history",
            "share": "/share",
            "health": "/health"
        }
    })

@app.route('/register', methods=['POST'])
def register_user():
    """Register new user account"""
    try:
        data = request.get_json()
        required_fields = ['email', 'name', 'country']
        
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Email, name, and country are required"}), 400
        
        user_id = afiyor.create_user_account(data)
        
        return jsonify({
            "status": "success",
            "user_id": user_id,
            "message": f"Akwaaba {data['name']}! Your AfiYor account is ready.",
            "personalization": "enabled"
        })
    
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            return jsonify({"error": "Email already registered"}), 400
        return jsonify({"error": "Registration failed"}), 500

@app.route('/login', methods=['POST'])
def login_user():
    """Simple login by email"""
    try:
        data = request.get_json()
        email = data.get('email')
        
        if not email:
            return jsonify({"error": "Email is required"}), 400
        
        with sqlite3.connect(afiyor.db.db_path) as conn:
            user_row = conn.execute("SELECT id, name FROM users WHERE email = ?", (email,)).fetchone()
            
            if user_row:
                return jsonify({
                    "status": "success",
                    "user_id": user_row[0],
                    "name": user_row[1],
                    "message": f"Welcome back, {user_row[1]}!"
                })
            else:
                return jsonify({"error": "Account not found"}), 404
    
    except Exception as e:
        return jsonify({"error": "Login failed"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Enhanced chat with personalization"""
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        country = data.get('country', 'ghana')
        user_id = data.get('user_id', 'anonymous')
        session_id = data.get('session_id', 'default')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Generate personalized response
        response = afiyor.generate_personalized_response(message, country, user_id)
        confidence = 0.9
        
        # Save conversation
        conv_id = afiyor.save_conversation(user_id, message, response, confidence, country, session_id)
        
        return jsonify({
            "response": response,
            "confidence": confidence,
            "conversation_id": conv_id,
            "country": country,
            "personalized": user_id != 'anonymous',
            "timestamp": int(time.time()),
            "version": "3.0.0"
        })
    
    except Exception as e:
        return jsonify({
            "error": "Ubuntu teaches us resilience. Let me try again.",
            "response": f"Akwaaba! I'm here to help with African business advice. How can I assist you today?",
            "confidence": 0.5
        }), 200

@app.route('/history/<user_id>')
def get_conversation_history(user_id):
    """Get user's conversation history"""
    try:
        conversations = afiyor.get_user_conversations(user_id)
        return jsonify({
            "conversations": conversations,
            "total": len(conversations),
            "user_id": user_id
        })
    except Exception as e:
        return jsonify({"error": "Could not fetch history"}), 500

@app.route('/share', methods=['POST'])
def create_share():
    """Create shareable conversation link"""
    try:
        data = request.get_json()
        conversation_id = data.get('conversation_id')
        user_id = data.get('user_id')
        title = data.get('title')
        
        if not conversation_id or not user_id:
            return jsonify({"error": "Conversation ID and user ID required"}), 400
        
        share_id = afiyor.create_shareable_link(conversation_id, user_id, title)
        share_url = f"/shared/{share_id}"
        
        return jsonify({
            "status": "success",
            "share_id": share_id,
            "share_url": share_url,
            "message": "Conversation shared successfully!"
        })
    
    except Exception as e:
        return jsonify({"error": "Could not create share link"}), 500

@app.route('/shared/<share_id>')
def view_shared_conversation(share_id):
    """View shared conversation"""
    try:
        conversation = afiyor.get_shared_conversation(share_id)
        
        if not conversation:
            return jsonify({"error": "Shared conversation not found or expired"}), 404
        
        return jsonify({
            "conversation": conversation,
            "shared": True,
            "message": "This AfiYor conversation was shared with you"
        })
    
    except Exception as e:
        return jsonify({"error": "Could not load shared conversation"}), 500

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": int(time.time()),
        "ai_status": "enhanced_personalization_ready",
        "ubuntu": "Ngiyaphila - I am well because we are well",
        "version": "3.0.0",
        "features": ["user_accounts", "personalization", "history", "sharing"]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
