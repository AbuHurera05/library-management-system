import os
from datetime import datetime
from library.file_handler import FileHandler

class Member:
    """
    Represents a library member.
    Handles registration, listing, and searching of members using CSV storage.
    """

    DATA_FILE = "data/members.csv"
    FIELDNAMES = ["member_id", "name", "email", "phone", "department", "join_date"]

    # ------------------------
    # Constructor
    # ------------------------
    def __init__(self, member_id, name, email, phone, department, join_date=None):
        self.__member_id = member_id
        self.__name = name.strip().title()
        self.__email = email.strip().lower()
        self.__phone = phone.strip()
        self.__department = department.strip().title()
        self.__join_date = join_date if join_date else datetime.now().strftime("%Y-%m-%d")

    # ------------------------
    # Encapsulation (Properties)
    # ------------------------
    @property
    def member_id(self):
        return self.__member_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def department(self):
        return self.__department

    @property
    def join_date(self):
        return self.__join_date

    # ------------------------
    # Utility Methods
    # ------------------------
    def to_dict(self):
        """Convert Member object to dictionary for CSV writing."""
        return {
            "member_id": self.__member_id,
            "name": self.__name,
            "email": self.__email,
            "phone": self.__phone,
            "department": self.__department,
            "join_date": self.__join_date
        }

    def display(self):
        """Display member details nicely."""
        print(f"[{self.__member_id}] {self.__name} | 📧 {self.__email} | "
              f"📞 {self.__phone} | 🏢 {self.__department} | Joined: {self.__join_date}")

    # ------------------------
    # CSV File Handling (via FileHandler)
    # ------------------------
    @classmethod
    def load_members(cls):
        """Load all members from CSV using FileHandler."""
        data = FileHandler.read_csv(cls.DATA_FILE, cls.FIELDNAMES)
        members = []
        for row in data:
            members.append(Member(
                row["member_id"],
                row["name"],
                row["email"],
                row["phone"],
                row["department"],
                row["join_date"]
            ))
        return members

    @classmethod
    def save_members(cls, members):
        """Save all members to CSV using FileHandler."""
        data_list = [m.to_dict() for m in members]
        FileHandler.write_csv(cls.DATA_FILE, cls.FIELDNAMES, data_list)

    # ------------------------
    # Functional Methods
    # ------------------------
    @classmethod
    def register(cls, name, email, phone, department):
        """Register a new member."""
        members = cls.load_members()

        # Check for duplicate email
        if any(m.email == email for m in members):
            print("⚠️ Member with this email already exists!")
            return

        new_id = f"M{len(members)+1:03d}"
        new_member = Member(new_id, name, email, phone, department)
        members.append(new_member)
        cls.save_members(members)
        print(f"✅ Member '{name}' registered successfully with ID {new_id}.")

    @classmethod
    def display_all(cls):
        """Display all registered members."""
        members = cls.load_members()
        if not members:
            print("👥 No members found in the library.")
        else:
            print("\n=== Library Members ===")
            for m in members:
                m.display()

    @classmethod
    def search(cls, keyword):
        """Search members by name, email, or department."""
        members = cls.load_members()
        result = [
            m for m in members
            if keyword.lower() in m.name.lower()
            or keyword.lower() in m.email.lower()
            or keyword.lower() in m.department.lower()
        ]

        if not result:
            print("⚠️ No matching members found.")
        else:
            print(f"\n🔍 Search results for '{keyword}':")
            for m in result:
                m.display()
