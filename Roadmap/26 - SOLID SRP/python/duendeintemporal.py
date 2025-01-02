#26 { Retos para Programadores } Principio SOLID de Responsabilidad Única (Single Responsibility Principle, SRP) 

# Bibliography reference
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
 
 """

"""  Single Responsibility Principle
A computer programming principle that states that every module, class, or
function should have responsibility over a single part of the functionality
provided by the software, and that responsibility should be entirely
encapsulated by the module, class, or function. All its services should be
narrowly aligned with that responsibility.  """

log = print
log('Retos para Programadores #26')

# Not Following the Single Responsibility Principle (SRP)

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        self.books.append({'title': title, 'author': author, 'copies': copies})

    def register_user(self, name, user_id, email):
        self.users.append({'name': name, 'id': user_id, 'email': email})

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u['id'] == user_id), None)
        book = next((b for b in self.books if b['title'] == book_title), None)

        if user and book and book['copies'] > 0:
            self.loans.append({'userId': user_id, 'bookTitle': book_title})
            book['copies'] -= 1
            log(f'Book "{book_title}" loaned to {user["name"]}')
        else:
            log("Loan failed: User or book not found, or no copies available.")

# Example usage
library = Library()
library.add_book("Learn Bash the Hard Way", "Ian Miell", 2)
library.add_book("MATLAB Notes for Professionals", "GoalKicker.com", 4)
library.register_user("Royer Rabit", "006", "happyrabbit@proton.me")
library.loan_book("006", "MATLAB Notes for Professionals")  # Book "MATLAB Notes for Professionals" loaned to Royer Rabit


import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define logging functions
def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

# Book class
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

# User class
class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.id = user_id
        self.email = email

# BookManager class
class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        self.books.append(Book(title, author, copies))
        log_info(f"Book added: {title} by {author} with {copies} copies.")

    def get_books(self):
        return self.books

    def find_book(self, title):
        return next((book for book in self.books if book.title == title), None)

    def increase_copies(self, book_title):
        book = self.find_book(book_title)
        if book:
            book.copies += 1
            log_info(f"Increased copies for book: {book_title}")

# Function to search books by partial title
def search_books_by_partial_title(books, search_term):
    return [book for book in books if search_term.lower() in book.title.lower()]

# UserManager class
class UserManager:
    def __init__(self):
        self.users = []

    def register_user(self, name, user_id, email):
        self.users.append(User(name, user_id, email))
        log_info(f"User registered: {name} with ID: {user_id}")

    def find_user(self, user_id):
        return next((user for user in self.users if user.id == user_id), None)

# LoanManager class
class LoanManager:
    def __init__(self):
        self.loans = []
        self.next_loan_id = 1

    def loan_book(self, user, book):
        if book.copies > 0:
            loan_id = self.next_loan_id
            self.loans.append({'loan_id': loan_id, 'user_id': user.id, 'book_title': book.title})
            book.copies -= 1
            log_info(f"Book \"{book.title}\" loaned to {user.name} with Loan ID: {loan_id}")
            self.next_loan_id += 1
        else:
            log_warning("Loan failed: No copies available.")

    def return_book(self, loan_id, book_manager):
        loan_index = next((index for index, loan in enumerate(self.loans) if loan['loan_id'] == loan_id), None)

        if loan_index is not None:
            loan = self.loans[loan_index]
            book = book_manager.find_book(loan['book_title'])
            if book:
                book.copies += 1
                log_info(f"Book \"{loan['book_title']}\" returned with Loan ID: {loan_id}")
            del self.loans[loan_index]
        else:
            log_error("Return failed: No loan record found for this Loan ID.")

    def get_loans_by_partial_book_title(self, search_term, user_id):
        return [loan for loan in self.loans if search_term.lower() in loan['book_title'].lower() and loan['user_id'] == user_id]

# Example usage of the library system
book_manager = BookManager()
user_manager = UserManager()
loan_manager = LoanManager()

book_manager.add_book("300 JavaScript Interview Mastery Questions Dive Deep into JavaScript Theory, Syntax, and APIs, and Interview with Confidence", "Middaugh, Jonathan", 3)
book_manager.add_book("Javascript Interview Questions and Answers", "Bandal, Pratik", 7)
book_manager.add_book("100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT...", "Aimee Mills", 2)
user_manager.register_user("Niko Zen", "008", "duendeintemporal@hotmail.com")

search_term1 = "JavaScript"
search_term2 = "Interview Questions"

search_results1 = search_books_by_partial_title(book_manager.get_books(), search_term1)
search_results2 = search_books_by_partial_title(book_manager.get_books(), search_term2)

log_info(f"Search results for '{search_term1}': {[book.title for book in search_results1]}")
log_info(f"Search results for '{search_term2}': {[book.title for book in search_results2]}")

user = user_manager.find_user("008")
book_title = search_results1[2].title if len(search_results1) > 2 else None
book = book_manager.find_book(book_title)

if book:
    loan_manager.loan_book(user, book)  # Loan the book to the user
    loans = loan_manager.get_loans_by_partial_book_title(book.title, user.id)
    if loans:
        loan_manager.return_book(loans[0]['loan_id'], book_manager)  # Return the book
else:
    log_warning("Book not found for loan.")

# Output:
    """  
2024-12-25 12:09:59,513 - INFO - Book added: 300 JavaScript Interview Mastery Questions Dive Deep into JavaScript Theory, Syntax, and APIs, and Interview with Confidence by Middaugh, Jonathan with 3 copies.
2024-12-25 12:09:59,513 - INFO - Book added: Javascript Interview Questions and Answers by Bandal, Pratik with 7 copies.
2024-12-25 12:09:59,513 - INFO - Book added: 100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT... by Aimee Mills with 2 copies.
2024-12-25 12:09:59,513 - INFO - User registered: Niko Zen with ID: 008
2024-12-25 12:09:59,514 - INFO - Search results for 'JavaScript': ['300 JavaScript Interview Mastery Questions Dive Deep into JavaScript Theory, Syntax, and APIs, and Interview with Confidence', 'Javascript Interview Questions and Answers', '100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT...']
2024-12-25 12:09:59,514 - INFO - Search results for 'Interview Questions': ['Javascript Interview Questions and Answers']
2024-12-25 12:09:59,515 - INFO - Book "100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT..." loaned to Niko Zen with Loan ID: 1
2024-12-25 12:09:59,515 - INFO - Book "100 MOST ASKED JOB READY QUESTIONS ANSWERS IN THE TECH SPACE Here are the most asked questions in PYTHON, SQL, JAVASCRIPT..." returned with Loan ID: 1
    
    """
