import streamlit as st
from parser import extract_entities

st.set_page_config(page_title="Document Parser", layout="centered")

st.title("📄 Intelligent Document Parser")
st.write("Convert unstructured document text into structured JSON")

st.divider()

text = st.text_area("📥 Paste your document text here")

if st.button("🚀 Extract Data"):

    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        result = extract_entities(text)

        st.success("Extraction Complete ✅")
        st.json(result)