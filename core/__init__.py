import os
import google.generativeai as genai
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Getting the Google API key from the environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Raising an error if the Google API key is not set
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Configuring the Google Generative AI with the API key
genai.configure(api_key=GOOGLE_API_KEY)
