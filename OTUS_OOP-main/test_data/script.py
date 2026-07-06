import csv_utils
import json_utils

data_json = json_utils.read_json("users.json")
data_csv = csv_utils.read_csv("books.csv")

users = [
    {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": [],
    }
    for user in data_json
]
books = [
    {
        "title": book["Title"],
        "author": book["Author"],
        "pages": book["Pages"],
        "genre": book["Genre"],
    }
    for book in data_csv
]

user_index = 0
for book in books:
    current_user = users[user_index]

    if "books" in current_user:
        current_user["books"].append(book)
    else:
        current_user["books"] = book

    user_index += 1
    if user_index >= len(users):
        user_index = 0

json_utils.write_json("result.json", users)
