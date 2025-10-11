# app.py — AfiYor FastAPI (Full Sankofa Hybrid, honors Afiyor Tetteh)
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv
import os
import random
import time
import traceback

# Load env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PORT = int(os.getenv("PORT", 8000))

# Try to import groq SDK (optional)
try:
    from groq import Groq
    groq_client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None
except Exception:
    groq_client = None

# FastAPI app
app = FastAPI(title="AfiYor API (Honouring Afiyor Tetteh)")

# Allow CORS (adjust allow_origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Sankofa Wisdom ----------------
class SankofaWisdom:
    UBUNTU_QUOTES = [
        "I am because we are - Ubuntu",
        "A person is a person through other people - Umuntu ngumuntu ngabantu",
        "I participate, therefore I am - Ubuntu philosophy",
        "My humanity is caught up in yours - Ubuntu wisdom",
        "We are, therefore I am - African communalism"
    ]
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

    def get_ubuntu_quote(self) -> str:
        return random.choice(self.UBUNTU_QUOTES)

    def get_african_proverb(self) -> str:
        return random.choice(self.AFRICAN_PROVERBS)

    def get_success_wisdom(self) -> str:
        return random.choice(self.SUCCESS_WISDOM)

sankofa = SankofaWisdom()

def apply_sankofa_full_hybrid(ai_text: str, user_message: str) -> str:
    opening = sankofa.get_success_wisdom()
    proverb = sankofa.get_african_proverb()
    ubuntu = sankofa.get_ubuntu_quote()
    if not ai_text:
        ai_text = "I'm unable to reach the AI service right now. Here's the best guidance I can offer from AfiYor's knowledge base."
    checklist = (
        "\n\nAction checklist:\n"
        "1. Validate local requirements and contacts.\n"
        "2. Prepare a 1-page pitch + 3 key metrics.\n"
        "3. Reach out to at least 3 local partners / VCs."
    )
    final = (
        f"{opening}\n\n"
        f"{ai_text}\n\n"
        f"Proverb: {proverb}\n"
        f"Ubuntu: {ubuntu}{checklist}"
    )
    return final

# ---------------- Knowledge Base (kept small & safe) ----------------
AFRICAN_BUSINESS_KNOWLEDGE_BASE = {
    "funding_data": {
        "pre_seed": {
            "amount": "$10K - $250K",
            "sources": ["Personal savings", "Friends & family", "Angel investors"],
            "african_vcs": ["TLcom Capital", "Partech Africa", "Knife Capital"]
        },
        "seed": {
            "amount": "$250K - $2M",
            "sources": ["Angel investors", "Seed VCs", "Corporate ventures"],
            "african_vcs": ["TLcom Capital", "Partech Africa", "4DX Ventures"]
        }
    },
    "mobile_money_data": {
        "ghana": {
            "mtn_momo": {"market_share": "65%", "users": "18M active"},
            "airteltigo": {"market_share": "20%", "focus": "Rural populations"},
            "vodafone_cash": {"market_share": "15%", "strength": "International transfers"}
        },
        "kenya": {
            "mpesa": {"market_share": "96%", "daily_volume": "$500M"}
        }
    }
}

