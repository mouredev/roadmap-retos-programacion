#23 { Retos para Programadores } PATRONES DE DISEÑO: SINGLETON

# Bibliography reference
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.

"""

log = print
log('Retos para Programadores #23')

# The Singleton design pattern ensures that a class has a single instance
# and provides a global point of access to that instance. Below, I will show
# you how to implement the Singleton pattern in Python, followed by an example
# that represents a class for managing user sessions.

# Implementation of the Singleton Pattern

class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialize any properties you need here
        return cls._instance

    # Example method
    def some_method(self):
        print("This is a method of the singleton.")

# Using the Singleton
instance1 = Singleton()
instance2 = Singleton()

# Note: both variables point to the same instance
log(instance1.some_method()) # This is a method of the singleton.
log(instance1 is instance2)  # True

# EXTRA DIFFICULTY EXERCISE

class UserSession:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
            cls._instance.user = None  # Initialize user property
        return cls._instance

    def set_user(self, id, username, name, email):
        self.user = {'id': id, 'username': username, 'name': name, 'email': email}

    def get_user(self):
        return self.user

    def clear_session(self):
        self.user = None

# Example usage of UserSession
session1 = UserSession()
session1.set_user(1, 'FritzCat', 'Fritz Cat', 'fritzcat@proton.me')

log(session1.get_user())  # {'id': 1, 'username': 'FritzCat', 'name': 'Fritz Cat', 'email': 'fritzcat@proton.me'}

session2 = UserSession()
log(session2.get_user())  # {'id': 1, 'username': 'FritzCat', 'name': 'Fritz Cat', 'email': 'fritzcat@proton.me'}

session2.clear_session()
log(session1.get_user())  
    
    # Note: 
"""  
When you call session2.clear_session(), it sets the user attribute to None. Since both session1 and session2 refer to the same instance, calling session1.get_user() afterward will also return None.

"""

