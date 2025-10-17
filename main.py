"""
=================================================
             LIBRARY MANAGEMENT SYSTEM
=================================================
Options:
 1. Display All Books
 2. Display Available Books
 3. Display All Members
 4. Search Books
 5. Borrow a Book
 6. Return a Book
 7. View Member's Borrowed Books
 8. View Overdue Books
 9. Library Report
10. Add New Book
11. Register New Member
 0. Exit
=================================================
"""

# from library import Member, Transaction, Report
from library.book import Book
from library.member import Member
from library.transaction import Transaction
from library.report import Report
import sys
import os


def clear_screen():
    """Clear terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Pause execution until user presses Enter."""
    input("\nPress ENTER to continue...")


def main():
    """Main interactive menu system."""
    while True:
        clear_screen()
        print("=" * 55)
        print("             LIBRARY MANAGEMENT SYSTEM")
        print("=" * 55)
        print("1. Display All Books")
        print("2. Display Available Books")
        print("3. Display All Members")
        print("4. Search Books")
        print("5. Borrow a Book")
        print("6. Return a Book")
        print("7. View Member's Borrowed Books")
        print("8. View Overdue Books")
        print("9. Library Report")
        print("10. Add New Book")
        print("11. Register New Member")
        print("0. Exit")
        print("=" * 55)

        choice = input("Enter your choice (0-11): ").strip()

        # ------------------------------------------------
        # Functional Menu Logic
        # ------------------------------------------------
        if choice == "1":
            Book.display_all()

        elif choice == "2":
            Book.available_books()

        elif choice == "3":
            Member.display_all()

        elif choice == "4":
            keyword = input("Enter book title/author to search: ")
            Book.search(keyword)

        elif choice == "5":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            Transaction.borrow_book(member_id, book_id)

        elif choice == "6":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            Transaction.return_book(member_id, book_id)

        elif choice == "7":
            member_id = input("Enter Member ID: ")
            print(f"\n📘 Books borrowed by {member_id}:")
            Transaction.view_member_borrowed(member_id)

        elif choice == "8":
            days = input("Enter overdue limit (default 7): ").strip()
            days = int(days) if days else 7
            Transaction.overdue_books(days)

        elif choice == "9":
            Report.total_summary()

        elif choice == "10":
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            genre = input("Enter Genre: ")
            year = input("Enter Published Year: ")
            Book.add_book(title, author, genre, year)

        elif choice == "11":
            name = input("Enter Member Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            dept = input("Enter Department: ")
            Member.register(name, email, phone, dept)

        elif choice == "0":
            print("\n👋 Exiting Library Management System... Goodbye!")
            sys.exit(0)

        else:
            print("⚠️ Invalid choice. Please try again!")

        pause()


# ------------------------------------------------
# ENTRY POINT
# ------------------------------------------------
if __name__ == "__main__":
    main()