# ---------------- AfiYor logic (lightweight) ----------------
class ProfessionalAfiYor:
    def __init__(self):
        self.knowledge_base = AFRICAN_BUSINESS_KNOWLEDGE_BASE

    def analyze_query(self, message: str) -> str:
        text = (message or "").lower()
        if any(w in text for w in ["funding", "investment", "investor", "capital"]):
            return "funding"
        if any(w in text for w in ["mobile money", "m-pesa", "momo", "payment"]):
            return "mobile_money"
        if any(w in text for w in ["register", "legal", "license", "incorporation"]):
            return "legal_registration"
        if any(w in text for w in ["ubuntu", "culture", "philosophy", "community"]):
            return "ubuntu"
        return "general_business"

    def generate_professional_response(self, message: str, country: str = "ghana", industry: str = "general") -> str:
        intent = self.analyze_query(message)
        if intent == "funding":
            return self._funding(message, country)
        if intent == "mobile_money":
            return self._mobile_money(message, country)
        if intent == "legal_registration":
            return self._legal(message, country)
        if intent == "ubuntu":
            return self._ubuntu(message, country)
        return self._general(message, country, industry)

    def _funding(self, message: str, country: str) -> str:
        stage = "seed" if "seed" in (message or "").lower() else "pre_seed"
        data = self.knowledge_base["funding_data"][stage]
        lines = [
            f"**Professional Funding Intelligence for {country.title()}**",
            "",
            f"**{stage.replace('_',' ').title()} Funding Overview:**",
            f"• Typical Amount: {data['amount']}",
            f"• Key Sources: {', '.join(data['sources'])}",
            "",
            "**Top African VCs:**"
        ]
        for vc in data["african_vcs"]:
            lines.append(f"• {vc}")
        lines.extend([
            "",
            "**Success Factors:**",
            "• Strong team with complementary skills",
            "• Clear market opportunity",
            "• Proven traction and growth",
            "• Scalable business model",
            "",
            "Ubuntu wisdom: Build partnerships that create mutual prosperity for your community."
        ])
        return "\n".join(lines)

    def _mobile_money(self, message: str, country: str) -> str:
        mm = self.knowledge_base["mobile_money_data"].get(country.lower(), {})
        lines = [f"**Mobile Money Intelligence for {country.title()}**", ""]
        if mm:
            if country.lower() == "ghana":
                g = mm["ghana"]
                lines += [
                    "**Ghana Mobile Money Market:**",
                    f"• MTN MoMo: {g['mtn_momo']['market_share']} market share, {g['mtn_momo']['users']}",
                    f"• AirtelTigo Money: {g['airteltigo']['market_share']}, focus on {g['airteltigo']['focus']}",
                    f"• Vodafone Cash: {g['vodafone_cash']['market_share']}, strength in {g['vodafone_cash']['strength']}"
                ]
            elif country.lower() == "kenya":
                k = mm["kenya"]
                lines += [
                    "**Kenya Mobile Money Leadership:**",
                    f"• M-Pesa: {k['mpesa']['market_share']} market share",
                    f"• Daily Volume: {k['mpesa']['daily_volume']}"
                ]
        else:
            lines += [
                "**African Mobile Money Overview:**",
                "• Africa processes 70% of global mobile money transactions",
                "• $490 billion transaction value in 2024",
                "• 469 million registered users continent-wide"
            ]
        lines += ["", "Ubuntu insight: Mobile money succeeds because it serves the entire community's financial needs."]
        return "\n".join(lines)

    def _legal(self, message: str, country: str) -> str:
        reg = self.knowledge_base.get("business_registration", {})
        country_data = reg.get(country.lower())
        if country_data:
            lines = [
                f"**Business Registration Guide for {country.title()}**",
                "",
                "**Registration Details:**",
                f"• Authority: {country_data['authority']}",
                f"• Cost: {country_data['cost']}",
                f"• Timeline: {country_data['timeline']}",
                f"• Process: {country_data['process']}",
                "",
                "**Next Steps:**",
                "• Complete name search and reservation",
                "• Prepare incorporation documents",
                "• Submit application with required fees",
                "• Obtain business certificate",
                "",
                "Ubuntu principle: Proper legal foundation protects your community's investment in your success."
            ]
            return "\n".join(lines)
        return ("**Business Registration**\n\n"
                "• Business name registration\n"
                "• Incorporation documents\n"
                "• Registered office address\n"
                "• Fee payment and certificate issuance\n\n"
                "Ubuntu principle: Proper legal foundation protects your community's investment in your success.")

    def _ubuntu(self, message: str, country: str) -> str:
        content = (
            "**Ubuntu Philosophy in Business**\n\n"
            "**Core Meaning:** \"I am because we are\" - Individual success comes from community prosperity.\n\n"
            "**Business Applications:**\n"
            "• Consultative decision-making processes\n"
            "• Employee development and mentorship\n"
            "• Community-first product design\n"
            "• Shared value creation with stakeholders\n"
            "• Long-term relationship building\n\n"
            "**Success Examples:**\n"
            "• M-Pesa: Financial inclusion for entire communities\n"
            "• Grameen Bank: Microfinance based on community trust\n"
            "• African Leadership Academy: Developing leaders for continent\n\n"
            "**Leadership Principles:**\n"
            "• Servant leadership approach\n"
            "• Emphasis on consensus building\n"
            "• Focus on collective outcomes\n"
            "• Investment in people development\n\n"
            f"Ubuntu wisdom: Your business success should strengthen the entire {country} community."
        )
        return content

    def _general(self, message: str, country: str, industry: str) -> str:
        content = (
            f"**Professional Business Guidance for {country.title()}**\n\n"
            "**Market Context:**\n"
            "• Africa's 1.4 billion population, 60% under 25\n"
            "• 84% mobile penetration across continent\n"
            "• Growing middle class of 350 million people\n"
            "• $490 billion mobile money transaction volume\n\n"
            f"**Success Principles for {industry.title()}:**\n"
            "• Focus on solving real community problems\n"
            "• Build for mobile-first users\n"
            "• Understand local payment preferences\n"
            "• Create sustainable business models\n"
            "• Integrate cultural values like Ubuntu\n"
        )
        if industry == "fintech":
            content += (
                "\n**Fintech Opportunities:**\n"
                "• 570 million unbanked adults\n"
                "• Cross-border payment needs\n"
                "• SME financing gap of $331 billion\n"
            )
        elif industry == "agriculture":
            content += (
                "\n**Agriculture Focus:**\n"
                "• Employs 60% of workforce\n"
                "• Climate-smart solutions needed\n"
                "• Value chain integration opportunities\n"
            )
        content += f"\n\nUbuntu wisdom: Individual success comes from community prosperity - build businesses that lift everyone in {country}."
        return content

professional_afiyor = ProfessionalAfiYor()

# ---------------- In-memory storage (for demo) ----------------
users_db: Dict[str, Dict[str, Any]] = {}
conversations: List[Dict[str, Any]] = []

