"""
=================================================
   📚 LIBRARY MANAGEMENT SYSTEM (OOP + CSV)
=================================================
Modules:
 - Book Management
 - Member Management
 - Transactions (Borrow/Return)
 - Reports (Summary & Analysis)
=================================================
"""

from library.book import Book
from library.member import Member
from library.transaction import Transaction
from library.report import Report
import sys


class LibraryManager:
    """Main menu-based controller for Library System."""

    @staticmethod
    def clear_screen():
        """Clear terminal screen (cross-platform)."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pause():
        input("\nPress ENTER to continue...")

    # ---------------------------------------------------
    # MENU SYSTEM
    # ---------------------------------------------------
    @classmethod
    def main_menu(cls):
        while True:
            cls.clear_screen()
            print("=" * 50)
            print("        📘 LIBRARY MANAGEMENT SYSTEM")
            print("=" * 50)
            print("1️⃣  Manage Books")
            print("2️⃣  Manage Members")
            print("3️⃣  Transactions (Borrow / Return)")
            print("4️⃣  Reports & Analysis")
            print("5️⃣  Exit")
            print("=" * 50)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                cls.book_menu()
            elif choice == "2":
                cls.member_menu()
            elif choice == "3":
                cls.transaction_menu()
            elif choice == "4":
                cls.report_menu()
            elif choice == "5":
                print("\n👋 Exiting Library System... Goodbye!")
                sys.exit(0)
            else:
                print("⚠️ Invalid option! Try again.")
                cls.pause()

    # ---------------------------------------------------
    # BOOK MENU
    # ---------------------------------------------------
    @classmethod
    def book_menu(cls):
        while True:
            cls.clear_screen()
            print("\n=== 📚 BOOK MANAGEMENT ===")
            print("1️⃣  Add New Book")
            print("2️⃣  View All Books")
            print("3️⃣  Search Book")
            print("4️⃣  Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                genre = input("Enter genre: ")
                Book.add_book(title, author, genre)
            elif choice == "2":
                Book.display_all()
            elif choice == "3":
                keyword = input("Enter keyword to search: ")
                Book.search(keyword)
            elif choice == "4":
                break
            else:
                print("⚠️ Invalid choice!")

            cls.pause()

    # ---------------------------------------------------
    # MEMBER MENU
    # ---------------------------------------------------
    @classmethod
    def member_menu(cls):
        while True:
            cls.clear_screen()
            print("\n=== 👥 MEMBER MANAGEMENT ===")
            print("1️⃣  Register New Member")
            print("2️⃣  View All Members")
            print("3️⃣  Search Member")
            print("4️⃣  Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter member name: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                dept = input("Enter department: ")
                Member.register(name, email, phone, dept)
            elif choice == "2":
                Member.display_all()
            elif choice == "3":
                keyword = input("Enter name/email/department: ")
                Member.search(keyword)
            elif choice == "4":
                break
            else:
                print("⚠️ Invalid choice!")

            cls.pause()

    # ---------------------------------------------------
    # TRANSACTION MENU
    # ---------------------------------------------------
    @classmethod
    def transaction_menu(cls):
        while True:
            cls.clear_screen()
            print("\n=== 🔄 TRANSACTIONS ===")
            print("1️⃣  Borrow Book")
            print("2️⃣  Return Book")
            print("3️⃣  View All Transactions")
            print("4️⃣  View Overdue Books")
            print("5️⃣  Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                member_id = input("Enter Member ID: ")
                book_id = input("Enter Book ID: ")
                Transaction.borrow_book(member_id, book_id)
            elif choice == "2":
                member_id = input("Enter Member ID: ")
                book_id = input("Enter Book ID: ")
                Transaction.return_book(member_id, book_id)
            elif choice == "3":
                Transaction.view_all()
            elif choice == "4":
                days = input("Enter overdue day limit (default 7): ").strip()
                days = int(days) if days else 7
                Transaction.overdue_books(days)
            elif choice == "5":
                break
            else:
                print("⚠️ Invalid choice!")

            cls.pause()

    # ---------------------------------------------------
    # REPORT MENU
    # ---------------------------------------------------
    @classmethod
    def report_menu(cls):
        while True:
            cls.clear_screen()
            print("\n=== 📊 REPORTS & ANALYSIS ===")
            print("1️⃣  Summary Report")
            print("2️⃣  Visualization (Chart)")
            print("3️⃣  Back to Main Menu")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                Report.summary()
            elif choice == "2":
                Report.visualize()
            elif choice == "3":
                break
            else:
                print("⚠️ Invalid choice!")

            cls.pause()


# ======================================================
# ENTRY POINT
# ======================================================
if __name__ == "__main__":
    LibraryManager.main_menu()
