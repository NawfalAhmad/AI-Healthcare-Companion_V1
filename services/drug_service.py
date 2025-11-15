import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def check_drug_interactions(drug_list):
    """
    Check possible interactions among a list of drugs.
    drug_list: List[str] e.g., ["Aspirin", "Ibuprofen"]
    """
    if not drug_list:
        return "No drugs provided."

    drugs_text = ", ".join(drug_list)
    
    prompt = f"""
You are a medical AI assistant.
Analyze the following drugs and provide:
1. Any known interactions between them
2. Warnings or precautions
3. Recommendations for safe use

Drugs: {drugs_text}

Provide output in JSON format with keys: "interactions", "warnings", "recommendations".
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
