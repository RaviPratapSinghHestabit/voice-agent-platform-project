from fastapi import APIRouter, Depends
from dependencies import get_current_user
from backend.services.supabase_client import supabase

router = APIRouter()

@router.post("/agents")
def create_agent(data: dict, user=Depends(get_current_user)):
    response = supabase.table("agents").insert({
        "user_id": user.id,
        "name": data["name"],
        "description": data["description"],
        "system_prompt": data["system_prompt"]
    }).execute()

    return response.data


@router.get("/agents")
def get_agents(user=Depends(get_current_user)):
    response = supabase.table("agents") \
        .select("*") \
        .eq("user_id", user.id) \
        .execute()

    return response.data