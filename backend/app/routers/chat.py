from fastapi import APIRouter, HTTPException
from ..schemas import ChatRequest, ChatResponse
from .. import sankofa, ai_client, db
from ..core.config import settings

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    try:
        draft = db.generate_afiyor_draft(req.message, req.country or "ghana", req.industry or "general")
        refined = None
        ai_error = None
        if ai_client.groq_client:
            try:
                refined = ai_client.generate_ai_message(draft, req.message, req.country, req.industry, tone="business_coach")
            except Exception as e:
                ai_error = str(e)
        final = sankofa.apply_sankofa_full_hybrid(refined if refined else draft, req.message)
        conv = db.save_conversation(req.user_id or "anonymous", req.message, final, req.country or "ghana", req.industry or "general")
        return ChatResponse(response=final, confidence=0.9, conversation_id=conv.id, ai_error=ai_error)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Chat processing failed")
