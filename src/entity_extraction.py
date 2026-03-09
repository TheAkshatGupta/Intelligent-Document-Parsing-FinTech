import re

INVOICE_PATTERN = re.compile(r'INV-\d+')
DATE_PATTERN = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
AMOUNT_PATTERN = re.compile(r'(?:Total Amount|Amount|Total)[:\s]*([\d,]+(?:\.\d{2})?)', re.IGNORECASE)


def extract_invoice_number(text):
    match = INVOICE_PATTERN.search(text)
    return match.group() if match else None


def extract_date(text):
    match = DATE_PATTERN.search(text)
    return match.group() if match else None


def extract_amount(text):
    match = AMOUNT_PATTERN.search(text)
    return match.group(1) if match else None


def extract_entities(text):
    return {
        "invoice_number": extract_invoice_number(text),
        "date": extract_date(text),
        "amount": extract_amount(text)
    }


if __name__ == "__main__":

    sample_text = """
    Invoice Number: INV-10234
    Invoice Date: 12/01/2025
    Total Amount: 25,000
    """

    result = extract_entities(sample_text)

    print("Extracted Entities:")
    print(result)