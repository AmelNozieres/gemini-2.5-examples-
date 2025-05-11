# 04_long_context_summary.py

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-2.5-pro")

# Load a long input from file
with open("user_feedback_dump.txt", "r") as file:
    feedback_data = file.read()

prompt = f"""
You are a product analyst reviewing user feedback.

1. Identify the top 3 recurring pain points.
2. Suggest 3 UX improvements.

Feedback data:
{feedback_data}
"""

response = model.generate_content(prompt)

print(response.text)
