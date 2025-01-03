# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -------------------------------------------------
# * SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
# -------------------------------------------------
# Se centra en la claridad, la cohesión y la separación de intereses.
# Cada clase debe tener una única razón para cambiar.
# Los metodos de una clase deben estar estrechamente relacionadas.

"""
* EJERCICIO #1:
* Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
* Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
* de forma correcta e incorrecta.
"""

#_______________________________________
# SIN APLICAR EL PRINCIPIO:

class Program():
    def __init__(self):
        self.customers: list = []
        self.suppliers: list = []

    def add_customer(self, name):
        self.customers.append(name)

    def add_supplier(self, name):
        self.suppliers.append(name)

    def remove_customer(self, name):
        self.customers.remove(name)

    def remove_supplier(self, name):
        self.suppliers.remove(name)


#_______________________________________
# APLICANDO EL PRINCIPIO:

class Customers():
    def __init__(self):
        self.customers: list = []
    
    def add(self, name: str):
        self.customers.append(name)
    
    def remove(self, name: str):
        self.customers.remove(name)

    # ... más métodos relacionados.

class Suppliers():
    def __init__(self):
        self.suppliers: list = []
    
    def add(self, name: str):
        self.suppliers.append(name)

    def remove(self, name: str):
        self.suppliers.remove(name)

    # ... más métodos relacionados.


"""
* EJERCICIO #2:
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

#____________________________________________________________________________
# SIN APLICAR SRP:

class Library():
    def __init__(self):
        self.books: dict = {}
        self.users: dict = {}
        self.borrowed: dict = {}
    
    def add_book(self, id_book: int, title: str, author: str, stock: int):
        if id_book in self.books:
            self.books[id_book]['stock'] += stock
            self.books[id_book]['available'] += stock
            print("El libro ya existe, se actualizó el inventario.")

        else:
            self.books[id_book] = {
                'title': title,
                'author': author,
                'stock': stock,
                'available': stock
            }
            print(f"\nSe agrego el libro '{title}'.") 

    def add_user(self, id_user: int, name: str, email: str):
        if id_user in self.users:
            print("Usuario ya existee")

        else:
            self.users[id_user] = {
                'name': name,
                'email': email
            }
            print(f"\nSe agrego a '{name}'.") 

    def lend_book(self, id_borrowed: int, id_user: int, id_book: int):
        if id_book not in self.books:
            print("Este libro no existe")
            return
        
        if id_user not in self.users:
            print("Este usuario no existe")
            return
        
        if self.books[id_book]['available'] > 0:
            self.borrowed[id_borrowed] = {  
                'id_user': id_user,
                'id_book': id_book
            }
            self.books[id_book]['available'] -= 1
            print(f"\nSe presto el libro '{id_book}'.") 

        else:
            print(f"No hay libro disponible.")

    def return_book(self, id_borrowed: int):
        if id_user not in self.borrowed:
            print("No está registrado.")
        
        else:
            self.books[id_borrowed[id_book]]['available'] += 1
            del self.borrowed[id_borrowed]
            print("Retorno exitoso.")

    def print_books(self):
        print("Lista de libros:\n", self.books)

    def print_users(self):
        print("Lista de usuarios", self.users)

    def print_borrowed(self):
        print("Lista de libros prestados", self.borrowed)

#____________________________________________________________________________
# APLICANDO SRP:

class LibraryData: # uso de SINGLETON para tener datos globales
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.books = {}
            cls.users = {}
            cls.borrowed = {}

        return cls._instance

#___________________
class Books:
    def __init__(self):
        self.data = LibraryData()

    def add(self, id_book: int, title: str, author: str, stock: int):
        if id_book in self.data.books:
            self.data.books[id_book]['stock'] += stock
            self.data.books[id_book]['available'] += stock
            print("El libro ya existe, se actualizó el inventario.")
            return

        self.data.books[id_book] = {
            'title': title,
            'author': author,
            'stock': stock,
            'available': stock
        }
        print(f"\nSe agrego el libro '{title}'.") 

    def print_dic(self):
        print("\nLibros:")
        if self.data.books:
            for ky, values in self.data.books.items():
                print(f"{ky}: {values}")
        else:
            print("- Vacio")

#___________________      
class Users:
    def __init__(self):
        self.data = LibraryData()

    def add(self, id_user: int, name: str, email: str):
        if id_user in self.data.users:
            print("Usuario ya existe.")
            return

        self.data.users[id_user] = {
            'name': name,
            'email': email
        }
        print(f"\nSe agrego a '{name}'.") 

    def print_dic(self):
        print("\nUsuarios:")
        if self.data.users:
            for ky, values in self.data.users.items():
                print(f"{ky}: {values}")
        else:
            print("- Vacio")

#___________________
class BorrowedBooks:
    def __init__(self):
        self.data = LibraryData()

    def _verify(self, id_user: int, id_book: int) -> bool:
        if id_book not in self.data.books:
            print("Este libro no existe")
            return False
        
        if id_user not in self.data.users:
            print("Este usuario no existe")
            return False
        
        if self.data.books[id_book]['available'] <= 0:
            print(f"El libro no está disponible.")
            return False
        
        return True

    def lend(self, id_borrowed: int, id_user: int, id_book: int):
        if self._verify(id_user, id_book) == False:
            return
        
        self.data.borrowed[id_borrowed] = {  
            'id_user': id_user,
            'id_book': id_book
        }
        self.data.books[id_book]['available'] -= 1
        print(f"\nSe presto el libro '{id_book}'.")           

    def return_book(self, id_borrowed: int):
        if id_borrowed not in self.data.borrowed:
            print("No está registrado.")
            return
        
        id_book =  self.data.borrowed[id_borrowed]['id_book']
        self.data.books[id_book]['available'] += 1
        del self.data.borrowed[id_borrowed]
        print(f"\nRetorno exitoso del libro '{id_book}'.")

    def print_dic(self):
        print("\nLibros prestados:")
        if self.data.borrowed:
            for ky, values in self.data.borrowed.items():
                print(f"{ky}: {values}")
        else:
            print("- Vacio")

#_________________________________
# Pruebas positivas

books = Books()
users = Users()
borrowed_books = BorrowedBooks()

# id, title, author, stock
books.add(1, "Libro A", "Ben", 1)
books.add(2, "Libro B", "Dan", 3)

# id, name, email
users.add(10, "Zoe", "Zoe@a.com")
users.add(11, "Ana", "Ana@a.com")

books.print_dic()
users.print_dic()
borrowed_books.print_dic()

# id_borrowed, id_user, id_book
borrowed_books.lend(100, 10, 1)
borrowed_books.lend(101, 11, 2)

books.print_dic()
borrowed_books.print_dic()

# id_borrowed
borrowed_books.return_book(100)
borrowed_books.return_book(101)

books.print_dic()
borrowed_books.print_dic()

borrowed_books.lend(103, 11, 1)

#_________________________________
# Pruebas negativas
print("\n_____\nPruebas negativas")
books.add(2, "..", "..", 1)
users.add(11, "..", "..")
borrowed_books.lend(104, 10, 1)
borrowed_books.return_book(100)

