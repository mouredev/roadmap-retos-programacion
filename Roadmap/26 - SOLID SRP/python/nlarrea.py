"""
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

# Incorrect


class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def add_user(self):
        pass

    def send_email(self):
        pass


# Correct


class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class UserService:
    def add_user(self, user: User):
        # add user to database
        pass


class EmailService:
    def send_email(self, email: str, message: str):
        # send an email
        pass


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

# Incorrect


class Library:
    def __init__(self) -> None:
        self.books: list[dict] = []
        self.users: list[dict] = []
        self.loans: list[dict] = []

    def add_book(self, title: str, author: str, copies: int):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, id: str, name: str, email: str):
        self.users.append({"id": id, "name": name, "email": email})

    def loan_book(self, user_id: str, book_title: str):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1
                self.loans.append(
                    {"user_id": user_id, "book_title": book_title}
                )

                return True

            return False

    def return_book(self, user_id: str, book_title: str):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                # Remove current loan
                self.loans.remove(loan)
                # Add a copy of the book to the library
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1
                        return True

        return False


# Correct


class Book:
    def __init__(self, title: str, author: str, copies: int = 1) -> None:
        self.title = title
        self.author = author
        self.copies = copies


class User:
    def __init__(self, id: str, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email


class BookLending:
    def __init__(self) -> None:
        self.loans = []

    def loan_book(self, user: User, book: Book) -> bool:
        if book.copies > 0:
            book.copies -= 1
            self.loans.append({"user_id": user.id, "book_title": book.title})
            return True

        return False

    def return_book(self, user: User, book: Book) -> bool:
        for loan in self.loans:
            if loan["user_id"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True

            return False


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.users: list[User] = []
        self.loans_service = BookLending()

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def loan_book(self, user_id: str, book_title: str) -> bool:
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if user and book:
            return self.loans_service.loan_book(user, book)

        return False

    def return_book(self, user_id: str, book_title: str) -> bool:
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if user and book:
            return self.loans_service.return_book(user, book)

        return False


# Execution to check if it works:
library = Library()

library.add_book(
    Book(title="The Lord Of The Rings", author="J.R.R. Tolkien", copies=10)
)
library.add_user(User(id="a11", name="Naia", email="naia@email.com"))

print(
    "loan book:",
    library.loan_book(user_id="a11", book_title="The Lord Of The Rings"),
)  # loan book: True
print(
    "loan book:",
    library.loan_book(user_id="123", book_title="This doesn't exist"),
)  # loan book: False

print(
    "return book:",
    library.return_book(user_id="a11", book_title="The Lord Of The Rings"),
)  # return book: True
print(
    "return book:",
    library.return_book(user_id="123", book_title="This doesn't exist"),
)  # return book: False
