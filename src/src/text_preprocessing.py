# text_preprocessing.py
# Responsible for cleaning and normalizing raw extracted text

import re

def clean_text(text):
    """
    Basic text cleaning:
    - remove extra spaces
    - remove unnecessary newlines
    - normalize text
    """
    text = text.lower()
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


if __name__ == "__main__":
    sample_text = """
    Invoice No: 12345

    Total Amount:   ₹25,000
    Date: 12/01/2025
    """
    print(clean_text(sample_text))
