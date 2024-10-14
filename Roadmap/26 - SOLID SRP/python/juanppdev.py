"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Incorrecto

class Report:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Calcula estadísticas
        return {"mean": sum(self.data) / len(self.data)}

    def print_report(self):
        # Imprime el reporte
        stats = self.calculate_statistics()
        print(f"Mean: {stats['mean']}")

    def save_to_file(self, filename):
        # Guarda el reporte en un archivo
        with open(filename, 'w') as file:
            file.write(str(self.data))


# Correcto

class Report:
    def __init__(self, data):
        self.data = data

class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self):
        # Calcula estadísticas
        return {"mean": sum(self.data) / len(self.data)}

class ReportPrinter:
    def __init__(self, report):
        self.report = report

    def print_report(self):
        # Imprime el reporte
        stats = StatisticsCalculator(self.report.data).calculate_statistics()
        print(f"Mean: {stats['mean']}")

class ReportSaver:
    def __init__(self, report):
        self.report = report

    def save_to_file(self, filename):
        # Guarda el reporte en un archivo
        with open(filename, 'w') as file:
            file.write(str(self.report.data))


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

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def register_book(self, title, author, copies):
        book = {"title": title, "author": author, "copies": copies}
        self.books.append(book)

    def register_user(self, name, user_id, email):
        user = {"name": name, "user_id": user_id, "email": email}
        self.users.append(user)

    def loan_book(self, user_id, title):
        for book in self.books:
            if book["title"] == title and book["copies"] > 0:
                book["copies"] -= 1
                self.loans.append({"user_id": user_id, "title": title})
                return f"Book '{title}' loaned to user {user_id}"
        return f"Book '{title}' not available"

    def return_book(self, user_id, title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["title"] == title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == title:
                        book["copies"] += 1
                return f"Book '{title}' returned by user {user_id}"
        return f"No record of loan for book '{title}' by user {user_id}"


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class User:
    def __init__(self, name, user_id, email):
        self.name = name
        self.user_id = user_id
        self.email = email

class BookRegistry:
    def __init__(self):
        self.books = []

    def register_book(self, title, author, copies):
        book = Book(title, author, copies)
        self.books.append(book)

class UserRegistry:
    def __init__(self):
        self.users = []

    def register_user(self, name, user_id, email):
        user = User(name, user_id, email)
        self.users.append(user)

class LoanProcessor:
    def __init__(self, book_registry, user_registry):
        self.book_registry = book_registry
        self.user_registry = user_registry
        self.loans = []

    def loan_book(self, user_id, title):
        for book in self.book_registry.books:
            if book.title == title and book.copies > 0:
                book.copies -= 1
                self.loans.append({"user_id": user_id, "title": title})
                return f"Book '{title}' loaned to user {user_id}"
        return f"Book '{title}' not available"

    def return_book(self, user_id, title):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["title"] == title:
                self.loans.remove(loan)
                for book in self.book_registry.books:
                    if book.title == title:
                        book.copies += 1
                return f"Book '{title}' returned by user {user_id}"
        return f"No record of loan for book '{title}' by user {user_id}"


# Interacción desde la consola
if __name__ == "__main__":
    book_registry = BookRegistry()
    user_registry = UserRegistry()
    loan_processor = LoanProcessor(book_registry, user_registry)

    # Registrar libros
    book_registry.register_book("1984", "George Orwell", 5)
    book_registry.register_book("To Kill a Mockingbird", "Harper Lee", 3)

    # Registrar usuarios
    user_registry.register_user("Alice", 1, "alice@example.com")
    user_registry.register_user("Bob", 2, "bob@example.com")

    # Procesar préstamos
    print(loan_processor.loan_book(1, "1984"))
    print(loan_processor.loan_book(2, "To Kill a Mockingbird"))
    print(loan_processor.loan_book(1, "To Kill a Mockingbird"))

    # Devolver libros
    print(loan_processor.return_book(1, "1984"))
    print(loan_processor.return_book(2, "To Kill a Mockingbird"))