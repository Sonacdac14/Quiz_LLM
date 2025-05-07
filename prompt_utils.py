def build_prompt(params):
    prompt = f"""Create a {params['difficulty']} {params['language']} quiz on the topic '{params['topic']}'.
Generate {params['num_questions']} {', '.join(params['q_types'])} questions."""

    if params["subtopics"]:
        prompt += f" Focus on subtopics: {params['subtopics']}."
    if params["keywords"]:
        prompt += f" Include context keywords: {params['keywords']}."
    if params["audience"]:
        prompt += f" Target audience: {params['audience']}."
    if params["explanations"] == "yes":
        prompt += " Include brief explanations for each answer."
    if params["max_length"] > 0:
        prompt += f" Limit each question to {params['max_length']} words."

    prompt += (
        "\n\nFormat output like this:\n\n"
        "Q: <question>\n"
        "Options: A. <text> B. <text> C. <text> D. <text>\n"
        "Answer: <correct answer>\n"
        "Explanation: <text> (if applicable)\n\n"
        "Start now:"
    )

    return prompt
