""" AfiYor Backend - Hybrid Groq (Full Sankofa Hybrid, Groq-only for now) This canvas contains the new backend files you can copy into backend/ on your GitHub repo.

Files included below:

app.py             (main Flask app with Groq + Sankofa Full Hybrid integration)

.env.example       (example env file - do NOT commit real keys)

requirements.txt   (dependencies to add)

README_AI.md       (instructions)


Security: keep your real GROQ_API_KEY inside backend/.env and never commit it. """

--- FILE: app.py ---

from flask import Flask, request, jsonify from flask_cors import CORS import os import time import traceback from dotenv import load_dotenv

Load env from backend/.env

load_dotenv() GROQ_API_KEY = os.environ.get('GROQ_API_KEY') PORT = int(os.environ.get('PORT', 5000))

Try to import groq SDK

try: from groq import Groq groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None except Exception: groq_client = None

app = Flask(name) CORS(app)

------------------ Sankofa Wisdom ------------------

import random

class SankofaWisdom: """African wisdom and cultural intelligence (full-hybrid engine) Use these building blocks to shape every outgoing message so it becomes both high-quality business advice and culturally rooted guidance. """ UBUNTU_QUOTES = [ "I am because we are - Ubuntu", "A person is a person through other people - Umuntu ngumuntu ngabantu", "I participate, therefore I am - Ubuntu philosophy", "My humanity is caught up in yours - Ubuntu wisdom", "We are, therefore I am - African communalism" ]

AFRICAN_PROVERBS = [
    "If you want to go fast, go alone. If you want to go far, go together.",
    "When spider webs unite, they can tie up a lion.",
    "A single bracelet does not jingle.",
    "Many hands make light work.",
    "The tree that survives the storm is the one that bends."
]

SUCCESS_WISDOM = [
    "Success in Africa comes from lifting others as you climb.",
    "Ubuntu teaches us that individual prosperity without community prosperity is hollow.",
    "In African business, trust is your most valuable currency.",
    "The strongest African businesses are built on community foundations.",
    "Remember: your success should make the whole village proud."
]

def get_ubuntu_quote(self):
    return random.choice(self.UBUNTU_QUOTES)

def get_african_proverb(self):
    return random.choice(self.AFRICAN_PROVERBS)

def get_success_wisdom(self):
    return random.choice(self.SUCCESS_WISDOM)

sankofa = SankofaWisdom()

------------------ Knowledge Base (existing AfiYor content) ------------------

AFRICAN_BUSINESS_KNOWLEDGE_BASE = { "funding_data": { "pre_seed": { "amount": "$10K - $250K", "sources": ["Personal savings", "Friends & family", "Angel investors"], "african_vcs": ["TLcom Capital", "Partech Africa", "Knife Capital"] }, "seed": { "amount": "$250K - $2M", "sources": ["Angel investors", "Seed VCs", "Corporate ventures"], "african_vcs": ["TLcom Capital (Kenya/Nigeria)", "Partech Africa (West Africa)", "4DX Ventures (Egypt)"] } }, "mobile_money_data": { "ghana": { "mtn_momo": {"market_share": "65%", "users": "18M active"}, "airteltigo": {"market_share": "20%", "focus": "Rural populations"}, "vodafone_cash": {"market_share": "15%", "strength": "International transfers"} }, "kenya": { "mpesa": {"market_share": "96%", "daily_volume": "$500M", "penetration": "96% of adults"} } }, "business_registration": { "ghana": { "authority": "Registrar General's Department", "cost": "GHS 150-300 ($25-50 USD)", "timeline": "1-5 business days", "process": "Online via RGD portal" }, "nigeria": { "authority": "Corporate Affairs Commission (CAC)", "cost": "NGN 10,000-35,000 ($25-85 USD)", "timeline": "24-48 hours online", "process": "Online via CAC portal" } } }

------------------ AfiYor Professional logic ------------------

class ProfessionalAfiYor: def init(self): self.knowledge_base = AFRICAN_BUSINESS_KNOWLEDGE_BASE

