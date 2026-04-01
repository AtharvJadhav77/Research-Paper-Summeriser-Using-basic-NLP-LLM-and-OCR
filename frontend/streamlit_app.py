import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.pipeline.pipeline import run_pipeline

st.title("📄 AI Academic Paper Simplifier")

uploaded_file = st.file_uploader("Upload PDF")

level = st.selectbox("Select Level", [
    "beginner", "intermediate", "expert"
])

if uploaded_file:
    with st.spinner("Processing... This might take a bit."):
        result = run_pipeline(uploaded_file, level)

    st.success("Analysis Complete!")

    tab1, tab2 = st.tabs(["📄 Final Paper Summary", "🖼️ Diagram & Image Analysis"])
    
    with tab1:
        st.write(result["summary"])
        
    with tab2:
        st.write(result["images"])