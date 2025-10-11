from fastapi import APIRouter
from .. import db

router = APIRouter(prefix="/history", tags=["history"])

@router.get("/{user_id}")
async def get_history(user_id: str):
    convs = db.get_conversations_by_user(user_id)
    return {"conversations": convs}
