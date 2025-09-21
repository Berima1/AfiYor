# AfiYor Backend with Cohere AI - Updated app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import random
import os
import cohere

app = Flask(__name__)
CORS(app)

# Initialize Cohere AI
co = cohere.Client(os.environ.get('COHERE_API_KEY', 'your-cohere-api-key-here'))

class AfiYorAI:
    """AfiYor - African AI with Ubuntu Philosophy and Real Intelligence"""
    
    def __init__(self):
        self.ubuntu_wisdom = [
            "Ubuntu teaches us 'I am because we are'",
            "Individual success comes from community prosperity", 
            "In African business, we lift each other as we climb",
            "Community strength creates individual opportunities",
            "Together we rise - that's the Ubuntu way"
        ]
        
        self.country_context = {
            "ghana": {
                "mobile_money": "MTN MoMo, AirtelTigo Money, Vodafone Cash",
                "business_hubs": "Accra Digital Centre, MEST Africa, Impact Hub Accra",
                "key_sectors": "cocoa, gold, oil, fintech, agriculture",
                "culture": "Akan values, respect for elders, community decision-making",
                "languages": "English, Twi, Ga, Ewe",
                "greeting": "Akwaaba! (Welcome)"
            },
            "nigeria": {
                "mobile_money": "Paystack, Flutterwave, Opay, PalmPay", 
                "business_hubs": "Lagos, Abuja, Port Harcourt tech ecosystems",
                "key_sectors": "oil, agriculture, fintech, entertainment (Nollywood)",
                "culture": "diverse ethnic groups, respect-based hierarchy, relationship-first business",
                "languages": "English, Yoruba, Igbo, Hausa",
                "greeting": "Sannu! Bawo! (Welcome/How are you)"
            },
            "kenya": {
                "mobile_money": "M-Pesa, Airtel Money, T-Kash",
                "business_hubs": "Nairobi Silicon Savannah, iHub, MEST",
                "key_sectors": "agriculture, tourism, mobile money, renewable energy",
                "culture": "Harambee (community cooperation), Ubuntu values",
                "languages": "English, Swahili, Kikuyu",
                "greeting": "Habari! (Hello)"
            },
            "south_africa": {
                "mobile_money": "SnapScan, Zapper, FNB eWallet",
                "business_hubs": "Cape Town, Johannesburg, Durban",
                "key_sectors": "mining, finance, tourism, renewable energy",
                "culture": "Ubuntu philosophy, Rainbow Nation diversity",
                "languages": "English, Zulu, Xhosa, Afrikaans",
                "greeting": "Sawubona! (I see you)"
            }
        }
    
    def create_african_prompt(self, message, country, language):
        """Create contextually rich prompt for Cohere"""
        
        country_info = self.country_context.get(country.lower(), self.country_context["ghana"])
        
        prompt = f"""You are AfiYor, an intelligent African AI assistant built with Ubuntu philosophy.

CONTEXT:
- User is from {country.title()}
- User question: "{message}"
- Your purpose: Help African entrepreneurs succeed with Ubuntu wisdom

AFRICAN KNOWLEDGE:
- {country.title()} mobile money: {country_info['mobile_money']}
- Business hubs: {country_info['business_hubs']}  
- Key sectors: {country_info['key_sectors']}
- Cultural values: {country_info['culture']}
- Languages: {country_info['languages']}

UBUNTU PHILOSOPHY:
"I am because we are" - Individual success must benefit the community.
Always consider how advice helps both the person and their community.

RESPONSE STYLE:
- Start with a warm African greeting
- Give practical, actionable advice for {country.title()}
- Include Ubuntu wisdom when relevant
- Mention specific African solutions (mobile money, local platforms, etc.)
- End with encouragement that builds community

IMPORTANT:
- Keep responses under 200 words
- Be specific to {country.title()}'s context
- Include real African business insights
- Always maintain Ubuntu philosophy

Your response:"""
        
        return prompt
    
    def get_intelligent_response(self, message, country="ghana", language="en"):
        """Get AI-powered response from Cohere"""
        
        try:
            # Create African-context prompt
            prompt = self.create_african_prompt(message, country, language)
            
            # Call Cohere AI
            response = co.generate(
                model='command',
                prompt=prompt,
                max_tokens=200,
                temperature=0.7,  # Creative but focused
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )
            
            ai_response = response.generations[0].text.strip()
            
            # Add Ubuntu wisdom if not already included
            if not any(ubuntu in ai_response.lower() for ubuntu in ["ubuntu", "i am because", "we are", "community"]):
                ubuntu_quote = random.choice(self.ubuntu_wisdom)
                ai_response += f"\n\n🤝 Ubuntu wisdom: {ubuntu_quote}!"
            
            return {
                "response": ai_response,
                "source": "cohere_ai",
                "country": country,
                "confidence": 0.9,
                "ubuntu_wisdom": True
            }
            
        except Exception as e:
            # Fallback to thoughtful pre-written response
            print(f"Cohere API error: {e}")
            return self.get_fallback_response(message, country)
    
    def get_fallback_response(self, message, country):
        """Intelligent fallback when API is unavailable"""
        
        country_info = self.country_context.get(country.lower(), self.country_context["ghana"])
        message_lower = message.lower()
        
        # Determine response type
        if any(word in message_lower for word in ["business", "startup", "company", "entrepreneur"]):
            response = f"{country_info['greeting']} For business success in {country.title()}, focus on building trust within your community first. The key sectors here are {country_info['key_sectors']}. Consider mobile money integration with {country_info['mobile_money']} - it's essential for reaching customers effectively."
            
        elif any(word in message_lower for word in ["mobile money", "payment", "fintech", "banking"]):
            response = f"In {country.title()}, mobile money is transformative! The main platforms are {country_info['mobile_money']}. These systems work because they build on existing trust networks and solve real community problems."
            
        elif any(word in message_lower for word in ["culture", "ubuntu", "community", "tradition"]):
            response = f"Ubuntu philosophy is central to {country.title()}'s business culture: 'I am because we are.' This means {country_info['culture']}. Successful businesses here strengthen the entire community, not just individual wealth."
            
        else:
            response = f"{country_info['greeting']} {country.title()} has incredible opportunities in {country_info['key_sectors']}. Focus on mobile-first solutions since {country_info['mobile_money']} are widely used. Build relationships and trust - that's how business works here."
        
        # Add Ubuntu wisdom
        ubuntu_quote = random.choice(self.ubuntu_wisdom)
        response += f"\n\n🌍 Ubuntu wisdom: {ubuntu_quote} - your success strengthens our entire African community!"
        
        return {
            "response": response,
            "source": "fallback_intelligent",
            "country": country,
            "confidence": 0.7,
            "ubuntu_wisdom": True
        }

