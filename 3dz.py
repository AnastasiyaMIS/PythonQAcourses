import\
    csv
import json

data = {}

with open('books-39204-271043.csv', 'r') as f:
    books = [book for book in csv.DictReader(f)]
with open('users.json.py', 'r') as f:
    user_list = json.load(f)
print(user_list)

# достать нужные теги и сунуть нужные теги в финальную схему

result = []

for value in user_list:
    d = {
        'name': value.get('name'),
        'gender': value.get('gender'),
        'address': value.get('address'),
        'books': [],
    }
    if len(books) > 0:
        book = books.pop(0)
        d['books'].append(dict(title=book.get('Title'), author=book.get('Author'), height=book.get('Height')))

    result.append(d)

#кидаем в финальный файл
print(result)
with open('End.json.py', 'w') as f:
    json.dump(result, f, indent=4)

