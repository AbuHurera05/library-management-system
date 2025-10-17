import csv
import os
from datetime import datetime

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
        self.__year = year
        self.__available = available

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
        """Convert a Book object into a dictionary (for CSV writing)."""
        return {
            "book_id": self.__book_id,
            "title": self.__title,
            "author": self.__author,
            "genre": self.__genre,
            "year": str(self.__year),
            "available": "True" if self.__available else "False"
        }

    def display(self):
        """Display the book info neatly."""
        status = "Available ✅" if self.__available else "Borrowed ❌"
        print(f"[{self.__book_id}] {self.__title} by {self.__author} ({self.__year}) | {self.__genre} | {status}")

    # ------------------------
    # Class-Level File Operations
    # ------------------------
    @classmethod
    def initialize_csv(cls):
        """Create CSV file if not exists."""
        if not os.path.exists(cls.DATA_FILE):
            os.makedirs(os.path.dirname(cls.DATA_FILE), exist_ok=True)
            with open(cls.DATA_FILE, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=cls.FIELDNAMES)
                writer.writeheader()

    @classmethod
    def load_books(cls):
        """Load all books from CSV as a list of Book objects."""
        cls.initialize_csv()
        books = []
        with open(cls.DATA_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(Book(
                    row["book_id"],
                    row["title"],
                    row["author"],
                    row["genre"],
                    int(row["year"]),
                    row["available"].lower() == "true"
                ))
        return books

    @classmethod
    def save_books(cls, books):
        """Save all books (list of Book objects) to CSV."""
        cls.initialize_csv()
        with open(cls.DATA_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cls.FIELDNAMES)
            writer.writeheader()
            for book in books:
                writer.writerow(book.to_dict())

    # ------------------------
    # Functional Methods
    # ------------------------
    @classmethod
    def add_book(cls, title, author, genre, year):
        """Add a new book to the collection."""
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