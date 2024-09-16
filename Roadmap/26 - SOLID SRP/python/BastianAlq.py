import time
import logging
# ---------------------------------------------
# | Principio de Responsabilidad Unica (SRP)  |  Información extraída de -> https://devexpert.io/principios-solid-guia-gratis/ 
# ---------------------------------------------

# - Una clase o modulo debe tener solo una razon para cambiar
# - el SRP se cumple cuando una clase hace una única "cosa"

# ¿CÓMO DETECTAR QUE SE ESTA VIOLANDO EL PRINCIPIO DE RESPONSABILIDAD ÚNICA? aquí algunos puntos para guiarse
# R. se pueden detectar situaciones en las que se viola el principio como por ejemplo:
# - cuando en una misma clase se involucran dos capas de arquitectura | (Ej: mezclar capa logica de negocio y persistencia)
# - numero de metodos publicos | (si la clase tiene muchos metodos, posiblemente tenga muchas responsabilidades)
# - numero de imports | (si se importan demasiadas clases, es posible que se este haciendo trabajo demas)
# - cuesta testear la clase | (si no es posible hacer test unitarios, es posible replantear en dividir la clase en dos )
# - cada vez que se se escribe una nueva funcionalidad, la clase se ve afectada | 
#  (si la clase se modifica a menudo, es porque esta involucrada en demasiadas cosas)
# - numero de lineas. (Si la clase es demasiado grande, dividir en clases mas manejables)


#  -------------------------- INICIO FUNCIONAMIENTO INCORRECTO DEL SRP --------------------------
#   en este ejemplo se esta mezclando la logica de negocio con la de presentación
#   posible problema: si se quiere mostrar de otra forma los datos del vehiculo (texto plano, html, etc)
#   la clase Vehicle tendrá dos responsabilidades, la cual es:
#       (1) representar los datos del objeto
#       (2) mostrarlos en distintos formatos
#
#

print("------------ FUNCIONAMIENTO INCORRECTO ------------")
class Vehicle:
    
    def __init__(self,wheelCount,maxSpeed) -> None:
        self.wheelCount = wheelCount
        self.maxSpeed = maxSpeed
    
    def printVehicle(self):
        print(f"wheelCount = {self.wheelCount}, maxSpeed = {self.maxSpeed} km/h")


vehicle = Vehicle(4,120)
vehicle.printVehicle()

#  -------------------------- FIN FUNCIONAMIENTO CORRECTO DEL SRP --------------------------

time.sleep(2)

#  -------------------------- INICIO FUNCIONAMIENTO CORRECTO DEL SRP --------------------------
#   Solución: 
#   Crear una clase VehiclePrinter que reciba el objeto vehiculo para mostrar sus datos.
#   al realizar esto, la clase Vehicle solo se encargará de representar los datos del vehiculo 
#   y la clase VehiclePrinter solo se encargará de mostrar los datos del vehiculo en distintos formatos.

print("------------ FUNCIONAMIENTO CORRECTO ------------")
class Vehicle:
    def __init__(self,wheelCount,maxSpeed) -> None:
        self.wheelCount = wheelCount
        self.maxSpeed = maxSpeed

class VehiclePrinter:
    
    @staticmethod
    def printVehicle(vehicle: Vehicle):
        print(f"wheelCount = {vehicle.wheelCount}, maxSpeed = {vehicle.maxSpeed} km/h")
        
    def printVehicleHtml(vehicle: Vehicle):
        print("Renderizar datos en un html")
    
    # etc...
vehicle = Vehicle(2,200)
vehiclePrinter = VehiclePrinter()
vehiclePrinter.printVehicle(vehicle)

#  -------------------------- FIN FUNCIONAMIENTO CORRECTO DEL SRP --------------------------


#  DIFICULTAD EXTRA (opcional):
#  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
#  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
#  * y el procesamiento de préstamos de libros.
#  * Requisitos:
#  * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
#  * información básica como título, autor y número de copias disponibles.
#  * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
#  * información básica como nombre, número de identificación y correo electrónico.
#  * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
#  * tomar prestados y devolver libros.
#  * Instrucciones:
#  * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
#  * los tres aspectos mencionados anteriormente (registro de libros, registro de
#  * usuarios y procesamiento de préstamos).
#  * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
#  * siguiendo el Principio de Responsabilidad Única.
#  *


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.StreamHandler()])

