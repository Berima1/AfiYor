# AfiYor Intelligent Dynamic Response System - app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import random
import os
import hashlib

app = Flask(__name__)
CORS(app)

class IntelligentAfiYor:
    """Intelligent dynamic response system for AfiYor"""
    
    def __init__(self):
        self.response_memory = {}  # Track what responses user has seen
        self.country_data = {
            "ghana": {
                "greeting": "Akwaaba!",
                "mobile_money": ["MTN MoMo", "AirtelTigo Money", "Vodafone Cash", "Zeepay"],
                "business_hubs": ["Accra Digital Centre", "MEST Africa", "Impact Hub Accra", "Ghana Tech Lab"],
                "key_sectors": ["cocoa", "gold", "oil", "fintech", "agriculture", "tourism"],
                "cultural_values": ["Akan respect systems", "communal decision-making", "extended family support", "respect for elders"],
                "languages": ["English", "Twi", "Ga", "Ewe", "Fante"],
                "business_traits": ["relationship-first", "trust-building", "community involvement", "patience in negotiations"],
                "challenges": ["access to capital", "infrastructure", "regulatory complexity", "skills gap"],
                "opportunities": ["youth population", "mobile adoption", "natural resources", "regional trade hub"],
                "success_factors": ["local partnerships", "cultural sensitivity", "mobile-first approach", "community engagement"]
            },
            "nigeria": {
                "greeting": "Sannu! Bawo!",
                "mobile_money": ["Paystack", "Flutterwave", "Opay", "PalmPay", "Kuda"],
                "business_hubs": ["Lagos ecosystem", "Abuja tech scene", "Port Harcourt innovation", "Ibadan startups"],
                "key_sectors": ["oil", "agriculture", "fintech", "entertainment", "e-commerce", "logistics"],
                "cultural_values": ["diverse ethnic respect", "relationship hierarchy", "extended family networks", "religious considerations"],
                "languages": ["English", "Yoruba", "Igbo", "Hausa", "Fulfulde"],
                "business_traits": ["networking-focused", "resilient", "entrepreneurial spirit", "adaptability"],
                "challenges": ["infrastructure gaps", "regulatory uncertainty", "security concerns", "currency volatility"],
                "opportunities": ["largest African market", "young population", "oil wealth", "Nollywood influence"],
                "success_factors": ["strong networks", "local partnerships", "understanding diversity", "mobile solutions"]
            },
            "kenya": {
                "greeting": "Habari!",
                "mobile_money": ["M-Pesa", "Airtel Money", "T-Kash", "Equitel"],
                "business_hubs": ["Nairobi Silicon Savannah", "iHub", "MEST", "Nailab"],
                "key_sectors": ["agriculture", "tourism", "mobile money", "renewable energy", "logistics"],
                "cultural_values": ["Harambee cooperation", "Ubuntu philosophy", "respect for age", "community support"],
                "languages": ["English", "Swahili", "Kikuyu", "Luo"],
                "business_traits": ["innovative", "collaborative", "tech-savvy", "environmentally conscious"],
                "challenges": ["drought cycles", "political uncertainty", "infrastructure needs", "youth unemployment"],
                "opportunities": ["M-Pesa leadership", "tourism growth", "renewable energy potential", "regional hub"],
                "success_factors": ["mobile money integration", "sustainability focus", "community partnerships", "innovation"]
            }
        }
        
        self.response_templates = {
            "business_startup": {
                "ghana": [
                    "Akwaaba! Starting a business in Ghana requires understanding our Akan cultural values. Focus on building relationships first - Ghanaians value trust and community connections. Consider these key factors: Register with Ghana Investment Promotion Centre, understand the local supply chains in sectors like {sectors}, and integrate mobile payments through {mobile_money}. The {business_hubs} can provide valuable networking opportunities.",
                    
                    "In Ghana, successful entrepreneurs combine traditional Akan business wisdom with modern innovation. Key strategies: Start with thorough market research in Accra or Kumasi, build partnerships with local suppliers, and ensure your business serves the community need. Ghana's strengths in {sectors} create opportunities, especially if you leverage {mobile_money} for payments and customer reach.",
                    
                    "Ghanaian business culture emphasizes patience and relationship-building. Before launching, spend time understanding local customs and business practices. Consider starting in Accra's tech ecosystem through {business_hubs}, focus on {sectors} where Ghana has competitive advantages, and use {mobile_money} platforms to reach customers effectively. Community support is crucial for long-term success.",
                    
                    "Starting a business in Ghana means embracing our communal values. Successful ventures often involve extended family and community input. Practical steps: Develop a business plan that considers local market dynamics, register with appropriate agencies, partner with established local businesses, and leverage Ghana's strengths in {sectors}. Mobile money adoption through {mobile_money} is essential for customer accessibility."
                ],
                "nigeria": [
                    "Sannu! Nigeria's entrepreneurial spirit is legendary, but success requires understanding our complex, diverse market. With over 200 million people, focus on: Choosing the right state for registration, understanding local regulations, building networks across ethnic lines, and leveraging fintech solutions like {mobile_money}. Lagos leads in {sectors}, but opportunities exist nationwide.",
                    
                    "Nigerian business success comes from adaptability and strong relationships. Key strategies: Start with a clear understanding of your target demographic, build alliances across Nigeria's diverse regions, leverage the massive market size, and use digital platforms like {mobile_money} for transactions. The {business_hubs} provide excellent startup support and networking.",
                    
                    "In Nigeria, resilience and innovation drive business success. Consider these factors: Nigeria's leadership in {sectors} creates opportunities, the youth demographic is tech-savvy and entrepreneurial, mobile money adoption through {mobile_money} is growing rapidly, and government initiatives support SME development. Network extensively and understand regional differences.",
                    
                    "Nigeria offers Africa's largest market, but requires cultural sensitivity and strategic thinking. Successful approaches: Research regulatory requirements thoroughly, build diverse teams reflecting Nigeria's ethnic diversity, leverage fintech infrastructure like {mobile_money}, and focus on sectors where Nigeria leads: {sectors}. Community engagement and ethical business practices are essential."
                ]
            },
            
            "ubuntu_philosophy": [
                "Ubuntu teaches us 'Ngiyakhona ngokuthi sikhona' - I am because we are. In business, this means your success should uplift your entire community. When you build a company, ask: How does this help my neighbors? How can my growth create opportunities for others? Ubuntu business practices include hiring locally, sourcing from community suppliers, sharing knowledge with other entrepreneurs, and ensuring profits benefit the broader community, not just individual wealth.",
                
                "The Ubuntu principle 'I am because we are' transforms how we approach entrepreneurship. Instead of zero-sum competition, Ubuntu encourages collaborative growth. Practical applications: Form business cooperatives with other entrepreneurs, create mentorship programs for upcoming business owners, design products that solve community problems, and measure success not just by profit but by community impact. Your business thrives when your community thrives.",
                
                "Ubuntu philosophy in modern entrepreneurship means recognizing our interconnectedness. When making business decisions, consider the ripple effects on your community. Ubuntu-driven businesses often: Partner with local suppliers and service providers, invest in employee development and well-being, create products that address real community needs, and share knowledge and resources with other entrepreneurs. Individual success without community growth is empty achievement.",
                
                "Understanding Ubuntu in business context: 'Umuntu ngumuntu ngabantu' - a person is a person through other people. This guides ethical business practices where success is measured by community upliftment. Ubuntu entrepreneurs focus on: Creating jobs and opportunities for others, building businesses that solve real community problems, sharing resources and knowledge freely, and ensuring business growth strengthens social bonds rather than creating inequality."
            ],
            
            "mobile_money": {
                "ghana": [
                    "Ghana's mobile money ecosystem is led by {mobile_money}, with MTN MoMo dominating the market. For business integration: MTN MoMo offers robust APIs for merchant payments, AirtelTigo Money serves specific demographics effectively, Vodafone Cash provides good enterprise solutions, and Zeepay enables international transfers. Consider multi-platform integration to reach all customer segments, and ensure your business model accounts for transaction fees and customer preferences.",
                    
                    "Mobile money in Ghana has achieved remarkable penetration, especially through {mobile_money}. Business opportunities include: Agent banking services in rural areas, merchant payment solutions for small businesses, integration with e-commerce platforms, and value-added services like savings and micro-loans. Success requires understanding customer behavior, regulatory compliance with Bank of Ghana requirements, and building trust through reliable service delivery.",
                    
                    "Ghana's mobile money success story centers on {mobile_money}, particularly MTN MoMo's market leadership. Key insights for businesses: Mobile money users prefer simple, fast transactions, agent networks are crucial for cash-in/cash-out services, integration with traditional banking is increasing, and opportunities exist in cross-border payments and merchant services. Focus on user experience and regulatory compliance for sustainable growth."
                ]
            },
            
            "culture_business": {
                "ghana": [
                    "Ghanaian business culture is rooted in Akan traditions emphasizing respect, patience, and community consensus. Key cultural factors: Meetings often start with relationship-building conversation, decision-making involves consultation with elders or senior colleagues, business deals are sealed through personal relationships rather than just contracts, and long-term thinking is valued over quick profits. Understanding these cultural nuances is essential for successful business relationships in Ghana.",
                    
                    "In Ghana, business success requires cultural sensitivity to our diverse ethnic groups and traditions. Important aspects: Respect for hierarchy and age in business settings, the importance of extended family in business decisions, communal approaches to problem-solving, and the integration of traditional values with modern business practices. Building trust takes time, but results in stronger, more sustainable business partnerships.",
                    
                    "Ghanaian business culture balances traditional Akan values with modern entrepreneurship. Cultural considerations include: The role of chiefs and traditional authorities in community business decisions, the importance of social responsibility and community contribution, preference for face-to-face meetings and relationship building, and the integration of religious considerations in business practices. Successful businesses honor these traditions while embracing innovation."
                ]
            }
        }
        
        self.ubuntu_wisdom = [
            "Ubuntu teaches us that individual success comes from community prosperity",
            "In African business, we lift each other as we climb - that's the Ubuntu way",
            "I am because we are - your business should strengthen the entire community",
            "Ubuntu wisdom: prosperity shared is prosperity multiplied",
            "Community strength creates individual opportunities - that's Ubuntu philosophy",
            "Ubuntu reminds us that sustainable success comes from empowering others",
            "In Ubuntu thinking, your business succeeds when your community succeeds"
        ]
    
    def analyze_query_intent(self, message):
        """Analyze user query to determine intent and extract key topics"""
        message_lower = message.lower()
        intents = []
        
        # Business startup intent
        if any(word in message_lower for word in ["start", "startup", "business", "company", "entrepreneur", "launch"]):
            intents.append("business_startup")
        
        # Ubuntu philosophy intent
        if any(word in message_lower for word in ["ubuntu", "philosophy", "community", "together", "values", "culture"]):
            intents.append("ubuntu_philosophy")
        
        # Mobile money intent
        if any(word in message_lower for word in ["mobile money", "m-pesa", "momo", "payment", "fintech", "banking", "financial"]):
            intents.append("mobile_money")
        
        # Culture/business culture intent
        if any(word in message_lower for word in ["culture", "traditional", "akan", "respect", "customs", "local"]):
            intents.append("culture_business")
        
        # Expansion intent
        if any(word in message_lower for word in ["expand", "growth", "scale", "international", "across"]):
            intents.append("expansion")
        
        # If no specific intent, default to business startup
        if not intents:
            intents.append("business_startup")
        
        return intents
    
    def get_user_memory_key(self, user_id, intent):
        """Create unique key for tracking user's seen responses"""
        return f"{user_id}_{intent}"
    
    def generate_dynamic_response(self, message, country, user_id="anonymous"):
        """Generate intelligent, varied response based on query analysis"""
        
        intents = self.analyze_query_intent(message)
        primary_intent = intents[0]
        country = country.lower()
        
        # Get country data
        country_info = self.country_data.get(country, self.country_data["ghana"])
        
        # Handle Ubuntu philosophy (universal response)
        if primary_intent == "ubuntu_philosophy":
            return self.get_ubuntu_response()
        
        # Handle country-specific responses
        if primary_intent in self.response_templates and country in self.response_templates[primary_intent]:
            return self.get_varied_response(primary_intent, country, country_info, user_id)
        
        # Handle mobile money
        elif primary_intent == "mobile_money" and country in self.response_templates["mobile_money"]:
            return self.get_mobile_money_response(country, country_info, user_id)
        
        # Handle culture/business
        elif primary_intent == "culture_business" and country in self.response_templates["culture_business"]:
            return self.get_culture_response(country, country_info, user_id)
        
        # Default to business startup advice
        else:
            return self.get_varied_response("business_startup", country, country_info, user_id)
    
    def get_varied_response(self, intent, country, country_info, user_id):
        """Get varied response that user hasn't seen before"""
        
        memory_key = self.get_user_memory_key(user_id, f"{intent}_{country}")
        seen_responses = self.response_memory.get(memory_key, set())
        
        templates = self.response_templates[intent][country]
        available_templates = [i for i in range(len(templates)) if i not in seen_responses]
        
        # If user has seen all templates, reset their memory
        if not available_templates:
            seen_responses = set()
            available_templates = list(range(len(templates)))
        
        # Select random template from unseen ones
        template_idx = random.choice(available_templates)
        template = templates[template_idx]
        
        # Update memory
        seen_responses.add(template_idx)
        self.response_memory[memory_key] = seen_responses
        
        # Fill template with country-specific data
        response = template.format(
            sectors=", ".join(random.sample(country_info["key_sectors"], 3)),
            mobile_money=", ".join(random.sample(country_info["mobile_money"], 2)),
            business_hubs=random.choice(country_info["business_hubs"])
        )
        
        # Add Ubuntu wisdom
        ubuntu_quote = random.choice(self.ubuntu_wisdom)
        response += f"\n\n🤝 Ubuntu wisdom: {ubuntu_quote}!"
        
        return response
    
    def get_ubuntu_response(self):
        """Get Ubuntu philosophy response"""
        ubuntu_responses = self.response_templates["ubuntu_philosophy"]
        response = random.choice(ubuntu_responses)
        return response
    
    def get_mobile_money_response(self, country, country_info, user_id):
        """Get mobile money specific response"""
        memory_key = self.get_user_memory_key(user_id, f"mobile_money_{country}")
        seen_responses = self.response_memory.get(memory_key, set())
        
        templates = self.response_templates["mobile_money"][country]
        available_templates = [i for i in range(len(templates)) if i not in seen_responses]
        
        if not available_templates:
            seen_responses = set()
            available_templates = list(range(len(templates)))
        
        template_idx = random.choice(available_templates)
        template = templates[template_idx]
        
        seen_responses.add(template_idx)
        self.response_memory[memory_key] = seen_responses
        
        response = template.format(mobile_money=", ".join(country_info["mobile_money"]))
        ubuntu_quote = random.choice(self.ubuntu_wisdom)
        response += f"\n\n🤝 Ubuntu wisdom: {ubuntu_quote}!"
        
        return response
    
    def get_culture_response(self, country, country_info, user_id):
        """Get culture-specific response"""
        memory_key = self.get_user_memory_key(user_id, f"culture_{country}")
        seen_responses = self.response_memory.get(memory_key, set())
        
        templates = self.response_templates["culture_business"][country]
        available_templates = [i for i in range(len(templates)) if i not in seen_responses]
        
        if not available_templates:
            seen_responses = set()
            available_templates = list(range(len(templates)))
        
        template_idx = random.choice(available_templates)
        template = templates[template_idx]
        
        seen_responses.add(template_idx)
        self.response_memory[memory_key] = seen_responses
        
        ubuntu_quote = random.choice(self.ubuntu_wisdom)
        response = template + f"\n\n🤝 Ubuntu wisdom: {ubuntu_quote}!"
        
        return response

