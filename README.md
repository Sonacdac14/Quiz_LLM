# LLM-Powered Quiz Creator (Groq API)

An interactive chatbot that builds a quiz from user input using LLMs via the Groq API.

## 🚀 How to Run

1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with:
    ```
    GROQ_API_KEY=your_key
    GROQ_API_BASE=https://api.groq.com/openai/v1
    MODEL=mistral-7b-32768
    ```
4. Run the app:
    ```bash
    streamlit run app.py
    ```

## ✅ Features

- Interactive parameter collection
- Supports topics, difficulty, types, subtopics, keywords, language, explanations
- Output formatted clearly with questions and answers
- Uses Groq's blazing fast LLMs

## 🧠 Prompt Strategy

We use a structured prompt with role-based messaging, enforced output formatting, and optional context injection.

## 🧪 Testing

Try mock topics like:
- Python Programming
- World History
- Quantum Physics

