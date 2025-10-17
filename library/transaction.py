import csv
import os
from datetime import datetime, timedelta
from library.book import Book
from library.member import Member

class Transaction:
    """
    Manages borrowing and returning of books.
    Stores all records in transactions.csv.
    """

    DATA_FILE = "data/transactions.csv"
    FIELDNAMES = ["transaction_id", "member_id", "book_id", "borrow_date", "return_date", "status"]

    # ------------------------
    # Constructor
    # ------------------------
    def __init__(self, transaction_id, member_id, book_id, borrow_date, return_date=None, status="Borrowed"):
        self.__transaction_id = transaction_id
        self.__member_id = member_id
        self.__book_id = book_id
        self.__borrow_date = borrow_date
        self.__return_date = return_date
        self.__status = status

    # ------------------------
    # Encapsulation (Properties)
    # ------------------------
    @property
    def transaction_id(self):
        return self.__transaction_id

    @property
    def member_id(self):
        return self.__member_id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def return_date(self):
        return self.__return_date

    @property
    def status(self):
        return self.__status

    # ------------------------
    # Utility Methods
    # ------------------------
    def to_dict(self):
        """Convert object to dict for CSV writing."""
        return {
            "transaction_id": self.__transaction_id,
            "member_id": self.__member_id,
            "book_id": self.__book_id,
            "borrow_date": self.__borrow_date,
            "return_date": self.__return_date if self.__return_date else "",
            "status": self.__status
        }

    def display(self):
        """Display transaction details."""
        print(f"[{self.__transaction_id}] Member: {self.__member_id} | Book: {self.__book_id} | "
              f"Borrowed: {self.__borrow_date} | Returned: {self.__return_date or 'Not Returned'} | "
              f"Status: {self.__status}")

    # ------------------------
    # File Handling
    # ------------------------
    @classmethod
    def initialize_csv(cls):
        """Create CSV if not exists."""
        if not os.path.exists(cls.DATA_FILE):
            os.makedirs(os.path.dirname(cls.DATA_FILE), exist_ok=True)
            with open(cls.DATA_FILE, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=cls.FIELDNAMES)
                writer.writeheader()

    @classmethod
    def load_transactions(cls):
        """Load all transactions."""
        cls.initialize_csv()
        transactions = []
        with open(cls.DATA_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(Transaction(
                    row["transaction_id"],
                    row["member_id"],
                    row["book_id"],
                    row["borrow_date"],
                    row["return_date"] or None,
                    row["status"]
                ))
        return transactions

    @classmethod
    def save_transactions(cls, transactions):
        """Save list of Transaction objects to CSV."""
        cls.initialize_csv()
        with open(cls.DATA_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=cls.FIELDNAMES)
            writer.writeheader()
            for t in transactions:
                writer.writerow(t.to_dict())

    # ------------------------
    # Functional Methods
    # ------------------------
    @classmethod
    def borrow_book(cls, member_id, book_id):
        """Borrow a book if available."""
        # Load data
        books = Book.load_books()
        members = Member.load_members()
        transactions = cls.load_transactions()

        # Check member exists
        member = next((m for m in members if m.member_id == member_id), None)
        if not member:
            print("❌ Member not found!")
            return

        # Check book exists and is available
        book = next((b for b in books if b.book_id == book_id), None)
        if not book:
            print("❌ Book not found!")
            return
        if not book.available:
            print("⚠️ Book is already borrowed.")
            return

        # Borrow book
        transaction_id = f"T{len(transactions)+1:04d}"
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        new_transaction = Transaction(transaction_id, member_id, book_id, borrow_date)
        transactions.append(new_transaction)

        # Update book availability
        book.available = False
        Book.save_books(books)
        cls.save_transactions(transactions)

        print(f"✅ Book '{book.title}' borrowed successfully by Member '{member.name}' (Transaction ID: {transaction_id}).")

    @classmethod
    def return_book(cls, member_id, book_id):
        """Return a borrowed book."""
        books = Book.load_books()
        transactions = cls.load_transactions()

        # Find matching transaction
        transaction = next(
            (t for t in transactions if t.member_id == member_id and t.book_id == book_id and t.status == "Borrowed"),
            None
        )
        if not transaction:
            print("⚠️ No active borrow found for this member and book.")
            return

        # Update transaction
        transaction.__return_date = datetime.now().strftime("%Y-%m-%d")
        transaction.__status = "Returned"

        # Update book availability
        book = next((b for b in books if b.book_id == book_id), None)
        if book:
            book.available = True

        # Save data
        cls.save_transactions(transactions)
        Book.save_books(books)
        print(f"📘 Book '{book.title}' successfully returned by Member ID {member_id}.")

    @classmethod
    def view_all(cls):
        """Display all transaction records."""
        transactions = cls.load_transactions()
        if not transactions:
            print("🕮 No transactions found.")
        else:
            print("\n=== All Transactions ===")
            for t in transactions:
                t.display()

    @classmethod
    def overdue_books(cls, days_limit=7):
        """Show all overdue books (borrowed more than N days ago)."""
        transactions = cls.load_transactions()
        overdue_list = []

        for t in transactions:
            if t.status == "Borrowed":
                borrow_date = datetime.strptime(t.borrow_date, "%Y-%m-%d")
                if datetime.now() - borrow_date > timedelta(days=days_limit):
                    overdue_list.append(t)

        if not overdue_list:
            print("✅ No overdue books.")
        else:
            print("\n⚠️ Overdue Books (Borrowed more than 7 days ago):")
            for t in overdue_list:
                t.display()
