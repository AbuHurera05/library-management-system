import os
from library.file_handler import FileHandler

class Book:
    """
    Represents a single Book and provides class-level methods
    to manage the entire book collection using CSV storage.
    """

    DATA_FILE = "data/books.csv"
    FIELDNAMES = ["book_id", "title", "author", "genre", "year", "available"]

    # ------------------------
    # Constructor
    # ------------------------
    def __init__(self, book_id, title, author, genre, year, available=True):
        self.__book_id = book_id
        self.__title = title.strip().title()
        self.__author = author.strip().title()
        self.__genre = genre.strip().title()
        self.__year = int(year)
        self.__available = available if isinstance(available, bool) else str(available).lower() == "true"

    # ------------------------
    # Properties (Encapsulation)
    # ------------------------
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def genre(self):
        return self.__genre

    @property
    def year(self):
        return self.__year

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, status):
        if isinstance(status, bool):
            self.__available = status
        else:
            raise ValueError("Available status must be True or False")

    # ------------------------
    # Instance Methods
    # ------------------------
    def to_dict(self):
        """Convert Book object to dict for CSV."""
        return {
            "book_id": self.__book_id,
            "title": self.__title,
            "author": self.__author,
            "genre": self.__genre,
            "year": str(self.__year),
            "available": "True" if self.__available else "False"
        }

    def display(self):
        """Display book details."""
        status = "Available ✅" if self.__available else "Borrowed ❌"
        print(f"[{self.__book_id}] {self.__title} by {self.__author} ({self.__year}) | {self.__genre} | {status}")

    # ------------------------
    # Class-Level Operations
    # ------------------------
    @classmethod
    def load_books(cls):
        """Load all books from CSV using FileHandler."""
        data = FileHandler.read_csv(cls.DATA_FILE, cls.FIELDNAMES)
        books = []
        for row in data:
            books.append(Book(
                row["book_id"],
                row["title"],
                row["author"],
                row["genre"],
                row["year"],
                row["available"]
            ))
        return books

    @classmethod
    def save_books(cls, books):
        """Save all books to CSV using FileHandler."""
        data_list = [b.to_dict() for b in books]
        FileHandler.write_csv(cls.DATA_FILE, cls.FIELDNAMES, data_list)

    # ------------------------
    # Functional Methods
    # ------------------------
    @classmethod
    def add_book(cls, title, author, genre, year):
        """Add a new book."""
        books = cls.load_books()
        new_id = f"B{len(books)+1:03d}"
        new_book = Book(new_id, title, author, genre, year)
        books.append(new_book)
        cls.save_books(books)
        print(f"✅ Book '{title}' added successfully with ID {new_id}.")

    @classmethod
    def search(cls, keyword):
        """Search books by title or author."""
        books = cls.load_books()
        result = [b for b in books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
        if not result:
            print("⚠️ No matching books found.")
        else:
            print(f"\n🔍 Search results for '{keyword}':")
            for b in result:
                b.display()

    @classmethod
    def display_all(cls):
        """Display all books."""
        books = cls.load_books()
        if not books:
            print("📚 No books found in the library.")
        else:
            print("\n=== All Books in Library ===")
            for b in books:
                b.display()

    @classmethod
    def available_books(cls):
        """Display only available books."""
        books = [b for b in cls.load_books() if b.available]
        if not books:
            print("❌ No available books at the moment.")
        else:
            print("\n=== Available Books ===")
            for b in books:
                b.display()
