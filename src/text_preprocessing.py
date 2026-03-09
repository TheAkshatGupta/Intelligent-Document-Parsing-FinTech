import re


def remove_extra_spaces(text):
    """Remove multiple spaces"""
    return re.sub(r"\s+", " ", text)


def normalize_colon_format(text):
    """Fix spacing around colon"""
    return re.sub(r"\s*:\s*", ": ", text)


def normalize_currency(text):
    """Ensure currency format is clean"""
    return re.sub(r"₹\s+", "₹", text)


def normalize_dates(text):
    """Standardize date format spacing"""
    return re.sub(r"\s*/\s*", "/", text)


def clean_text(text):
    """
    Main preprocessing function
    """

    # remove new lines
    text = text.replace("\n", " ")

    # remove extra spaces
    text = remove_extra_spaces(text)

    # normalize formatting
    text = normalize_colon_format(text)

    # normalize currency
    text = normalize_currency(text)

    # normalize date format
    text = normalize_dates(text)

    # convert to lowercase
    text = text.lower()

    return text.strip()


if __name__ == "__main__":

    raw_text = """
    Invoice   No : 23456

    Total Amount : ₹ 12,500
    Date : 10 / 01 / 2025
    """

    cleaned = clean_text(raw_text)

    print("Raw Text:")
    print(raw_text)

    print("\nCleaned Text:")
    print(cleaned)