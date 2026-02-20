# pipeline.py
# End-to-end pipeline (document -> clean text)

from text_extraction import extract_text_from_txt
from text_preprocessing import clean_text


def run_pipeline(file_path):
    raw_text = extract_text_from_txt(file_path)
    cleaned_text = clean_text(raw_text)
    return cleaned_text


if __name__ == "__main__":
    sample_file = "sample.txt"  # temporary
    output = run_pipeline(sample_file)
    print("CLEANED TEXT OUTPUT:\n")
    print(output)
