# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
#  * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
#  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
#  * y el procesamiento de préstamos de libros.
#  * Requisitos:
#  * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
#  * información básica como título, autor y número de copias disponibles.
#  * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
#  * información básica como nombre, número de identificación y correo electrónico.
#  * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
#  * tomar prestados y devolver libros.
#  * Instrucciones:
#  * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
#  * los tres aspectos mencionados anteriormente (registro de libros, registro de
#  * usuarios y procesamiento de préstamos).
#  * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
#  * siguiendo el Principio de Responsabilidad Única.
#  */

# incorrect
class Number_I:
    def __init__(self,n1 = 0,n2 =0) -> None:
        self.n1 = n1
        self.n2 = n2

    def sum_numbers(self):
        self.sum = self.n1+self.n2
        
    def rest_numbers(self):
        self.rest = self.n1-self.n2
    
    def mult_number(self):
        self.mult = self.n1*self.n2

    def div_number(self):
        if self.n2 == 0:
            self.div = 0
        else:
            self.div = self.n1/self.n2

    def print_result(self):
        print(self.div)
        print(self.mult)
        print(self.sum)
        print(self.rest)

     

#correct
class Number_c:
    def __init__(self, n1,n2) -> None:
        self.n1 = n1
        self.n2 = n2

class Operation:

    def sum_number(self,n: Number_c):
        self.sum =  n.n1+ n.n2
        
    def rest_number(self,n: Number_c):
        self.rest =  n.n1- n.n2
    
    def mult_number(self,n: Number_c):
        self.mult =  n.n1* n.n2

    def div_number(self,n: Number_c):
        if  n.n2 == 0:
            self.div = 0
        else:
            self.div =  n.n1/ n.n2

class Print:
    
     def print_result(self,result, operation):
            print(f"El resultado de la {operation} es {result}")

         


  

number = Number_I(12,12)
number.rest_numbers()
number.mult_number()
number.sum_numbers()
number.div_number()
number.print_result()

number_1 = Number_c(33,33)
operation = Operation()
p = Print()
operation.div_number(number_1)
operation.mult_number(number_1)
operation.rest_number(number_1)
operation.sum_number(number_1)
p.print_result(operation.div,"division")
p.print_result(operation.mult,"multiplicacion")
p.print_result(operation.rest,"resta")
p.print_result(operation.sum,"suma")


#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
#  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
#  * y el procesamiento de préstamos de libros.
#  * Requisitos:
#  * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
#  * información básica como título, autor y número de copias disponibles.
#  * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
#  * información básica como nombre, número de identificación y correo electrónico.
#  * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
#  * tomar prestados y devolver libros.
#  * Instrucciones:
#  * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
#  * los tres aspectos mencionados anteriormente (registro de libros, registro de
#  * usuarios y procesamiento de préstamos).
#  * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
#  * siguiendo el Principio de Responsabilidad Única.
#  */


# SIn usar SRP
class Book:

    def __init__(self, title, author,copies) -> None:
        self.title = title
        self.author = author
        self.copies = copies
    def print_book(self):
        print(f"Titulo : {self.title}, Autor {self.author}, Copias {self.copies}")

class User:
    def __init__(self,name, id, email) -> None:
        self.name = name
        self.id = id
        self. email = email

    def print_user(self):
        print(f"Nombre : {self.name}, Id {self.id}, email {self.email}")

class library:
    
    prestamo = {}
    user  = []
    book = []

    def Add_user(self, *user: User):
        self.user = list(user)
    
    def Add_book(self, *book:Book):
        self.book = list(book)



    def get_user(self,user ):
        if not user in self.user:
            print(f"Usuario {user.name} no resgistrado, registrese primero")
            return False
        return True
             

    
    def get_book(self,book ):
        if not book in self.book:
            print(f"Libro {book.title} no resgistrado, registrelo primero")
            return False
        return True
             
    
    def get_book_prestamo(self, book: Book):
        for i,v in self.prestamo.items():
            
            if book.title == i.title:
                 print(f"Libro {book.title} actualmente en prestamos, imposible volver a prestar")
                 return True
        return False
    
    def Set_Prestamo(self, user: User, book: Book):
        if not self.get_user(user):
            return
        if not self.get_book(book):
            return
        
        if self.get_book_prestamo(book):
            return
        self.prestamo[book] = user 
        print(f" Libro {book.title } ha sido prestado a {user.name }")
        
    def back_prestamo(self,book: Book):
        
        if not self.get_book(book):
            return
        
        if  not self.get_book_prestamo(book):
            print(f"Libro {book.title} no esta en  prestamos, imposible devolver")
            return
         
        self.prestamo.pop(book)
        print(f"El libro {book.title} se ha devuelto correctamente")
    
    def list_user(self):
        print("Lista de Usuarios")
        for i in self.user:
            print(i.print_user())
    
    def list_book(self):
        print("Lista de libros")
        for i in self.book:
            print(i.print_book())

    def list_prestamos(self):
        print("Lista de prestamos")
        if len(self.prestamo) == 0:
            print(f" NO existen prestamos")
        for i, v in self.prestamo.items():
            print(f" Libro {i.title} Usuario {v.name}")

