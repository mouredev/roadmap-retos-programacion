# @Author Daniel Grande (mhayhem)

# EJERCICIO:
# Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
# Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.

"""
not SRP
"""
class User:
    def __init__(self, name: str, mail: str):
        self.name = name
        self.mail = mail
    
    def save_data_base(self):
        return f"{self.name} añadido a base de datos."
    
    def sent_mail(self):
        return f"Correo enviado a {self.mail}."
    
    def user_registration(self):
        return f"{self.name} registrado."

""" 
SRP
"""

class User:
    def __init__(self, name: str, mail: str):
        self.name = name
        self.mail = mail

class UserRepository:
    
    @staticmethod
    def save(user: User):
        return f"EL usuario: {user.name} se ha guardado en la base de datos."

class EmailService:
    
    @staticmethod
    def sent_mail(user: User):
        return f"Correo enviado a {user.mail}"

class UserRegistration:
    
    @staticmethod
    def registration(user: User):
        return f"Usuario: {user.name} Registrado con exito."


# DIFICULTAD EXTRA (opcional):
# Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
# manejar diferentes aspectos como el registro de libros, la gestión de usuarios
# y el procesamiento de préstamos de libros.
# Requisitos:
# 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
# información básica como título, autor y número de copias disponibles.
# 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
# información básica como nombre, número de identificación y correo electrónico.
# 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
# tomar prestados y devolver libros.
# Instrucciones:
# 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
# los tres aspectos mencionados anteriormente (registro de libros, registro de
# usuarios y procesamiento de préstamos).
# 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
# siguiendo el Principio de Responsabilidad Única.


""" not SRP """
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []
    
    def add_book(self, title: str, author: str, stock: int) -> None:
        self.books.append({"title": title,
                        "author": author.capitalize(),
                        "stock": stock})
    
    def add_user(self, name: str, id: int, mail: str) -> None:
        self.users.append({"Name": name.capitalize(),
                        "ID": id,
                        "Mail": mail})
    
    def loan_book(self, book_title: str, user_name: str) -> None:
        book = None
        for b in self.books:
            if b["title"] == book_title:
                book = b
                break
        if not book:
            return f"EL libro '{book_title}' no encontrado."
        if book["stock"] <= 0:
            return f"No hay stock del libro '{book_title}'."

        user = None
        for u in self.users:
            if u["name"] == user_name:
                user = u
                break
        
        for loan in self.loans:
            if loan[0] == book_title and loan[1] == user_name:
                return f"El usuario {user_name} ya tiene el libro '{book_title}."
        
        self.loans.append((book_title, user_name))
        book["stock"] -= 1

    def return_book(self, book_title, user_name) -> None:
        loan_found = None
        for i ,loan in enumerate(self.loans):
            if loan[0] == book_title and loan[1] == user_name:
                loan_found = i
                break
        
        if not loan_found:
            return f"El usuario {user_name} no tiene el libro '{book_title}."
        
        del self.loans[loan_found]
        
        for book in self.books:
            if book["title"] == book_title:
                book["stock"] += 1
                break


""" SRP """

class Book:
    def __init__(self, title: str, author: str, stock: int) -> None:
        self.title = title
        self.author = author
        self.stock = stock

    def book(self):
        return {"titlte": self.title,
                "author": self.author, 
                "stock": self.stock
                }

class User:
    def __init__(self, name: str, mail: str, id: int) -> None:
        self.name = name
        self.mail = mail
        self.id = id

    def user(self):
        return {
            "name": self.name,
            "mail": self.mail,
            "ID": self.id
        }

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self):
        self.books.append(Book())

library = Library()
book1 = Book("death", "dany", 2)

library.add_book(book1)