# ---------------------------------------------
# Ejemplo de Principio de responsabilidad única
# ---------------------------------------------

# El siguiente ejemplo muestra un código que viola el principio de responsabilidad única.
# La clase ImageManager tiene dos responsabilidades: 
#   1.- Obtener estadísticas de una imagen
#   2.- Graficar una imagen

import matplotlib.pyplot as plt
import numpy as np

import logging


class ImageManager:
    def __init__(self, array):
        self.array = array

    def get_statistics(self):
        return {
            "mean": np.mean(self.array),
            "std": np.std(self.array),
        }
    
    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.array)
        plt.show()

# Para cumplir con el principio de responsabilidad única, separamos las responsabilidades en dos clases diferentes.

class ImageStatistics:
    def __init__(self, array):
        self.array = array

    def get_statistics(self):
        return {
            "mean": np.mean(self.array),
            "std": np.std(self.array),
        }
    
class ImagePlotter:
    def __init__(self, array):
        self.array = array

    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.array)
        plt.show()


# ---------------------------------------------
# Dificultad extra
# Sistema de gestion para una bibioteca
#
# FORMA INCORRECTA
#
# ---------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_user(self, name: str, id: int, email: str):
        self.users.append({
            "name": name,
            "id": id,
            "email": email,
            "books": [],
            }
        )
        logging.info(f"User {name} added successfully")

    def add_book(self, title: str, author: str, copies: int):
        self.books.append({
            "title": title,
            "author": author,
            "copies": copies
            }
        )
        logging.info(f"Book {title} added successfully")
        
    def print_books(self):
        for book in self.books:
            print(f"\tTitle: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")

    def print_users(self):
        for user in self.users:
            print(f"\tName: {user['name']}, ID: {user['id']}, Email: {user['email']}, Books: {user['books']}")

    
    def lend_book(self, title: str, name: str):

        for book in self.books:
            if book["title"] == title:
                if book["copies"] > 0:
                    book["copies"] -= 1
                    logging.info(f"Book {title} borrowed by user {name}")
                else:
                    logging.info(f"Book {title} is not available")
                break
            else:
                logging.warning(f"Book {title} not found")

        for user in self.users:
            if user["name"] == name:
                user["books"].append(
                    {
                        "title": title,
                    }
                )
                logging.info(f"Book {title} added to user {name}")
                break
        
    def return_book(self, title: str, name: str):

        for book in self.books:
            if book["title"] == title:
                book["copies"] += 1
                logging.info(f"Book {title} returned by user {name}")
                break
            else:
                logging.warning(f"Book {title} not found")

        for user in self.users:
            if user["name"] == name:
                for book in user["books"]:
                    if book["title"] == title:
                        user["books"].remove(book)
                        logging.info(f"Book {title} removed from user {name}")
                        break


# Testing the class
print("\n"*3)
print("### Testing: Dificultad extra (FORMA INCORRECTA)\n")
my_library = Library()
my_library.add_user("Alice", 1, "alice@dev")
my_library.add_user("Bob", 2, "bob@dev")

my_library.add_book("The Hobbit", "J.R.R. Tolkien", 5)
my_library.add_book("The Lord of the Rings", "J.R.R. Tolkien", 3)

print("\nBooks in the library:")
my_library.print_books()

my_library.lend_book("The Hobbit", "Alice")

print("\nBooks in the library:")
my_library.print_books()
my_library.print_users()


my_library.return_book("The Hobbit", "Alice")
my_library.print_books()
my_library.print_users()


# ---------------------------------------------
# Dificultad extra
# Sistema de gestion para una bibioteca
#
# Forma CORRECTA
# 
# Se crean dos clases diferentes, BooksManager y UsersManager, para manejar los libros y a los usuarios.
# Se crea una clase que maneja la biblioteca y delega las responsabilidades a las clases BooksManeger y UsersManager.
# ---------------------------------------------

class BooksManeger:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, copies: int):
        self.books.append(
            {"title": title, "author": author, "copies": copies}
        )
        logging.info(f"Book {title} added successfully")

    def print_books(self):
        for book in self.books:
            print(f"\tTitle: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")

    def lend_book(self, title: str):
        for book in self.books:
            if book["title"] == title:
                if book["copies"] > 0:
                    book["copies"] -= 1
                    logging.info(f"Book {title} borrowed")
                else:
                    logging.info(f"Book {title} is not available")
                break
            else:
                logging.warning(f"Book {title} not found")

    def return_book(self, title: str):
        for book in self.books:
            if book["title"] == title:
                book["copies"] += 1
                logging.info(f"Book {title} returned")
                break
            else:
                logging.warning(f"Book {title} not found")


class UsersManager:
    def __init__(self):
        self.users = []

    def add_user(self, name: str, id: int, email: str):
        self.users.append(
            {"name": name, "id": id, "email": email, "books": []}
        )
        logging.info(f"User {name} added successfully")

    def print_users(self):
        for user in self.users:
            print(f"\tName: {user['name']}, ID: {user['id']}, Email: {user['email']}, Books: {user['books']}")

    def lend_book(self, title: str, name: str):
        for user in self.users:
            if user["name"] == name:
                user["books"].append({"title": title})
                logging.info(f"Book {title} added to user {name}")
                break
            else:
                logging.warning(f"User {name} not found")

    def return_book(self, title: str, name: str):
        for user in self.users:
            if user["name"] == name:
                for book in user["books"]:
                    if book["title"] == title:
                        user["books"].remove(book)
                        logging.info(f"Book {title} removed from user {name}")
                        break
                break
            else:
                logging.warning(f"User {name} not found")

class Library_v2:
    def __init__(self):
        self.books_m = BooksManeger()
        self.users_m = UsersManager()

    def add_user(self, name: str, id: int, email: str):
        self.users_m.add_user(name, id, email)

    def add_book(self, title: str, author: str, copies: int):
        self.books_m.add_book(title, author, copies)
        
    def print_books(self):
        self.books_m.print_books()

    def print_users(self):
        self.users_m.print_users()

    def lend_book(self, title: str, name: str):
        self.books_m.lend_book(title)
        self.users_m.lend_book(title, name)
        
    def return_book(self, title: str, name: str):
        self.books_m.return_book(title)
        self.users_m.return_book(title, name)


# Testing the classes
print("\n"*3)
print("### Testing: Dificultad extra (FORMA CORRECTA)\n")

my_library_v2 = Library_v2()
my_library_v2.add_user("Alice", 1, "alice@dev")
my_library_v2.add_user("Bob", 2, "bob@dev")

my_library_v2.add_book("The Hobbit", "J.R.R. Tolkien", 5)
my_library_v2.add_book("The Lord of the Rings", "J.R.R. Tolkien", 3)

print("\nBooks in the library:")
my_library_v2.print_books()

my_library_v2.lend_book("The Hobbit", "Alice")

print("\nBooks in the library:")
my_library_v2.print_books()

print("\nUsers in the library:")
my_library_v2.print_users()

my_library_v2.return_book("The Hobbit", "Alice")

print("\nBooks in the library:")
my_library_v2.print_books()

print("\nUsers in the library:")
my_library_v2.print_users()