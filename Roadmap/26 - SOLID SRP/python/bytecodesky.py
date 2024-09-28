'''
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
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
 */
'''

#El principio de SRP consiste en que una clase debe tener una única responsabilidad, es decir, una clase debe tener una única razón para cambiar. Si una clase tiene más de una responsabilidad, entonces la clase debe ser dividida en clases más pequeñas, cada una con una única responsabilidad.

#Ejemplo incorrecto
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def dibujar(self):
        for i in range(self.alto):
            print('*' * self.ancho)
#Es incorrecto porque la clase Rectangulo tiene dos responsabilidades: calcular el área y dibujar el rectángulo, por lo que no cumple con el principio SRP.

#Ejemplo correcto

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto

class DibujarRectangulo:
    def __init__(self, rectangulo):
        self.rectangulo = rectangulo
    
    def dibujar(self):
        for i in range(self.rectangulo.alto):
            print('*' * self.rectangulo.ancho)

#En este ejemplo, la clase Rectangulo tiene la responsabilidad de calcular el área, mientras que la clase DibujarRectangulo tiene la responsabilidad de dibujar el rectángulo. Cada clase tiene una única responsabilidad, por lo que cumple con el principio SRP.

#Ejemplo de sistema de gestión de biblioteca incorrecto

class Library:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def prestar_libro(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        prestamo = (libro, usuario, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
    
    def devolver_libro(self, prestamo):
        self.prestamos.remove(prestamo)

#Es incorrecto porque la clase Library tiene tres responsabilidades: registrar libros, registrar usuarios y procesar préstamos de libros, por lo que no cumple con el principio SRP.

#Ejemplo de sistema de gestión de biblioteca corecto

class Library:
    def __init__(self, titulo, autor, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles

class Usuario:
    def __init__(self, nombre, identificacion, correo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class RegistroLibros:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)

class RegistroUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

class ProcesarPrestamos:
    def __init__(self):
        self.prestamos = []
    
    def prestar_libro(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
    
    def devolver_libro(self, prestamo):
        self.prestamos.remove(prestamo)

#En este ejemplo, se han creado diferentes clases para manejar las responsabilidades de registrar libros, registrar usuarios y procesar préstamos de libros. Cada clase tiene una única responsabilidad, por lo que cumple con el principio SRP.
