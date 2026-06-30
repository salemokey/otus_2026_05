import csv_utils
import json_utils

data_json = json_utils.read_json("users.json")
data_csv = csv_utils.read_csv("books.csv")

users = [user["name"] for user in data_json]
books = [book["Title"] for book in data_csv]

result_list = []

for name in users:
    result_list += [{'Name': name}]

name_index = 0
for book in books:
    current_user = result_list[name_index]

    if 'Books' in current_user:
        current_user['Books'] += ', ' + book
    else:
        current_user['Books'] = book

    name_index += 1
    if name_index >= len(users):
        name_index = 0

json_utils.write_json("result.json", result_list)