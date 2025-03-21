import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check API key
if not GEMINI_API_KEY:
    print("❌ API key is missing!")
    exit(1)

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Test a basic request
try:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Generate a short commit message for adding a new feature")
    print("✅ Gemini API Response:", response.text)
except Exception as e:
    print(f"❌ Gemini API Error: {e}")