def analyze_query(self, message):
    message_lower = message.lower()
    
    if any(word in message_lower for word in ['funding', 'investment', 'investor', 'capital']):
        return 'funding'
    elif any(word in message_lower for word in ['mobile money', 'm-pesa', 'momo', 'payment']):
        return 'mobile_money'
    elif any(word in message_lower for word in ['register', 'legal', 'license', 'incorporation']):
        return 'legal_registration'
    elif any(word in message_lower for word in ['ubuntu', 'culture', 'philosophy', 'community']):
        return 'ubuntu'
    else:
        return 'general_business'

def generate_professional_response(self, message, country='ghana', industry='general'):
    intent = self.analyze_query(message)
    
    if intent == 'funding':
        return self.get_funding_response(message, country)
    elif intent == 'mobile_money':
        return self.get_mobile_money_response(message, country)
    elif intent == 'legal_registration':
        return self.get_legal_response(message, country)
    elif intent == 'ubuntu':
        return self.get_ubuntu_response(message, country)
    else:
        return self.get_general_response(message, country, industry)

def get_funding_response(self, message, country):
    funding_data = self.knowledge_base['funding_data']
    
    if 'seed' in message.lower():
        stage_data = funding_data['seed']
        response = f"""**Professional Funding Intelligence for {country.title()}**

Seed Funding Overview: • Typical Amount: {stage_data['amount']} • Key Sources: {', '.join(stage_data['sources'])}

Top African VCs:""" for vc in stage_data['african_vcs']: response += f" • {vc}" else: stage_data = funding_data['pre_seed'] response = f"""Professional Funding Intelligence for {country.title()}

Pre-Seed Funding Overview: • Typical Amount: {stage_data['amount']} • Key Sources: {', '.join(stage_data['sources'])}

African Funding Sources:""" for vc in stage_data['african_vcs']: response += f" • {vc}"

response += "

Success Factors: • Strong team with complementary skills • Clear market opportunity • Proven traction and growth • Scalable business model" response += "

Ubuntu wisdom: Build partnerships that create mutual prosperity for your community."

return response

def get_mobile_money_response(self, message, country):
    mm_data = self.knowledge_base['mobile_money_data']
    
    response = f"**Mobile Money Intelligence for {country.title()}**

"

if country.lower() == 'ghana' and 'ghana' in mm_data:
        ghana_data = mm_data['ghana']
        response += "**Ghana Mobile Money Market:**

" response += f"• MTN MoMo: {ghana_data['mtn_momo']['market_share']} market share, {ghana_data['mtn_momo']['users']} " response += f"• AirtelTigo Money: {ghana_data['airteltigo']['market_share']}, focus on {ghana_data['airteltigo']['focus']} " response += f"• Vodafone Cash: {ghana_data['vodafone_cash']['market_share']}, strength in {ghana_data['vodafone_cash']['strength']}"

elif country.lower() == 'kenya' and 'kenya' in mm_data:
        kenya_data = mm_data['kenya']
        response += "**Kenya Mobile Money Leadership:**

" response += f"• M-Pesa: {kenya_data['mpesa']['market_share']} market share " response += f"• Daily Volume: {kenya_data['mpesa']['daily_volume']} " response += f"• Penetration: {kenya_data['mpesa']['penetration']}" else: response += "African Mobile Money Overview: " response += "• Africa processes 70% of global mobile money transactions " response += "• $490 billion transaction value in 2024 " response += "• 469 million registered users continent-wide"

if 'integrate' in message.lower():
        response += "

Integration Requirements: " response += "• HTTPS secure connections " response += "• API key management " response += "• KYC compliance " response += "• Transaction reconciliation"

response += "

Ubuntu insight: Mobile money succeeds because it serves the entire community's financial needs." return response

def get_legal_response(self, message, country):
    legal_data = self.knowledge_base['business_registration']
    
    if country.lower() in legal_data:
        country_data = legal_data[country.lower()]
        
        response = f"""**Business Registration Guide for {country.title()}**

Registration Details: • Authority: {country_data['authority']} • Cost: {country_data['cost']} • Timeline: {country_data['timeline']} • Process: {country_data['process']}

Next Steps: • Complete name search and reservation • Prepare incorporation documents • Submit application with required fees • Obtain business certificate""" else: response = f"""Business Registration for {country.title()}

General Requirements: • Business name registration • Incorporation documents • Registered office address • Share capital declaration (if applicable)

Typical Process: • Online application submission • Document verification • Fee payment • Certificate issuance"""

