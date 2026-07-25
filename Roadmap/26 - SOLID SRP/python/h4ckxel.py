"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
#EJEMPLO INCORRECTO
class Book2():
    def __init__(self,name:str,price:float,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def print_invoice(self): #si quisiéramos cambiar el formato de impresión, hay que modificar la clase
        print(f"FACTURA DEL LIBRO \"{self.name.upper()}\"\n\n - Precio(s.IVA): {self.price} EUR || Precio (IVA incl.): {self.price*1.04} EUR\n\n ---- TOTAL: {self.price*1.04*self.quantity} EUR")
        
book2 = Book2("El Señor de los Anillos",25,2)
book2.print_invoice()

#EJEMPLO CORRECTO
class Book1(): #clase responsable de crear el libro que vas a comprar (nombre, precio y unidades)
    def __init__(self,name:str,price:float,quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

class BookInvoice(): #clase encargada de imprimir la factura de los libros que vas a comprar
    def __init__(self,book:Book1):
        self.book = book

    def print_invoice(self):
        print(f"FACTURA DEL LIBRO \"{self.book.name.upper()}\"\n\n - Precio(s.IVA): {self.book.price} EUR || Precio (IVA incl.): {self.book.price*1.04} EUR\n\n ---- TOTAL: {self.book.price*1.04*self.book.quantity} EUR")

book = Book1("El Señor de los Anillos",25,3)
book_invoce = BookInvoice(book)
book_invoce.print_invoice()
print("\n")

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
import logging
from time import time,sleep
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s -- %(levelname)s - %(message)s",
                    datefmt="%d/%m/%Y - %H:%M:%S",
                    handlers=[logging.StreamHandler()])

def books_number_decorator1(function):
    def original_function(library):
        result = function(library)
        logging.debug(f"Hay almacenados {len(library.books)} libro(s) en la biblioteca")
        return result
    return original_function

def users_number_decorator1(function):
    def original_function(library):
        result = function(library)
        logging.debug(f"Hay {len(library.users)} usuarios almancenados en el sistema")
        return result
    return original_function
"""
#1 - NO CUMPLE SRP
class Library1():
    def __init__(self):
            self.books=list()
            self.users=list()

    @books_number_decorator1
    def register_book(self):
        book = {"name":str(""),
                "author":str(""),
                "copies":int(0)}
        book["name"] = input("Introduce el nombre del libro: ")
        for element in self.books:
            if element["name"] == book["name"]:
                logging.warning("Ya existe un libro almacenado con este título") #posibilidad de pedirle al usuario que añada las unidades?
                break
        else:
            book["author"] = input("Ahora introduce el nombre del autor del libro: ")
            book["copies"] = int(input("Y para acabar introduce el número de copias de las que disponemos: "))
            self.books.append(book)

    @users_number_decorator1
    def register_user(self):
        user = {"name":str(""),
                "id_number":int,
                "email":"str"}
        user["name"] = input("Introduce el nombre del usuario a agregar: ")
        for element in self.users:
            if element["name"] == user["name"]:
                logging.warning("El usuario ya existe en el sistema")
                break
        else:
            user["id_number"] = int(input("Introduce ahora el número de identificación: "))
            user["email"] = input("Y para acabar el email: ")
            self.users.append(user)

    def __find_user(self,id):
        for element in self.users:
            if element["id_number"] == id:
                return True
        else:
            return False

    @books_number_decorator1
    def pick_book(self):
        if len(self.users) == 0:
            logging.warning("No hay usuarios en el sistema")
            print("No es posible sacar préstamos porque no hay usuarios registrados en el sistema")
        else:
            id = int(input("Para poder sacar un préstamo, por favor, introduce tu número de identificación: "))
            logging.debug(f"El usuario existe: {self.__find_user(id)}")
            if self.__find_user(id):
                book_name = input("Introduce por favor el título del libro que quieres sacar de préstamo: ")
                for element in self.books:
                    if element["name"] == book_name:
                        logging.debug("Libro encontrado")
                        if element["copies"] == 0:
                            logging.warning(f"No hay unidades de {book_name}")
                            print(f"No hay libros disponnibles del título {book_name}")
                            break
                        else:
                            print(f"Entendido sacarás de préstamo el libro {book_name}")
                            element["copies"] -= 1
                            break
                else:
                    logging.warning("Título no disponible")
                    print ("No tenemos ese título en la biblioteca, por tanto no se puede sacar de préstamo")
            else:
                logging.info("El usuario no está dado de alta")
                new_user_option = input("Parece que no hay ningún usuario dado de alta con ese id. ¿Quieres registrarlo?(S/N): ").upper()
                if new_user_option == "S":
                    logging.debug("Registrando nuevo usuario")
                    self.register_user()
                else:
                    print("Entendido")
            
    @books_number_decorator1
    def return_book(self):
        if len(self.users) == 0:
            logging.warning("No hay usuarios en el sistema")
            print("No es posible devolver ningún libro porque no hay usuarios registrados en el sistema")
        else:
            id = int(input("Para poder sacar un préstamo, por favor, introduce tu número de identificación: "))
            logging.debug(f"El usuario existe: {self.__find_user(id)}")
            if self.__find_user(id):
                book_name = input("Introduce por favor el título del libro a devolver: ")
                for element in self.books:
                    if element["name"] == book_name:
                        logging.debug("Libro encontrado")
                        element["copies"] +=1
                        break
                else:
                    logging.warning("El título no pertenece a esta biblioteca")
                    new_book_option = input("El libro que estás tratando de devolver no es un título de esta biblioteca ¿Quieres añadirlo?(S/N): ").upper()
                    if new_book_option == "S":
                        logging.debug("registrando nuevo libro")
                        self.register_book()
                    else:
                        print("Entendido")
            else:
                print("Parece que no hay ningún usuario dado de alta con ese id, por tanto no es posible devolver ningún libro.")
    
    def show_books(self):
        if len(self.books) == 0:
            logging.warning("No hay libros en la biblioteca")
            print("No hay ningún libro almacenado en la biblioteca")
        else:
            for element in self.books:
                print(element)

    def show_users(self):
        if len(self.users) == 0:
            logging.warning("No hay usuarios registrados")
            print("No hay usuarios registrados en la biblioteca")
        else:
            for element in self.users:
                print(element)

my_library_1 = Library1()
print("------- Te doy la bievnenida al sistema de la Biblioteca NO-SRP -------")
while True:
    option = input("¿Que deseas hacer?:\n- Registrar un nuevo libro(L)\n- Registrar un nuevo usuario/a(U)\n- Sacar un préstamo(P)\n- Devolver un préstamo(D)\n- Mostrar todos los libros(M)\n- Mostrar todos los usuarios/as(A)\n- Salir(S)\n-----> ").upper()
    if option == "L":
        my_library_1.register_book()
    elif option == "U":
        my_library_1.register_user()
    elif option == "P":
        my_library_1.pick_book()
    elif option == "D":
        my_library_1.return_book()
    elif option == "M":
        my_library_1.show_books()
    elif option == "A":
        my_library_1.show_users()
    elif option == "S":
        print("Gracias por usar el sistema de la Biblioteca NO-SRP")
        break
    else:
        logging.warning("Opción no válida")
        print("La opción que has elegido no es válida, prueba de nuevo: ")"""

#CUMPLE CON SRP

def books_number_decorator(function):
    def original_function(reg_book):
        result = function(reg_book)
        if type(reg_book) == Library:
            logging.debug(f"Hay almacenados {len(reg_book.books)} libro(s) en la biblioteca")
        else:
            logging.debug(f"Hay almacenados {len(reg_book.library.books)} libro(s) en la biblioteca")
        return result
    return original_function

def users_number_decorator(function):
    def original_function(reg_user):
        result = function(reg_user)
        if type(reg_user) == Library:
            logging.debug(f"Hay almacenados {len(reg_user.books)} libro(s) en la biblioteca")
        else:
            logging.debug(f"Hay {len(reg_user.library.users)} usuarios almancenados en el sistema")
        return result
    return original_function

class Book():
    def __init__(self,name,author,copies) -> None:
        self.name:str = name
        self.author:str = author
        self.copies:int = copies

    def show_data(self):
        print(f"- Título: {self.name}\n- Author: {self.author}\n- Copias Disponibles: {self.copies}")
        print("\n")

class User():
    def __init__(self,name,id_number,email) -> None:
        self.name:str = name
        self.id_number:int = id_number
        self.email:str = email

    def show_data(self):
        print(f"- Nombre: {self.name}\n- ID: {self.id_number}\n- Email: {self.email}")
        print("\n")

class Library():
    def __init__(self):
        self.books = list()
        self.users = list()

    def show_books(self):
        if len(self.books) == 0:
            logging.warning("No hay libros en la biblioteca")
            print("No hay ningún libro almacenado en la biblioteca")
        else:
            for element in self.books:
                element.show_data()
    
    def show_users(self):
        if len(self.users) == 0:
            logging.warning("No hay usuarios registrados")
            print("No hay usuarios registrados en la biblioteca")
        else:
            for element in self.users:
                element.show_data()

class Loan():
    def __init__(self,library:Library):
        self.library = library

    def __find_user(self,id):
        for element in self.library.users:
            if element.id_number == id:
                return True
        else:
            return False
    
    def pick_book(self):
        if len(self.library.users) == 0:
            logging.warning("No hay usuarios en el sistema")
            print("No es posible sacar préstamos porque no hay usuarios registrados en el sistema")
        else:
            id = int(input("Para poder sacar un préstamo, por favor, introduce tu número de identificación: "))
            logging.debug(f"El usuario existe: {self.__find_user(id)}")
            if self.__find_user(id):
                book_name = input("Introduce por favor el título del libro que quieres sacar de préstamo: ")
                for element in self.library.books:
                    if element.name == book_name:
                        logging.debug("Libro encontrado")
                        if element.copies == 0:
                            logging.warning(f"No hay unidades de {book_name}")
                            print(f"No hay libros disponnibles del título {book_name}")
                            break
                        else:
                            print(f"Entendido sacarás de préstamo el libro {book_name}")
                            element.copies -= 1
                            break
                else:
                    logging.warning("Título no disponible")
                    print ("No tenemos ese título en la biblioteca, por tanto no se puede sacar de préstamo")
            else:
                logging.info("El usuario no está dado de alta")
                new_user_option = input("Parece que no hay ningún usuario dado de alta con ese id. ¿Quieres registrarlo?(S/N): ").upper()
                if new_user_option == "S":
                    logging.debug("Registrando nuevo usuario")
                    new_user = Register_User(self)
                    new_user.register_user()
                else:
                    print("Entendido")

    def return_book(self):
        if len(self.library.users) == 0:
            logging.warning("No hay usuarios en el sistema")
            print("No es posible devolver ningún libro porque no hay usuarios registrados en el sistema")
        else:
            id = int(input("Para poder devolver un préstamo, por favor, introduce tu número de identificación: "))
            logging.debug(f"El usuario existe: {self.__find_user(id)}")
            if self.__find_user(id):
                book_name = input("Introduce por favor el título del libro a devolver: ")
                for element in self.library.books:
                    if element.name == book_name:
                        logging.debug("Libro encontrado")
                        element.copies += 1
                        break
                else:
                    logging.warning("El título no pertenece a esta biblioteca")
                    new_book_option = input("El libro que estás tratando de devolver no es un título de esta biblioteca ¿Quieres añadirlo?(S/N): ").upper()
                    if new_book_option == "S":
                        logging.debug("registrando nuevo libro")
                        new_book = Register_Book(self)
                        new_book.register_book()
                    else:
                        print("Entendido")
            else:
                print("Parece que no hay ningún usuario dado de alta con ese id, por tanto no es posible devolver ningún libro.")
    

class Register_Book():
    def __init__(self,library:Library) -> None:
        self.library = library

    @books_number_decorator
    def register_book(self):
        name = input("Introduce el nombre del libro: ")
        for element in self.library.books:
            if element.name == name:
                logging.warning("Ya existe un libro almacenado con este título") #posibilidad de pedirle al usuario que añada las unidades?
                break
        else:
            author = input("Ahora introduce el nombre del autor del libro: ")
            copies = int(input("Y para acabar introduce el número de copias de las que disponemos: "))
            book = Book(name,author,copies)
            self.library.books.append(book)

class Register_User():
    def __init__(self,library) -> None:
        self.library = library

    @users_number_decorator
    def register_user(self):
        name = input("Introduce el nombre del usuario a agregar: ")
        if type(self.library) == Library: #si el tipo del dato es "library"
            for element in self.library.users:
                if element.name == name:
                    logging.warning("El usuario ya existe en el sistema")
                    break
            else:  #si el tipo del dato es "loan", esto solo pasa si el usuario se registra desde la clase Loan()
                id_number = int(input("Introduce ahora el número de identificación: "))
                email = input("Y para acabar el email: ")
                user = User(name,id_number,email)
                self.library.users.append(user)
        else:
            for element in self.library.library.users:
                if element.name == name:
                    logging.warning("El usuario ya existe en el sistema")
                    break
            else:
                id_number = int(input("Introduce ahora el número de identificación: "))
                email = input("Y para acabar el email: ")
                user = User(name,id_number,email)
                self.library.library.users.append(user)

my_srp_library = Library()
register_book = Register_Book(my_srp_library)
register_user = Register_User(my_srp_library)
my_loan = Loan(my_srp_library)
print("------- Te doy la bievnenida al sistema de la Biblioteca SI-SRP -------")
while True:
    option = input("¿Que deseas hacer?:\n- Registrar un nuevo libro(L)\n- Registrar un nuevo usuario/a(U)\n- Sacar un préstamo(P)\n- Devolver un préstamo(D)\n- Mostrar todos los libros(M)\n- Mostrar todos los usuarios/as(A)\n- Salir(S)\n-----> ").upper()
    if option == "L":
        register_book.register_book()
    elif option == "U":
        register_user.register_user()
    elif option == "P":
        my_loan.pick_book()
    elif option == "D":
        my_loan.return_book()
    elif option == "M":
        my_srp_library.show_books()
    elif option == "A":
        my_srp_library.show_users()
    elif option == "S":
        print("Gracias por usar el sistema de la Biblioteca SI-SRP")
        break
    else:
        logging.warning("Opción no válida")
        print("La opción que has elegido no es válida, prueba de nuevo: ")
"""
POSIBLES MEJORAS
- Regex tanto en nombres como en los emails
- Manejo de excepciones, sobre todo en datos int.
- Dentro de usuario, parámetro "prestamo" para guardar el préstamo y no preguntarlo
"""
