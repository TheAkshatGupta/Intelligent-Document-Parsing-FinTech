🏦 Intelligent Document Parsing System

An end-to-end rule-based document parsing system that extracts structured information from unstructured financial documents.

This project uses a modular pipeline architecture to process documents and convert them into structured JSON output.

---

🌐 Live Demo

https://intelligent-document-parsing-fintech.streamlit.app/

---

📌 Project Overview

This system processes financial documents such as invoices and transaction records by extracting key entities like invoice number, date, and transaction amount.

The pipeline follows a structured approach:

Document File → Text Extraction → Text Cleaning → Entity Extraction → JSON Output

---

⚙️ Features

- 📂 File-based document parsing
- 🧠 Rule-based entity extraction using Regex
- 🔄 Modular pipeline architecture
- 📊 Structured JSON output
- 🌐 Interactive UI using Streamlit
- 🚀 Live deployment

---

🧠 System Architecture

User Upload (.txt)
        ↓
Text Extraction
        ↓
Text Preprocessing
        ↓
Entity Extraction (Regex)
        ↓
Structured JSON Output

---

📊 Extracted Entities

- Invoice Number
- Date
- Transaction Amount

---

🛠 Tech Stack

- Python
- Streamlit
- Regular Expressions (Regex)
- Modular Pipeline Design

---

📁 Project Structure

Intelligent-Document-Parsing-FinTech
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── pipeline.py
    ├── entity_extraction.py
    ├── text_preprocessing.py
    ├── text_extraction.py

---

▶️ How to Run Locally

Clone the repository

git clone https://github.com/TheAkshatGupta/Intelligent-Document-Parsing-FinTech

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

---

👨‍💻 Team CYBERsYNTH

- Akshat Gupta
- Anushka
- Nishit
- Kashak

---

🚀 Future Enhancements

- 📄 PDF document parsing
- 🧠 ML-based Named Entity Recognition (NER)
- 📊 Validation rules for extracted data
- 📥 Download extracted JSON
- 🌐 API integration (FastAPI)

---

📜 License

This project is developed for educational and research purposes.
