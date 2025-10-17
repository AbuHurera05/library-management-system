"""
====================================================
   LIBRARY MANAGEMENT SYSTEM PACKAGE INITIALIZER
====================================================
This package includes all core modules required for
the Library Management System:

Modules:
 - book.py          → Book data model & operations
 - member.py        → Member data model & operations
 - transaction.py  → Borrowing & returning logic
 - report.py        → Reports and summaries
 - file_handler.py  → File I/O operations

Usage Example:
--------------
from library import Book, Member, Transaction, Report
"""

from .book import Book
from .member import Member
from .transaction import Transaction
from .report import Report
from .file_handler import FileHandler

__all__ = ["Book", "Member", "Transaction", "Report", "FileHandler"]
