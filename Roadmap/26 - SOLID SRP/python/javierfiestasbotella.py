'''/*
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
 */'''

#Ejemplo de SOLID Creamos 3 clases cada una con una funcion
class Factura:
    def __init__(self, items):
        self.items = items 
    def calcular_total(self):
        return sum(item['precio'] for item in self.items)

class ImpresoraDeFacturas:
    def imprimir_factura(self, factura):
        print("Factura:")
        for item in factura.items:
            print(f"{item['nombre']}: {item['precio']}")
        print(f"Total: {factura.calcular_total()}")

class GuardarFactura:
    def guardar_en_bd(self, factura):
        print("Guardando la factura en la base de datos...")
   
#Ahora creamos lo que no se debería hacer una sola clase con las trés funciones
class Factura:
    def __init__(self, items):
        self.items = items

    def calcular_total(self):
        return sum(item['precio'] for item in self.items)

    def imprimir_factura(self):
        print("Factura:")
        for item in self.items:
            print(f"{item['nombre']}: {item['precio']}")
        print(f"Total: {self.calcular_total()}")

    def guardar_en_bd(self):
        print("Guardando la factura en la base de datos...")


#EJEMPLO DE LA BIBLIOTECA

'''* 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).'''
 
class Biblioteca:
    def __init__(self, items):
        self.items = items

    def registrar_libro(self):
        registro=[]
        for item in self.items:
            registro.append(item['numero_libro']+item['titulo_libro']+item['autor_libro'])
    def registrar_usuario(self):
        bbdd=[]
        for item in self.items:
            bbdd.append(item['dni']+item['nombre'])
    def prestamos(self):
        prestamos_note=[]
        for item in self.items:
            prestamos_note.append(item['dni']+item['titulo_libro'])

'''* 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.'''

class RegistroLibros:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, numero_libro, titulo_libro, autor_libro):
        libro = {
            'numero_libro': numero_libro,
            'titulo_libro': titulo_libro,
            'autor_libro': autor_libro,
            'copias_disponibles': 1
        }
        self.libros.append(libro)

    def listar_libros(self):
        return self.libros

class RegistroUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, dni, nombre, correo):
        usuario = {
            'dni': dni,
            'nombre': nombre,
            'correo': correo
        }
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        return self.usuarios


class GestionPrestamos:
    def __init__(self, registro_libros, registro_usuarios):
        self.prestamos = []
        self.registro_libros = registro_libros
        self.registro_usuarios = registro_usuarios

    def prestar_libro(self, dni, numero_libro):
        usuario = next((u for u in self.registro_usuarios.listar_usuarios() if u['dni'] == dni), None)
        libro = next((l for l in self.registro_libros.listar_libros() if l['numero_libro'] == numero_libro), None)

        if usuario and libro and libro['copias_disponibles'] > 0:
            self.prestamos.append({'dni': dni, 'numero_libro': numero_libro})
            libro['copias_disponibles'] -= 1
            print(f"Libro {numero_libro} prestado a {usuario['nombre']}")
        else:
            print("Préstamo no disponible")

    def devolver_libro(self, dni, numero_libro):
        prestamo = next((p for p in self.prestamos if p['dni'] == dni and p['numero_libro'] == numero_libro), None)
        if prestamo:
            self.prestamos.remove(prestamo)
            libro = next((l for l in self.registro_libros.listar_libros() if l['numero_libro'] == numero_libro), None)
            libro['copias_disponibles'] += 1
            print(f"Libro {numero_libro} devuelto por {dni}")
        else:
            print("No se encontró el préstamo")