response += "

Ubuntu principle: Proper legal foundation protects your community's investment in your success." return response

def get_ubuntu_response(self, message, country):
    response = """**Ubuntu Philosophy in Business**

Core Meaning: "I am because we are" - Individual success comes from community prosperity.

Business Applications: • Consultative decision-making processes • Employee development and mentorship • Community-first product design • Shared value creation with stakeholders • Long-term relationship building

Success Examples: • M-Pesa: Financial inclusion for entire communities • Grameen Bank: Microfinance based on community trust • African Leadership Academy: Developing leaders for continent

Leadership Principles: • Servant leadership approach • Emphasis on consensus building • Focus on collective outcomes • Investment in people development"""

response += f"

Ubuntu wisdom: Your business success should strengthen the entire {country} community." return response

def get_general_response(self, message, country, industry):
    response = f"""**Professional Business Guidance for {country.title()}**

Market Context: • Africa's 1.4 billion population, 60% under 25 • 84% mobile penetration across continent • Growing middle class of 350 million people • $490 billion mobile money transaction volume

Success Principles for {industry.title()}: • Focus on solving real community problems • Build for mobile-first users • Understand local payment preferences • Create sustainable business models • Integrate cultural values like Ubuntu"""

if industry == 'fintech':
        response += "

Fintech Opportunities: • 570 million unbanked adults • Cross-border payment needs • SME financing gap of $331 billion" elif industry == 'agriculture': response += "

Agriculture Focus: • Employs 60% of workforce • Climate-smart solutions needed • Value chain integration opportunities"

response += f"

Ubuntu wisdom: Individual success comes from community prosperity - build businesses that lift everyone in {country}." return response

Initialize professional AfiYor

professional_afiyor = ProfessionalAfiYor()

Simple user storage (in production, use a proper database)

users_db = {}

------------------ Groq integration helper (Groq only for now) ------------------

def generate_ai_message(afiyor_text, user_message, country='Ghana', industry='general', tone='business_coach'): """Send the AfiYor text + user message to Groq to refine and return a coached version.

Tone options supported internally: 'professional', 'friendly', 'business_coach'
"""
if not groq_client:
    return None, "Groq client not configured"

tone_description = {
    'professional': 'Formal, concise, investor-ready tone.',
    'friendly': 'Warm, simple language, occasionally uses local phrases.',
    'business_coach': 'Professional coach: encouraging, actionable, with next-step recommendations.'
}.get(tone, 'Professional and helpful tone.')

