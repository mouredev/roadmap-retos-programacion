"""
26 - Principios de Responsabilidad Unica (SRP)
"""
# "Una clase debe tener una, y solo una, razon para cambiar."
# Una clase solamente debe tener una unica responsbilidad o funcion en el sistema.

"""
Beneficios
"""
# Mantenibilidad mejorada: Cada clase es más pequeña y enfocada, lo que facilita la comprensión y modificación.
# Código más testeable: Es más fácil escribir pruebas unitarias para clases con una sola responsabilidad.
# Reducción de acoplamiento: Las clases dependen menos unas de otras.
# Mayor reutilización: Servicios como el de email pueden reutilizarse en diferentes contextos.
# Cambios más localizados: Si cambia la forma de autenticación, solo necesitamos modificar ServicioAutenticacion.

"""
¿Cómo identificar si una clase viola el SRP?
"""
# Si al describir lo que hace la clase usas "y" o "también", probablemente tenga más de una responsabilidad.
# Si los métodos de la clase manipulan diferentes tipos de datos o recursos.
# Si los cambios en una parte del código afectan a funcionalidades no relacionadas.

"""
Ejemplo
"""

class Usuario:
    def __init__(self, nombre: str, email:str):
        self.nombre = nombre
        self.email = email
        self.esta_logueado = False

    def actualizar_estado_login(self, esta_logueado: bool):
        self.esta_logueado = esta_logueado

    
class Autenticacion:
    def login(self, usuario: Usuario):
        print(f'El usuario {usuario.nombre} ha iniciado sesion.')
        usuario.actualizar_estado_login(True)

    def logout(self, usuario: Usuario):
        print(f'El usuario {usuario.nombre} ha cerrado sesion.')
        usuario.actualizar_estado_login(False)

usuario = Usuario('Diego', 'diego@example.com')
autenticacion_usuario = Autenticacion()

autenticacion_usuario.login(usuario)
autenticacion_usuario.logout(usuario)


"""
Extra
"""
# Gestion sistema de biblioteca
# Resgistrar libros
# Registrar usuarios
# Prestamo de libro


class Users:
    def __init__(self, name: str, id: int, email: str):
        self.name = name
        self.id = id
        self.email = email

class Books:
    def __init__(self, title: str, author:str, available_copies: int):
        self.title = title
        self.author = author
        self.available_copies = available_copies

class BookLoans:
    def __init__(self):
        self.loans = []
    
    def lend_book(self, user: Users, book: Books):
        if book.available_copies > 0:
            book.available_copies -= 1
            self.loans.append({'user_id': user.id, 'title_book': book.title})
            print(f'El libro {book.title} a sido prestado con exito')
        else:
            print(f'Lo sentimos el libro {book.title} no tiene copias actualmente.')

    def return_book(self, user: Users, book:Books):
        for loan in self.loans:
            if loan['user_id'] == user.id and loan['title_book'] == book.title:
                self.loans.remove(loan)
                book.available_copies += 1
                print(f'El libro {book.title} ha sido devuelto con exito.')
            else:
                print(f'El libro no se ha devuelto.')


usuario_1 = Users('Diego', 1, 'diego@example.com')
usuario_2 = Users('Andres', 2, 'andres@example.com')
libro_1 = Books('El Hobbit', 'J.R.R. Tolkien', 1)

prestamo_libro = BookLoans()
prestamo_libro.lend_book(usuario_1, libro_1)
prestamo_libro.lend_book(usuario_2, libro_1)
prestamo_libro.return_book(usuario_1, libro_1)
prestamo_libro.lend_book(usuario_2, libro_1)