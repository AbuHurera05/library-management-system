## 📘 **README.md — Library Management System**

```markdown
# 📚 Library Management System (Python OOP + CSV)

A **console-based Library Management System** built in **Python** using **Object-Oriented Programming (OOP)** concepts.  
This project manages **Books**, **Members**, and **Transactions**, stores data in **CSV files**,  
and provides **automated reports and analytics** — all without any external database.

---

## 🧠 Features

✅ Object-Oriented Architecture (Encapsulation, Class Methods, etc.)  
✅ Persistent Storage using CSV Files  
✅ Book & Member Management  
✅ Borrow and Return System with Transaction History  
✅ Overdue Book Detection  
✅ Detailed Reports (Summary, Top Borrowed Books, Active Members)  
✅ Modular Code Structure with `__init__.py` for package management  

---

## 🗂️ Project Structure

```

library_management_system/
│
├── main.py
│
├── library/
│   ├── **init**.py
│   ├── book.py
│   ├── member.py
│   ├── transaction.py
│   ├── report.py
│   └── file_handler.py
│
├── data/
│   ├── books.csv
│   ├── members.csv
│   └── transactions.csv
│
└── README.md

````

---

## ⚙️ Installation & Setup

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
````

2. **Ensure Python 3.8+ is installed**:

   ```bash
   python --version
   ```

3. **Run the main program**:

   ```bash
   python main.py
   ```

---

## 🧩 Modules Overview

| Module            | Description                                              |
| ----------------- | -------------------------------------------------------- |
| `book.py`         | Manages book records (Add, Update, View, Save)           |
| `member.py`       | Handles member registration and department info          |
| `transaction.py`  | Controls book borrowing, returning, and overdue tracking |
| `report.py`       | Generates analytical and summary reports                 |
| `file_handler.py` | Provides CSV file read/write utilities                   |
| `main.py`         | User interface and system control flow                   |

---

## 🧾 Example Usage

### ▶ Borrow a Book

```
Enter Member ID: M001
Enter Book ID: B003
✅ Book 'Python Crash Course' borrowed successfully by 'Ali Khan'.
```

### ▶ Return a Book

```
Enter Member ID: M001
Enter Book ID: B003
📘 Book 'Python Crash Course' successfully returned by Member ID M001.
```

### ▶ Generate Summary Report

```
📊 LIBRARY SUMMARY REPORT
=============================================
Total Books:            50
Total Members:          25
Total Transactions:     90
Currently Borrowed:     8
Total Returned Books:   82
=============================================
```

---

## 📊 Reports Included

* **Summary Report** → Total books, members, transactions, borrowed & returned
* **Most Borrowed Books** → Top N books with borrow count
* **Active Members Report** → Members currently holding books
* **Overdue Report** → Books borrowed longer than a specified limit

---

## 🧱 Object-Oriented Concepts Used

| Concept            | Description                                    |
| ------------------ | ---------------------------------------------- |
| **Encapsulation**  | Private attributes with getter methods         |
| **Class Methods**  | Used for file-level data operations            |
| **Static Methods** | Used for utility functions                     |
| **Composition**    | `Transaction` uses `Book` and `Member` objects |
| **Polymorphism**   | Report generation with dynamic data handling   |

---

## 📈 Future Enhancements

🚀 Add GUI using **Tkinter / PyQt**
💾 Integrate with **SQLite / MySQL** for larger datasets
📊 Add Data Visualization with **Matplotlib or Pandas**
🌐 Convert to a Web App using **Flask or Django**

---

## 👨‍💻 Author

**Abu Hurera**
📧 Email: [[junejoabuhurer52@gmail.com](mailto:junejoabuhurer52@gmail.com)]
💼 GitHub: [github.com/your-username](https://github.com/AbuHurera05)

---

## 🏁 License

This project is released under the **MIT License**.
You’re free to use, modify, and distribute it with attribution.

```