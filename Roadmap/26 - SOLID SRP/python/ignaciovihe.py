"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""


#Esta clase no cumple SRP (Single Responsibility Principle)
#La clase tiene 3 responsabilidades:
    #Contener los datos del estudiante
    #Registrar un estudiante
    #Enviar email de bienvenida.
# Si se necesita modificar cualquiera de las tres hay que modificar la misma clase
# lo que podría romper todo
class Student:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def register_student(self):
        print(f"Registrando el estudiante {self.name} en la base de datos.") #Simulamos el registro en la base de datos.

    def send_email(self):
        print(f"Enviando email de bienbenida a {self.email}") # simulamos el envio de correo.

student = Student("Pedro", "pedro@email.com")
student.register_student()
student.send_email()


# Mismo caso cumpliendo SRP.
# Separamos resposabilidades. De esta forma si tenemos que modificar alguna solo tocamos esa parte.

class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class RegisterService:
    def register_DDBB(self, student: Student):
        print(f"Registrando el estudiante {student.name} en la base de datos.") #Simulamos el registro en la base de datos.

class EmailService:
    def send_email(self, student: Student):
        print(f"Enviando email de bienbenida a {student.email}") # simulamos el envio de correo.

student = Student("Ignacio", "ignacio@email.com")

register = RegisterService()
register.register_DDBB(student)

sender = EmailService()
sender.send_email(student)


