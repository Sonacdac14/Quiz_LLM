import streamlit as st
from quiz_generator import generate_quiz

st.set_page_config(page_title="LLM Quiz Generator", layout="wide")
st.title("📚 LLM-Powered Quiz Creator (Groq)")

with st.form("quiz_form"):
    topic = st.text_input("Topic", "Quantum Physics")
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
    num_questions = st.number_input("Number of Questions", 1, 20, 5)
    q_types = st.multiselect("Question Types", ["multiple choice", "short answer", "true/false"], default=["multiple choice"])
    subtopics = st.text_input("Subtopics (optional)")
    keywords = st.text_input("Context Keywords (optional)")
    audience = st.text_input("Target Audience (optional)")
    language = st.text_input("Language", "en")
    explanations = st.radio("Include Explanations?", ["yes", "no"])
    max_length = st.number_input("Max Length per Question (optional)", 0, 500, 0)

    submitted = st.form_submit_button("Generate Quiz")

if submitted:
    with st.spinner("Generating quiz..."):
        params = {
            "topic": topic,
            "difficulty": difficulty,
            "num_questions": num_questions,
            "q_types": q_types,
            "subtopics": subtopics,
            "keywords": keywords,
            "audience": audience,
            "language": language,
            "explanations": explanations,
            "max_length": max_length,
        }

        quiz_output = generate_quiz(params)
        st.markdown("### ✏️ Quiz Output")
        st.markdown(quiz_output)
