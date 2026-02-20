# text_extraction.py
# Responsible for extracting raw text from input documents

def extract_text_from_txt(file_path):
    """
    Reads text from a .txt file and returns raw text
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


if __name__ == "__main__":
    # temporary test
    sample_text = extract_text_from_txt("sample.txt")
    print(sample_text)
