from models import Book
from io_utils import load_books, save_books

FILENAME = 'books.json'
library = load_books(FILENAME)

while True:
    print("\nМеню:")
    print("1) Добавить книгу")
    print("2) Удалить книгу")
    print("3) Найти книги по автору")
    print("4) Список книг за год")
    print("5) Показать все книги")
    print("6) Сохранить и выйти")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        title = input("Название: ")
        author = input("Автор: ")
        year = int(input("Год: "))
        genre = input("Жанр: ")
        library.add_book(Book(title, author, year, genre))

    elif choice == '2':
        title = input("Название книги для удаления: ")
        found = [book for book in library.books if book.title == title]
        if found:
            library.remove_book(found[0])
            print("Книга удалена.")
        else:
            print("Книга не найдена.")

    elif choice == '3':
        author = input("Имя автора: ")
        books = library.find_books_by_author(author)
        print("\n".join(map(str, books)) or "Книги не найдены.")

    elif choice == '4':
        year = int(input("Год: "))
        books = library.list_books_by_year(year)
        print("\n".join(map(str, books)) or "Книги не найдены.")

    elif choice == '5':
        print(library or "Библиотека пуста.")

    elif choice == '6':
        save_books(library, FILENAME)
        print("Сохранено. До свидания!")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")