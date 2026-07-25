"""
Ejercicio
"""

# Incorrecta

class Usuario():
    
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        
    def save_to_database(self):
        pass
    
    def send_email(self):
        pass

# Correcta
    
class User:
    
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        

class DataBase:
    data = {}
    def save_to_database(self, user):
        pass
    
class EmailService:
    
    def send_email(self, email, message):
        pass
    

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

class Library:
    
    def __init__(self):
        self.libros = []
        self.users = []
        self.prestamos = []
        
    def añadir_libro(self, titulo, autor, copias):
        self.libros.append({"titulo" : titulo, "autor" : autor, "copias" : copias})
        
    def registrar_users(self, name, user_id, email):
        self.users.append({"nombre" : name, "id" : user_id, "email" : email})
        
    def prestar_libro(self, user_id, titulo):
        for libro in self.libros:
            if libro["titulo"] == titulo and libro["copias"] > 0:
                libro["copias"] -= 1
                self.prestamos.append(
                    {"user_id" : user_id, "titulo" : titulo}
                )
                return True
        return False

    def retornar_libro(self, user_id, titulo):
        for prestamo in self.prestamos:
            if prestamo["user_id"] ==  user_id and prestamo["titulo"] == titulo:
                self.prestamos.remove(prestamo)
                for libro in self.libros:
                    if libro["titulo"] == titulo:
                        libro["copias"] += 1
                    return True
        return False

# Correcta

    
    
class Libro:
    
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
        
    
class User:
    
    def __init__(self, nombre, user_id, email):
        self.nombre = nombre
        self.user_id = user_id
        self.email = email
        
class Prestamo:
    
    def __init__(self):
        self.prestamos = []
    
    def prestar_libro(self, usuario, libro):
        if libro.copias > 0:
            libro.copias -= 1
            self.prestamos.append(
                {"user_id" : usuario.id, "titulo" : libro.titulo}
            )
            return True
        return False
    
    def devolver_libro(self, usuario, libro):
        for prestamo in self.prestamos:
            if prestamo["user_id"] == usuario.id and prestamo["titulo"] == libro.titulo:
                self.prestamos.remove(prestamo)
                libro.copias += 1
                return True
        return False

class Library:
    
    def _init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = Prestamo() 
        
    def añadir_libro(self, libro):
        self.libros.append(libro)

    def añadir_usuario(self, usuario):
        self.usuarios.append(usuario)
        
    def prestar_libro(self, user_id, titulo_libro):
        user = next((u for u in self.usuarios if u.user_id == user_id), None)
        book = next((b for b in self.libros if b.titulo == titulo_libro), None)
        if user and book:
            return self.prestamos.prestar_libro(user, book)
        return False
    
    def retornar_libro(self, user_id, titulo_libro):
        user = next((u for u in self.usuarios if u.user_id == user_id), None)
        book = next((b for b in self.libros if b.titulo == titulo_libro), None)
        if user and book:
            return self.prestamos.devolver_libro(user, book)
        return False

