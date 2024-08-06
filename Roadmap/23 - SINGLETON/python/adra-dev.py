"""
EJERCICIO:
Explora el patrón de diseño "singleton" y muestra cómo crearlo con un
ejemplo genérico.

DIFICULTAD EXTRA(opcional):
Utiliza el patrón de diseño "singleton" para representar una clase 
que haga referencia a la sesión de usuario de una aplicación ficticia.
La sesión debe permitir asignar un usuario (id, username, nombre y 
email), recuperar los datos del ususario y borrar los datos de la 
sesión.sesión

by adra-dev
"""

"""
EJERCICIO:
"""


"""
¿Qué es un patrón de diseño?:
    Los patrones de diseño son soluciones habituales a problemas que 
    ocurren con frecuencia en el diseño de software. Son como planos 
    prefabricados que se pueden personalizar para resolver un 
    problema de diseño recurrente en tu código.

    url: https://refactoring.guru/es/design-patterns/what-is-pattern 
"""

"""
Singleton: Es un patrón de diseño creacional que nos permite 
asegurarnos de que una clase tenga una única instancia, a la vez que 
proporciona un punto de acceso global a dicha instancia.
"""

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


"""
Extra
"""

class UserSession:
    
    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    

    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email},"

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

session1 = UserSession()
print(session1.get_user())
session1.set_user(1, "adra-dev", "Adrian R", "aralfaro98@gmail.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())
