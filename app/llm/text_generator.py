from groq import Groq
from app.prompts.templates import PROMPTS
from app.utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_text(chunk, level):
    prompt = PROMPTS[level].replace("{text}", chunk)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content