

'''
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.


'''
'''
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

'''

# Incorrecto 

class Library: 

    books = []
    users = []
    loans = []

    def new_book(self, author, title, n_copies):
        self.books.append({"author": author,
                            "title": title,
                            "n_copies": n_copies})

    def new_user(self, name, id, email):
        self.users.append({"name": name,
                            "id": id,
                            "email": email})

    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["n_copies"] > 0:
                self.loans.append({"user_id": user_id,
                                    "title_book": book_title})
                book["n_copies"] -=1


    def return_book(self, user_id, book_title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["title_book"] == book_title:
                self.loans.remove(loan)
                for books in self.books:
                    if books["title"] == book_title:
                        books["n_copies"] += 1
                        



my_library = Library()
my_library.new_book("Cervantes", "El quijote", 10)
my_library.new_book("Rowling", "Harry Potter", 10)
my_library.new_book("Tolkien", "El señor de los anillos", 20)

my_library.new_user("Brais", 105, "mouredev@gmail.com")
my_library.new_user("Borja", 120, "xxxxx@gmail.com")

print(my_library.books)
print(my_library.users)

my_library.loan_book(120, "Harry Potter")
print(my_library.loans)
print(my_library.books)

my_library.return_book(120, "Harry Potter")
print(my_library.books)




# Correcto 
class Book:
    def __init__(self, title, author, n_copies):
        self.title = title
        self.author = author
        self.n_copies = n_copies


class User:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

class BookLoanProcesing:
    
    def __init__(self):
        self.loans = []

    def book_borrowing(self, book, user):
        if book.n_copies > 0:
            book.n_copies -= 1
            self.loans.append({"user_id": user.id,
                                "title_book": book.title })
        else:
            print("No hay libros suficientes")

    def book_returning(self, user, book):
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["title_book"] == book.title:
                book.n_copies += 1
                self.loans.remove(loan)


class Library():
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = BookLoanProcesing()
    
    def new_book(self, book):
        self.books.append(book)
    
    def new_user(self, user):
        self.users.append(user)

    def new_loan_book(self, user_id, title_book):
        user = next((user for user in self.users if user.id == user_id), None)
        book = next((book for book in self.books if book.title == title_book), None)
        if user and book:
            return self.loans.book_borrowing(user, book)
    
    def return_book(self, user_id, title_book):
        user = next((user for user in self.user if user_id == user.id),None)
        book = next((book for book in self.books if book.title == title_book), None)
        if user and book:
            return self.loans.book_returning(user, book)



