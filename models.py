class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: [{self.genre}]"


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def list_books_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return '\n'.join(str(book) for book in self.books)