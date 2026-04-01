from groq import Groq
from app.utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def describe_image(ocr_text):
    if not ocr_text.strip():
        ocr_text = "[No readable text found in this diagram by OCR.]"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"Please explain the likely purpose or meaning of a research paper diagram containing this extracted OCR text.\n\nIMPORTANT RULES:\n- Provide a direct and factual analysis of the diagram.\n- DO NOT include conversational filler.\n- DO NOT output disclaimers or apologies like 'Without more context, it is challenging...' or 'I hypothesize that...'\n- Be direct, confident, and stick strictly to the facts found in the text.\n\nOCR Text:\n{ocr_text}"
            }
        ]
    )

    return response.choices[0].message.content