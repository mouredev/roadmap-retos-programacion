

print("\n\n=======================================EJERCICIOa=======================================\n\n")

"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Unica (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# * Ejemplo sin aplicar el principio "SRP". La clase tiene la responsabilidad sobre cualquier cambio que queramos hacer
    

class MouredevAcademy:

    def __init__(self) -> None:
        self.students = []
        
    def auth(self, name: str, password: str):
        self.name = name
        self.password = password
        
    def students_db(self, id: int, username: str, name: str, surname: str, email: str):
        self.id = id
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        
    def subs_type(self, monthly: any, quarterly: any, half_yearly: any, yearly: any):
        self.monthly = monthly
        self.quarterly = quarterly
        self.half_yearly = half_yearly
        self.yearly = yearly
        
    def payment(self, credit_card: dict, debit_card: dict, bizum: dict, bank_transfer: dict):
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.bizum = bizum
        self.bank_transfer = bank_transfer
        

# * Aplicando el principio "SRP"


class auth:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password
        
    def authenticate():
        # Logica de autenticacion
        pass
        
class Student:
    def __init__(self, id: int, username: str, name: str, surname:str, email: str):
        self.id = id
        self.username = username
        self.name = name
        self.surname = surname
        self.email = email
        
class Subscription:
    def __init__(self, monthly: any, quarterly: any, half_yearly: any, yearly: any):
        self.monthly = monthly
        self.quarterly = quarterly
        self.half_yearly = half_yearly
        self.yearly = yearly
        
class Payment:
    def __init__(self, credit_card: dict, debit_card: dict, bizum: dict, bank_transfer: dict):
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.bizum = bizum
        self.bank_transfer = bank_transfer
        
    def process_payment(self):
        # Logica de procesamiento de pagos
        pass
    
class MouredevAcademy:
    def __init__(self):
        self.students = []
        self.subscription = []
        self.payment = []
        
    def add_students(self, student: Student):
        self.students.append(student)
        
    def add_subscription(self, subscription: Subscription):
        self.subscription.append(subscription)
        
    def add_payment(self, payment: Payment):
        self.payment.append(payment)
         
    



print("\n\n=======================================DIFICULTAD EXTRA SIN 'SRP'=======================================\n\n")

"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestionn para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestion de usuarios
 * y el procesamiento de prestamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
 * informacion basica como ti­tulo, autor y numero de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * informacion basica como nombre, numero de identificacion y correo electronico.
 * 3. Procesar prestamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseñ±a una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de prestamos).
 * 2. Refactoriza el codigo: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Ãšnica.
