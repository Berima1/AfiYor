from flask import Flask, request, jsonify  
from flask_cors import CORS  
import json  
import time  
import random  
import os  
  
app = Flask(__name__)  
CORS(app)  
  
# African Cultural Intelligence Database  
CULTURAL_RESPONSES = {  
    "nigeria": {  
        "business": [  
            "In Nigeria, relationships are everything! Build trust in your community first. Lagos is Africa's largest market with 24M people - focus on mobile-first solutions.",  
            "Consider Paystack or Flutterwave for payments. Over 80% of Nigerians use mobile phones. Start with solving traffic, payments, or communication problems.",  
            "Nigerian entrepreneurs value 'connection before transaction.' Spend time networking and building authentic relationships before pitching."  
        ],  
        "culture": [  
            "Nigeria is incredibly diverse with over 250 ethnic groups. Respect for elders and community consensus are important in business decisions.",  
            "Ubuntu philosophy applies here: 'I am because we are.' Your business success should lift the whole community.",  
            "Extended family networks are crucial. Consider how your product serves not just individuals but entire family units."  
        ]  
    },  
    "kenya": {  
        "business": [  
            "Kenya pioneered mobile money with M-Pesa! 96% of Kenyans use mobile payments. Consider how your business can integrate with this ecosystem.",  
            "Nairobi is East Africa's Silicon Savannah with strong startup support from iHub, MEST, and local VCs. The talent pool is excellent.",  
            "Harambee (working together) is central to Kenyan culture. Collaborative business models often succeed better than individual approaches."  
        ],  
        "culture": [  
            "Harambee means 'let's pull together' - community cooperation is essential. Design your business to strengthen community bonds.",  
            "Respect for elders and consensus-building are important. Include community leaders in your planning process.",  
            "Kenya's entrepreneurial spirit is strong. Focus on solutions that serve the broader East African market."  
        ]  
    },  
    "south_africa": {  
        "business": [  
            "South Africa has the most developed financial system in Africa. Consider both formal and informal markets in your strategy.",  
            "Cape Town and Johannesburg are major tech hubs with strong infrastructure and talent. The startup ecosystem is mature.",  
            "Ubuntu philosophy is deeply rooted: 'I am because we are.' Design your business to create shared prosperity."  
        ],  
        "culture": [  
            "Ubuntu is central to South African culture: 'umuntu ngumuntu ngabantu' - a person is a person through other people.",  
            "South Africa's diversity is its strength. Build inclusive products that serve all communities.",  
            "Legacy of apartheid means economic inclusion must be intentional. Focus on empowering previously disadvantaged communities."  
        ]  
    }  
}  
  
GENERAL_RESPONSES = {  
    "fintech": [  
        "Africa leads the world in mobile money innovation! M-Pesa processes more transactions daily than Western Union globally.",  
        "Financial inclusion is huge - 57% of African adults still lack access to formal banking. Your fintech could change millions of lives.",  
        "Cross-border payments are a massive opportunity with AfCFTA creating a continental market of 1.3 billion people.",  
        "Mobile money works because it built on existing trust networks and social structures. Study these patterns."  
    ],  
    "startup": [  
        "Africa has the world's youngest population - 60% under 25. Design for mobile-first, tech-savvy users who think globally.",  
        "The African Continental Free Trade Area (AfCFTA) creates incredible opportunities for continental business expansion.",  
        "African solutions often work better globally than foreign solutions work in Africa. Think big from day one.",  
        "Focus on solving real African problems. The continent needs solutions for payments, education, healthcare, and agriculture."  
    ],  
    "culture": [  
        "Ubuntu philosophy teaches 'I am because we are' - individual success comes from community prosperity.",  
        "African cultures emphasize community, respect for elders, and collective decision-making. Build these into your business model.",  
        "Extended family networks are crucial across Africa. Consider how your product serves family units, not just individuals.",  
        "Storytelling and oral tradition are important. Use narrative to connect with your audience authentically."  
    ]  
}  
  
class AfricanAI:  
    def __init__(self):  
        self.responses = CULTURAL_RESPONSES  
        self.general = GENERAL_RESPONSES  
          
    def get_response(self, message, country="nigeria", language="en"):  
        message_lower = message.lower()  
        country = country.lower()  
          
        # Determine category  
        if any(word in message_lower for word in ["business", "startup", "company", "entrepreneur"]):  
            category = "business"  
        elif any(word in message_lower for word in ["ubuntu", "culture", "tradition", "community"]):  
            category = "culture"  
        elif any(word in message_lower for word in ["fintech", "payment", "mobile money", "m-pesa", "banking"]):  
            return self._add_ubuntu_wisdom(random.choice(self.general["fintech"]), message_lower)  
        elif any(word in message_lower for word in ["startup", "innovation", "technology"]):  
            return self._add_ubuntu_wisdom(random.choice(self.general["startup"]), message_lower)  
        else:  
            category = "business"  # Default to business advice  
          
        # Get country-specific response  
        if country in self.responses and category in self.responses[country]:  
            response = random.choice(self.responses[country][category])  
        else:  
            # Fallback to general advice  
            response = f"For {country.title()}, focus on mobile-first solutions and community engagement. Understanding local culture and building trust are key to success in African markets."  
          
        return self._add_ubuntu_wisdom(response, message_lower)  
      
    def _add_ubuntu_wisdom(self, response, message):  
        if any(word in message for word in ["help", "community", "together", "ubuntu", "success"]):  
            return response + "\n\n🌍 Ubuntu wisdom: 'I am because we are' - your success strengthens our entire African community!"  
        return response  
  
# Initialize AI  
ai = AfricanAI()  
  
@app.route('/')  
def home():  
    return jsonify({  
        "name": "AfiYor API",  
        "version": "1.0.0",  
        "description": "African AI Assistant with Ubuntu Philosophy",  
        "ubuntu": "I am because we are 🌍",  
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
        "ubuntu": "Ngiyaphila - I am well because we are well"  
    })  
  
@app.route('/chat', methods=['POST'])  
def chat():  
    try:  
        data = request.get_json()  
        message = data.get('message', '').strip()  
        country = data.get('country', 'nigeria')  
        language = data.get('language', 'en')  
          
        if not message:  
            return jsonify({"error": "Message is required"}), 400  
          
        # Get AI response  
        response = ai.get_response(message, country, language)  
          
        # Calculate confidence (simple heuristic)  
        confidence = 0.9 if any(word in message.lower() for word in ["business", "startup", "ubuntu"]) else 0.7  
          
        return jsonify({  
            "response": response,  
            "confidence": confidence,  
            "country": country,  
            "language": language,  
            "timestamp": int(time.time()),  
            "ubuntu": "Sawubona - I see you! 👁️"  
        })  
      
    except Exception as e:  
        return jsonify({  
            "error": "Ubuntu teaches us resilience. Let me try again.",  
            "response": "I'm here to help with African business, culture, and Ubuntu philosophy. Could you rephrase your question?",  
            "confidence": 0.5  
        }), 200  
  
@app.route('/feedback', methods=['POST'])  
def feedback():  
    try:  
        data = request.get_json()  
        rating = data.get('rating', 0)  
        comment = data.get('comment', '')  
          
        # In production, save to database  
        print(f"Feedback received: {rating}/5 - {comment}")  
          
        return jsonify({  
            "status": "success",  
            "message": "Asante sana! Your feedback helps me learn! 🧠",  
            "ubuntu": "Through your feedback, we grow together"  
        })  
      
    except Exception as e:  
        return jsonify({"error": "Could not process feedback"}), 500  
  
if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port, debug=False)
