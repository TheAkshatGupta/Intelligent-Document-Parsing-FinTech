# pipeline.py
# End-to-end pipeline (document -> clean text)

from text_extraction import extract_text_from_txt
from text_preprocessing import clean_text
from entity_extraction import extract_entities


def run_pipeline(file_path):
    raw_text = extract_text_from_txt(file_path)
    cleaned_text = clean_text(raw_text)
    entities = extract_entities(cleaned_text)
    return  entities


if __name__ == "__main__":
    sample_file = "data/fintech_invoice1.txt"
    output = run_pipeline(sample_file)
    print("FINAL EXTRACTED ENTITIES:\n")
    print(output)
