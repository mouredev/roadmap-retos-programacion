# EJERCICIO:
# Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
# Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.

# --- EJEMPLO INCORRECTO ---


class UserIncorrect:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def save_to_db(self):
        # Responsabilidad 1: Manejo de persistencia
        print(f"Guardando usuario {self.name} en la base de datos...")

    def send_welcome_email(self):
        # Responsabilidad 2: Manejo de notificaciones/email
        print(f"Enviando correo de bienvenida a {self.email}...")

    def generate_report(self):
        # Responsabilidad 3: Generación de documentos/formateo
        print(f"Generando reporte PDF para el usuario {self.name}...")


# --- EJEMPLO CORRECTO ---
class User:
    """Clase que solo maneja los datos del usuario."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class UserRepository:
    """Clase encargada exclusivamente de la persistencia."""

    def save(self, user: User):
        print(f"Guardando usuario {user.name} en la base de datos...")


class EmailService:
    """Clase encargada exclusivamente de enviar correos."""

    def send_welcome_email(self, user: User):
        print(f"Enviando correo de bienvenida a {user.email}...")


class UserReportGenerator:
    """Clase encargada de generar reportes."""

    def generate(self, user: User):
        print(f"Generando reporte PDF para el usuario {user.name}...")


# Uso correcto:
user = User("Cristian", "cristian@example.com")
repo = UserRepository()
email_service = EmailService()

repo.save(user)
email_service.send_welcome_email(user)


#
# DIFICULTAD EXTRA (opcional):
# Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
# manejar diferentes aspectos como el registro de libros, la gestión de usuarios
# y el procesamiento de préstamos de libros.
# Requisitos:
# 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
# información básica como título, autor y número de copias disponibles.
# 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
# información básica como nombre, número de identificación y correo electrónico.
# 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
# tomar prestados y devolver libros.
# Instrucciones:
# 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
# los tres aspectos mencionados anteriormente (registro de libros, registro de
# usuarios y procesamiento de préstamos).
# 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
# siguiendo el Principio de Responsabilidad Única.


# --- EJEMPLO INCORRECTO ---
class LibraryIncorrect:
    def __init__(self):
        self.libros = []
        self.users = []
        self.prestamos = []

    def add_libro(self, titulo: str, autor: str, copias: int):
        self.libros.append({"titulo": titulo, "autor": autor, "copias": copias})

    def registrar_usuario(self, nombre: str, id: int, email: str):
        usuario = {"nombre": nombre, "id": id, "email": email}
        self.users.append(usuario)

    def libro_prestado(self, usuario_id: int, libro_title: str):
        for libro in self.libros:
            if libro["titulo"] == libro_title and libro["copias"] > 0:
                libro["copias"] -= 1
                self.prestamos.append(
                    {"usuario_id": usuario_id, "libro_title": libro_title}
                )
                return True
        return False

    def libro_devolver(self, usuario_id: int, libro_title: str):
        for prestamo in self.prestamos:
            if (
                prestamo[usuario_id] == usuario_id
                and prestamo["libro_title"] == libro_title
            ):
                self.prestamos.remove(prestamo)
                for libro in self.libros:
                    if libro["titulo"] == libro_title:
                        libro["copias"] += 1
                    return True
        return False


# --- EJEMPLO REFACTORIZADO ---
# Entidades
class Libro:
    def __init__(self, id: int, title: str, author: str, copies: int):
        self.id = id
        self.title = title
        self.author = author
        self.copies = copies

    def __repr__(self):
        return f"Libro(id={self.id}, title='{self.title}', copies={self.copies})"


class Usuario:
    def __init__(self, id: int, name: str, email: str):
        self.name = name
        self.id = id
        self.email = email

    def __repr__(self):
        return f"Usuario(id={self.id}, name='{self.name}', email='{self.email}')"


class Prestamo:
    def __init__(self, libro_id: int, user_id: int):
        self.id = libro_id
        self.user_id = user_id

    def __repr__(self):
        return f"Prestamo(libro_id={self.id}, user_id={self.user_id})"


# Repositorios
class LibroRepository:
    def __init__(self):
        self.libros = []

    def add_libro(self, libro: Libro):
        self.libros.append(libro)


    def find_by_id(self, id: int):
        for libro in self.libros:
            if libro.id == id:
                return libro
        return None

    def update_libro(self, libro: Libro):
        for i, lib in enumerate(self.libros):
            if lib.id == libro.id:
                self.libros[i] = libro
                return True
        return False

    def last_id(self) -> int:
        return self.libros[-1].id


class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def registrar(self, usuario: Usuario):
        if usuario in self.usuarios:
            print(f"Usuario {usuario.name} ya se encuentra registrado")
            return
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.name} registrado correctamente")

    def find_by_id(self, usuario_id: int):
        for usuario in self.usuarios:
            if usuario.id == usuario_id:
                return usuario
        return None

    def last_id(self) -> int:
        return self.usuarios[-1].id


# Servicio
class PrestamoService:
    def __init__(
        self, libro_repository: LibroRepository, usuario_repository: UsuarioRepository
    ):
        self.prestamos = []
        self.usuario_repository = usuario_repository
        self.libro_repository = libro_repository

    def prestar_libro(self, usuario_id: int, libro_id: int):
        usuario = self.usuario_repository.find_by_id(usuario_id)
        libro = self.libro_repository.find_by_id(libro_id)
        if usuario and libro:
            if libro.copies > 0:
                libro.copies -= 1
                self.prestamos.append(Prestamo(libro_id, usuario_id))
                print(f"Libro {libro.title} prestado a {usuario.name}")
                return True
            print(f"No hay copias disponibles del libro {libro.title}")
            return False
        print("Usuario o libro no encontrado")
        return False

    def devolver_libro(self, usuario_id: int, libro_id: int):
        for prestamo in self.prestamos:
            if prestamo.user_id == usuario_id and prestamo.id == libro_id:
                libro = self.libro_repository.find_by_id(libro_id)
                if libro:
                    libro.copies += 1
                    self.prestamos.remove(prestamo)
                    print(f"Libro {libro.title} devuelto por {usuario_id}")
                    return True
                print("Libro no encontrado")
                return False
        print("Prestamo no encontrado")
        return False

    def last_id(self) -> int:
        return self.prestamos[-1].id


# ORQUESTADOR DEL SISTEMA
class LibraryManager:
    """
    Responsabilidad: Orquestar el sistema de gestión de la biblioteca.
    """

    def __init__(self):
        self.libro_repository = LibroRepository()
        self.usuario_repository = UsuarioRepository()
        self.prestamo_service = PrestamoService(
            self.libro_repository, self.usuario_repository
        )

    def add_libro(self, id: int, title: str, author: str, copies: int):
        libro = Libro(id, title, author, copies)
        return self.libro_repository.add_libro(libro)

    def registrar_usuario(self, user_id: int, name: str, email: str):
        usuario = Usuario(user_id, name, email)
        return self.usuario_repository.registrar(usuario)

    def prestar_libro(self, user_id: int, book_id: int):
        return self.prestamo_service.prestar_libro(user_id, book_id)

    def devolver_libro(self, user_id: int, book_id: int):
        return self.prestamo_service.devolver_libro(user_id, book_id)


def main():
    print("=" * 100)
    print("Iniciando sistema de gestión de biblioteca...")
    library_manager = LibraryManager()
    library_manager.add_libro(1, "Libro 1", "Autor 1", 10)
    library_manager.add_libro(2, "Libro 2", "Autor 2", 10)
    library_manager.add_libro(3, "Libro 3", "Autor 3", 10)
    library_manager.registrar_usuario(1, "arca", "usuario1@example.com")
    library_manager.registrar_usuario(2, "cristian", "usuario2@example.com")
    library_manager.prestar_libro(1, 1)
    library_manager.devolver_libro(1, 1)
    library_manager.devolver_libro(1, 2)
    library_manager.prestar_libro(2, 2)
    print(library_manager.libro_repository.libros)
    print(library_manager.usuario_repository.usuarios)
    print(library_manager.prestamo_service.prestamos)
    print("=" * 100)


if __name__ == "__main__":
    main()
