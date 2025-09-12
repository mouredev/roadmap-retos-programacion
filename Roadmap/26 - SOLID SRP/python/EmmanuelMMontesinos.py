"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 */
"""
# SOLID: Principio de responsabilidad única

'''Sin aplicar'''
class Pedido:
    def __init__(self,plato,numero,precio) -> None:
        self.comanda = []
        self.total = 0
        self.comanda.append((plato,precio,numero))
        self.total += precio * numero
    
# Prueba
mi_pedido = Pedido("pollo",1,5.2)
print(mi_pedido.total)

'''Aplicado'''
class Pedido_2:
    def __init__(self) -> None:
        self.comanda = []
    
    def agregar_plato(self,plato,precio,numero):
        self.comanda.append((plato,precio,numero))
        self.calcula_total()

    def calcula_total(self):
        total = 0
        for plato,precio,numero in self.comanda:
            parte = precio*numero
            total += parte
            print(f"{plato} -> Precio: {precio} X {numero} -> {parte}")
        print(f"------------Total: {total}€-------------\n")

# Prueba
mi_pedido_2 = Pedido_2()
mi_pedido_2.agregar_plato("Pollo",5.20,1)
mi_pedido_2.agregar_plato("Coca Cola",2.50,4)
mi_pedido_2.agregar_plato("Cafe",1.20,6)

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

'''Sin Aplicar'''

class Librery:
    def __init__(self) -> None:
        self.users = {}
        self.books = {}
    
    def add_book(self,name,autor,n_copy):
        self.books[name.lower()] = [autor.lower(),n_copy]
    
    def add_user(self,user,id,email):
        self.users[user.lower()] = [id,email.lower()]

    def lend_book(self,name_book,user):
        if user.lower() in self.users.keys():
            if name_book.lower() in self.books.keys():
                autor,copy = self.books[name_book.lower()]
                if copy > 0:
                    self.books[name_book.lower()][1] -= 1
                    print(f"{name_book} de {autor.title()} prestado a {user} con id {self.users[user.lower()][0]}\n")


# Prueba
my_librery = Librery()
my_librery.add_book("Git y Github desde cero","Brais Moure", 5)
my_librery.add_user("Emmanuel",1,"emmanuelmmontesinos@xmail.com")
my_librery.lend_book("Git y Github desde cero","Emmanuel")

'''Aplicado'''

class User:
    list_users = {}
    def add_user(self,user,id,email):
        User.list_users[user.lower()] = [id,email.lower()]

class Book:
    list_books = {}
    def add_book(self,name,autor,n_copy):
        Book.list_books[name.lower()] = [autor.lower(),n_copy]
    

class Librery_2:
    list_users = User().list_users
    list_books = Book().list_books

    def add_book(self,name,autor,n_copy):
        Book.add_book(Book,name,autor,n_copy)
    
    def add_user(self,user,id,email):
        User.add_user(User,user,id,email)

    def lend_book(self,name_book,user):
        if user.lower() in Librery_2.list_users.keys():
            if name_book.lower() in Librery_2.list_books.keys():
                autor,copy = Librery_2.list_books[name_book.lower()]
                if copy > 0:
                    Librery_2.list_books[name_book.lower()][1] -= 1
                    print(f"{name_book} de {autor.title()} prestado a {user} con id {Librery_2.list_users[user.lower()][0]}")

# Prueba

my_librery_2 = Librery_2()
my_librery_2.add_book("Git y Github desde cero","Brais Moure", 5)
my_librery_2.add_user("Emmanuel",17,"emmanuelmmontesinos@xmail.com")
my_librery_2.lend_book("Git y Github desde cero","Emmanuel")

