"""
 EJERCICIO:
 Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 de forma correcta e incorrecta.

 DIFICULTAD EXTRA (opcional):
 Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 y el procesamiento de préstamos de libros.
 Requisitos:
 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 información básica como título, autor y número de copias disponibles.
 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 información básica como nombre, número de identificación y correo electrónico.
 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 tomar prestados y devolver libros.
 Instrucciones:
 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 los tres aspectos mencionados anteriormente (registro de libros, registro de
 usuarios y procesamiento de préstamos).
 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 siguiendo el Principio de Responsabilidad Única.
"""

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Para entender fácilmente los 5 ppios SOLID recomiendo leer:

    https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/

en donde se explican de manera ordenada uno por uno, de manera sencilla y ejemplicada de manera progresiva (de hecho, de acá
voy a tomar el ejemplo).

El primer de los ppios SOLID es "Single Responsibility Principle" <= una clase SOLO debe ser responsable de una única cosa.

    class Duck:
       
        def __init__(self, name):
            self.name = name
       
        def fly(self):
            print(f"{self.name} is flying not very high")
    
        def swim(self):
            print(f"{self.name} swims in the lake and quacks")
    
        def do_sound(self) -> str:
            return "Quack"
    
        def greet(self, duck2: Duck):
            print(f"{self.name}: {self.do_sound()}, hello {duck2.name}")

Esta clase Duck es responsable por definir los atributos de un pato, PERO, además, se encarga de definir como un pato
saluda a otro => esta otra responsabilidad viola el ppio SRP => debe estar en otra clase específica.

    class Duck:
       
        def __init__(self, name):
            self.name = name
       
        def fly(self):
            print(f"{self.name} is flying not very high")
    
        def swim(self):
            print(f"{self.name} swims in the lake and quacks")
    
        def do_sound(self) -> str:
            return "Quack"
    
    class Communicator:
    
        def __init__(self, channel):
            self.channel = channel
    
        def communicate(self, duck1 : Duck, duck2: Duck):
            sentence1 = f"{duck1.name}: {duck1.do_sound()}, hello {duck2.name}"
            sentence2 = f"{duck2.name}: {duck2.do_sound()}, hello {duck1.name}"
            conversation = [sentence1, sentence2]
            print(*conversation,
                  f"(via {self.channel})",
                  sep = '\n')

