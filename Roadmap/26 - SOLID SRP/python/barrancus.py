#26 - Python - Principio de Responsabilidad Única (SRP)
# EJERCICIO:
# Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
# Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.
# 
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
# 

class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

identifier = iter(Counter())

def separacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena} {'-.-' * 20}')

# Incorrecto

class User:
    
    def __init__(self, name, email) -> None:
        self.name = name
        self.emmail = email

    def save_to_datababase(self):
        pass

    def send_email(self):
        pass

# Correcto

class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.emmail = email

class UserService:

    def save_to_datababase(self, user):
        pass

class EmailServie:

    def send_email(self, email, message):
        pass


# DIFICULTAD EXTRA (opcional):

class Book:

    def __init__(self, title: str, author: str, ncopies: int):
        self.title = title
        self.author = author
        self.ncopies = ncopies
        self.borrow = 0

    def __str__(self):
        return f'Libro: {self.title}.\n Autor: {self.author}.\n Número de copias: {self.ncopies}.\n En préstamo: {self.borrow}'
    
user_lib_id = iter(Counter())
class UserLibrary:

    def __init__(self, name: str, email: str):
        self.name = name
        self.codeid = f'{next(user_lib_id):06}'
        self.email = email
        self.borrowed = []

    def __str__(self):
        return f'ID: {self.codeid}\n Nombre: {self.name}.\n Mail: {self.email}\n Libros: {self.borrowed}'

# 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje los tres aspectos mencionados anteriormente (registro de libros, registro de usuarios y procesamiento de préstamos).
class LibraryManagement:

    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title: str, author: str, ncopies: int | None = 0) -> tuple[bool, str]:
        book = self.search_book(title)
        if book != None:
            if ncopies == 0: ncopies = 1
            book.ncopies += ncopies
            return True, f'Se añaden {ncopies} copias al listado.'
        else:
            self.books.append(Book(title, author, ncopies))
            return True, f'Libro {title} añadido al catálogo.'

    def delete_book(self, title: str) -> tuple[bool, str]:
        book = self.search_book(title)
        if book != None:
            self.books.remove(book)
            return True, 'Libro borrado del catálogo.'
        else:
            return False, 'El libro no existe en el catálogo.'
    
    def search_book(self, search_title: str):
        for book in self.books:
            if book.title == search_title:
                return book
        return None

    def show_stock(self):
        for element in self.books:
            print(element)

    def borrow_book(self, title: str, inout: bool) -> tuple[bool, str]:
        book = self.search_book(title)
        if inout:
            if book != None:
                if book.ncopies >= book.borrow + 1:
                    book.borrow += 1
                    return True, 'Libro prestado'
                else:
                    return False, 'No hay libros disponibles'
        else:
            if book != None:
                book.borrow -= 1
                return True, 'Libro devuelto'

    def add_user(self, name: str, email: str) -> tuple[bool, str]:
        user = self.search_user(name)
        if user != None:
            if name == user.name and email == user.email:
                print(user)
                return False, 'El usuario ya existe.'
        else:
            self.users.append(UserLibrary(name, email))
            return True, 'Usuario añadido.'

    def delete_user(self, name: str) -> tuple[bool, str]:
        user = self.search_user(name)
        if user != None:
            self.users.remove(user)
            return True, 'Usuario borrado.'
        else:
            return False, 'El usuario no existe.'

    def search_user(self, search_name: str):
        for user in self.users:
            if user.name == search_name:
                return user
        return None

    def show_list(self):
        for element in self.users:
            print(element)

    def borrow_book(self, search_name: str, title: str, inout: bool) -> None:
        if inout:
            user = self.search_user(search_name)
            user.borrowed.append(title)
        else:
            user = self.search_user(search_name)
            user.borrowed.remove(title)

