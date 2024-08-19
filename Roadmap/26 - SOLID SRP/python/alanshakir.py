"""
/*
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
 */
"""

#incorrecta

class Employees:

    def __init__(self) -> None:
        self.dni
        self.name
        self.surname
        self.birthdate
        self.date_of_hire
        
    
    def employee(self, dni, name, surname, birthdate, date_of_hire):
        self.dni = dni
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.date_of_hire = date_of_hire
        

    def salary(self, dni, hours_worked, hours_price):
        return f"El salario del {dni} es: {hours_worked * hours_price}"
    
    def vacations(self, dni, start_time, end_time):
        return f"Dias de vacaciones pendientes para {dni} es: {end_time-start_time}"

#Correcta
class Employees:

    def __init__(self) -> None:
        self.dni
        self.name
        self.surname
        self.birthdate
        self.date_of_hire
        
    
    def employee(self, dni, name, surname, birthdate, date_of_hire):
        self.dni = dni
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.date_of_hire = date_of_hire

class payroll:
    def __init__(self) -> None:
        self.hours_worked
        self.hours_price
        self.start_time
        self.end_time
        DAYSVACATION = 21  #vacaciones proporcionadas por la empresa
    
    def salary(self, hours_worked, hours_price):
        return f"El salario es: {hours_worked * hours_price}"
    
    def vacations(self, start_time,end_time):
        return f"Dias de vacaciones a disfrutar {end_time-start_time}"
    
    def pending_vacancies(self, start_time,end_time, DAYSVACATION):
        return f"Cantidad de dias pendientes de vacaciones: {DAYSVACATION -(end_time-start_time) }"
    
#EXTRA

class LibraryManager:

    def __init__(self) -> None:
        self.list_book = {}
        self.list_users = {}
        self.list_loans = {}
        
    def add_book(self, title, author, copies):
        if title in self.list_book:
            print(f"Titulo {title} ya existe")
            return
        self.list_book[title] = {"author": author,
                                 "copies": copies}
        print(f"Titulo {title} fue agregado correctamente")
    
    def add_user(self, name, dni, email):
        if name in self.list_users:
            print(f"Usuario {name} ya se encuentra registrado")
            return
        self.list_users[name] = {"dni": dni, 
                                 "email": email}
        print(f"Usuario {name} fue agregado correctamente")

    def process_loans(self,dni, titles):
        for title, copies in self.list_book.items():
            if title == titles and copies['copies'] > 0:
                self.list_loans[dni] =  titles
                print(f"Libro {title} fue prestado al dni {dni} y quedan {copies['copies']-1} disponibles")
                return
        print(f"No exiten copias disponibles para el Libro {title}")
    
    def return_loans(self, dni, title):
        for dnis, titles in self.list_loans.items():
            if dnis == dni and titles == title:
                del self.list_loans[dni]
                for titles, copies in self.list_book.items():
                    if titles == title:
                        print(f"Libro {title} fue devuelto por el id {dni}, quedan {copies['copies']} disponibles")
                        return
        print(f"No exite prestamo para el Libro {title}")

library = LibraryManager()
library.add_user("alan", 124578, "alan2085@gmail.com")
library.add_user("alan", 124578, "alan2085@gmail.com")
library.add_book("La culpa es de la vaca", "Jaime Lopera", 5)
library.add_book("Clean Code", "Robert Martin", 10)
library.process_loans(124578, "La culpa es de la vaca")
library.process_loans(2124578, "Clean Code")
library.return_loans(2124578, "Clean Code")
library.return_loans(124578, "La culpa es de la vaca")


#Aplicando principio Single Responsibility Principle, SRP

class Book:
    def __init__(self) -> None:
        self.list_book = {}
    
    def add_book(self, title, author, copies):
        if title in self.list_book:
            print(f"Titulo {title} ya existe")
            return
        self.list_book[title] = {"author": author,
                                 "copies": copies}
        print(f"Titulo {title} fue agregado correctamente")
    
    def search_book(self, title):
        for titles, book in self.list_book.items():
            if titles == title:
                return titles, book
        print(f"Titulo {title} no fue encontrado")

class User:
    def __init__(self) -> None:
        self.list_user = {}
    
    def add_user(self, name, dni, email):
        if name in self.list_user:
            print(f"Usuario {name} ya se encuentra registrado")
            return
        self.list_user[dni] = {"name": name, 
                                 "email": email}
        print(f"Usuario {name} fue agregado correctamente")
    
    def search_user(self , dni):
        for dnis, user in self.list_user.items():
            if dnis == dni:
                return dnis, user
        print(f"Identificador {dni} no fue encontrado")

class LibraryManager:
    def __init__(self, book_manager, user_manager) -> None:
        self.list_loans = {}
        self.book_manager = book_manager
        self.user_manager = user_manager

    def process_loans(self,dni, titles):
        book = self.book_manager.search_book(titles)
        user = self.user_manager.search_user(dni)
        if user and book and book[1]['copies'] > 0:
            self.list_loans[dni] =  titles
            book[1]['copies'] -= 1
            print(f"Libro {titles} fue prestado al dni {dni} y quedan {book[1]['copies']} disponibles")
            return
        print(f"Ha ocurrido un error")
    
    def return_loans(self, dni, title):
        for dnis, titles in self.list_loans.items():
            if dnis == dni and titles == title:
                del self.list_loans[dni]
                book = self.book_manager.search_book(title)
                if book:
                    book[1]['copies']+=1
                    print(f"Libro {title} fue devuelto por el id {dni}, quedan {book[1]['copies']} disponibles")
                    return
        print(f"Ha ocurrido un error al retornar el libro")
book_manager = Book()
book_manager.add_book("La culpa es de la vaca", "Jaime Lopera", 15)
book_manager.add_book("El programador pragmatico", "Andrew Hunt", 20)

user_manager = User()
user_manager.add_user("alan", 123456, "alan2085@gmail.com")
user_manager.add_user("matheo", 852963, "matheo0301@gmail.com")

library_manager = LibraryManager(book_manager, user_manager)
library_manager.process_loans(123456, "El programador pragmatico")
library_manager.process_loans(852963, "El programador pragmatico")
library_manager.return_loans(123456, "El programador pragmatico")
library_manager.return_loans(852963, "El programador pragmatico")
