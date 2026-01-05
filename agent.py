import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Tu es un assistant professionnel d’aide à la gestion documentaire hygiène
destiné au secteur agroalimentaire.
Tu aides à analyser, comprendre et améliorer les documents.
Tu ne fais aucune validation réglementaire officielle.
"""

def analyze_document(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content
