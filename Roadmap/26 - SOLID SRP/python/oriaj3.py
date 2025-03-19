"""
26 - SOLID SRP

Teoría - Single Responsibility Principle

El principio de responsabilidad única (SRP) establece que una clase debe tener una única razón para cambiar, es decir, una clase debe tener una única responsabilidad.
En otras palabras, una clase debe tener un único trabajo, una única responsabilidad, una única razón para cambiar.
Si una clase tiene más de una responsabilidad, entonces los cambios en una responsabilidad podrían afectar a las otras responsabilidades.

En este ejemplo, la clase `User` tiene dos responsabilidades:
- Crear un usuario
- Mostrar un usuario

Para cumplir con el principio de responsabilidad única, se debe dividir la clase `User` en dos clases:
- `UserCreator` que se encargará de crear un usuario
- `UserViewer` que se encargará de mostrar un usuario

El principio de responsabilidad única es uno de los cinco principios SOLID de la programación orientada a objetos.

"""
"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Clase con dos responsabilidades
class UserBad:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_user(self):
        print(f"Usuario creado: {self.name} - {self.email}")

    def show_user(self):
        print(f"Nombre: {self.name}")
        print(f"Email: {self.email}")

# Crear usuario con dos responsabilidades
userbad = UserBad("John Doe", "john@email.com")
userbad.create_user()
userbad.show_user()

# Clase con una responsabilidad correcta
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
class UserService:
    def show(user):
        print(f"{user.name}-{user.email}")

class EmailService:
    def send_email(self, email, message):
        pass
    
# Crear un usuario con una responsabilidad
user = User("John Doe", "jonh@email.com")
UserService.show(user)


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

# Clase con múltiples responsabilidades
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author, copies):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name, id, email):
        self.users.append({"name": name, "id": id, "email": email})

    def loan_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1 
                return True
        return False
    
    def return_book(self, user_id, book_title):
        for book in self.books:
            if book["title"] == book_title:
                book["copies"] += 1
                return True
        return False
    


# Principio de responsabilidad única
class Book:
    
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class User:
    id = 0

    def __init__(self, name, email):
        self.name = name
        self.id = User.id
        self.email = email
        User.id += 1

class Loan:
    
    def __init__(self):
        self.loans=[]

    def loan_book(self, user:User, book: Book):
        if (book.copies > 0):
            book.copies -= 1
            self.loans.append({"user_id":user.id, "book_title":book.title}) 
            return True
        return False
    
    def return_book(self, user: User, book: Book):
        
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies+=1
                return True
            
        return False

class Library:

    def __init__(self):
        self.books = []
        self.users = []
        self.loans = Loan()

    def add_book(self, book: Book):
        self.books.append(book)
    
    def add_user(self, user: User):
        self.users.append(user)
        print(f"Usuario añadido {user.id}")	
    
    # Presta un libro usando fors.
    def loan_book(self, user_id, book_title):
        for user in self.users:
            if user.id == user_id:
                for book in self.books:
                    if book.title == book_title:
                        return self.loans.loan_book(user, book)
                return False
    
    # Devuelve un libro usando operación generadora 
    def return_book(self, user_id, book_title):
        user = next((user for user in self.users if user.id == user_id), None)
        book = next((book for book in self.books if book.title == book_title), None)
        if user and book:
            return self.loans.return_book(user, book) 
        return False 

# Crear objetos
book1 = Book("Python Programming", "John Doe", 2)
book2 = Book("JavaScript Programming", "Jane Doe", 1)
user1 = User("Alice", "Alice@gmail.com")
user2 = User("Bob", "Bob@gmail.com")

# Crear biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)

# Prestar libros
print(f'{library.loan_book(0, "Python Programming")}, Alice-Python') # True
print(f'{library.loan_book(1, "JavaScript Programming")}, Bob-Jav') # True
print(f'{library.loan_book(0, "JavaScript Programming")}, Alice-Jav') # False

# Devolver libros
print(f'{library.return_book(0, "Python Programming")}, Alice-Python') # True
print(f'{library.return_book(1, "JavaScript Programming")}, Bob-Java') # True
print(f'{library.return_book(0, "JavaScript Programming")}, Alice-Java') # False
