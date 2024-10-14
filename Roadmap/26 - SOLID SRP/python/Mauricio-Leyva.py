# Implementación que viola SRP
class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.loans = {}

    def add_book(self, title, author, copies):
        if title not in self.books:
            self.books[title] = {"author": author, "copies": copies, "available": copies}
            print(f"Libro '{title}' agregado con {copies} copias.")
        else:
            print(f"El libro '{title}' ya existe en el sistema.")

    def register_user(self, name, user_id, email):
        if user_id not in self.users:
            self.users[user_id] = {"name": name, "email": email}
            print(f"Usuario {name} registrado con ID {user_id}.")
        else:
            print(f"El usuario con ID {user_id} ya existe en el sistema.")

    def lend_book(self, user_id, title):
        if user_id not in self.users:
            print(f"Usuario con ID {user_id} no encontrado.")
            return
        if title not in self.books:
            print(f"Libro '{title}' no encontrado.")
            return
        if self.books[title]["available"] == 0:
            print(f"No hay copias disponibles de '{title}'.")
            return
        
        self.books[title]["available"] -= 1
        if user_id not in self.loans:
            self.loans[user_id] = []
        self.loans[user_id].append(title)
        print(f"Libro '{title}' prestado a usuario {user_id}.")

    def return_book(self, user_id, title):
        if user_id not in self.loans or title not in self.loans[user_id]:
            print(f"El usuario {user_id} no tiene prestado el libro '{title}'.")
            return
        
        self.books[title]["available"] += 1
        self.loans[user_id].remove(title)
        print(f"Libro '{title}' devuelto por usuario {user_id}.")

# Implementación que cumple con SRP
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.available = copies

class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.user_id = user_id
        self.email = email

class BookManager:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title not in self.books:
            self.books[book.title] = book
            print(f"Libro '{book.title}' agregado con {book.copies} copias.")
        else:
            print(f"El libro '{book.title}' ya existe en el sistema.")

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user):
        if user.user_id not in self.users:
            self.users[user.user_id] = user
            print(f"Usuario {user.name} registrado con ID {user.user_id}.")
        else:
            print(f"El usuario con ID {user.user_id} ya existe en el sistema.")

class LoanManager:
    def __init__(self, book_manager, user_manager):
        self.loans = {}
        self.book_manager = book_manager
        self.user_manager = user_manager

    def lend_book(self, user_id, title):
        if user_id not in self.user_manager.users:
            print(f"Usuario con ID {user_id} no encontrado.")
            return
        if title not in self.book_manager.books:
            print(f"Libro '{title}' no encontrado.")
            return
        book = self.book_manager.books[title]
        if book.available == 0:
            print(f"No hay copias disponibles de '{title}'.")
            return
        
        book.available -= 1
        if user_id not in self.loans:
            self.loans[user_id] = []
        self.loans[user_id].append(title)
        print(f"Libro '{title}' prestado a usuario {user_id}.")

    def return_book(self, user_id, title):
        if user_id not in self.loans or title not in self.loans[user_id]:
            print(f"El usuario {user_id} no tiene prestado el libro '{title}'.")
            return
        
        book = self.book_manager.books[title]
        book.available += 1
        self.loans[user_id].remove(title)
        print(f"Libro '{title}' devuelto por usuario {user_id}.")

# Uso del sistema refactorizado
book_manager = BookManager()
user_manager = UserManager()
loan_manager = LoanManager(book_manager, user_manager)

book_manager.add_book(Book("1984", "George Orwell", 5))
book_manager.add_book(Book("To Kill a Mockingbird", "Harper Lee", 3))

user_manager.register_user(User("Ana García", "001", "ana@email.com"))
user_manager.register_user(User("Pedro López", "002", "pedro@email.com"))

loan_manager.lend_book("001", "1984")
loan_manager.lend_book("002", "To Kill a Mockingbird")
loan_manager.return_book("001", "1984")
