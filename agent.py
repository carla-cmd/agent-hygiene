import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))

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
