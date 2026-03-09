import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "agents.json")


def load_agents():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_agents(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def create_agent(agent_id: str, name: str, system_prompt: str):
    data = load_agents()
    data[agent_id] = {
        "name": name,
        "system_prompt": system_prompt,
        "knowledge": ""
    }
    save_agents(data)


def add_knowledge(agent_id: str, text: str):
    data = load_agents()
    if agent_id in data:
        data[agent_id]["knowledge"] += "\n" + text
        save_agents(data)


def get_agent(agent_id: str):
    data = load_agents()
    return data.get(agent_id)