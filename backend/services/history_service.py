from services.supabase_client import supabase
from datetime import datetime


def save_call(
    user_id: str,
    agent_id: str,
    user_text: str,
    ai_response: str,
    duration: float,
    sentiment: int,
    quality: int
):
    supabase.table("calls").insert({
        "user_id": user_id,
        "agent_id": agent_id,
        "input_text": user_text,
        "response": ai_response,
        "duration": duration,
        "sentiment": sentiment,
        "quality": quality,
        "created_at": datetime.utcnow().isoformat()
    }).execute()


def get_user_calls(user_id: str):
    response = (
        supabase.table("calls")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )

    return response.data