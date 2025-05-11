import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

def get_order_status(order_id):
    return {"status": "shipped", "eta": "May 14"}

model = genai.GenerativeModel(
    model_name="gemini-2.5-pro",
    tools=[get_order_status]
)

chat = model.start_chat()

prompt = "Can you check where order #12567 is?"

response = chat.send_message(prompt)

print(response.text)
