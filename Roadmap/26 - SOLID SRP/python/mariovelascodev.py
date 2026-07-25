#Ejercicio

#Forma incorrecta
class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def sendEmail(self):
        pass

#Forma correcto
class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user(self):
        return self.name
    
    def get_email(self):
        return self.email
    
class Mailer:
    def sendEmail(self, email):
        pass

#Extra

#Forma incorrecta
class Library:

    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []
    
    def register_book(self, title:str, author:str, available_copies:int):

        self.books.append({"title": title, "author": author, "available copies": available_copies})

    def register_user(self, name:str, id:int, email:str):

        self.users.append({"name": name, "id": id, "email": email})

    def loan_book(self, id:int, title:str):
        for book in self.books:
            if book["title"] == title and book["available copies"] > 0:
                book["available copies"] -= 1
                self.loans.append(
                    {"id": id, "title": title})
                return "Libro reservado"
        return "No se ha podido reservar el libro"
    
    def return_book(self, id:int, title:str):
        for loan in self.loans:
            if loan["id"] == id and loan["title"] == title:
                self.loans.remove(loan)
                for book in self.books:
                    if book["title"] == title:
                        book["copies"] += 1
                    return "Libro devuelto"
        return "No se ha podido devolver el libro"

#Forma Correcta
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = Loan()

    def register_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def loan_book(self, id:int, title:str):
        user = next((u for u in self.users if u.id == id), None)
        book = next((b for b in self.books if b.title == title), None)

        if user and book:
            return self.loans.loan_book(user, book)
        return False
    
    def return_book(self, id:int, title:str):
        user = next((u for u in self.users if u.id == id), None)
        book = next((b for b in self.books if b.title == title), None)

        if user and book:
            return self.loans.return_book(user, book)
        return False

class Book:
    def __init__(self, title:str, author:str, available_copies:int):
        self.title = title
        self.author = author
        self.available_copies = available_copies

class User:
    def __init__(self, name:str, id:int, email:str):
        self.name = name
        self.id = id
        self.email = email

class Loan:
    def __init__(self):
        self.loans = []

    def loan_book(self, user, book):
        if book.available_copies > 0:
                book.available_copies -= 1
                self.loans.append(
                    {"id": user.id, "title": book.title})
                return "Libro reservado"
        return "No se ha podido reservar el libro"
    
    def return_book(self, user, book):
        for loan in self.loans:
            if loan["id"] == user.id and loan["title"] == book.title:
                self.loans.remove(loan)
                book.available_copies += 1
                return "Libro devuelto"
        return "No se ha podido devolver el libro"
