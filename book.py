# Name: Raj Tilak Singh
# Date: 20-11-2025
# Assignment 03 - Book Class

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        """Marks the book as not available."""
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        """Marks the book as available again."""
        self.available = True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }
