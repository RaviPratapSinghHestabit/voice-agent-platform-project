import os
import requests
from dotenv import load_dotenv
from services.rag_service import get_agent
import json
from datetime import datetime

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_MODEL = "meta-llama/llama-3-8b-instruct"  


def generate_ai_response(prompt: str, agent_id: str = "default"):

    agent = get_agent(agent_id)

    system_prompt = "You are a helpful AI assistant."
    knowledge_context = ""

    if agent:
        system_prompt = agent["system_prompt"]
        knowledge_context = agent["knowledge"]

    full_prompt = f"""
Use the following knowledge base to answer the question.
If the answer is not in the knowledge base, say you don't know.

Knowledge Base:
{knowledge_context}

User Question:
{prompt}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            "max_tokens": 120
        }
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]


def analyze_call(user_text: str, ai_response: str):

    analysis_prompt = f"""
Rate the following conversation:

User: {user_text}
AI: {ai_response}

Return strictly in this format:
Sentiment: <1-10>
Quality: <1-10>
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "system", "content": "You evaluate AI conversations."},
                {"role": "user", "content": analysis_prompt}
            ],
            "max_tokens": 50
        }
    )

    data = response.json()
    text = data["choices"][0]["message"]["content"]

    sentiment = 5
    quality = 5

    try:
        lines = text.split("\n")
        for line in lines:
            if "Sentiment" in line:
                sentiment = int(line.split(":")[1].strip())
            if "Quality" in line:
                quality = int(line.split(":")[1].strip())
    except:
        pass

    return sentiment, quality

