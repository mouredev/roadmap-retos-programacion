# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 * """

# Violación del Single Responsibility Principle

class User:
    users = []

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        print("Usuario creado!")

    def get_info(self):
        return f"{self.name}, {self.age}, {self.country}"
    
    def save_to_db(self):
        User.users.append(User(self.name, self.age, self.country))
        print("Usuario guardado en la base de datos!")


# Siguiendo el SRP

class UserSRP:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
        print("Usuario creado!")

    def get_info(self):
        return f"{self.name}, {self.age}, {self.country}"

class UserDB:
    users = []

    @classmethod
    def save_user(cls, user: UserSRP) -> None:
        cls.users.append(user)
        print("Usuario guardado en la base de datos!")

    @classmethod
    def get_users(cls):
        for user in cls.users:
            print(f"{user.name}, {user.age}, {user.country}")


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
 */
"""

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.rented_books = {}

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            self.books[book_id]['copies'] += copies
            print(f"El libro {title}, ha sido guardado con {copies} copias.")
        else:
            self.books[book_id] = {
                "title": title,
                "author": author,
                "copies": copies
            }
            print(f"El libro {title}, ha sido guardado con {copies} copias.")
        

    def add_user(self, user_id, name, ni, email):
        if user_id in self.users:
            print("El usuario ya se encuentra registrado")
        else:
            self.users[user_id] = {
                "name": name,
                "document": ni,
                "email": email
            }

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print("El usuario no existe")
            return False    # Detiene el método aquí
        elif book_id not in self.books:
            print("El libro no existe... :(")
            return False
        
        book = self.books[book_id]
        if book['copies'] <= 0:
            print(f"No hay copias disponibles del libro {book['title']}")
            return False
        
        if book_id in self.rented_books.get(user_id, set()):
            print("El usuario ya tiene el libro prestado!")
            return False
            
        book['copies'] -= 1
        if user_id not in self.rented_books:
            self.rented_books[user_id] = set()
        self.rented_books[user_id].add(book_id)
        
        print(f"El libro {book_id} ha sido prestado a {self.users[user_id]['name']}")
        return True
    
    def return_book(self, user_id, book_id):
        if user_id not in self.rented_books or book_id not in self.rented_books[user_id]:
            print("El usuario no tiene el libro registrado")
            return False
        self.rented_books[user_id].remove(book_id)
        self.books[book_id]['copies'] += 1
        if not self.rented_books[user_id]:
            del self.rented_books[user_id]
        print("Libro devuelto correctamente")
        return True



# Refactorizando el código siguiente el SRP
class Library2:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, copies):
        if book_id in self.books:
            self.books[book_id]['copies'] += copies
            print(f"El libro {title}, ha sido guardado con {copies} copias.")
        else:
            self.books[book_id] = {
                "title": title,
                "author": author,
                "copies": copies
            }
            print(f"El libro {title}, ha sido guardado con {copies} copias.")

class LibraryUsers:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name, ni, email):
        if user_id in self.users:
            print("El usuario ya se encuentra registrado")
        else:
            self.users[user_id] = {
                "name": name,
                "document": ni,
                "email": email
            }

class LoanLibrary:
    def __init__(self, users, library):
        self.rented_books = {}
        self.user_manager: LibraryUsers = users
        self.book_manager: Library2 = library
    
    def borrow_book(self, user_id, book_id):
        if user_id not in self.user_manager.users:
            print("El usuario no existe")
            return False    # Detiene el método aquí
        elif book_id not in self.book_manager.books:
            print("El libro no existe... :(")
            return False
        
        book = self.book_manager.books[book_id]
        if book['copies'] <= 0:
            print(f"No hay copias disponibles del libro {book['title']}")
            return False
        
        if book_id in self.rented_books.get(user_id, set()):
            print("El usuario ya tiene el libro prestado!")
            return False
            
        book['copies'] -= 1
        if user_id not in self.rented_books:
            self.rented_books[user_id] = set()
        self.rented_books[user_id].add(book_id)
        
        print(f"El libro {book_id} ha sido prestado a {self.user_manager.users[user_id]['name']}")
        return True
    
    def return_book(self, user_id, book_id):
        if user_id not in self.rented_books or book_id not in self.rented_books[user_id]:
            print("El usuario no tiene el libro registrado")
            return False
        self.rented_books[user_id].remove(book_id)
        self.book_manager.books[book_id]['copies'] += 1
        if not self.rented_books[user_id]:
            del self.rented_books[user_id]
        print("Libro devuelto correctamente")
        return True



# Clase principal que orquesta la gestión
class LibraryManager:
    def __init__(self):
        self.library = Library2()
        self.user_manager = LibraryUsers()
        self.loan_manager = LoanLibrary(self.user_manager, self.library)

    def add_book(self, book_id, name, author, copies):
        self.library.add_book(book_id, name, author, copies)

    def add_user(self, user_id, name, ni, email):
        self.user_manager.add_user(user_id, name, ni, email)

    def borrow_book(self, user_id, book_id):
        self.loan_manager.borrow_book(user_id, book_id)

    def return_book(self, user_id, book_id):
        self.loan_manager.return_book(user_id, book_id)


if __name__ == "__main__":

    l2 = LibraryManager()
    l2.add_book("B000", "Python", "Yo", 2)

    l2.add_user("U001", "Duban",1, "jheison@")
    l2.borrow_book("U001", "B000")
    print(l2.library.books)
    l2.return_book("U001", "B000")
    print(l2.library.books)