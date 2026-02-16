import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyBX87F-d2IvucPMixEjtQzHu7wggW12QXw"))

generation_config = {
    "temperature": 0.7,
    "top_p": 0.8,
    "top_k": 45,
    "max_output_tokens": 2048,
}
