# explanation.py
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_explanation(user_input: str) -> str:
    """
    Generate a short explanation for the user input using Gemini.
    Compatible with google-genai v1.56.0.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        return response.text
    except Exception as e:
        return f"Error generating explanation: {e}"
