# Library Inventory System  
### Assignment 03 – Programming for Problem Solving Using Python  
**Author:** Raj Tilak Singh  
**Course:** MCA (AI & ML) – Semester I  
**Subject Code:** ETCCPP171  

---

##  Project Overview
This project is a simple **Library Inventory System** built using **Object-Oriented Programming in Python**.  
It allows adding books, registering members, issuing and returning books, and generating a small report.  
It also includes **file persistence**, so the data is saved even after the program closes.

The project fulfills all requirements mentioned in **Assignment 03**.

---

##  Project Structure
library_system/

│── book.py

│── member.py

│── library.py
│── main.py
│── books.json (auto-generated)
│── members.json (auto-generated)
│── README.md

---

##  Features Implemented

###  Book Management
- Add new books  
- Borrow/Return handling  
- Track availability  

###  Member Management
- Register members  
- Track borrowed books per member  

###  Library Operations
- Issue a book  
- Accept return  
- Store all data in `.json` files  

###  Persistence (File Storage)
- Uses JSON for saving/loading books & members  
- Runs even if file is missing (handled by try-except)

###  Analytics Report
- Total number of borrowed books  
- Displayed cleanly using formatted output  

###  Bonus (Interactive Menu)
A looped menu in `main.py` allows:

1. Add Book

2. Register Member

3. Borrow Book

4. Return Book

5. Library Report

6. Exit


---

##  How to Run the Program

1. Open terminal inside the `library_system/` folder  
2. Run the program:


3. Choose any option from the menu  
4. JSON files will be auto-created on first run

---

##  Screenshots Required (as per assignment)

You should include at least 3–5 screenshots:

1. Program Start (Menu display)  
2. Add Book  
3. Register Member  
4. Borrow Book  
5. Library Report  

(Optional)  
6. Return Book  
7. JSON data files  

---

##  Academic Integrity Note
This project is written originally for the assignment and follows OOP principles, clean formatting, meaningful variable names, and proper indentation.

---

##  End of README



