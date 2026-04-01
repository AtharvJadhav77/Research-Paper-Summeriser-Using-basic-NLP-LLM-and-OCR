from app.extraction.pdf_extractor import extract_text
from app.extraction.image_extractor import extract_images
from app.processing.preprocessing import clean_text
from app.processing.chunking import chunk_text
from app.processing.ocr import extract_text_from_image
from app.llm.text_generator import generate_text
from app.llm.image_understanding import describe_image


def process_text(file, level):
    text = extract_text(file)
    text = clean_text(text)
    
    # To get a single cohesive summary and avoid proxies timing out, 
    # we take a large chunk of the paper (e.g., first 15,000 characters ~ 3000 words)
    # This covers the Abstract, Intro, and Methodology usually.
    limited_text = text[:15000]

    # Generate one final cohesive summary instead of gluing 20 chunks together!
    final_summary = generate_text(limited_text, level)

    return final_summary


def process_images(file):
    image_paths = extract_images(file)

    results = []

    for path in image_paths:
        ocr_text = extract_text_from_image(path)
        explanation = describe_image(ocr_text).replace("**", "").replace("__", "")

        results.append(
            f"**📷 Image Analysis:**\n\n*OCR Extracted:* {ocr_text}\n\n*Explanation:* {explanation}\n---"
        )

    if not results:
        return "No images were found in the document."
        
    return "\n\n".join(results)


def run_pipeline(file, level):
    text_output = process_text(file, level)
    image_output = process_images(file)

    return {
        "summary": text_output,
        "images": image_output
    }