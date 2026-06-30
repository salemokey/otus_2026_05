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
    for user in data:
        print("\nRead user information:\n")
        for key, value in user.items():
            print (key, value)