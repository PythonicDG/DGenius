import os
from pyexpat.errors import messages
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def ask_llm(message, temperature = 0.7):
    completion = client.chat.completions.create(
        model = "llm-3.1-8b-instant",
        messages = messages,
        temperature = temperature)
    return completion.choices[0].message.content


    