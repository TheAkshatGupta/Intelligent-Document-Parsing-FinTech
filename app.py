import streamlit as st
from src.pipeline import run_pipeline
import os
import json

st.set_page_config(page_title="Document Parser", layout="wide")

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align: center; color: #00C9A7;'>📄 Intelligent Document Parser</h1>
<p style='text-align: center; font-size:18px;'>
Convert unstructured financial documents into structured data using a modular AI pipeline
</p>
""", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)

# ---------- LEFT SIDE ----------
with col1:
    st.subheader("📂 Upload Document")

    uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])

    if uploaded_file is not None:

        file_path = "temp.txt"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("File uploaded successfully ✅")

        if st.button("🚀 Extract Data", use_container_width=True):

            result = run_pipeline(file_path)
            st.session_state["result"] = result

# ---------- RIGHT SIDE ----------
with col2:
    st.subheader("📊 Extracted Output")

    if "result" in st.session_state:
        result = st.session_state["result"]

        st.json(result)

        # ---------- DOWNLOAD BUTTON ----------
        json_str = json.dumps(result, indent=4)
        st.download_button(
            label="📥 Download JSON",
            data=json_str,
            file_name="extracted_data.json",
            mime="application/json"
        )

        # ---------- METRICS ----------
        st.markdown("### 📈 Extraction Summary")

        colA, colB, colC = st.columns(3)

        colA.metric("Invoice", result.get("invoice_number", "N/A"))
        colB.metric("Date", result.get("date", "N/A"))
        colC.metric("Amount", result.get("amount", "N/A"))

        # ---------- STATUS ----------
        if result.get("invoice_number"):
            st.success("✅ Valid Document Parsed Successfully")
        else:
            st.warning("⚠️ Partial Extraction Detected")

        # ---------- EXPLANATION ----------
        st.markdown("""
        ### 📘 Explanation

        The system extracts key entities from the uploaded document:

        - **Invoice Number** → Unique transaction identifier  
        - **Date** → Transaction or invoice date  
        - **Amount** → Total transaction value  

        This is achieved using a rule-based extraction pipeline.
        """)

    else:
        st.info("Upload a document and click Extract to see results")

st.divider()

# ---------- FOOTER ----------
st.markdown("""
<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: rgba(0,0,0,0.85);
color: white;
text-align: center;
padding: 12px;
font-size:15px;
}
.footer a {
color: #00C9A7;
margin: 0 10px;
text-decoration: none;
}
.footer a:hover {
color: #FFD700;
}
</style>

<div class="footer">
Created with ❤️ by <b>Team CYBERsYNTH</b><br>
<a href="https://github.com/TheAkshatGupta" target="_blank">Akshat</a>
<a href="https://github.com/anushka4523" target="_blank">Anushka</a>
<a href="https://github.com/nish-debug15" target="_blank">Nishit</a>
<a href="https://github.com/kashak09" target="_blank">Kashak</a>
</div>
""", unsafe_allow_html=True)