### SOLID PRINCPIO DE RESPONSABILIDAD ÚNICA (SRP)

'''
El Principio de Responsabilidad Única (SRP) es uno de los cinco principios SOLID en la programación orientada a objetos. 
Este principio establece que una clase debe tener una única razón para cambiar, es decir, una sola responsabilidad o 
propósito.
En términos simples, cada clase debe encargarse de una sola tarea y hacerlo bien.
'''

'''
VENTAJAS:
- Facilita la comprensión y el mantenimiento del código.
- Reduce la complejidad del código.
- Mejora la reutilización del código.
'''

# Ejemplo que viola este principio
#class User():
#    
#    def __init__(self, name, email):
#        self.name = name
#        self.email = email
#        
#    def save_to_file(self):
#        with open('users.txt', 'w') as file:
#            file.write(f"Name: {self.name}, Email: {self.email}")

# El ejemplo anterior viola el SRP, ya que gestiona tanto los datos del usuario como su almacenamiento en un registro.

# Vamos a reestructuar el diseño para cumplir con SRP con dos clases separadas
#class User():
#    
#    def __init__(self, name, email):
#        self.name = name
#        self.email = email
#
#class UserFileHandler():
#    @staticmethod
#    def save_to_file(user, filename):
#        with open(filename, 'w') as file:
#            file.write(f"Name: {user.name}, Email: {user.email}")


# Prueba de funcionamiento
#user = User("Manuel", "manuel@example.com")
#UserFileHandler.save_to_file(user, "user_data.txt")


## EJERCICIO EXTRA

# Clase que incumple el principio SRP
#class Library():
#    
#    users = []
#    loans = []
#    
#    def __init__(self, title, author, copies):
#                
#        self.books.append({'title': title, 'author':author, 'copies': copies})
#        
#    def register_book(self, title, author, copies):
#        self.books.append({'title': title, 'author': author, 'copies': copies})
#        print(f"Registro de libro realizado con éxito")
#    
#    def register_user(self, name, id, email):
#        self.users.append({'name': name, 'id': id, 'email': email})
#        print(f"Registro de usuario realizado con éxito")
#    
#    def loan_book(self, user, book):
#        if book['copies'] > 0:
#            self.loans.append({'user': user, 'book': book})
#            book['copies'] -= 1
#            print(f"Préstamo de libro realizado con éxito")
#        else:
#            print(f"No hay copias disponibles del libro {book['title']}")
#    
#    def return_book(self, user, book):
#        if user in [loan['user'] for loan in self.loans] and book in [book['name'] for book in self.books]:
#            self.loans.remove({'user': user, 'book': book})
#            book['copies'] += 1
#            print(f"Devolución de libro realizada con éxito")
#        else:
#            print(f"No hay préstamos activos del libro {book['title']}")

# Aplicando SRP
class User():
    
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email
    
class Book():
    
    def __init__(self, name, author, copies):
        self.name = name
        self.author = author
        self.copies = copies
        
class Library():
    
    def __init__(self, users = [], books = [], loans=[]):
        self.users = users
        self.books = books
        self.loans = loans
        
    def register_user(self, user: User):
        self.users.append(user)
        print(f"Registro de usuario realizado con éxito")
    
    def register_book(self, book: Book):
        self.books.append(book)
        print(f"Registro de libro realizado con éxito")
        
    def register_loan(self, user: User, book: Book):
        if book.copies > 0:
            self.loans.append({"user": user, "book" : book})
            book.copies -= 1
            print(f"Préstamo de libro realizado con éxito")
        else:
            print(f"No hay copias disponibles del libro {book.name}")
    
    def return_loan(self, user: User, book: Book):
        if user in [loan['user'] for loan in self.loans] and book in [loan['book'] for loan in self.loans]:
            self.loans.remove({'user': user, 'book': book})
            book.copies += 1
            print(f"Devolución de libro realizada con éxito")

# Pruebas del programa          
user1 = User(name="Manuel", id=1, email="manuel@correo.es")
user2 = User(name="Pedro", id=2, email="pedro@correo.es")
book1 = Book(name="Libro 1", author="Autor 1", copies=2)
book2 = Book(name="Libro 2", author="Autor 2", copies=1)
library = Library()
library.register_user(user1)
library.register_user(user2)
library.register_book(book1)
library.register_book(book2)
library.register_loan(user1, book1)
library.register_loan(user2, book2)
library.register_loan(user1, book2)
library.return_loan(user2, book2)
library.register_loan(user1, book2)

# Fin Aplicando SRP
    
## FIN EJERCICIO EXTRA

### FIN SOLID PRINCPIO DE RESPONSABILIDAD ÚNICA (SRP)