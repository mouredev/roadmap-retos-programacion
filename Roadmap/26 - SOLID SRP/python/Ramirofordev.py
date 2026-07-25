'''
Ejercicio:
Explora el "Principio SOLID de Responsabilidad Unica (Single Responsability Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
'''

#! Forma incorrecta
class Empleado():
    def __init__(self, id, nombre, puesto):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto

    def calcular_salario(self):
        horas = int(input("Inserte la cantidad de horas trabajadas: "))
        print(f"Su salario es de {horas * 40}")

    def generar_informe(self): 
        print(f"El trabajador {self.nombre}, con el identificador unico {self.id} esta trabajando en el area {self.puesto}")

#! Forma correcta
class Empleado:
    def __init__(self, id, nombre, puesto):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto

class CalculadoraSalario:
    def calular(self, empleado, horas, tarifa_hora):
        return f"El {empleado.nombre} ha ganado {horas * tarifa_hora}"
    
class GeneradorInforme:
    def generar(self, empleado, salario):
        return f"{empleado.nombre} ({empleado.id}) - Puesto: {empleado.puesto} - Salario: {salario}"
    
'''
Dificultad extra:
Desarrolla un sistema de gestion para una biblioteca. El sistema necesita manejar diferentes aspectos como el registro de libros, la gestion de usuarios y el procesamiento de libros.

Requisitos:
    1. Registrar libros: El sistema debe permitir agregar nuevos libros con informacion basica como titulo, autor y numero de copias disponibles.
    2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con informacion basica como nombre, numero de identificacion y correo electronico.
    3. Procesar y prestamos de libros: El sistema debe permitir a los usuarios tomar prestados y devolver libros.

Instrucciones:
    1. Diseña una clase que no cumple el SRP: Crea una clase de Library que maneje los tres aspectos mencionados anteriormente (registro de libros, usuarios y procesamiento de prestamos)
    2. Refactoriza el codigo: Separa las responsabilidades en diferentes cdlases siguiendo el principio de responsabilidad unica.
'''

class Library: 
    def registrar_libro(self, titulo, autor, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles

    def registrar_usuario(self, nombre, id, correo):
        self.nombre = nombre
        self.id = id
        self.correo = correo

    def prestamos_libros(self, libro):
        if self.copias_disponibles > 0:
            print(f"El usuario {self.nombre}, ha tomado prestado el libro {self.titulo}")
            self.copias_disponibles -= 1
        else:
            print(f"Ya no poseemos mas copias del libro {self.titulo}")

class BookManager:
    def __init__(self, titulo, autor, copias_disponibles = 1):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles

class UserManager:
    def __init__(self, nombre, id, correo):
        self.nombre = nombre
        self.id = id
        self.correo = correo

class LoanManager:
    def prestamos(self, book, user):
        if book.copias_disponibles > 0:
            print(f"{user.nombre} ha tomado prestado el libro {book.titulo}")
            book.copias_disponibles -= 1
        else:
            print("No tenemos ese libro disponible")

    def devolver(self, book, user):
        print(f"{user.nombre} ha devuelto el libro {book.titulo}.")
        book.copias_disponibles += 1