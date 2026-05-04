def get_prompt(mode, text):
    if mode == "1":
        return f"""
You are an expert AI tutor.

Explain the topic in simple terms for a beginner.

Rules:
- Use bullet points
- Give 1 real-life example
- Keep it under 10 lines

Topic: {text}
"""

    elif mode == "2":
        return f"""
Summarize the following content into key points.

Rules:
- Use bullet points
- Keep it short and clear
- Remove unnecessary details

Content: {text}
"""

    elif mode == "3":
        return f"""
Generate 5 multiple choice questions (MCQs) from the topic.

Format:
Q1...
A) ...
B) ...
C) ...
D) ...
Answer: ...

Topic: {text}
"""