"""
    Explora el concepto de funciones de orden superior en tu lenguaje 
    creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""


class Singleton():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

"""
    Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
    lista de calificaciones), utiliza funciones de orden superior para 
    realizar las siguientes operaciones de procesamiento y análisis:
        - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
            y promedio de sus calificaciones.
        - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
            que tienen calificaciones con un 9 o más de promedio.
        - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
        - Mayor calificación: Obtiene la calificación más alta de entre todas las
            de los alumnos.
        - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).

"""


class UserSession():
    _instance = None

    id = int
    username = str
    name = str
    email = str

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, id, name, username, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id},{self.username},{self.name},{self.email}"

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None


session1 = UserSession()
print(session1.get_user())
session1.set_user(1, "aldroide", "Aldo AC", "aldroidegmail.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())
