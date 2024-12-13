from datetime import datetime


def bill_amount(amount: float, tax_rate: float = 21.0, book: str = "default_book.log") -> float:
    total_amount = amount * (1 + tax_rate / 100)

    print(f"Facturamos {total_amount:.2f} eur ({amount:.2f} + tasas) en '{book}'")


def get_taxable_data(amount: float, tax_rate: float = 21.0) -> dict:
    taxes = amount * tax_rate / 100

    return {
        "base": amount,
        "taxes": taxes,
        "total": amount + taxes,
    }


def save_bill(taxable: dict, book: str = "default_book.log"):
    base = taxable.get("base")
    total = taxable.get("total")
    if not base or not total:
        return

    print(f"Facturamos {total:.2f} eur ({base:.2f} + tasas) en '{book}'")


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def register_book(self, book_id: int, title: str | None = None, author: str | None = None, amount: int = 1):
        if book_id in self.books:
            self.books[book_id]["amount"] += amount
            if amount == 1:
                print(f"Nuevo ejemplar del libro '{title}' con ID {book_id} añadido.")
            else:
                print(f"{amount} ejemplares del libro '{title}' con ID {book_id} añadidos.")
            return

        self.books[book_id] = {
            "title": title,
            "author": author,
            "amount": amount,
            "borrowed": 0,
        }
        if amount == 1:
            print(f"Libro '{title}' registrado con ID {book_id}")
        else:
            print(f"{amount} ejemplares del libro '{title}' con ID {book_id} registrados.")

    def register_user(self, user_id: int, name: str, email: str):
        self.users[user_id] = {
            "name": name,
            "email": email,
            "borrowed_books": {},
        }
        print(f"Usuario '{name}' registrado con ID {user_id}")

    def borrow_book(self, user_id: int, book_id: int):
        if book_id not in self.books:
            print(f"No hay libro con ID {book_id}")
            return

        if self.books[book_id]["amount"] == 0:
            print(f"No hay copias disponibles de libro con ID {book_id}")
            return

        if book_id in self.users[user_id]["borrowed_books"]:
            print(f"El usuario con ID {user_id} ya tiene un ejemplar del libro con ID {book_id}")
            return

        self.books[book_id]["amount"] -= 1
        self.books[book_id]["borrowed"] += 1
        self.users[user_id]["borrowed_books"][book_id] = datetime.now()
        print(f"Libro con ID {book_id} prestado a {self.users[user_id]['name']}")

    def return_book(self, user_id: int, book_id: int):
        if book_id not in self.books:
            print(f"No conocemos un libro con ID {book_id}")
            return

        if user_id not in self.users:
            print(f"No conocemos a un usuario con ID {user_id}")
            return

        self.books[book_id]["amount"] += 1
        self.books[book_id]["borrowed"] -= 1
        print(f"Libro con ID {book_id} devuelto por {self.users[user_id]['name']}")


class User:

    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email


class Book:

    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author


class UserRegistry:

    def __init__(self):
        self.users = {}

    def register_user(self, user: User) -> None:
        if user.user_id in self.users:
            print(f"El usuario con ID {user.user_id} ya existe en el registro.")
            return

        self.users[user.user_id] = user
        print(f"Usuario '{user.name}' registrado con ID {user.user_id}")

    def is_registered(self, user: User) -> bool:
        return user.user_id in self.users


