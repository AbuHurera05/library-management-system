from library.transaction import Transaction

def main():
    while True:
        print("\n" + "="*45)
        print("     LIBRARY TRANSACTION MANAGEMENT ")
        print("="*45)
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View All Transactions")
        print("4. View Overdue Books")
        print("0. Exit")
        print("="*45)

        choice = input("Enter choice (0-4): ").strip()

        if choice == "1":
            member_id = input("Enter Member ID (e.g., M001): ")
            book_id = input("Enter Book ID (e.g., B002): ")
            Transaction.borrow_book(member_id, book_id)

        elif choice == "2":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            Transaction.return_book(member_id, book_id)

        elif choice == "3":
            Transaction.view_all()

        elif choice == "4":
            Transaction.overdue_books()

        elif choice == "0":
            print("👋 Exiting Transaction Menu...")
            break

        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()