u1 = User("pepe1",123,"aa@aa")
u2 = User("pepe2",123,"aa@aa")
u3 = User("pepe3",123,"aa@aa")
u4 = User("pepe4",123,"aa@aa")

b1 = Book("b1","cc",12)
b2 = Book("b2","cc",12)
b3 = Book("b3","cc",12)
b4 = Book("b4","cc",12)



library = library()
library.Add_user(u1,u2,u3)
library.Add_book(b1,b2,b3)
library.list_book()
library.list_user()

library.Set_Prestamo(u1 ,b1 )
library.list_prestamos()
library.Set_Prestamo(u2 ,b1 )
library.list_prestamos()
library.Set_Prestamo(u2 ,b2)
library.list_prestamos()

library.back_prestamo(b3 )
library.list_prestamos()
library.back_prestamo(b4 )
library.list_prestamos()
library.Set_Prestamo(u2 ,b3)
library.list_prestamos()
library.back_prestamo(b3 )
library.list_prestamos()

library.Set_Prestamo(u3 ,b2 )
library.Set_Prestamo(u3 ,b3 )
library.list_prestamos()


#  RSP

class Book1:

    def __init__(self, title, author,copies) -> None:
        self.title = title
        self.author = author
        self.copies = copies
    
    

class User1:
    def __init__(self,name, id, email) -> None:
        self.name = name
        self.id = id
        self. email = email

    def print_user(self):
        print(f"Nombre : {self.name}, Id {self.id}, email {self.email}")




class Library1:
    
    

    def __init__(self) -> None:
        self.user = []
        self.book = []
        self.loans = Lending()

    def Add_user(self,*user: User):
        self.user = list(user)

 
    def Add_book(self,*book:Book ):
        self.book = list(book)

    def is_user_in(self,user):
        return user in self.user

    def is_book_in(self,book):
        return book in self.book

    def loan_book(self, user:User,book:Book):
        if not self.is_user_in(user):
            print(f"Usuario {user.name} no resgistrado, registrese primero")
            return
        if not self.is_book_in(book):
            print(f"Libro {book.title} no resgistrado, registrelo primero")
            return 
        
        self.loans.Set_loans(user,book)
    
    def return_book(self,book):
        if not self.is_book_in(book):
            print(f"Libro {book.title} no resgistrado, registrelo primero")
            return 
        self.loans.Back_loans(book)

    
   


class Lending:

    def __init__(self) -> None:
        self.loans =  {}
    

    def Set_loans(self, user: User, book: Book, ):
         
        if book.title in self.loans:
                 print(f"Libro {book.title} actualmente en prestamos, imposible volver a prestar")
                 return True 

        self.loans[book] = user 
        print(f" Libro {book.title } ha sido prestado a {user.name }")
        
    def Back_loans(self,book: Book):
         
        if  not book in self.loans:
            print(f"Libro {book.title} no esta en  prestamos, imposible devolver")
            return
         
        self.loans.pop(book)
        print(f"El libro {book.title} se ha devuelto correctamente")

     

class PrintService:

    # @staticmethod  puede llamarse al metodo sin necesidad de instanciar la clase
    @staticmethod
    def print_book(book: Book1):
        print(f"Titulo : {book.title}, Autor {book.author}, Copias {book.copies}")

    @staticmethod
    def print_user(user: User1):
        print(f"Nombre : {user.name}, Id {user.id}, email {user.email}")

    @staticmethod  
    def list_loans(loans):
        print("Lista de prestamos")
        if len(loans.loans) == 0:
            print(f" NO existen prestamos")
        for i, v in loans.loans.items():
            print(f" Libro {i.title} Usuario {v.name}")

    @staticmethod
    def list_user(users):
        print("Lista de Usuarios")
        for i in users:
           PrintService.print_user(i)

    @staticmethod
    def list_book(books):
        print("Lista de libros")
        for i in books:
            PrintService.print_book(i)
    
    




u11 = User1("user 1",123,"aa@aa")
u22 = User1("user 2",123,"aa@aa")
u33 = User1("user 3",123,"aa@aa")
u44 = User1("user 4",123,"aa@aa")

b11 = Book1("book 1","cc",12)
b22 = Book1("book 2","cc",12)
b33 = Book1("book 3","cc",12)
b44 = Book1("book 4","cc",12)

print("Refactorizando ... RSP")

l1 = Library1()

 
l1.Add_user(u11,u22,u33)
l1.Add_book(b11,b2,b33)
PrintService.list_book(l1.book)
PrintService.list_user(l1.user)
PrintService.list_loans(l1.loans)

l1.loan_book(u44,b1)
l1.loan_book(u1,b44)
l1.loan_book(u11,b11)
l1.loan_book(u22,b33)
PrintService.list_loans(l1.loans)
l1.loan_book(u22,b22)
PrintService.list_loans(l1.loans)
 
 

l1.return_book(b44)
PrintService.list_loans(l1.loans)
l1.return_book(b11)
PrintService.list_loans(l1.loans)
 
 






