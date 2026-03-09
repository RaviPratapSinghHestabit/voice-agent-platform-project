# Voice Agent Platform

An AI-powered voice assistant platform that allows users to talk with an AI agent in real time.
The system converts speech to text, sends it to an AI model, analyzes the conversation, stores analytics, and responds back using voice.

This project demonstrates a full-stack voice AI system built with **Next.js, FastAPI, Supabase, and OpenRouter**.

---

## Features

* User authentication (register / login)
* Voice-based interaction with AI
* Speech-to-text using browser speech recognition
* AI responses using OpenRouter LLM API
* Text-to-speech AI responses
* Call analytics (duration, sentiment, quality score)
* Call history stored in Supabase
* Dashboard interface for interaction

---

## Architecture

User Voice
↓
Browser Speech Recognition
↓
Next.js Frontend
↓
FastAPI Backend
↓
LLM API (OpenRouter)
↓
Call Analysis (sentiment & quality)
↓
Supabase Database
↓
Voice Response to User

---

## Tech Stack

### Frontend

* Next.js
* TypeScript
* Tailwind CSS
* Web Speech API

### Backend

* FastAPI
* Python
* REST API

### AI

* OpenRouter LLM API

### Database & Auth

* Supabase
* PostgreSQL

---

## Project Structure

```
voice-agent-platform-project

backend/
│
├── main.py
├── dependencies.py
├── services/
│   ├── voice_service.py
│   ├── rag_service.py
│   └── history_service.py
│
├── data/
│   └── agents.json
│
└── requirements.txt


frontend/
│
├── app/
│   ├── login/
│   ├── register/
│   ├── dashboard/
│   └── voice/
│
├── lib/
│   └── supabase.ts
│
└── package.json
```

---

## Database Schema

Table: **calls**

| column          | type             |
| --------------- | ---------------- |
| id              | uuid             |
| user_id         | uuid             |
| agent_id        | text             |
| input_text      | text             |
| response        | text             |
| duration        | double precision |
| sentiment_score | double precision |
| quality_score   | double precision |
| created_at      | timestamp        |

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/voice-agent-platform-project.git
cd voice-agent-platform-project
```

---

### 2. Backend Setup

Create a virtual environment:

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create `.env` file:

```
OPENROUTER_API_KEY=your_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

Run the backend server:

```
uvicorn main:app --reload --port 8000
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

Navigate to frontend folder:

```
cd frontend
```

Install dependencies:

```
npm install
```

Create `.env.local`:

```
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

Run the development server:

```
npm run dev
```

Frontend will run at:

```
http://localhost:3000
```

---

## Voice Interaction Flow

1. User clicks **Start Talking**
2. Browser records speech
3. Speech converted to text
4. Text sent to FastAPI backend
5. Backend generates AI response
6. Conversation analyzed
7. Call stored in Supabase
8. AI response spoken back to user

---

## Example Response

```
User: Hello

AI: Hello! How can I assist you today?

Duration: 2.14 seconds
Sentiment Score: 10
Quality Score: 8
```

---

## Future Improvements

* Continuous conversation mode
* Agent creation UI
* Knowledge upload (RAG system)
* Vector embeddings for document search
* Real-time streaming responses
* Voice call analytics dashboard
* Multi-agent support

---

## Live Demo

Try the application here:

https://voice-agent-platform-project.vercel.app/

### Demo Flow

1. Register a new account
2. Login to dashboard   
3. Open Voice Agent
4. Allow microphone access
5. Start speaking with the AI agent

## Learning Goals

This project demonstrates:

* Full stack AI application architecture
* Voice interface integration
* LLM API integration
* FastAPI backend development
* Supabase authentication & database usage
* Real-time user interaction systems

---

## Author

Ravi Pratap Singh

GitHub:
https://github.com/RaviPratapSinghHestabit

---