# ---------------- Pydantic models ----------------
class RegisterRequest(BaseModel):
    name: str
    email: str
    country: Optional[str] = "ghana"
    industry: Optional[str] = "general"

class LoginRequest(BaseModel):
    email: str

class ChatRequest(BaseModel):
    message: str
    country: Optional[str] = "ghana"
    industry: Optional[str] = "general"
    user_id: Optional[str] = None
    tone: Optional[str] = "business_coach"

class ChatResponse(BaseModel):
    response: str
    confidence: float
    conversation_id: Optional[int] = None
    ai_error: Optional[str] = None

# ---------------- Groq helper (optional) ----------------
def generate_ai_message(afiyor_text: str, user_message: str, country: str='Ghana', industry: str='general', tone: str='business_coach'):
    if not groq_client:
        return None, "Groq client not configured"
    tone_description = {
        'professional': 'Formal, concise, investor-ready tone.',
        'friendly': 'Warm, simple language, occasionally uses local phrases.',
        'business_coach': 'Professional coach: encouraging, actionable, with next-step recommendations.'
    }.get(tone, 'Professional and helpful tone.')
    system_prompt = (
        "You are an African business coach and editor.\n"
        "Refine the provided AfiYor response into a single clear message.\n"
        f"Tone guideline: {tone_description}\n"
        "Be actionable and concise. Do NOT invent facts not present in the AfiYor text."
    )
    user_prompt = f"User question: {user_message}\n\nAfiYor draft: {afiyor_text}\n\nReturn the refined message as plain text. Include a short 2-3 item action checklist."
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

# ---------------- Routes ----------------
@app.get("/")
async def root():
    intro = (
        "I am AfiYor, named in eternal memory of Afiyor Tetteh — a mother whose wisdom walks with us still. "
        "I am your African business elder, rooted in Sankofa and Ubuntu. I blend research-based advice with "
        "proverbs and practical next steps. Ɔkasa mu nokware yɛ nkabom (truth builds unity)."
    )
    return {"name": "AfiYor", "intro": intro, "version": "1.0", "status": "ready"}

@app.post("/auth/register")
async def register(req: RegisterRequest):
    if not req.email or not req.name:
        raise HTTPException(status_code=400, detail="Name and email required")
    if req.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_id = f"user_{len(users_db)+1}"
    users_db[req.email] = {
        "id": user_id, "name": req.name, "email": req.email,
        "country": req.country, "industry": req.industry, "created_at": int(time.time())
    }
    return {"status": "success", "user_id": user_id, "message": f"Akwaaba {req.name}!"}

@app.post("/auth/login")
async def login(req: LoginRequest):
    user = users_db.get(req.email)
    if not user:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"status": "success", "user_id": user["id"], "name": user["name"], "message": f"Welcome back, {user['name']}!"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    if not req.message or not req.message.strip():
        raise HTTPException(status_code=400, detail="Message is required")
    # Local draft from AfiYor KB
    draft = professional_afiyor.generate_professional_response(req.message, req.country or "ghana", req.industry or "general")
    refined = None
    ai_error = None
    # Try Groq (optional)
    if groq_client:
        try:
            refined, ai_error = generate_ai_message(draft, req.message, req.country or "ghana", req.industry or "general", req.tone or "business_coach")
        except Exception as e:
            ai_error = str(e)
    final = apply_sankofa_full_hybrid(refined if refined else draft, req.message)
    conversation = {
        "id": len(conversations) + 1,
        "user_id": req.user_id or "anonymous",
        "query": req.message,
        "response": final,
        "country": req.country or "ghana",
        "industry": req.industry or "general",
        "confidence": 0.9 if refined else 0.85,
        "created_at": int(time.time())
    }
    conversations.append(conversation)
    return ChatResponse(response=final, confidence=conversation["confidence"], conversation_id=conversation["id"], ai_error=ai_error)

@app.get("/history/{user_id}")
async def get_history(user_id: str):
    user_convs = [c for c in conversations if c["user_id"] == user_id]
    return {"conversations": user_convs}

@app.get("/ai/ask")
async def ai_ask(q: Optional[str] = "Hello from AfiYor"):
    # Quick convenience GET that runs through the same pipeline (country=ghana)
    draft = professional_afiyor.generate_professional_response(q, "ghana", "general")
    refined = None
    ai_error = None
    if groq_client:
        try:
            refined, ai_error = generate_ai_message(draft, q, "ghana", "general", "business_coach")
        except Exception as e:
            ai_error = str(e)
    final = apply_sankofa_full_hybrid(refined if refined else draft, q)
    return {"question": q, "answer": final, "ai_error": ai_error}

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": "1.0",
        "ai_status": "groq_configured" if groq_client else "groq_not_configured",
        "knowledge_base_loaded": True
    }

# ---------------- Run (only when running app.py directly) ----------------
if __name__ == "__main__":
    # When running locally you can use: uvicorn app:app --reload --port 8000
    print("Starting AfiYor FastAPI (Full Sankofa Hybrid) — honoring Afiyor Tetteh")
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, log_level="info")
