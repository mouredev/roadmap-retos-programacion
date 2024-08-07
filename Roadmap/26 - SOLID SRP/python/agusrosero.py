"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Forma incorrecta


class Incorrecta:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Empleado: {self.name}, Posicion: {self.position}"

    def generate_report(self):
        return f"Generando reporte para empleado: {self.name}"

# Forma correcta


class Correcta:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_details(self):
        return f"Empleado: {self.name}, Posicion: {self.position}"


class Correcta2:
    def __init__(self, employee):
        self.employee = employee

    def generate_report(self):
        return f"Generando reporte para empleado: {self.employee.name}"


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
 */
"""