# Initialize intelligent AfiYor
afiyor = IntelligentAfiYor()

@app.route('/')
def home():
    return jsonify({
        "name": "AfiYor API",
        "version": "2.1.0",
        "description": "African AI Assistant with Ubuntu Philosophy - Intelligent Dynamic System",
        "ubuntu": "I am because we are 🌍",
        "creator": "Built with love for African entrepreneurs",
        "intelligence": "Dynamic contextual responses with memory",
        "endpoints": {
            "chat": "/chat",
            "health": "/health"
        }
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": int(time.time()),
        "ai_status": "intelligent_dynamic_ready",
        "ubuntu": "Ngiyaphila - I am well because we are well",
        "version": "2.1.0",
        "memory_active": len(afiyor.response_memory) > 0
    })

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        country = data.get('country', 'ghana')
        language = data.get('language', 'en')
        user_id = data.get('user_id', 'anonymous')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Generate intelligent dynamic response
        response = afiyor.generate_dynamic_response(message, country, user_id)
        
        # Calculate confidence based on response quality and country match
        confidence = 0.9 if country.lower() in ["ghana", "nigeria", "kenya"] else 0.8
        
        return jsonify({
            "response": response,
            "confidence": confidence,
            "country": country,
            "language": language,
            "ai_source": "intelligent_dynamic",
            "ubuntu_wisdom": True,
            "timestamp": int(time.time()),
            "version": "2.1.0",
            "personalized": user_id != "anonymous"
        })
    
    except Exception as e:
        return jsonify({
            "error": "Ubuntu teaches us resilience. Let me try again.",
            "response": f"Akwaaba! I'm here to help with African business, culture, and Ubuntu philosophy. Could you rephrase your question? I specialize in {country.title()}'s business environment.",
            "confidence": 0.5,
            "ubuntu": "Even in challenges, we grow together"
        }), 200

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        data = request.get_json()
        rating = data.get('rating', 0)
        comment = data.get('comment', '')
        message = data.get('original_message', '')
        
        feedback_entry = {
            "rating": rating,
            "comment": comment, 
            "message": message,
            "timestamp": int(time.time())
        }
        print(f"AfiYor Feedback: {feedback_entry}")
        
        return jsonify({
            "status": "success",
            "message": "Medaase! (Thank you!) Your feedback helps AfiYor learn and serve our community better! 🧠",
            "ubuntu": "Through your feedback, we all grow stronger together"
        })
    
    except Exception as e:
        return jsonify({"error": "Could not process feedback"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
