# 💳 Intelligent Document Parsing – FinTech

🚀 This project builds an **Intelligent Document Parsing system** that automatically extracts important financial information from invoice documents and converts it into structured data.

The system processes documents step-by-step using a modular pipeline.

---

## 🎯 Project Objective

Manual extraction of financial data from invoices is **time-consuming and error-prone**.

This project automates the process by extracting key entities such as:

- ✔ Invoice Number
- ✔ Invoice Date
- ✔ Total Amount

and converting them into **structured JSON output**.

---

## 🧠 System Architecture

```text
Document
   ↓
Text Extraction
   ↓
Text Preprocessing
   ↓
Entity Extraction
   ↓
JSON Output
```

Each module processes the data and passes it to the next stage.

---

## ⚙️ Technologies Used

| Technology | Purpose |
|------|------|
| 🐍 Python | Core programming language |
| 🔎 Regex | Entity extraction from invoice text |
| 🧠 Modular Pipeline | Structured processing |
| 🌐 GitHub | Version control & collaboration |

---

## 📂 Project Structure

```text
Intelligent-Document-Parsing-FinTech
│
├── data
│   └── sample invoice documents
│
├── src
│   ├── text_extraction.py
│   ├── text_preprocessing.py
│   ├── entity_extraction.py
│   └── pipeline.py
│
├── outputs
│   └── extracted JSON files
│
└── README.md
```

---

## 🔍 Module Overview

### 📄 Text Extraction

Reads the document and extracts raw text.

Example input:

```text
Invoice Number: INV-10234
Date: 12/01/2025
Total Amount: 25000
```

---

### 🧹 Text Preprocessing

Cleans and normalizes the text by:

- Removing extra spaces
- Fixing colon formatting
- Normalizing currency formatting
- Standardizing date formatting

Example output:

```text
invoice number: inv-10234 date: 12/01/2025 total amount: 25000
```

---

### 🧩 Entity Extraction

Extracts key financial entities using **regex patterns**.

Entities extracted:

- Invoice Number
- Invoice Date
- Total Amount

Example result:

```json
{
  "invoice_number": "INV-10234",
  "date": "12/01/2025",
  "amount": "25000"
}
```

---

## 🚀 Running the Pipeline

Run the pipeline using:

```bash
python src/pipeline.py
```

Expected output:

```text
FINAL EXTRACTED ENTITIES:

{
  "invoice_number": "INV-10234",
  "date": "12/01/2025",
  "amount": "25000"
}
```

---

## 👥 Team Responsibilities

| Member | Role |
|------|------|
| 👨‍💻 Akshat Gupta | Project Lead & Pipeline Integration |
| 🧠 Nishit | Entity Extraction Module |
| 📄 Anushka | Sample Financial Documents |
| 📝 Kashak | JSON Output & Documentation |

---

## 📊 Example Output

```json
{
  "invoice_number": "INV-2026-001",
  "date": "2026-01-15",
  "amount": "950.00"
}
```

---

## 🔮 Future Improvements

- 📌 Support for **PDF invoice parsing**
- 📌 Advanced **NLP-based entity extraction**
- 📌 **Streamlit UI for document upload**
- 📌 Integration with **financial systems**

---

## ⭐ Conclusion

This project demonstrates how **AI-assisted document parsing** can automate financial document processing and convert unstructured documents into structured data.