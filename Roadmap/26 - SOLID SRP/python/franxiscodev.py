"""
SOLID
SRP: principio de responsabilidad única
"""
# NO solid


class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    # no son responsabilidad de una clase usuario
    def save_to_database(self):
        pass

    def sen_email():
        pass

# SOLID


class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class UserService:
    def save_to_database(self, user):
        pass


class EmailService:
    def sen_email(self, email, message):
        pass


"""
Extra 
"""
# Incorrecto


class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title: str, author: str, copies: int):
        self.books.append({"title": title, "author": author, "copies": copies})

    def add_user(self, name: str, user_id: int, email: str):
        self.users.append({"name": name, "user_id": user_id, "email": email})

    def loan_book(self, user_id: int, book_title: str):
        for book in self.books:
            if book["title"] == book_title and book["copies"] > 0:
                book["copies"] -= 1
                self.loans.append(
                    {"user_id": user_id, "book_title": book_title})
                return True
        return False

    def return_book(self, user_id: int, book_title: str):
        for loan in self.loans:
            if loan["user_id"] == user_id and loan["book_title"] == book_title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == book_title:
                        book["copies"] += 1
                        return True
        return False


# Correcto
class Book:
    def __init__(self, title: str, author: str, copies: int) -> None:
        self.title = title
        self.author = author
        self.copies = copies


class User:
    def __init__(self, name: str, user_id: int, email: str) -> None:
        self.name = name
        self.user_id = user_id
        self.email = email


class Loan:
    def __init__(self) -> None:
        self.loans = []

    def loan_book(self, user: User, book: Book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append(
                {"user_id": user.user_id, "book_title": book.title})
            return True
        return False

    def return_book(self, user: User, book: Book):
        for loan in self.loans:
            if loan["user_id"] == user.user_id and loan["book_title"] == book.title:
                # Remove the loan from the list
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False


class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book: Book):
        self.books.append(book)

    def add_user(self, user: User):
        self.users.append(user)

    def loan_book(self, user_id: int, book_title: str):
        user = next(
            (user for user in self.users if user.user_id == user_id), None)
        book = next(
            (book for book in self.books if book.title == book_title), None)
        if user and book:
            return self.loans_service.loan_book(user, book)
        return False

    def return_book(self, user_id: int, book_title: str):
        user = next(
            (user for user in self.users if user.user_id == user_id), None)
        book = next(
            (book for book in self.books if book.title == book_title), None)
        if user and book:
            return self.loans_service.return_book(user, book)
        return False