class BookRegistry:

    def __init__(self):
        self.books = {}
        self.borrowed = {}
        self.amount = {}

    def register_book(self, book: Book):
        if book.book_id in self.books:
            self.amount[book.book_id] += 1
            print(f"Registramos un nuevo ejemplar del libro '{book.title}' con ID {book.book_id}")
            return

        self.books[book.book_id] = book
        self.amount[book.book_id] = 1
        print(f"Primer ejemplar del libro '{book.title}' registrado con ID {book.book_id}")

    def borrow_book(self, book: Book, user: User, user_registry: UserRegistry) -> None:
        if not user_registry.is_registered(user):
            print(f"El usuario con ID {user.user_id} no está registrado.")
            return

        if book.book_id not in self.books:
            print(f"No hay libro con ID {book.book_id}")
            return

        if self.amount[book.book_id] == 0:
            print(f"No hay copias disponibles de libro con ID {book.book_id}")
            return

        borrowed = self.borrowed.get(book.book_id)
        if borrowed and user.user_id in borrowed:
            print(f"El usuario con ID {user.user_id} ya tiene un ejemplar del libro con ID {book.book_id}")
            return

        self.amount[book.book_id] -= 1
        self.borrowed[book.book_id] = self.borrowed.get(book.book_id, {})
        self.borrowed[book.book_id][user.user_id] = datetime.now()
        print(f"Prestamos el libro '{book.title}' con ID {book.book_id} a {user.name}")

    def return_book(self, book: Book, user: User, user_registry: UserRegistry) -> None:
        if not user_registry.is_registered(user):
            print(f"El usuario con ID {user.user_id} no está registrado.")
            return

        if book.book_id not in self.books:
            print(f"No conocemos un libro con ID {book.book_id}")
            return

        borrowed = self.borrowed.get(book.book_id)
        if not borrowed:
            print(f"No hay ejemplares prestados de libro con ID {book.book_id}")
            return

        if user.user_id not in borrowed:
            print(f"El usuario con ID {user.user_id} no tiene un ejemplar del libro con ID {book.book_id}")
            return

        self.amount[book.book_id] += 1
        del self.borrowed[book.book_id][user.user_id]
        print(f"El usuario con ID {user.user_id} devuelve el libro '{book.title}' con ID {book.book_id}")


def main():
    print("===== MAIN =====")
    print("Con la implementación no-SRP, tenemos una función que hace dos cosas:")
    print("1. calcula los impuestos")
    print("2. guarda la factura.")
    print(">>> bill_amount(100, 21)")
    bill_amount(100, 21)

    print("\nAquí el problema es que tendremos que modificar bill_amount() en dos circunstancias:")
    print("1. Si se modifica algo relativo a cómo se calculan los impuestos (por ejemplo,")
    print("   que en lugar de aplicar un porcentaje fijo, se sume una constante, o que")
    print("   el procentaje dependa de la cantidad base).")
    print("2. Si se modifica algo relacionado con cómo se guarda la factura (por ejemplo,")
    print("   que en lugar de guardar la factura en un archivo, se guarde en una base de datos,")
    print("   o que se quiera guardar la información en otro formato).")

    print("\nCon una implementación SRP, hemos separado las dos responsabilidades en dos funciones:")
    print('taxable_data = get_taxable_data(250, 15)')
    print('save_bill(taxable_data)')
    taxable_data = get_taxable_data(250, 15)
    save_bill(taxable_data)

    print("\nDe esta manera, si el cálculo de los impuestos cambia, sólo tendremos que modificar la")
    print("función get_taxable_data(). Por otro lado, si se quiere cambiar cómo se guarda la factura,")
    print("sólo tendremos que modificar la función save_bill().")
    print("El único requisito común es que ambas funciones respeten el contrato de que get_taxable_data()")
    print("devuelva un diccionario compatible con lo que save_bill() espera. En un caso real, podríamos usar")
    print("una clase ad hoc para esto, y forzar que una función devuelva un objeto de esa clase, y la otra lo use.")


