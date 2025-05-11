import google.generativeai as genai
from PIL import Image

# Configure with your Gemini API key
genai.configure(api_key="YOUR_API_KEY")

# Load the image
image_path = "invoice_sample.png"
image = Image.open(image_path)

# Create a Gemini model with vision support
model = genai.GenerativeModel("gemini-2.5-pro-vision")

# Prompt for reasoning over the image
prompt = "Extract the total amount and the due date from this invoice."

# Run the model
response = model.generate_content([prompt, image])

# Print the output
print(response.text)