#     _____________________
#     |                    |
#     | Dificultad Extra   |
#     |____________________|
#
#    Sistema gestion de prestamos de libros y de usuarios
#    Incumplimiento de SRP

print("Dificultad extra")
print("---------- FORMA INCORRECTA ----------")

class Library:
    
    def __init__(self) -> None:
        
        self.books = []
        self.users = []
        self.loans = []
        pass
    
    def addNewBook(self, title: str , author: str , copies: int):
        self.books.append({"title": title , "author": author, "copies": copies})
        logging.info(f"El libro {title} se ha añadido correctamente")
    
    def addNewUser(self, userId: int, name: str, email: str):
        self.users.append({"id": userId, "name": name, "email": email})
        logging.info(f"Usuario {name} registrado correctamente")
    
    def lendBook(self, bookTitle: str, userId: int):
        for book in self.books:
            if book["title"] == bookTitle and book["copies"] >0:
                book["copies"] -= 1
                self.loans.append({"userId": userId, "bookTitle": bookTitle})
                logging.info(f"Se ha prestado el libro {bookTitle} al usuario con id {userId}")
    
    
    def returnBook(self, bookTitle: str, userId: str):
        for loan in self.loans:
            if loan["userId"] == userId and loan["bookTitle"] == bookTitle:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == bookTitle:
                        book["copies"] +=1
                        logging.info(f"el libro {bookTitle} ha sido devuelto por el usuario con id: {userId}")

library = Library()
library.addNewBook("Habitos atomicos", "James Clear",6)
library.addNewUser(12,"Pedro", "pedro@gmail.com")
library.lendBook("Habitos atomicos",12)
library.returnBook("Habitos atomicos",12)


print("---------- FORMA CORRECTA ----------")


class User:
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email

class Book: 
    def __init__(self, title: str, author: str, copies: int) -> None:
        self.title = title
        self.author = author
        self.copies = copies


class UserService:
    def __init__(self) -> None:
        self.users = []
    
    def addUser(self, user: User):
        self.users.append(user)
        return True
        
        
    def findUserById(self, id: int):
        for user in self.users:
            if user.id == id:
                return user
        return None
    

class BookService:
    def __init__(self) -> None:
        self.books = []
        
    def addBook(self, book: Book):
        self.books.append(book)
        return True
        
    
    def findBookByTitle(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None
        
class Loan:
    def __init__(self) -> None:
        self.loans = []
        
    
    def loanBook(self, user: User, book: Book):
        if book.copies > 0:
            self.loans.append({"userId": user.id, "bookTitle": book.title})
            book.copies -= 1
            return True
        return False
        
    
    def returnBook(self, user: User, book: Book):
        for loan in self.loans:
            if loan["userId"] == user.id and loan["bookTitle"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
                
        return False
    
class Library:
    def __init__(self) -> None:
        self.loanService = Loan()
        self.bookService = BookService()
        self.userService = UserService()
        
    def loanBook(self, userId: int, bookTitle: str):
        added = False
        user = self.userService.findUserById(userId)
        book = self.bookService.findBookByTitle(bookTitle)
        if user and book:
                added = self.loanService.loanBook(user,book)
                if added:
                    logging.info(f"Se ha registrado un prestamo del libro {book.title} al usuario {user.name}")
                else:
                    logging.error("el libro esta agotado")
        else:
            logging.error("usuario o libro no existen")
                    
    
    def returnBook(self, userId: int, bookTitle: str):
        user = self.userService.findUserById(userId)
        book = self.bookService.findBookByTitle(bookTitle)
        if user and book:
            returned = self.loanService.returnBook(user,book)
            if returned:
                logging.info(f"el usuario {user.name} ha devuelto el libro {book.title}")
            else:
                logging.error(f"No se encontró prestamo del usuario {user.name} con el libro {book.title}")
        else:
            logging.error("el libro o usuario no existen")
            
    def addUser(self, user: User):
        self.userService.addUser(user)
        logging.info(f"Usuario {user.name} añadido correctamente")
    
    def addBook(self, book: Book):
        self.bookService.addBook(book)
        logging.info(f"Libro {book.title} añadido correctamente")
        

time.sleep(2)


library = Library()
library.addBook(Book("Habitos atomicos", "James Clear", 10))
library.addUser(User(23,"Pedro Pablo","pp@gmail.com"))

library.loanBook(23,"Habitos atomicos")
library.returnBook(23,"Habitos atomicos")
library.returnBook(23,"Habitos atomicos")
library.loanBook(23,"Perico trepa por Chile")