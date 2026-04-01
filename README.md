# 📄 AI Academic Paper Simplifier

A multi-modal NLP web application built with Streamlit and Groq to extract, process, and summarize complex research papers directly from their raw PDF form.

## Features
- **PDF Parsing:** Automatically chunks academic papers and identifies relevant figures.
- **Image OCR:** Leverages PyTesseract to extract raw technical data embedded inside charts and diagrams.
- **LLM Summary:** Seamlessly integrates with Groq's high-speed open-source endpoints (`llama-3.3-70b-versatile`) to map complex academics into cohesive, understandable insights.

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file and insert your API credentials:
```env
GROQ_API_KEY=your_key_here
```
4. Verify you have [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) installed on Windows and modify the PATH in `app/processing/ocr.py`.

## Usage
```bash
streamlit run frontend/streamlit_app.py
```
