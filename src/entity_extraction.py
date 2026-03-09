import re

INVOICE_PATTERN = re.compile(r'INV-\d+', re.IGNORECASE)
DATE_PATTERN = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}\b')
AMOUNT_PATTERN = re.compile(r'(?:Total|Amount|Amount Paid)[:\s]*₹?([\d,]+(?:\.\d{2})?)', re.IGNORECASE)


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
    Transaction Receipt

    Invoice #: INV-56789
    Date: 14-02-2025

    Amount Paid: ₹5,200
    """



    result = extract_entities(sample_text)

    print("Extracted Entities:")
    print(result)