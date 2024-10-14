#26 SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
"""
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
"""

import os


#uso incorrecto
class AdministradorDeEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for empleado in self.empleados:
                archivo.write(f'{empleado}\n')

    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            self.empleados = [linea.strip() for linea in archivo]

#uso correcto
class AdministradorDeEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)

class AlmacenamientoDeEmpleadosEnArchivo:
    def guardar_en_archivo(self, empleados, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for empleado in empleados:
                archivo.write(f'{empleado}\n')

    def cargar_desde_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return [linea.strip() for linea in archivo]

# Uso del código
administrador = AdministradorDeEmpleados()
administrador.agregar_empleado('Juan Perez')
administrador.agregar_empleado('Ana Gomez')

almacenamiento = AlmacenamientoDeEmpleadosEnArchivo()
almacenamiento.guardar_en_archivo(administrador.empleados, 'empleados.txt')
administrador.empleados = almacenamiento.cargar_desde_archivo('empleados.txt')
print(administrador.empleados)
os.remove('empleados.txt')

"""
cada clase solo tiene que cumplir una funcionalidad y no sobrecargar una clase en su lugar hacer
otras clases o funciones aparte para que cada una cumpla una funcion especifica en ves de que una
clase lo haga o tenga todo
"""

#Extra

#No usando SRP
class Librery:
    libros = []
    usuario = []
    prestamos = []

    def registrar_libro(self , titulo , autor , copias_disponibles):
        datos = [titulo , autor , copias_disponibles]
        info_libro = "--".join(datos)
        self.libros.append(f"Informacion del libro : {info_libro}")

    def registrar_usuario(self , nombre , id , correo):
        datos = [nombre , id , correo]
        info_usuario = "==".join(datos)
        self.usuario.append(f"Informacion del usuario : {info_usuario}")

    def registrar_prestamos(self , usuario , libro):
        self.formato = f"el usuario : {usuario} iso un prestamo del libro {libro}"
        self.prestamos.append(self.formato)

    def devolver(self , usuario , libro):
        if self.formato in self.prestamos:
            print(f"el usuario {usuario} regreso el libro {libro}")

        else :
            print(f"el usuario {usuario} no ha prestado el libro {libro}")

#usando SRP
class GestionLibros:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, titulo, autor, copias_disponibles):
        datos = [titulo, autor, copias_disponibles]
        info_libro = "--".join(datos)
        self.libros.append(f"Información del libro: {info_libro}")

class GestionUsuarios:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, id, correo):
        datos = [nombre, id, correo]
        info_usuario = "==".join(datos)
        self.usuarios.append(f"Información del usuario: {info_usuario}")

class GestionPrestamos:
    def __init__(self):
        self.prestamos = []

    def registrar_prestamo(self, usuario, libro):
        formato = f"el usuario: {usuario} hizo un préstamo del libro {libro}"
        self.prestamos.append(formato)
        return formato

    def devolver(self, usuario, libro):
        formato = f"el usuario: {usuario} hizo un préstamo del libro {libro}"
        if formato in self.prestamos:
            self.prestamos.remove(formato)
            print(f"el usuario {usuario} regresó el libro {libro}")
        else:
            print(f"el usuario {usuario} no ha prestado el libro {libro}")

# Crear instancias de las clases
gestion_libros = GestionLibros()
gestion_usuarios = GestionUsuarios()
gestion_prestamos = GestionPrestamos()

# Registrar libros
gestion_libros.registrar_libro('Cien Años de Soledad', 'Gabriel García Márquez', '5')
gestion_libros.registrar_libro('Don Quijote', 'Miguel de Cervantes', '3')

# Registrar usuarios
gestion_usuarios.registrar_usuario('Juan Pérez', '1', 'juan.perez@example.com')
gestion_usuarios.registrar_usuario('Ana Gómez', '2', 'ana.gomez@example.com')

# Registrar préstamos
formato_prestamo = gestion_prestamos.registrar_prestamo('Juan Pérez', 'Cien Años de Soledad')

# Devolver libros
gestion_prestamos.devolver('Juan Pérez', 'Cien Años de Soledad')
gestion_prestamos.devolver('Ana Gómez', 'Don Quijote')