def extra():
    print("\n===== EXTRA =====")
    print("Versión monolítica. Todo ocurrirá en un objeto de la clase Library:")
    print('>>> library = Library()')
    library = Library()

    print("\nRegistramos un libro y un usuario:")
    print('>>> library.register_book(1, "El Quijote de la Mancha", "Yo", 5)')
    library.register_book(1, "El Quijote de la Mancha", "Yo", 5)
    print('>>> library.register_user(1, "Chiquito", "chiquito@example.com")')
    library.register_user(1, "Chiquito", "chiquito@example.com")

    print("\nPrestamos un libro al usuario:")
    print('library.borrow_book(user_id=1, book_id=1)')
    library.borrow_book(user_id=1, book_id=1)

    print("\nEl mismo usuario no puede sacar otro ejemplar del libro:")
    print('>>> library.borrow_book(user_id=1, book_id=1)')
    library.borrow_book(user_id=1, book_id=1)

    print("\nEl usuario devuelve el libro:")
    print('>>> library.return_book(user_id=1, book_id=1)')
    library.return_book(user_id=1, book_id=1)

    print("\nEn la versión SRP tendremos que instanciar varios objetos:")
    print('>>> book_registry = BookRegistry()')
    book_registry = BookRegistry()
    print('>>> user_registry = UserRegistry()')
    user_registry = UserRegistry()
    print('>>> book = Book(1, "El lazarillo de Tormes", "Yo")')
    book = Book(1, "El lazarillo de Tormes", "Yo")
    print('>>> user = User(1, "Carl Sagan", "carl@example.com")')
    user = User(1, "Carl Sagan", "carl@example.com")

    print("\nRegistraremos el libro y el usuario creados en sus respectivos registros:")
    print('>>> book_registry.register_book(book)')
    book_registry.register_book(book)
    print('>>> user_registry.register_user(user)')
    user_registry.register_user(user)

    print("\nPrestamos un libro al usuario:")
    print('>>> book_registry.borrow_book(user=user, book=book, user_registry=user_registry)')
    book_registry.borrow_book(user=user, book=book, user_registry=user_registry)

    print("\nCreamos y registramos a un segundo usuario:")
    print('>>> user2 = User(2, "Isaac Asimov", "isaac@example.com")')
    user2 = User(2, "Isaac Asimov", "isaac@example.com")
    print('>>> user_registry.register_user(user2)')
    user_registry.register_user(user2)

    print("\nRegistramos un segundo ejemplar del libro:")
    print('>>> book_registry.register_book(book)')
    book_registry.register_book(book)

    print("\nEl primer usuario no puede sacar otro ejemplar del libro")
    print('>>> book_registry.borrow_book(user=user, book=book, user_registry=user_registry)')
    book_registry.borrow_book(user=user, book=book, user_registry=user_registry)

    print("\nPero el segundo usuario sí puede:")
    print('>>> book_registry.borrow_book(user=user2, book=book, user_registry=user_registry)')
    book_registry.borrow_book(user=user2, book=book, user_registry=user_registry)

    print("\nSi el primer usuario devuelve el libro, luego puede volver a sacarlo:")
    print('>>> book_registry.return_book(user=user, book=book, user_registry=user_registry)')
    book_registry.return_book(user=user, book=book, user_registry=user_registry)
    print('>>> book_registry.borrow_book(user=user, book=book, user_registry=user_registry)')
    book_registry.borrow_book(user=user, book=book, user_registry=user_registry)

    print("\nUn tercer usuario no registrado no puede sacar libros:")
    print('>>> user3 = User(3, "Isaac Newton", "isaac2@example.com")')
    user3 = User(3, "Isaac Newton", "isaac2@example.com")
    print('>>> book_registry.borrow_book(user=user3, book=book, user_registry=user_registry)')
    book_registry.borrow_book(user=user3, book=book, user_registry=user_registry)

    print("\nSi lo registramos, ahora sí podrá sacar libros (pero no del libro 1,")
    print("puesto que los dos ejemplares que hay están prestados).")
    print('>>> user_registry.register_user(user3)')
    user_registry.register_user(user3)
    print('>>> book_registry.borrow_book(user=user3, book=book, user_registry=user_registry)')
    book_registry.borrow_book(user=user3, book=book, user_registry=user_registry)


if __name__ == "__main__":
    main()
    extra()
