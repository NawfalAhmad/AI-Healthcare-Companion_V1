import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_medical_text(text):
    """
    Summarize a medical document or text.
    """
    if not text.strip():
        return "No text provided."

    prompt = f"""
You are a medical AI assistant.
Summarize the following medical text into a concise, easy-to-understand summary.
Keep the medical accuracy intact.

Text: {text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    answer = response['choices'][0]['message']['content']
    return answer
