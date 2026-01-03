import json
import zipfile
import os

ZIP_PATH = "data/drug-label-0001-of-0013.json.zip"
OUTPUT_JSON = "data/processed_labels.json"

def clean_text(lst):
    return " ".join(x.strip() for x in lst if x.strip()) if lst else ""

def get_drug_name(record):
    fda = record.get("openfda", {})
    return (
        fda.get("generic_name", [None])[0]
        or fda.get("brand_name", ["unknown"])[0]
    ).lower()

def process_labels():
    os.makedirs("data/extracted", exist_ok=True)
    documents = []

    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall("data/extracted")

    for file in os.listdir("data/extracted"):
        if not file.endswith(".json"):
            continue

        with open(f"data/extracted/{file}", "r", encoding="utf-8") as f:
            data = json.load(f)

        for r in data.get("results", []):
            drug = get_drug_name(r)
            sections = {
                "dosage": clean_text(r.get("dosage_and_administration")),
                "warnings": clean_text(r.get("warnings")),
                "contraindications": clean_text(r.get("contraindications")),
                "pregnancy": clean_text(r.get("pregnancy")),
                "interactions": clean_text(r.get("drug_interactions")),
            }

            for sec, text in sections.items():
                if text:
                    documents.append({
                        "drug": drug,
                        "section": sec,
                        "text": text
                    })

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print(f"Processed {len(documents)} documents")