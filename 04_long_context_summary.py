import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="YOUR_API_KEY")

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-pro")

# Load long context data (user feedback)
with open("user_feedback_dump.txt", "r") as file:
    feedback_data = file.read()

# Construct the prompt
prompt = f"""
You are a product analyst reviewing user feedback.

1. Identify the top 3 recurring pain points.
2. Suggest 3 UX improvements.

Feedback data:
{feedback_data}
"""

# Generate the response
response = model.generate_content(prompt)

# Output the result
print(response.text)