system_prompt = (
    "You are an African business coach and editor.

" "Refine the provided AfiYor response into a single clear message. " "Keep cultural context in mind, be actionable, and provide concise next steps. " f"Tone guideline: {tone_description} " "If the AfiYor text contains bullet lists, keep them but make them clearer. " "If integration or legal steps are mentioned, summarize required actions and who should do them. " "Do NOT invent facts not present in the AfiYor text; when asked about numbers outside the knowledge base, say you can research further." )

user_prompt = (
    f"User question: {user_message}

" f"AfiYor draft: {afiyor_text}

" "Return the refined message as plain text. Include a 2-3 item action checklist at the end." )

try:
    completion = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=512,
        temperature=0.2
    )

    content = completion.choices[0].message.content if hasattr(completion, 'choices') else str(completion)
    return content, None
except Exception as e:
    traceback.print_exc()
    return None, str(e)

def apply_sankofa_full_hybrid(ai_text, user_message): """Transform the AI text into a Sankofa-shaped final message. Full hybrid mode: reshape tone, add ubuntu wisdom, proverbs, and an action checklist. """ # Opening coach line opening = sankofa.get_success_wisdom() proverb = sankofa.get_african_proverb() ubuntu = sankofa.get_ubuntu_quote()

# Ensure ai_text is string
if not ai_text:
    ai_text = "I'm unable to reach the AI service right now. Here's the best guidance I can offer from AfiYor's knowledge base."

# Compose final message: open strong, then AI content, then Sankofa elements and checklist
checklist = "

Action checklist:

1. Validate local requirements and contacts.


2. Prepare 1-page pitch + 3 key metrics.


3. Reach out to at least 3 local partners/VCs."

final = f"{opening}



{ai_text}

Proverb: {proverb} Ubuntu: {ubuntu}{checklist}" return final

------------------ Flask routes ------------------

@app.route('/') def home(): return jsonify({ "name": "AfiYor Professional API", "version": "4.2.0", "description": "Research-Based African Business Intelligence + Groq AI (Full Sankofa Hybrid)", "ubuntu": "I am because we are", "status": "hybrid_sankofa_ready" })

@app.route('/register', methods=['POST']) def register_user(): try: data = request.get_json() email = data.get('email') name = data.get('name') country = data.get('country', 'ghana') if not email or not name: return jsonify({"error": "Email and name are required"}), 400 if email in users_db: return jsonify({"error": "Email already registered"}), 400 user_id = f"user_{len(users_db) + 1}" users_db[email] = { "id": user_id, "name": name, "email": email, "country": country, "industry": data.get('industry', 'general'), "business_stage": data.get('business_stage', 'idea'), "created_at": int(time.time()) } return jsonify({ "status": "success", "user_id": user_id, "message": f"Akwaaba {name}! Your AfiYor account is ready.", "personalization": "enabled" }) except Exception as e: return jsonify({"error": "Registration failed", "detail": str(e)}), 500

@app.route('/login', methods=['POST']) def login_user(): try: data = request.get_json() email = data.get('email') if not email: return jsonify({"error": "Email is required"}), 400 if email in users_db: user = users_db[email] return jsonify({ "status": "success", "user_id": user["id"], "name": user["name"], "message": f"Welcome back, {user['name']}!" }) else: return jsonify({"error": "Account not found. Please register first."}), 404 except Exception as e: return jsonify({"error": "Login failed", "detail": str(e)}), 500

@app.route('/history/<user_id>') def get_conversation_history(user_id): try: return jsonify({ "conversations": [], "total": 0, "user_id": user_id, "message": "History feature will be available soon!" }) except Exception as e: return jsonify({"error": "Could not fetch history", "detail": str(e)}), 500

@app.route('/chat', methods=['POST']) def professional_chat(): try: data = request.get_json() message = data.get('message', '').strip() country = data.get('country', 'ghana') industry = data.get('industry', 'general') tone_choice = data.get('tone', 'business_coach')  # accept override from client

if not message:
        return jsonify({"error": "Message is required"}), 400

    # Step 1: Local AfiYor draft
    afiyor_draft = professional_afiyor.generate_professional_response(message, country, industry)

    # Step 2: Send to Groq to refine (hybrid)
    refined_text, error = None, None
    if groq_client:
        refined_text, error = generate_ai_message(afiyor_draft, message, country, industry, tone_choice)

    # Step 3: Apply Sankofa full-hybrid transformation (always)
    final_response = apply_sankofa_full_hybrid(refined_text if refined_text else afiyor_draft, message)

    return jsonify({
        "response": final_response,
        "confidence": 0.95 if refined_text else 0.85,
        "source": "hybrid_sankofa_groq",
        "country": country,
        "industry": industry,
        "version": "4.2.0",
        "ai_error": error
    })

except Exception as e:
    traceback.print_exc()
    return jsonify({
        "error": "Processing professional guidance",
        "response": f"I'm analyzing your {industry} question for {country}. Ubuntu teaches us patience - let me provide research-based guidance.",
        "confidence": 0.7
    }), 200

@app.route('/health') def health(): return jsonify({ "status": "healthy", "version": "4.2.0", "ai_status": "hybrid_sankofa_ready" if groq_client else "groq_not_configured", "knowledge_base_loaded": True, "ubuntu": "Ngiyaphila - I am well because we are well" })

if name == 'main': print("AfiYor Professional System Starting with Groq Hybrid (Full Sankofa)...") print("Groq configured:" , bool(groq_client)) app.run(host='0.0.0.0', port=PORT, debug=False)
