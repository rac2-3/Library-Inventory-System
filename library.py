# Name: Raj Tilak Singh
# Assignment 03 - Library Management Logic

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    # ------------------------- File Persistence -----------------------------

    def load_data(self):
        """Loads books & members from JSON files."""
        try:
            with open("books.json", "r") as f:
                for item in json.load(f):
                    self.books.append(Book(**item))
        except:
            print("No book data found, starting fresh.")

        try:
            with open("members.json", "r") as f:
                for item in json.load(f):
                    member = Member(item["name"], item["member_id"])
                    member.borrowed_books = item["borrowed_books"]
                    self.members.append(member)
        except:
            print("No member data found, starting fresh.")

    def save_data(self):
        """Saves all data back to files."""
        with open("books.json", "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

        with open("members.json", "w") as f:
            json.dump([m.to_dict() for m in self.members], f, indent=4)

    # ------------------------- Core Functions -------------------------------

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def register_member(self, name, member_id):
        self.members.append(Member(name, member_id))
        self.save_data()

    def lend_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not member or not book:
            return False

        result = member.borrow_book(book)
        self.save_data()
        return result

    def take_return(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not member or not book:
            return False

        result = member.return_book(book)
        self.save_data()
        return result

    # ----------------------- Analytics (Task 5) -----------------------------

    def total_borrowed_books(self):
        """Counts total borrowed books."""
        return sum(1 for b in self.books if not b.available)
