# Autor: Héctor Adán 
# GitHub: https://github.com/hectorio23
import os

'''
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA:
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
'''

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self):
        os.system('clear')
        title = input("Ingrese el título del libro: ")
        author = input("Ingrese el autor del libro: ")
        copies = int(input("Ingrese el número de copias: "))
        self.books.append(Book(title, author, copies))
        print("Libro agregado exitosamente.")

    def list_books(self):
        os.system('clear')
        if not self.books:
            print("No hay libros disponibles.")
            return
        for book in self.books:
            print(f"Título: {book.title}, Autor: {book.author}, Copias: {book.copies}")

class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.id = user_id
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self):
        os.system('clear')
        name = input("Ingrese el nombre del usuario: ")
        user_id = int(input("Ingrese el ID del usuario: "))
        email = input("Ingrese el correo electrónico del usuario: ")
        self.users.append(User(name, user_id, email))
        print("Usuario agregado exitosamente.")

    def list_users(self):
        os.system('clear')
        if not self.users:
            print("No hay usuarios registrados.")
            return
        for user in self.users:
            print(f"Nombre: {user.name}, ID: {user.id}, Correo: {user.email}")

class LoanManager:
    def lend_book(self, user_manager, book_manager):
        os.system('clear')
        user_id = int(input("Ingrese el ID del usuario: "))
        book_title = input("Ingrese el título del libro a prestar: ")
        # Lógica de préstamo
        print(f"Libro '{book_title}' prestado al usuario ID {user_id}.")

    def return_book(self, user_manager, book_manager):
        os.system('clear')
        user_id = int(input("Ingrese el ID del usuario: "))
        book_title = input("Ingrese el título del libro a devolver: ")
        # Lógica de devolución
        print(f"Libro '{book_title}' devuelto por el usuario ID {user_id}.")

def display_menu():
    os.system('clear')
    print("******** Menú de la Biblioteca ********")
    print("[1] - Agregar un libro")
    print("[2] - Listar libros")
    print("[3] - Agregar un usuario")
    print("[4] - Listar usuarios")
    print("[5] - Prestar un libro")
    print("[6] - Devolver un libro")
    print("[7] - Salir")
    return int(input("Seleccione una opción: "))

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    loan_manager = LoanManager()
    option = 0

    while option != 7:
        option = display_menu()
        if option == 1:
            book_manager.add_book()
        elif option == 2:
            book_manager.list_books()
        elif option == 3:
            user_manager.add_user()
        elif option == 4:
            user_manager.list_users()
        elif option == 5:
            loan_manager.lend_book(user_manager, book_manager)
        elif option == 6:
            loan_manager.return_book(user_manager, book_manager)
        elif option == 7:
            print("Saliendo del sistema...")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
