from typing import List


class Book:
    id: int
    name: str
    author: str
    stock: int

    def __init__(self, id, name, author, stock):
        self.id = id
        self.name = name
        self.author = author
        self.stock = stock


class User:
    id: int
    name: str
    email: str
    books: List[Book]

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.books = []

    def remove_book(self, book):
        self.books.remove(book)


class UserRegister:
    users: List[User]
    next_id: int

    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name: str, email: str):
        new_user = User(self.next_id, name, email)
        self.users.append(new_user)
        self.next_id += 1

    def search_user(self, book_id):
        for user in self.users:
            return user if user.id == book_id else None


class BookRegister:
    books: List[Book]
    next_id: int

    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, name: str, author: str, stock: int):
        new_book = Book(self.next_id, name, author, stock)
        self.books.append(new_book)
        self.next_id += 1

    def search_book(self, id):
        for book in self.books:
            return book if book.id == id else None


class BookBorrower:
    book_register: BookRegister
    user_register: UserRegister

    def __init__(self):
        self.book_register = BookRegister()
        self.user_register = UserRegister()

    def borrow_book(self, user_id: int, book_id: int):
        book = self.book_register.search_book(book_id)
        user = self.user_register.search_user(user_id)

        if book and user:

            if book.stock > 0:
                user.books.append(book)
                book.stock -= 1
            else:
                raise Exception("No hay stock disponible")
        else:
            raise Exception("El libro o el usuario no existe")

    def return_book(self, user_id: int, book_id: int):
        book = self.book_register.search_book(book_id)
        user = self.user_register.search_user(user_id)

        if book and user:
            user.remove_book(book)
            book.stock += 1
        else:
            raise Exception("El libro o el usuario no existe")

    def list_users(self):
        users = self.user_register.users

        for user in users:
            borrowed_books = ', '.join([book.name for book in user.books])
            print(f"{user.id} - {user.name} - {user.email} - Libros prestados: {borrowed_books}")

    def list_books(self):
        books = self.book_register.books

        for book in books:
            print(f"{book.id} - {book.name} - {book.author} – {book.stock}")


def main():
    book_borrower = BookBorrower()
    quit = False

    print("Bienvenido a la librería")

    while not quit:
        print("\nSelecciona una opción")
        print("\n1 - Añadir usuario"
              "\n2 - Añadir libro"
              "\n3 - Prestar libro"
              "\n4 - Devolver libro"
              "\n5 - Listar libros"
              "\n6 - Listar usuarios"
              "\n7 - Salir")
        choice = input("> ")

        match choice:
            case "1":
                name = input("Nombre: ")
                email = input("Email: ")
                book_borrower.user_register.add_user(name, email)
            case "2":
                name = input("Nombre: ")
                author = input("Autor: ")
                stock = int(input("Stock: "))
                book_borrower.book_register.add_book(name, author, stock)
            case "3":
                try:
                    book_id = int(input("ID del libro: "))
                    user_id = int(input("ID del usuario: "))
                    book_borrower.borrow_book(user_id, book_id)
                except Exception as e:
                    print(e)
            case "4":
                try:
                    book_id = int(input("ID del libro: "))
                    user_id = int(input("ID del usuario: "))
                    book_borrower.return_book(user_id, book_id)
                except Exception as e:
                    print(e)
            case "5":
                book_borrower.list_books()
            case "6":
                book_borrower.list_users()
            case "7":
                print("Hasta pronto")
                quit = True
            case _:
                print("Opción incorrecta")


if __name__ == '__main__':
    main()