"""

# * Ejemplo sin aplicar el principio "SRP"


class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.lending = []
    
    def add_book(self, title: str, author: str, n_copies: int):

        new_book = {"title": title, "author": author, "n_copies": n_copies}    
        self.books.append(new_book)
        print(f"[+] Se ha aÃ±adido {new_book} a la biblioteca")
        
        book_found = False
        for book in self.books:
            if book["title"] == title:
                book["n_copies"] += n_copies
                book_found = True
                print(f"Ahora hay {n_copies} en la biblioteca del libro {title}")
            else:
                n_copies += 1
                print(f"Hay un titulo nuevo en la biblioteca: {title}")
    
    def add_user(self, name: str, user_id: int, email: str):
        
        new_user = {"name": name, "id": user_id, "email": email }
        
        if new_user not in self.users:
            self.users.append(new_user)
            print(f"[+] Se ha aÃ±adido el nuevo usuario {new_user} a la biblioteca")
        else:
            print(f"[!] {new_user} ya es usuario de la biblioteca")
    
    def book_lending(self, title: str, user_id: int):
        
        user_found = False
        for user in self.users:
            if user["id"] == user_id:
                user_found = True
                break
            
        if not user_found:
            print("[!] No estas registrado en la biblioteca, no puedes llevarte ningun libro")
            return
                
        for book in self.books:
            if book["title"] == title:
                if book["n_copies"] > 0:
                    book["n_copies"] -= 1
                    print(f"[!] El usuario con el id {user_id} ha recogido el libro {title}")
                else: 
                    print(f"[!] Ahora mismo no hay ninguna copia disponible del libro {title}")
                return
            
        print(f"[!] El libro {title} no lo tenemos en la biblioteca")
                

my_library = Library()

my_library.add_book("git & github desde cero", "Brais Moure", 4)
my_library.add_book("Codigo limpio", "Robert C. Martin", 2)
my_library.add_book("Ultimate Python", "Nicolas shurmann", 3)

my_library.add_user("Rantam", 1, "rantam@rantam.com")
my_library.add_user("Pablo", 2, "Pablo@rantam.com")

print(f"[+] Libros en la biblioteca: {my_library.books}")
print(f"[+] Usuarios de la biblioteca: {my_library.users}")

my_library.book_lending("git & github desde cero", 1)
my_library.book_lending("Codigo limpio", 2)
my_library.book_lending("git & github desde cero", 3)
my_library.book_lending("Ultimate Python", 1)

print(f"[+] Libros en la biblioteca: {my_library.books}")


print("\n\n=======================================DIFICULTAD EXTRA CON 'SRP'=======================================\n\n")


# * Ejemplo aplicando el principio "SRP"


class Book:
    def __init__(self, title: str, author: str, n_copies: int):
        self.title = title
        self.author = author
        self.n_copies = n_copies
        
    def lend_book(self):
        if self.n_copies > 0:
            self.n_copies -= 1
            return True
        return False
    
    def return_book(self):
        self.n_copies += 1
    
class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.user_id = user_id
        self.email = email



class Library:
    def __init__(self):
        self.books = []
        self.users = []
                
    def add_book(self, book: Book):
        self.books.append(book)
        print(f"[+] Se ha aÃ±adido {book.title} a la biblioteca")
        
    def add_user(self, user: User):
        if user not in self.users:
            self.users.append(user)
            print(f"[+] Se ha aÃ±adido el nuevo usuario {user.name} a la biblioteca")
        else:
            print(f"[!] {user.name} ya es usuario de la biblioteca")
    

        
    
class BookLending:
    def __init__(self, library: Library):
        self.library = library
        self.lending_records = []
        
    def lend_book(self, title: str, user_id: int):
        
        user_found = False
        for user in self.library.users:
            if user.user_id == user_id:
                user_found = True
                break
            
        if not user_found:
            print("[!] No estas registrado en la biblioteca, no puedes llevarte ningun libro")
            return
                
        for book in self.library.books:
            if book.title == title:
                if book.lend_book():
                    self.lending_records.append((title, user_id))
                    print(f"[!] El usuario con el id {user_id} ha recogido el libro {title}")
                else: 
                    print(f"[!] Ahora mismo no hay ninguna copia disponible del libro {title}")
                return
            
        print(f"[!] El libro {title} no lo tenemos en la biblioteca")
        
    def return_book(self, title: str, user_id: int):
        if (title, user_id) in self.lending_records:
            for book in self.library.books:
                if book.title == title:
                    book.return_book()
                    self.lending_records.remove((title, user_id))
                    print(f"[+] El ususario con el id {user_id} ha devuelto el libro {title}")
                    return
        print(f"[!] No se encontro el registro de prestamo para el libro {title} por el usuario con el id {user_id}")
                

my_library = Library()

book1 = Book("git & github desde cero", "Brais Moure", 4)
book2 = Book("Codigo limpio", "Robert C. Martin", 2)
book3 = Book("Ultimate Python", "Nicolas shurmann", 3)

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

user1 = User("Rantam", 1, "rantam@rantam.com")
user2 = User("Pablo", 2, "Pablo@rantam.com")

my_library.add_user(user1)
my_library.add_user(user2)

book_lending = BookLending(my_library)


print(f"[+] Libros en la biblioteca: {[book.title for book in my_library.books]}")
print(f"[+] Usuarios de la biblioteca: {[user.name for user in my_library.users]}")

book_lending.lend_book("git & github desde cero", 1)
book_lending.lend_book("Codigo limpio", 2)
book_lending.lend_book("git & github desde cero", 3)

book_lending.return_book("git & github desde cero", 1)
book_lending.return_book("Codigo limpio", 2)
book_lending.return_book("git & github desde cero", 3)


print(f"[+] Libros en la biblioteca: {[book.title for book in my_library.books]}")
