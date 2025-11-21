# Name: Raj Tilak Singh
# Assignment 03 - Main Program

from library import Library

def main():
    lib = Library()
    print("\n=== Welcome to the Library Inventory System ===\n")

    while True:
        print("""
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. Library Report
6. Exit
""")

        choice = input("Enter option: ")

        if choice == "1":
            t = input("Book Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            lib.add_book(t, a, i)
            print("Book added successfully.\n")

        elif choice == "2":
            n = input("Member Name: ")
            mid = input("Member ID: ")
            lib.register_member(n, mid)
            print("Member registered.\n")

        elif choice == "3":
            mid = input("Member ID: ")
            isbn = input("Book ISBN: ")
            if lib.lend_book(mid, isbn):
                print("Book issued!\n")
            else:
                print("Issue failed. Book unavailable or ID wrong.\n")

        elif choice == "4":
            mid = input("Member ID: ")
            isbn = input("Book ISBN: ")
            if lib.take_return(mid, isbn):
                print("Book returned!\n")
            else:
                print("Return failed.\n")

        elif choice == "5":
            print("\n--- Library Report ---")
            print(f"Total Borrowed Books: {lib.total_borrowed_books()}\n")

        elif choice == "6":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
