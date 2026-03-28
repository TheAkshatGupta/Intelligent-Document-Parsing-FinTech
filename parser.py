def extract_entities(text):

    data = {
        "party_name": "",
        "invoice_id": "",
        "invoice_date": "",
        "due_date": "",
        "subtotal_amount": "",
        "tax_amount": "",
        "total_amount": "",
        "ifsc_code": ""
    }

    lines = text.split("\n")

    for line in lines:

        if "invoice no" in line.lower():
            data["invoice_id"] = line.split(":")[-1].strip()

        if "invoice date" in line.lower():
            data["invoice_date"] = line.split(":")[-1].strip()

        if "due date" in line.lower():
            data["due_date"] = line.split(":")[-1].strip()

        if "bill to" in line.lower():
            data["party_name"] = line.split(":")[-1].strip()

        if "subtotal" in line.lower():
            data["subtotal_amount"] = line.split(":")[-1].strip()

        if "gst" in line.lower():
            data["tax_amount"] = line.split(":")[-1].strip()

        if "total" in line.lower():
            data["total_amount"] = line.split(":")[-1].strip()

        if "ifsc" in line.lower():
            data["ifsc_code"] = line.split(":")[-1].strip()

    return data