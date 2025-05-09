# Solid SRP: Single Responsability Principle

# Forma incorrecta: la clase usuario solo debe almacenar los datos del mismo, verificar si el email es correcto.

class Usuario():
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def check_email(self):
        if "@" not in self.email:
            raise ValueError("El email es invalido.")

# Forma correcta: se debe separar en dos clases

class Usuario2():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
class check_email():
    def check(self, email):
        if "@" not in email:
            print("El email es invalido.")
        else:
            print("Email correcto")

boy = Usuario2("Gordo-Master", "gordomastergmail.com")

data_email = check_email()

data_email.check(boy.email)

"""
Ejercicio extra
"""

"""
class Library():

    def __init__(self, books = [], users = []):
        self.books = books
        self.users = users

    def new_book(self, title: str, author: str, amount: int):
        self.books.append([title, author, amount])

    
    def new_user(self, name: str, id: int, email: str):
        self.users.append([name, id, email])

    def borrow_book(self, user, book):
        self.book_ubi = user
        pass
        

    def return_book(self):
        pass

sanson = Library()

sanson.new_book("One", "Carlos", 5)
sanson.new_book("Two", "Carlos", 7)
sanson.new_book("ABC", "Jose", 5)

sanson.new_user("Maria",1,"maria@gmail.com")
sanson.new_user("Belén",2,"belen@gmail.com")
sanson.new_user("Vanesa",3,"vanesa@gmail.com")

print(sanson.books)
print(sanson.users)

"""

## Refactorización

class User():
    def __init__(self, name: str, id: int, email: str):
        self.name = name
        self.id = id
        self.email = email
        self.book_borrowed = []
    
    def show(self):
        print(f"{self.name}, {self.id}, {self.email}")

class Book():
    def __init__(self, title: str, author: str, copies: int):
        self.title = title
        self.author = author
        self.copies = copies

    def show(self):
        print(f"{self.title}, {self.author}, {self.copies}")


class Loan():
    def __init__(self):
        self.loans = []

    def loan_book(self, user: User, book: Book):
        if book.copies > 0:
            book.copies -= 1
            self.loans.append({"id_user": user.id, "book_title": book.title})
            return True
        return False
    
    def return_book(self, user: User, book: Book):
        for loan in self.loans:
            if loan["id_user"] == user.id and loan["book_title"] == book.title:
                self.loans.remove(loan)
                book.copies += 1
                return True
        return False
    


class Library():
    
    def __init__(self):
        self.books = []
        self.users = []
        self.loans_service = Loan()

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)


    def loan_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id),None)
        book = next((b for b in self.books if b.title == book_title),None)  
        if user and book:
            return self.loans_service.loan_book(user,book)
        return False
    
    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.id == user_id),None)
        book = next((u for u in self.books if u.title == book_title),None)
        if user and book:
            return self.loans_service.return_book(user,book)
        return False
    



u_1 = User("Jorge", 1, "jorge@gmail.com")
u_2 = User("Francisco", 2, "francisco@gmail.com")
u_3 = User("Lorenzo", 3, "lorenzo@gmail.com")

b_1 = Book("Harry Potter", "J. K. Rowling", 7)
b_2 = Book("Percy Jackson", "Rick Riordan", 4)
b_3 = Book("El mago de los libros", "JIM C. HINES ", 2)

library = Library()

library.add_book(b_1)
library.add_book(b_2)
library.add_book(b_3)

library.add_user(u_1)
library.add_user(u_2)
library.add_user(u_3)

print(library.loan_book(u_1.id,"Harry Potter"))
print(library.loan_book(u_1.id,"HarryPotter"))

print()

print(library.loan_book(u_1.id,"El mago de los libros"))
print(library.loan_book(u_2.id,"El mago de los libros"))
print(library.loan_book(u_3.id,"El mago de los libros"))