import os
from openai import OpenAI
from dotenv import load_dotenv
from config import PROMPT, MAX_DLUGOSC_DIFFA

load_dotenv()

klient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generuj_release_notes(lista_zmian):
    tekst_commitow = ""
    for zmiana in lista_zmian:
        tekst_commitow += f"- [{zmiana['hash']}] {zmiana['wiadomosc']}\n"
        if zmiana["diff"]:
            tekst_commitow += f"  Zmiany: {zmiana['diff'][:MAX_DLUGOSC_DIFFA]}\n"

    odpowiedz = klient.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.3,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": f"Oto lista commitow:\n{tekst_commitow}"}
        ]
    )
    return odpowiedz.choices[0].message.content