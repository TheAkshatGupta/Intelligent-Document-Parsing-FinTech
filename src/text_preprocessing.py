import re

def clean_text(text):

    # remove new lines
    text = text.replace("\n", " ")

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # normalize colon formatting
    text = re.sub(r"\s*:\s*", ": ", text)

    # convert to lowercase
    text = text.lower()

    return text.strip()


if __name__ == "__main__":

    raw_text = """
    Invoice   No : 23456
    Total Amount : ₹12,500
    Date : 10/01/2025
    """

    cleaned_text = clean_text(raw_text)

    print("Cleaned Text:")
    print(cleaned_text)