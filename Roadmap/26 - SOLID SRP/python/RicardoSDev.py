'''
* Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
* Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
'''
# Incorrecta

class Animal:
    def __init__(self, name, sonido, movimiento):
        self.name = name
        self.sonido = sonido
        self.movimiento = movimiento

    def hacer_sonido(self):
        print(f"{self.name} hace {self.sonido}")

    def mover(self):
        print(f"{self.name} se mueve de la siguiente manera: {self.movimiento}")

perro = Animal("Perro", "Guau", "corre")
perro.hacer_sonido()
perro.mover()
gato = Animal("Gato", "Miau", "camina")
gato.hacer_sonido()         
gato.mover()

# Correcta

class Animal:
    def __init__(self, name):
        self.name = name

class Sonido:
    def __init__(self, sonido):
        self.sonido = sonido

    def hacer_sonido(self, animal):
        print(f"{animal.name} hace {self.sonido}")

class Movimiento:
    def __init__(self, movimiento):
        self.movimiento = movimiento

    def mover(self, animal):
        print(f"{animal.name} se mueve de la siguiente manera: {self.movimiento}")

perro = Animal("Tobi")
sonido_perro = Sonido("Guau")
movimiento_perro = Movimiento("corre")
sonido_perro.hacer_sonido(perro)
movimiento_perro.mover(perro)
gato = Animal("Michi")
sonido_gato = Sonido("Miau")
movimiento_gato = Movimiento("camina")
sonido_gato.hacer_sonido(gato)
movimiento_gato.mover(gato) 



'''
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
*
'''

# Incorrecto
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        book = {"title": title, "author": author, "copies": copies}
        self.books.append(book)

    def add_user(self, name, id_number, email):
        user = {"name": name, "id_number": id_number, "email": email}
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u["id_number"] == user_id), None)
        book = next((b for b in self.books if b["title"] == book_title), None)
        if user and book and book["copies"] > 0:
            book["copies"] -= 1
            self.loans.append({"user_id": user_id, "book_title": book_title})
            print(f"{user['name']} ha tomado prestado el libro '{book_title}'")
        else:
            print("No se puede realizar el préstamo.")

    def return_book(self, user_id, book_title):
        loan = next((l for l in self.loans if l["user_id"] == user_id and l["book_title"] == book_title), None)
        if loan:
            book = next((b for b in self.books if b["title"] == book_title), None)
            if book:
                book["copies"] += 1
                self.loans.remove(loan)
                print(f"{user_id} ha devuelto el libro '{book_title}'")
        else:
            print("No se puede realizar la devolución.")        

prestamo = Library()
prestamo.add_book("El Principito", "Antoine de Saint-Exupéry", 5)
prestamo.add_user("Juan Pérez", "123456", "juan.perez@email.com")
prestamo.loan_book("123456", "El Principito")
prestamo.return_book("123456", "El Principito")

# Correcto
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
class User:
    def __init__(self, name, id_number, email):
        self.name = name
        self.id_number = id_number
        self.email = email
class Loan:
    def __init__(self, user, book):
        self.user = user
        self.book = book
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id_number == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if user and book and book.copies > 0:
            book.copies -= 1
            loan = Loan(user, book)
            self.loans.append(loan)
            print(f"{user.name} ha tomado prestado el libro '{book.title}'")
        else:
            print("No se puede realizar el préstamo.")

    def return_book(self, user_id, book_title):
        loan = next((l for l in self.loans if l.user.id_number == user_id and l.book.title == book_title), None)
        if loan:
            loan.book.copies += 1
            self.loans.remove(loan)
            print(f"{loan.user.name} ha devuelto el libro '{loan.book.title}'")
        else:
            print("No se puede realizar la devolución.")    


El_principito = Book("El Principito", "Antoine de Saint-Exupéry", 5)
juan_perez = User("Juan Pérez", "123456", "juan.perez@email.com")
prestamo = Library()
prestamo.add_book(El_principito)
prestamo.add_user(juan_perez)
prestamo.loan_book("123456", "El Principito")
prestamo.return_book("123456", "El Principito")
prestamo.return_book("123456", "El Principito")
prestamo.loan_book("123456", "El Principito")
El_Quijote = Book("El Quijote", "Miguel de Cervantes", 3)
prestamo.add_book(El_Quijote)
prestamo.loan_book("123456", "El Quijote")

