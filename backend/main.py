from fastapi import FastAPI, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

from services.voice_service import generate_ai_response, analyze_call
from services.rag_service import create_agent, add_knowledge
from services.history_service import save_call, get_user_calls
from dependencies import get_current_user


app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://voice-agent-platform-project.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AgentCreate(BaseModel):
    agent_id: str
    name: str
    system_prompt: str


class KnowledgeUpload(BaseModel):
    agent_id: str
    content: str


class VoiceRequest(BaseModel):
    input_text: str
    agent_id: str = "default"


@app.get("/")
def root():
    return {"status": "Voice backend running"}


@app.post("/create-agent")
def create_agent_api(agent: AgentCreate, user=Depends(get_current_user)):

    print("Creating agent:", agent.agent_id)

    create_agent(agent.agent_id, agent.name, agent.system_prompt)

    return {"message": "Agent created successfully"}


@app.post("/add-knowledge")
def add_knowledge_api(data: KnowledgeUpload):

    print("Adding knowledge to agent:", data.agent_id)

    add_knowledge(data.agent_id, data.content)

    return {"message": "Knowledge added"}


@app.post("/test-voice")
def test_voice(data: VoiceRequest, user=Depends(get_current_user)):

    try:

        print("Voice request received:", data.input_text)

        start_time = time.time()

        response = generate_ai_response(data.input_text, data.agent_id)

        end_time = time.time()
        duration = round(end_time - start_time, 2)

        sentiment, quality = analyze_call(data.input_text, response)

        save_call(
            user.id,
            data.agent_id,
            data.input_text,
            response,
            duration,
            sentiment,
            quality
        )

        return {
            "response": response,
            "duration_seconds": duration,
            "sentiment_score": sentiment,
            "quality_score": quality
        }

    except Exception as e:

        print("ERROR IN /test-voice:", str(e))

        return {
            "error": str(e)
        }


@app.get("/calls")
def get_calls(user=Depends(get_current_user)):

    print("Fetching calls for user:", user.id)

    return get_user_calls(user.id)


@app.post("/start-call")
async def start_call(authorization: str = Header(None)):

    if not authorization:
        return {"message": "Unauthorized"}

    token = authorization.split(" ")[1]

    print("User JWT:", token)

    return {"message": "Voice call started"}


@app.get("/voice")
def voice():
    return {"response": "Voice agent connected successfully"}