# library_manager.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"《{self.title}》 by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"✅ Book added: {new_book}")

    def show_books(self):
        if not self.books:
            print("📭 No books in the library.")
        else:
            print("📚 Books in the library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
