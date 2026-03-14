import streamlit as st

from src.text_preprocessing import clean_text
from src.entity_extraction import extract_entities


st.title("Intelligent Document Parsing - FinTech")

st.write("Upload a document or paste text to extract entities.")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

text_input = st.text_area("Or paste document text here")

text = ""

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

elif text_input:
    text = text_input


if st.button("Run Extraction"):

    if not text:
        st.warning("Please upload or enter text.")
    else:
        st.subheader("Original Text")
        st.write(text)

        cleaned_text = clean_text(text)

        st.subheader("Cleaned Text")
        st.write(cleaned_text)

        entities = extract_entities(cleaned_text)

        st.subheader("Extracted Entities")
        st.json(entities)