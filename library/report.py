import csv
import os
from datetime import datetime
import pandas as pd
from library.book import Book
from library.member import Member
from library.transaction import Transaction


class Report:
    """
    Generates analytical and summary reports
    from library data (books, members, transactions).
    """

    @staticmethod
    def total_summary():
        """Show overall summary of books, members, and transactions."""
        books = Book.load_books()
        members = Member.load_members()
        transactions = Transaction.load_transactions()

        total_books = len(books)
        total_members = len(members)
        total_transactions = len(transactions)
        borrowed_books = len([b for b in books if not b.available])
        returned_books = total_transactions - borrowed_books

        print("\n📊 LIBRARY SUMMARY REPORT")
        print("=" * 45)
        print(f"Total Books:            {total_books}")
        print(f"Total Members:          {total_members}")
        print(f"Total Transactions:     {total_transactions}")
        print(f"Currently Borrowed:     {borrowed_books}")
        print(f"Total Returned Books:   {returned_books}")
        print("=" * 45)

    # ------------------------------------------------------------
    @staticmethod
    def most_borrowed_books(top_n=5):
        """Show most borrowed books using pandas."""
        Transaction.initialize_csv()
        df = pd.read_csv(Transaction.DATA_FILE)

        if df.empty:
            print("⚠️ No transaction data found.")
            return

        book_counts = df['book_id'].value_counts().head(top_n)
        print(f"\n🏆 TOP {top_n} MOST BORROWED BOOKS")
        print("=" * 45)
        for book_id, count in book_counts.items():
            book = next((b for b in Book.load_books() if b.book_id == book_id), None)
            title = book.title if book else "Unknown"
            print(f"{book_id} - {title:25} | Borrowed {count} times")
        print("=" * 45)

    # ------------------------------------------------------------
    @staticmethod
    def active_members_report():
        """Show members with at least one borrowed book."""
        transactions = Transaction.load_transactions()
        active_member_ids = {t.member_id for t in transactions if t.status == "Borrowed"}

        members = Member.load_members()
        active_members = [m for m in members if m.member_id in active_member_ids]

        print("\n👥 ACTIVE MEMBERS REPORT")
        print("=" * 45)
        if not active_members:
            print("✅ No active members (no borrowed books).")
        else:
            for m in active_members:
                print(f"{m.member_id} | {m.name:20} | {m.department:15}")
        print("=" * 45)

    # ------------------------------------------------------------
    @staticmethod
    def overdue_report(days_limit=7):
        """List all overdue transactions."""
        transactions = Transaction.load_transactions()
        overdue_list = []

        for t in transactions:
            if t.status == "Borrowed":
                borrow_date = datetime.strptime(t.borrow_date, "%Y-%m-%d")
                days_passed = (datetime.now() - borrow_date).days
                if days_passed > days_limit:
                    overdue_list.append((t, days_passed))

        print(f"\n⏰ OVERDUE BOOKS (>{days_limit} days)")
        print("=" * 45)
        if not overdue_list:
            print("✅ No overdue books.")
        else:
            for t, days in overdue_list:
                member = next((m for m in Member.load_members() if m.member_id == t.member_id), None)
                book = next((b for b in Book.load_books() if b.book_id == t.book_id), None)
                member_name = member.name if member else "Unknown"
                book_title = book.title if book else "Unknown"
                print(f"{t.transaction_id} | {member_name:15} | {book_title:20} | {days} days overdue")
        print("=" * 45)

    # ------------------------------------------------------------
    @staticmethod
    def export_to_csv(output_file="data/report_summary.csv"):
        """Generate combined summary CSV for management records."""
        books = Book.load_books()
        members = Member.load_members()
        transactions = Transaction.load_transactions()

        summary_data = {
            "Total_Books": [len(books)],
            "Total_Members": [len(members)],
            "Total_Transactions": [len(transactions)],
            "Borrowed_Books": [len([b for b in books if not b.available])],
            "Returned_Books": [len([t for t in transactions if t.status == "Returned"])],
        }

        df = pd.DataFrame(summary_data)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_csv(output_file, index=False)
        print(f"📁 Summary report exported successfully to: {output_file}")
