import csv
from pathlib import Path

CSV_PATH = Path("data/load_example.csv")

def get_load_by_reference(ref_number: str):
    try:
        with CSV_PATH.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row["reference_number"].strip().upper() == ref_number.strip().upper():
                    return row
    except FileNotFoundError:
        print("CSV file not found at:", CSV_PATH)
        return None
    return None
