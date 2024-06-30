"""
    SOLID: Principio de Responsibilidad Única (SRP)
    Ejercicio
    Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
    Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
    de forma correcta e incorrecta.
"""
# Uso incorrecto del SRP
from typing import Any


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_user(self):
        print(f"El usuario {self.name} ha sido guardado.")

    def print_report(self):
        print(f"Imprimiendo reporte para {self.name} con email {self.email}.")


user = User("Aldroide", "aldroide@dev.com.")
user.save_user()
user.print_report()

# Uso correcto del SRP


class User1:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        print(f"Guardando usuario {self.name}.")


class Info():
    def __init__(self, user):
        self.user = user

    def print_inform(self):
        print(
            f"Imprimiendo informe  para {self.user.name} con email {self.user.email}.")


user = User1("Emmanuel", "emma@dev.com")
user.save()

informe = Info(user)
informe.print_inform()

"""
    DIFICULTAD EXTRA (opcional):
    Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
    manejar diferentes aspectos como el registro de libros, la gestión de usuarios
    y el procesamiento de préstamos de libros.
    Requisitos:
        1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
            información básica como título, autor y número de copias disponibles.
        2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
            información básica como nombre, número de identificación y correo electrónico.
        3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
            tomar prestados y devolver libros.
    Instrucciones:
        1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
            los tres aspectos mencionados anteriormente (registro de libros, registro de
            usuarios y procesamiento de préstamos).
        2. Refactoriza el código: Separa las responsabilidades en diferentes clases
            siguiendo el Principio de Responsabilidad Única.
"""

# No cumple con el SRP


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def Register_book(self, title, author, copies):
        book = {'title': title, "author": author, "copies": copies}
        self.books.append(book)
        print(f"Titulo registrado: {title}.")

    def Register_user(self, id, name, email):
        user = {'id': id, "name": name, "email": email}
        self.users.append(user)
        print(f"Usuario registrado: {name}.")

    def Process_Loans(self, id, title):
        for book in self.books:
            if book["title"] == title and book['copies'] > 0:
                book['copies'] -= 1
                self.loans.append({'id': id, 'title': title})
                print(f"Libro prestado: {book['title']} a {id}.")
                return
        print(f"No existen copias disponibles de {title}.")

    def Return_book(self, id, title):
        for loan in self.loans:
            if loan["id"] == id and loan["title"] == title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == title:
                        book["copies"] += 1
                        print(f"Libro devuelto: {title} por {id}.")
                        return
        print(f"No se encontró el prestamo del {title} para {id}. ")


library = Library()
library.Register_book("Baluarte", "Elvira Sastre", 5)
library.Register_book("Dias sin ti", "Elvira Sastre", 3)
library.Register_book(
    "Cuarenta y tres maneras de soltarse el pelo", "Elvira Sastre", 5)
library.Register_user("Aldo", 1, "aldo@dev.com")
library.Register_user("Emmanuel", 2, "emma@dev.com")
library.Register_user("Samira", 3, "sami@dev.com")
library.Process_Loans(2, "Baluarte")
library.Process_Loans(3, "Baluarte")
library.Return_book(2, "Baluarte")


# Codigo Refactorizado cumple con el SRP
class Book_Manager:
    def __init__(self):
        self.books = []

    def Register_book(self, title, author, copies):
        book = {'title': title, 'author': author, 'copies': copies}
        self.books.append(book)
        print(f"Libro Registrado: {title}.")

    def Search_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None


class User_Manager:
    def __init__(self):
        self.users = []

    def Register_user(self, id, name, email):
        user = {'id': id, "name": name, "email": email}
        self.users.append(user)
        print(f"Usuario registrado: {name}.")

    def Search_user(self, id):
        for user in self.users:
            if user['id'] == id:
                return user
        return None


class Loan_manager:
    def __init__(self, book_manager, user_manager):
        self.loans = []
        self.book_manager = book_manager
        self.user_manager = user_manager

    def Process_loan(self, id, title):
        user = self.user_manager.Search_user(id)
        book = self.book_manager.Search_book(title)

        if user and book and book['copies'] > 0:
            book['copies'] -= 1
            self.loans.append({'id': id, 'title': title})
            print(f"Libro prestado {book['title']} a {user['name']}.")
        else:
            print(f"No se puede presta el libro {title}.")

    def Return_book(self, id, title):
        for loan in self.loans:
            if loan['id'] == id and loan['title'] == title:
                self.loans.remove(loan)
                book = self.book_manager.Search_book(title)
                if book:
                    book['copies'] += 1
                    print(f"Libro devuelto: {title} por {id}.")
                return
        print(f"No se encontro el prestamo de {title} para {id}.")


book_manager = Book_Manager()
user_manager = User_Manager()
loan_manager = Loan_manager(book_manager, user_manager)

book_manager.Register_book("El Quijote", "Cervantes", 5)
book_manager.Register_book("La panza del tepozteco", "José Agustin", 3)

user_manager.Register_user(name="Sebastian", id=1, email="sebas@dev.com")
user_manager.Register_user(name="Erwin", id=2, email="erwin@dev.com")
loan_manager.Process_loan(1, "El Quijote")
loan_manager.Return_book(1, "El Quijote")
