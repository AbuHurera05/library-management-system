from datetime import datetime, timedelta
from library.book import Book
from library.member import Member
from library.file_handler import FileHandler


class Transaction:
    """
    Manages borrowing and returning of books.
    Uses FileHandler for CSV operations.
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
        """Convert transaction object to dictionary for CSV storage."""
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
        print(
            f"[{self.__transaction_id}] Member: {self.__member_id} | "
            f"Book: {self.__book_id} | Borrowed: {self.__borrow_date} | "
            f"Returned: {self.__return_date or 'Not Returned'} | Status: {self.__status}"
        )
    @classmethod
    def view_member_borrowed(cls, member_id):
        """Display all books borrowed by a specific member."""
        from library.file_handler import FileHandler

        # Load all transactions
        transactions = FileHandler.read_csv(cls.DATA_FILE)

        # Filter transactions for the given member_id
        borrowed_books = [t for t in transactions if t.get("member_id") == member_id and t.get("return_date") == ""]

        if not borrowed_books:
            print(f"\nNo active borrowed books found for Member ID: {member_id}")
            return

        print(f"\nBooks currently borrowed by Member ID {member_id}:")
        print("-" * 60)
        for t in borrowed_books:
            print(f"Book ID: {t['book_id']} | Issue Date: {t['issue_date']} | Due Date: {t['due_date']}")
        print("-" * 60)

    # ------------------------
    # File Handling via FileHandler
    # ------------------------
    @classmethod
    def load_transactions(cls):
        """Load all transactions from CSV using FileHandler."""
        rows = FileHandler.read_csv(cls.DATA_FILE)
        transactions = []
        for row in rows:
            transactions.append(Transaction(
                row["transaction_id"],
                row["member_id"],
                row["book_id"],
                row["borrow_date"],
                row.get("return_date") or None,
                row["status"]
            ))
        return transactions

    @classmethod
    def save_transactions(cls, transactions):
        """Save all transactions (list of Transaction objects) using FileHandler."""
        data = [t.to_dict() for t in transactions]
        FileHandler.write_csv(cls.DATA_FILE, cls.FIELDNAMES, data)

    # ------------------------
    # Functional Methods
    # ------------------------
    @classmethod
    def borrow_book(cls, member_id, book_id):
        """Borrow a book if available."""
        books = Book.load_books()
        members = Member.load_members()
        transactions = cls.load_transactions()

        # Validate member
        member = next((m for m in members if m.member_id == member_id), None)
        if not member:
            print("❌ Member not found!")
            return

        # Validate book
        book = next((b for b in books if b.book_id == book_id), None)
        if not book:
            print("❌ Book not found!")
            return
        if not book.available:
            print("⚠️ Book is already borrowed.")
            return

        # Create transaction
        transaction_id = f"T{len(transactions) + 1:04d}"
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        new_transaction = Transaction(transaction_id, member_id, book_id, borrow_date)
        transactions.append(new_transaction)

        # Update book availability
        book.available = False
        Book.save_books(books)
        cls.save_transactions(transactions)

        print(f"✅ Book '{book.title}' borrowed successfully by '{member.name}' (Transaction ID: {transaction_id}).")

    @classmethod
    def return_book(cls, member_id, book_id):
        """Return a borrowed book."""
        books = Book.load_books()
        transactions = cls.load_transactions()

        # Find active transaction
        transaction = next(
            (t for t in transactions if t.member_id == member_id and t.book_id == book_id and t.status == "Borrowed"),
            None
        )
        if not transaction:
            print("⚠️ No active borrow record found for this member and book.")
            return

        # Update transaction and book status
        transaction.__return_date = datetime.now().strftime("%Y-%m-%d")
        transaction.__status = "Returned"

        book = next((b for b in books if b.book_id == book_id), None)
        if book:
            book.available = True

        # Save updates
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
        """Display overdue books (borrowed for more than N days)."""
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
            print(f"\n⚠️ Overdue Books (Borrowed more than {days_limit} days ago):")
            for t in overdue_list:
                t.display()
