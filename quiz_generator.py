import os
import requests
from dotenv import load_dotenv
from prompt_utils import build_prompt

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_BASE = os.getenv("GROQ_API_BASE")
MODEL = os.getenv("MODEL")

def generate_quiz(params):
    prompt = build_prompt(params)

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful quiz generator."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(f"{GROQ_API_BASE}/chat/completions", json=payload, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    result = response.json()
    return result["choices"][0]["message"]["content"]
