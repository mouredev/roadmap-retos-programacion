"""*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
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
 *"""

#-----------------------------------------------------------------------------
#SRP Principio de responsabilidad unica 
# Las clases deben encargarse de una única responsabilidad; es decir, cada clase debe manejar una única tarea en el funcionamiento del sistema
# ----------------------------------------------------------------------------

# Ejemplo de uso incorrecto 
import random

class SensorTemperature:
    def __init__(self):
        pass  

    def read_sensor(self):
        # Simulación de lectura del sensor
        temperature = random.uniform(15.0, 50.0)
        return round(temperature , 2)
    
    def alert(self):
        temperature = self.read_sensor()
        if temperature > 35.0:
            print(f"Critical temperature state: {temperature} °C")
        else :
            print(f"Stable temperature: {temperature} °c")

sensor = SensorTemperature()
sensor.alert()

# Ejemplo de uso correcto

class ReadTemperature: 
    def __init__(self):
        pass 

    def read_sensor(self):
        # Simulación de lectura del sensor
        temperature = random.uniform(15.0, 50.0)
        return round(temperature , 2)

class AlertTemperature:
    def __init__(self):
        pass

    def alert(self, temperature):
        
        if temperature > 35.0:
            print(f"Critical temperature state: {temperature} °C")
        else :
            print(f"Stable temperature: {temperature} °c")

# Uso de las clases de manera correcta
sensor = ReadTemperature()
alert = AlertTemperature()

temperature = sensor.read_sensor()
alert.alert(temperature)


# DIFICULTAD EXTRA 

class Library :

    def __init__(self):
         self.books = []
         self.users = []
         self.borrowedBooks = []
    
    def add_books(self, title , author , copies):
        self.books.append({"Title": title, "Author": author, "Copies": copies})
    
    def add_users(self, name , Id , email):
        self.users.append({"Name": name, "Identification number": Id , "Email":email })
    
    def borrow_books(self , user , title ):

        for book in self.books :
            if book["title"] == title and book["copies"] > 0:
                book["copies"] -= 1
                self.borrowedBooks.append({"user_id": user, "book_title": title, "action": "borrow"})
                return True
        return False
    
    def return_books(self , user , title):

        for book in self.books :
            if book["title"] == title and book["Copies"] > 0:
                book["copies"] += 1
                self.borrowedBooks.append({"user_id": user, "book_title": title, "action": "borrow"})
                return True
        return False
    
# usando el principio de responsabilidad unica 
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies_available = copies

    def borrow(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return True
        else:
            return False

    def return_book(self):
        self.copies_available += 1

class User:
    def __init__(self, name, id_number, email):
        self.name = name
        self.id_number = id_number
        self.email = email

class Loan:
    def __init__(self, user, book):
        self.user = user
        self.book = book

    def borrow_book(self):
        if self.book.borrow():
            print(f"Book '{self.book.title}' borrowed successfully by {self.user.name}.")
            return True
        else:
            print("Unable to borrow the book. Please check availability.")
            return False

    def return_book(self):
        self.book.return_book()
        print(f"Book '{self.book.title}' returned successfully.")

# Ejemplo de uso
book1 = Book("El principito", "Antoine de Saint-Exupéry", 3)
book2 = Book("Cien años de soledad", "Gabriel García Márquez", 5)

user1 = User("Juan Perez", "12345", "juan@example.com")
user2 = User("María López", "54321", "maria@example.com")

loan1 = Loan(user1, book1)
loan2 = Loan(user2, book2)

# Procesar préstamos
loan1.borrow_book()  
loan2.borrow_book()  

# Devolver libros
loan1.return_book()  