Ahora sí, ambas clases, cumplen con SRP (Duck solo de los atributos de los patos y Communicator solo de la
comunicación entre ellos).
""")

print(f"{'#' * 52}")
print(f"##  Dificultad Extra  {'#' * 30}")
print(f"{'#' * 52}\n")

print(f"""\n##  Libreria SRP  {'#' * 50}
Acá LibraryNoSRP se encarga de todo: los libros, los socios y el mvto de libros.
Así, si es necesario, por ejemplo, cambiar la política de préstamos se afecta a TODA la clase.
""")


class LibraryNoSRP:
    library = None
    books = {}
    authors = []
    members = {}

    def __new__(cls, *args, **kwargs):
        if not cls.library:
            cls.library = super().__new__(cls)
            cls.library._initialized = False
        return cls.library

    def __init__(self, name: str = None):
        if not self._initialized:
            self.value = name
            self._initialized = True

    @classmethod
    def add_book(cls, title: str, author: str, book_copies: int = 1):

        full_name = title + "_" + author
        if full_name in cls.books.keys():
            cls.books[full_name]["copies"] += book_copies
        else:
            if author not in cls.authors:
                cls.authors.append(author)
            cls.books[full_name] = {"copies": book_copies}

    @classmethod
    def add_member(cls, name: str, id: int):

        if id not in cls.members.keys():
            cls.members[id] = {"name": name, "borroughts": []}

    @classmethod
    def receive_book(cls, title: str, author: str, member: int):
        full_name = title + "_" + author
        cls.add_book(title, author, 1)
        cls.members[member]["borroughts"].remove(full_name)
        print(f"{cls.members[member]['name']} devolvió {title} de {author}")

    @classmethod
    def lend_book(cls, title: str, author: str, member: int):

        full_name = title + "_" + author
        if member not in cls.members.keys():
            print(f"El socio {member} no está registrado")
            return False
        if author not in cls.authors:
            print(f"No hay libros para el autor {author}")
            return False
        if full_name not in cls.books.keys():
            print(f"No tenemos el libro {title} del autor {author}")
            return False
        if cls.books[full_name]["copies"] <= 0:
            print(f"No hay copias disponibles de {title} de {author}")
            return False
        print(f"{title} de {author} prestado a {cls.members[member]['name']}")
        cls.books[full_name]["copies"] -= 1
        cls.members[member]["borroughts"].append(full_name)
        return True


library = LibraryNoSRP("Public")
library.add_book("Romi y Julito", "Willie Shakes", 3)
library.add_book("Quique Quinto", "Willie Shakes", 2)
library.add_book("Romi y Julito", "Willie Shakes", 1)
library.add_book("Mi Vida con Álvarez", "Alberto Borges", 1)

library.add_member("Tito", 12345678)
library.add_member("Pepe", 87654321)

print(f"\nBooks: {library.books}")
print(f"Members: {library.members}\n")

library.lend_book("Romi y Julito", "Willie Shakes", 12345678)
library.lend_book("Romi y Julito", "Willie Shakes", 87654321)
library.lend_book("Quique Quinto", "Alberto Borges", 12345678)
library.lend_book("Mi Vida con Álvarez", "Alberto Borges", 12345678)
library.lend_book("Mi Vida con Álvarez", "Alberto Borges", 87654321)

print(f"\nBooks: {library.books}")
print(f"Members: {library.members}\n")

library.receive_book("Romi y Julito", "Willie Shakes", 12345678)
library.receive_book("Mi Vida con Álvarez", "Alberto Borges", 12345678)
library.lend_book("Mi Vida con Álvarez", "Alberto Borges", 87654321)
library.lend_book("Quique Quinto", "Willie Shakes", 12345678)

print(f"\nBooks: {library.books}")
print(f"Members: {library.members}\n")

print(f"""\n##  Libreria SRP  {'#' * 50}
Acá se separan las responsabilidades: LibrarySRP se encarga de los libros, Member de los socios y BooksInOut del mvto de libros.
Así, si es necesario, por ejemplo, cambiar la política de préstamos NO se afecta Library ni Members.
""")


class LibrarySRP:
    library = None
    books = {}
    authors = []

    def __new__(cls, *args, **kwargs):
        if not cls.library:
            cls.library = super().__new__(cls)
            cls.library._initialized = False
        return cls.library

    def __init__(self, name: str = None):
        if not self._initialized:
            self.value = name
            self._initialized = True

    @classmethod
    def add_book(cls, title: str, author: str, book_copies: int = 1):

        full_name = title + "_" + author
        if full_name in cls.books.keys():
            cls.books[full_name]["copies"] += book_copies
        else:
            if author not in cls.authors:
                cls.authors.append(author)
            cls.books[full_name] = {"copies": book_copies}


class Member:
    member_id = []

    def __init__(self, name: str, id: int):
        if id not in self.member_id:
            self.name = name
            self.id = id
            self.borroughts = []
            self.new_member(self.id)
        else:
            self.id = self.member_id[id]

    def __str__(self):
        return {self.id: {"name": self.name, "borroughts": self.borroughts}}    # no devuelve str para mantener la misma salida que antes.

    @classmethod
    def new_member(cls, id):
        cls.member_id.append(id)

    @classmethod
    def is_member(cls, id):
        return id in cls.member_id


class BooksInOut:
    books_movement = None

    def __new__(cls, *args, **kwargs):
        if not cls.books_movement:
            cls.books_movement = super().__new__(cls)
            cls.books_movement._initialized = False
        return cls.books_movement

    def __init__(self, library: LibrarySRP):
        if not self._initialized:
            self.library = library

    def lend_book(self, title: str, author: str, member: Member):
        full_name = title + "_" + author
        if author not in self.library.authors:
            print(f"No tenemos libros del autor {author}")
            return False
        if full_name not in self.library.books.keys():
            print(f"No tenemos el libro {title} del autor {author}")
            return False
        if self.library.books[full_name]["copies"] <= 0:
            print(f"No hay copias disponibles de {title} de {author}")
            return False
        print(f"{title} de {author} prestado a {member.name}")
        self.library.books[full_name]["copies"] -= 1
        member.borroughts.append(full_name)
        return True

    def receive_book(self, title: str, author: str, member: Member):
        full_name = title + "_" + author
        self.library.add_book(title, author, 1)
        member.borroughts.remove(full_name)
        print(f"{member.name} devolvió {title} de {author}")


library = LibrarySRP("Public")
library.add_book("Romi y Julito", "Willie Shakes", 3)
library.add_book("Quique Quinto", "Willie Shakes", 2)
library.add_book("Romi y Julito", "Willie Shakes", 1)
library.add_book("Mi Vida con Álvarez", "Alberto Borges", 1)

log_book = BooksInOut(library)

tito = Member("Tito", 12345678)
pepe = Member("Pepe", 87654321)

print(f"\nBooks: {library.books}")
print(f"Members: {tito.__str__()} - {pepe.__str__()}\n")

log_book.lend_book("Romi y Julito", "Willie Shakes", tito)
log_book.lend_book("Romi y Julito", "Willie Shakes", pepe)
log_book.lend_book("Quique Quinto", "Alberto Borges", tito)
log_book.lend_book("Mi Vida con Álvarez", "Alberto Borges", tito)
log_book.lend_book("Mi Vida con Álvarez", "Alberto Borges", pepe)

print(f"\nBooks: {library.books}")
print(f"Members: {tito.__str__()} - {pepe.__str__()}\n")

log_book.receive_book("Romi y Julito", "Willie Shakes", tito)
log_book.receive_book("Mi Vida con Álvarez", "Alberto Borges", tito)
log_book.lend_book("Mi Vida con Álvarez", "Alberto Borges", pepe)
log_book.lend_book("Quique Quinto", "Willie Shakes", tito)

print(f"\nBooks: {library.books}")
print(f"Members: {tito.__str__()} - {pepe.__str__()}\n")
