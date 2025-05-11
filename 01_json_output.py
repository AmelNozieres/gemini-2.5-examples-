import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-pro")

prompt = '''
You are an assistant helping summarize customer support emails.
Return the result in this JSON format:
{
  "summary": "...",
  "sender": "...",
  "urgency": "low/medium/high"
}
Email:
Hi, I need help with my invoice, I can't find it in my portal.
'''

response = model.generate_content(
    prompt,
    generation_config={"response_mime_type": "application/json"}
)

print(response.text)
