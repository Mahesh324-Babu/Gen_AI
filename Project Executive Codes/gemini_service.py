import google.generativeai as genai
from config import generation_config

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config=generation_config
)