"""
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
# No cumple SRP
class Library:

    def __init__(self):
        self.books = {}
        self.users = {}
        self.book_loans = {}

    def register_book(self, title: str, writer: str, copies_available: int):
        if title not in self.books:
            self.books[title] = {"writer": writer, "copies_available": copies_available}
        else:
            print(f" El libro {title} ya esta registrado.")

    def register_user(self, name, email):
        self.users[len(self.users)] = {"name": name, "email": email}

    def borrowBook(self, title, user_id):
        if title in self.books and user_id in self.users:
            if self.books[title]["copies_available"] > 0:
                if user_id not in self.book_loans:
                    self.book_loans[user_id] = [title]
                    self.books[title]["copies_available"] -= 1
                else:
                    if title not in self.book_loans[user_id]:
                        self.book_loans[user_id].append(title)
                        self.books[title]["copies_available"] -= 1
                    else:
                        print(f"El usuario {user_id} ya tiene prestado el libro {title}")
            else:
                print(f"El libro {title} no esta disponible temporalmente.")
        else:
            print(F"El libro no esta disponible en la biblioteca o usuario no registrado")

    def return_book(self, title, user_id):
        if user_id in self.book_loans:
            if title in self.book_loans[user_id]:
                self.book_loans[user_id].remove(title)
                self.books[title]["copies_available"] += 1
            else:
                print(f"El usuario con id {user_id} no tiene prestado el libro {title}")
        else:
            print(f"Id usuario incorrecto")



my_library = Library()
my_library.register_book("La comunidad del anillo", "JRR Tolkien", 3)
my_library.register_user("Pedro","pedro@email.com")
my_library.register_book("Las dos Torres", "JRR Tolkien", 2)
my_library.register_user("Ignacio","ignacio@email.com")
my_library.register_user("Lore","lore@email.com")
my_library.register_user("Jaun","juan@email.com")
my_library.borrowBook("La comunidad del anillo", 1)
my_library.borrowBook("Las dos Torres", 0)
my_library.borrowBook("La comunidad del anillo", 0)
my_library.borrowBook("La comunidad del anillo", 0)
my_library.borrowBook("La comunidad del anillo", 2)
my_library.borrowBook("La comunidad del anillo", 3)
my_library.borrowBook("Las dos Torres", 3)
print(my_library.books)
print(my_library.users)
print(my_library.book_loans)

my_library.return_book("La comunidad del anillo", 1)
my_library.borrowBook("La comunidad del anillo", 3)
print(my_library.books)
print(my_library.users)
print(my_library.book_loans)


# Cumple SRP

class Book: #Contiene la info de un libro y modifica su número de copias.

    def __init__(self, title: str, writer: str, copies: int):
        self.title = title
        self.writer = writer
        self.copies = copies
    
    def increment_copies(self):
        self.copies += 1

    def decrement_copies(self):
        self.copies -= 1



class User: #Contiene la info de un usuario creando su identificador automaticamente.

    index = 1
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.user_id = User.index
        User.index += 1



class Loan: # Contiene la info de un prestamo uniendo un libro con un usuario.

    def __init__(self, user: User, book: Book):
        self.user = user
        self.book = book



class Library:  # Contiene la info de libros usuarios y prestamos. Se podria ser mas estricto separando el registro
                # de usuarios y libros en otras clases UserManager y BookManager, pero es aceptable.
    def __init__(self):
        self.books = {}
        self.users = {}
        self.loans = {}

    def register_user(self, user: User):
        self.users[user.user_id] = user

    def register_book(self, book : Book):
        self.books[book.title] = book



class LoanManager: # Se encarga de gestionar la logica de los prestamos.

    def __init__(self, library: Library):
        self.library = library

    def _check_borrowed(self, title: str, loans):
        for loan in loans:
            if title == loan.book.title:
                return True
        return False

    def borrow_book(self, loan: Loan):
        if self.library.books[loan.book.title].copies > 0:
            if loan.user.user_id not in self.library.loans:
                self.library.loans[loan.user.user_id] = []
                self.library.loans[loan.user.user_id].append(loan)
                self.library.books[loan.book.title].decrement_copies()
            else:
                if not self._check_borrowed(loan.book.title, self.library.loans[loan.user.user_id]):
                    self.library.loans[loan.user.user_id].append(loan)
                    self.library.books[loan.book.title].decrement_copies()
                else:
                    print(f"El usuario ya tiene una copia del libro '{loan.book.title}'")
        else:
            print(f"El libro {loan.book.title} no esta disponible temporalmente.")

    def return_book(self, loan: Loan):
            for l in self.library.loans[loan.user.user_id]:
                if loan.book.title == l.book.title:
                    self.library.loans[loan.user.user_id].remove(l)
                    self.library.books[loan.book.title].increment_copies()
                    return True
            print(f"El usuario no tiene el libro {loan.book.title}.")
            return False



class LibraryPrinter: #Imprime los datos de la biblioteca pasada.

    def __init__(self, library: Library):
        self.library = library

    def print_users(self):
        for key, user in self.library.users.items():
            print(f"USER_ID: {key} - NAME: {user.name} - EMAIL: {user.email}")

    def print_books(self):
        for key, book in self.library.books.items():
            print(f"TITLE: {key} - WRITER: {book.writer} - COPIES: {book.copies}")

    def print_loans(self):
        for user_id, loans in self.library.loans.items():
            print(f"USER_ID: {user_id}:")
            for loan in loans:
                print(f"\t{loan.book.title}")



my_library = Library()
library_printer = LibraryPrinter(my_library)
loan_manager = LoanManager(my_library)

book1 = Book("La comunidad del anillo", "JRR Tolkien", 3)
my_library.register_book(book1)
book2 = Book("Las dos torres", "JRR Tolkien", 2)
my_library.register_book(book2)
book3 = Book("El rotorno del rey", "JRR Tolkien", 1)
my_library.register_book(book3)
user1 = User("Pedro","pedro@email.com")
my_library.register_user(user1)
user2 = User("Ignacio","ignacio@email.com")
my_library.register_user(user2)
user3 = User("Lore","lore@email.com")
my_library.register_user(user3)
user4 = User("Juan","juan@email.com")
my_library.register_user(user4)
loan = Loan(user1, book1)
loan_manager.borrow_book(loan)
loan = Loan(user1, book2)
loan_manager.borrow_book(loan)
loan = Loan(user1, book1)
loan_manager.borrow_book(loan)
loan = Loan(user2, book1)
loan_manager.borrow_book(loan)
loan = Loan(user3, book1)
loan_manager.borrow_book(loan)
loan = Loan(user4, book1)
loan_manager.borrow_book(loan)
loan = Loan(user4, book2)
loan_manager.borrow_book(loan)
library_printer.print_loans()
loan = Loan(user1, book1)
loan_manager.return_book(loan)
loan = Loan(user4, book1)
loan_manager.borrow_book(loan)
loan = Loan(user1, book2)
loan_manager.return_book(loan)
loan = Loan(user3, book1)
loan_manager.return_book(loan)

library_printer.print_users()
library_printer.print_books()
library_printer.print_loans()