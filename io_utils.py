import json
from models import Book, Library

def load_books(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            books = [Book(**item) for item in data]
            return Library(books)
    except FileNotFoundError:
        print("Файл не найден. Начинаем с пустой библиотеки.")
        return Library([])

def save_books(library, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([book.__dict__ for book in library.books], f, indent=4, ensure_ascii=False)