# Initialize AfiYor AI
afiyor = AfiYorAI()

@app.route('/')
def home():
    return jsonify({
        "name": "AfiYor API",
        "version": "2.0.0",
        "description": "African AI Assistant with Ubuntu Philosophy - Powered by Cohere",
        "ubuntu": "I am because we are 🌍",
        "creator": "Built with love for African entrepreneurs",
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
        "ai_status": "cohere_ready",
        "ubuntu": "Ngiyaphila - I am well because we are well",
        "version": "2.0.0"
    })

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        country = data.get('country', 'ghana')
        language = data.get('language', 'en')
        
        if not message:
            return jsonify({"error": "Message is required"}), 400
        
        # Get AI response
        result = afiyor.get_intelligent_response(message, country, language)
        
        return jsonify({
            "response": result["response"],
            "confidence": result["confidence"],
            "country": country,
            "language": language,
            "ai_source": result["source"],
            "ubuntu_wisdom": result["ubuntu_wisdom"],
            "timestamp": int(time.time()),
            "version": "2.0.0"
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
        
        # Log feedback for improvement
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

@app.route('/countries')
def get_countries():
    """Get supported African countries with context"""
    countries = []
    for country, info in afiyor.country_context.items():
        countries.append({
            "code": country,
            "name": country.title(),
            "greeting": info["greeting"],
            "mobile_money": info["mobile_money"],
            "key_sectors": info["key_sectors"]
        })
    
    return jsonify({
        "countries": countries,
        "ubuntu": "Unity in diversity - celebrating all of Africa!"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
