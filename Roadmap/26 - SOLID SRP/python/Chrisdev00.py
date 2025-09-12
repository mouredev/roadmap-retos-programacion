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

# El Principio de Responsabilidad Única (Single Responsibility Principle, SRP) es uno de los cinco principios de 
# diseño de software SOLID, que fue definido por Robert C. Martin. 
# Este principio establece que una clase debe tener una, y solo una, razón para cambiar, 
# es decir, una única responsabilidad o propósito.

# Ejemplo (Forma incorrecta)

class Order:
    def __init__(self, items, tax_rate):
        self.items = items # tupla (item: precio)
        self.tax_rate = tax_rate
    
    def calculate_total(self):
        total = sum(price for item, price in self.items)
        discount = 5  # Añadir un descuento fijo
        tax = (total - discount) * self.tax_rate
        return total - discount + tax
    
    def generate_invoice(self):
        total = self.calculate_total()
        invoice = "Factura:\n"
        for item, price in self.items:
            invoice += f"{item}: ${price}\n"
        invoice += f"Total (incluyendo impuestos): ${total}\n"
        return invoice
    
    def send_confirmation_email(self, email):
        invoice = self.generate_invoice()
        print(f"Enviando email a {email} con la siguiente Factura:\n{invoice}")


order = Order([("Libro", 12.99), ("Lapicero", 0.99)], 0.1)
print(order.calculate_total())
print(order.generate_invoice())
order.send_confirmation_email("customer@example.com")


# Ejemplo (Forma correcta cumpliendo con el SRP)


class Order:
    def __init__(self, items):
        self.items = items
    
    def get_total(self):
        return sum(price for item, price in self.items)

class TaxCalculator:
    def calculate_tax(self, total, tax_rate, discount=0):
        return (total - discount) * tax_rate

class InvoiceGenerator:
    def generate_invoice(self, order, total, tax):
        invoice = "Factura:\n"
        for item, price in order.items:
            invoice += f"{item}: ${price}\n"
        invoice += f"Subtotal: ${total}\n"
        invoice += f"Impuesto: ${tax}\n"
        invoice += f"Total (incluyendo impuestos): ${total + tax}\n"
        return invoice

class EmailSender:
    def send_email(self, email, content):
        print(f"Enviando email a {email} con el siguiente contenido:\n{content}")


order = Order([("Libro", 12.99), ("Lapiz", 0.99)])
tax_calculator = TaxCalculator()
invoice_generator = InvoiceGenerator()
email_sender = EmailSender()

total = order.get_total()
tax = tax_calculator.calculate_tax(total, 0.1, discount=5)
subtotal = total - 5

factura = invoice_generator.generate_invoice(order, subtotal, tax)

email_sender.send_email("comprador@example.com", factura)


########## ------------------------------- EXTRA ---------------------------------- #######################

# Forma Incorrecta

class Library:

    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        book = {"title": title, "author": author, "copies": copies}
        self.books.append(book)

    def add_usser(self, name, user_id, email):
        user = {"name": name, "user_id": user_id, "email": email}
        self.users.append(user)

    def borrow_book(self, user_id, title):
        for book in self.books:
            if book["title"] == title and book["copies"] > 0:
                book["copies"] -= 1
                loan = {"user_id": user_id, "title": title}
                self.loans.append(loan)
                return f"El usuario '{user_id}' se presto el libro '{title}'."
        return f"Libro '{title}' no esta disponible."
    
    def return_book(self, user_id, title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["title"] == title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == title:
                        book["copies"] += 1
                return f"Libro '{title}' retornado por el usuario '{user_id}'."
        return f"No hay registro de que el usuario '{user_id}' se haya prestado el libro '{title}'"
    

library = Library()

library.add_book("Lord of the Rings", "JRR Tolkien", 4)
library.add_book("Harry Potter", "JK Rowling", 2)

library.add_usser("Alice", "1", "alice@example.com")
library.add_usser("Matias", "2", "matias@example.com")

print(library.borrow_book("1", "Lord of the Rings"))
print(library.borrow_book("2", "Harry Potter"))
print(library.borrow_book("1", "Lord of the Rings"))
print(library.return_book("2", "The Great Gatsby"))


# Forma correcta (usando SRP)

class Library:
    def __init__(self):
        self.books = []
        self.users = []        

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def total_books(self):
        return sum(book.copies for book in self.books)
    
    def get_library_info(self):
        total_books = self.total_books()
        books_info = [book.show_info() for book in self.books]
        return total_books, books_info

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def show_info(self):
        return f"'{self.title}' por '{self.author}', numero de copias {self.copies}"
    
class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.user_id = user_id
        self.email = email
        self.loans = []

class LoanProcess:
    
    def borrow_book(self, library, user_id, title):
        user = library.find_user(user_id)
        book = library.find_book(title)
        if book and user:
            if book.copies > 0:
                user.loans.append(book)
                book.copies -= 1
                print(f"Libro '{book.title}' prestado a '{user.name}'")
            else:
                print(f"Este libro no esta disponible para prestamo")
        else:
            print(f"Usuario o libro no encontrado")

    def return_book(self, library, user_id, title):
        user = library.find_user(user_id)
        book = library.find_book(title)
        if book and user:
            if book in user.loans:
                user.loans.remove(book)
                book.copies += 1
                print(f"Libro '{book.title}' devuelto por '{user.name}'.")
            else:
                print(f"No hay registro de que el libro '{book.title}' haya sido prestado a '{user.name}'.")
        else:
            print("Usuario o libro no encontrado.")


library = Library()
book1 = Book("Lord of the Rings", "JRR Tolkien", 4)
book2 = Book("1984", "George Orwell", 5)
user = User("Alice", "1", "alice@example.com")
library.add_book(book1)
library.add_book(book2)
library.add_user(user)

loan_processor = LoanProcess()
loan_processor.borrow_book(library, "1", "Lord of the Rings")
loan_processor.return_book(library, "1", "Lord of the Rings")


# Total de libros en la biblioteca
total_libros, info_libros = library.get_library_info()
print(f"Total de libros en la biblioteca: {total_libros}")
print("Informacion de la biblioteca:")
for info in info_libros:
    print(info)




    
