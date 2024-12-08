
"""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
"""

class Singleton():
    
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

class SonSingleton(Singleton):
    pass

my_singleton1 = Singleton()
my_singleton2 = Singleton()
my_singleton3 = SonSingleton()
print(my_singleton1)
print(my_singleton2)
print(my_singleton3)

"""

 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */

"""

class UserSession: 

    id = None
    username = None
    nombre = None
    email = None
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def new_user(self, id, username, nombre, email):
        self.id = id
        self.username = username
        self.nombre = nombre
        self.email = email
    def show_data_user(self):
        print(f"{self.id , self.username, self.nombre, self.email}")

    def clean_data(self):
        self.id = None
        self.username = None
        self.nombre = None
        self.email = None
        



session1 = UserSession()
session2 = UserSession()
print(session1)
print(session2)

session3 = UserSession()
session3.new_user(1, "fborjalv", "Borja", "xxxxx@gmail.com")
session3.show_data_user()
session3.clean_data()

session4 = UserSession()
session4.show_data_user()

