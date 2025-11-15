import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def predict_symptoms(symptoms_text: str):
    """
    Predict possible medical conditions or severity from user symptoms.
    """
    if not symptoms_text.strip():
        return "No symptoms provided."

    prompt = f"""
You are a medical AI assistant.
Analyze the following patient symptoms and provide:
1. Possible conditions
2. Severity level (mild, moderate, severe)
3. Any urgent warning signs

Symptoms: {symptoms_text}
Provide output in JSON format with keys: "conditions", "severity", "warnings".
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
