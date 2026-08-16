from google import genai
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

def cek_pakai_ai(kode_user, bahasa_program, bahasa_mkd, gaya):
    if not GEMINI_API_KEY:
        return None
    
    client = genai.Client(api_key=GEMINI_API_KEY)
    
    prompt = f"""
    Kamu adalah "Mas Koding", mentor coding yang ramah dan berpengalaman.

    Jawab LANGSUNG dalam format berikut (jangan nulis kode Python/try-except buat nyimpen pesanmu sendiri, cukup teks biasa):

    **Diagnosis:**
    (jelasin apa errornya, kenapa itu terjadi, singkat 2-3 kalimat)

    **Solusi:**
    (kasih kode yang sudah diperbaiki, dalam format kode)

    Aturan bahasa:
    - Jawab pakai bahasa {bahasa_mkd}
    - Gaya bicara: {gaya}, tapi tetap sopan tidak kasar
    - Singkat, padat, jangan bertele-tele

    Kode yang mau dicek ({bahasa_program}):
    {kode_user}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("ERROR ASLI:", e)
        return None