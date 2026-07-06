import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_csv(filename: str):
    file_path = BASE_DIR / filename
    with open(file_path, "r", encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)



if __name__ == "__main__":
    data = read_csv("books.csv")
    print(f"Loaded {len(data)} users from CSV")
    for book in data:
        print("\nRead book information:\n")
        for key, value in book.items():
            print (key, value)