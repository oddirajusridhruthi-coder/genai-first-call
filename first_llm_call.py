
from dotenv import load_dotenv
from google import genai
import os

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Check your .env file.")

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain Generative AI in simple terms in three bullet points."
)

# Display the answer
print(response.text)