# 2. Refactoriza el código: Separa las responsabilidades en diferentes clases siguiendo el Principio de Responsabilidad Única.
class BookManager:

    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, ncopies: int | None = 0) -> tuple[bool, str]:
        book = self.search_book(title)
        if book != None:
            if ncopies == 0: ncopies = 1
            book.ncopies += ncopies
            return True, f'Se añaden {ncopies} copias al listado.'
        else:
            self.books.append(Book(title, author, ncopies))
            return True, f'Libro {title} añadido al catálogo.'

    def delete_book(self, title: str) -> tuple[bool, str]:
        book = self.search_book(title)
        if book != None:
            self.books.remove(book)
            return True, 'Libro borrado del catálogo.'
        else:
            return False, 'El libro no existe en el catálogo.'
    
    def search_book(self, search_title: str):
        for book in self.books:
            if book.title == search_title:
                return book
        return None

    def show_stock(self):
        for element in self.books:
            print(element)

    def borrow_book(self, title: str, inout: bool) -> tuple[bool, str]:
        book = self.search_book(title)
        if inout:
            if book != None:
                if book.ncopies >= book.borrow + 1:
                    book.borrow += 1
                    return True, 'Libro prestado'
                else:
                    return False, 'No hay libros disponibles'
        else:
            if book != None:
                book.borrow -= 1
                return True, 'Libro devuelto'
        
class UserLibraryManager:

    def __init__(self):
        self.users = []

    def add_user(self, name: str, email: str) -> tuple[bool, str]:
        user = self.search_user(name)
        if user != None:
            if name == user.name and email == user.email:
                print(user)
                return False, 'El usuario ya existe.'
        else:
            self.users.append(UserLibrary(name, email))
            return True, 'Usuario añadido.'

    def delete_user(self, name: str) -> tuple[bool, str]:
        user = self.search_user(name)
        if user != None:
            self.users.remove(user)
            return True, 'Usuario borrado.'
        else:
            return False, 'El usuario no existe.'

    def search_user(self, search_name: str):
        for user in self.users:
            if user.name == search_name:
                return user
        return None

    def show_list(self):
        for element in self.users:
            print(element)

    def borrow_book(self, search_name: str, title: str, inout: bool) -> None:
        if inout:
            user = self.search_user(search_name)
            user.borrowed.append(title)
        else:
            user = self.search_user(search_name)
            user.borrowed.remove(title)
        
        
usuarios = [
    {"nombre": "Juan Pérez", "email": "juan.perez@example.com"},
    {"nombre": "María García", "email": "maria.garcia@test.com"},
    {"nombre": "Carlos López", "email": "carlos.lopez@dominio.net"},
    {"nombre": "Ana Martínez", "email": "ana.martinez@web.org"},
    {"nombre": "Luis González", "email": "luis.gonzalez@example.com"},
    {"nombre": "Elena Rodríguez", "email": "elena.rodriguez@test.com"},
    {"nombre": "Pedro Sánchez", "email": "pedro.sanchez@dominio.net"},
    {"nombre": "Laura Fernández", "email": "laura.fernandez@web.org"},
    {"nombre": "Miguel Ramírez", "email": "miguel.ramirez@example.com"},
    {"nombre": "Sofía Torres", "email": "sofia.torres@test.com"},
    {"nombre": "David Díaz", "email": "david.diaz@dominio.net"},
    {"nombre": "Carmen Ruiz", "email": "carmen.ruiz@web.org"},
    {"nombre": "Javier Morales", "email": "javier.morales@example.com"}
]

libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "cantidad": 2},
    {"titulo": "1984", "autor": "George Orwell", "cantidad": 1},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "cantidad": 3},
    {"titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "cantidad": 1},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "cantidad": 2},
    {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "cantidad": 3},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "cantidad": 1},
    {"titulo": "Crimen y Castigo", "autor": "Fiódor Dostoyevski", "cantidad": 2},
    {"titulo": "La Odisea", "autor": "Homero", "cantidad": 3},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "cantidad": 1},
    {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "cantidad": 2},
    {"titulo": "En busca del tiempo perdido", "autor": "Marcel Proust", "cantidad": 1},
    {"titulo": "El nombre de la rosa", "autor": "Umberto Eco", "cantidad": 3},
    {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "cantidad": 2},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "cantidad": 1},
    {"titulo": "Matar a un ruiseñor", "autor": "Harper Lee", "cantidad": 3},
    {"titulo": "Los Miserables", "autor": "Victor Hugo", "cantidad": 2},
    {"titulo": "La Metamorfosis", "autor": "Franz Kafka", "cantidad": 1},
    {"titulo": "El Retrato de Dorian Gray", "autor": "Oscar Wilde", "cantidad": 3},
    {"titulo": "Un mundo feliz", "autor": "Aldous Huxley", "cantidad": 2},
    {"titulo": "El Alquimista", "autor": "Paulo Coelho", "cantidad": 1},
    {"titulo": "Cumbres Borrascosas", "autor": "Emily Brontë", "cantidad": 3},
    {"titulo": "Drácula", "autor": "Bram Stoker", "cantidad": 2},
    {"titulo": "El Código Da Vinci", "autor": "Dan Brown", "cantidad": 1},
    {"titulo": "Sapiens", "autor": "Yuval Noah Harari", "cantidad": 3},
    {"titulo": "La Divina Comedia", "autor": "Dante Alighieri", "cantidad": 2},
    {"titulo": "Frankenstein", "autor": "Mary Shelley", "cantidad": 1},
    {"titulo": "El viejo y el mar", "autor": "Ernest Hemingway", "cantidad": 3},
    {"titulo": "Hamlet", "autor": "William Shakespeare", "cantidad": 2},
    {"titulo": "Madame Bovary", "autor": "Gustave Flaubert", "cantidad": 1}
]

def main() -> None:
    user_lib_manager = UserLibraryManager()
    for element in usuarios:
        print(user_lib_manager.add_user(element["nombre"], element["email"]))
    book_manager = BookManager()
    for element in libros:
        print(book_manager.add_book(title=element["titulo"], author=element["autor"], ncopies=element["cantidad"]))
    #user_lib_manager.show_list()
    #book_manager.show_stock()
    while True:
        print("\nBienvenido al servicio de gestión de la librería.\nSeleccione la operación a realizar.")
        print("1.- Para añadir libro.")
        print("2.- Para añadir usuario.")
        print("3.- Para sacar un libro.")
        print("4.- Para devolver un libro.")
        print("5.- Para buscar un libro.")
        print("6.- Para buscar un usuario.")
        print("7.- Para listar los libros.")
        print("8.- Para listar los usuarios.")
        print("0.- Para terminar la sesion.")
        option = (input("Opcion: ")).strip()
        print(option)

        match option:
            case "1":
                title = (input("\nIngrese el título del libro: ")).strip().title()
                author = (input("Ingrese el autor del libro: ")).strip().title()
                ncopies = (input("Ingrese número de copias: ")).strip()
                if ncopies == "":
                    ncopies = 0
                else:
                    ncopies = int(ncopies)
                print(book_manager.add_book(title=title, author=author, ncopies=ncopies))
            case "2":
                name = (input("\nIngrese el nombre del usuario: ")).strip().title()
                email = (input("Ingrese email del usuario: ")).strip()
                print(user_lib_manager.add_user(name, email))
            case "3":
                title = (input("\nIngrese el título del libro: ")).strip().title()
                borrowed, mensage = book_manager.borrow_book(title, True)
                if borrowed:
                    name = (input("\nIngrese el nombre del usuario: ")).strip().title()
                    user_lib_manager.borrow_book(name, title, True)
                    print(mensage)
                else:
                    print(mensage)
            case "4":
                title = (input("\nIngrese el título del libro: ")).strip().title()
                borrowed, mensage = book_manager.borrow_book(title, False)
                if borrowed:
                    name = (input("\nIngrese el nombre del usuario: ")).strip().title()
                    user_lib_manager.borrow_book(name, title, False)
                    print(mensage)
                else:
                    print(mensage)
            case "5":
                title = (input("\nIngrese el título del libro a buscar: ")).strip().title()
                print(book_manager.search_book(search_title=title))
            case "6":
                name = (input("\nIngrese el nombre del usuario: ")).strip().title()
                print(name)
                print(user_lib_manager.search_user(search_name=name))
            case "7":
                book_manager.show_stock()
            case "8":
                user_lib_manager.show_list()
            case "0":
                print("\nHasta la próxima.")
                break

if __name__ == '__main__':
    main()
