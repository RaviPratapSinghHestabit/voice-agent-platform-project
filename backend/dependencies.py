from fastapi import Header, HTTPException
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

supabase_auth = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = authorization.split(" ")[1]

    response = supabase_auth.auth.get_user(token)

    if not response.user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return response.user