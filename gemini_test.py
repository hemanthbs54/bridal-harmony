import os
from dotenv import load_dotenv
from google import genai  # Correct import for the current GenAI SDK

# Load environment variables from .env
load_dotenv()

# Ensure the API key is set in .env like:
# GEMINI_API_KEY=your_real_api_key_here
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create the Gemini client
client = genai.Client(api_key=api_key)

# Call the Gemini API for simple text generation
response = client.models.generate_content(
    model="gemini-2.5-flash",                  # A valid Gemini model
    contents="Hello Gemini! Tell me a one-line introduction."
)

# Print the generated text
print("Gemini response:", response.text)
