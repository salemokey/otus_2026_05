import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_json(filename: str):
    file_path = BASE_DIR / filename
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filename: str, data):
    file_path = BASE_DIR / filename
    with open(file_path, "w", encoding="utf-8") as f:
        return json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    data = read_json("users.json")
    print(f"Loaded {len(data)} users from JSON")
    for user in data:
        print("\nRead user information:\n")
        for key, value in user.items():
            print (key, value)
