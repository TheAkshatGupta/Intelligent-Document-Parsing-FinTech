import streamlit as st
from src.pipeline import run_pipeline
import os

st.set_page_config(page_title="Document Parser", layout="centered")

# TITLE
st.title("📄 Intelligent Document Parser")
st.write("Upload a document and extract structured data")

st.divider()

# FILE UPLOAD
uploaded_file = st.file_uploader("📂 Upload your document (.txt)", type=["txt"])

if uploaded_file is not None:

    file_path = "temp.txt"

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully ✅")

    # EXTRACT BUTTON
    if st.button("🚀 Extract Data", use_container_width=True):

        result = run_pipeline(file_path)

        st.subheader("📤 Extracted Data")
        st.json(result)

st.divider()

# FOOTER
st.markdown("""
<center>
<b>Created with ❤️ by Team CYBERsYNTH</b><br>
Akshat | Anushka | Nishit | Kashak
</center>
""", unsafe_allow_html=True)