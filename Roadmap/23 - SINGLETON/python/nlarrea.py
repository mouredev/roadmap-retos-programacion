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


class Singleton:
    _instance = None

    def __new__(cls):
        """Constructor of the Singleton."""

        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


singleton_1 = Singleton()
print(singleton_1)
singleton_2 = Singleton()
print(singleton_2)

print(singleton_1 is singleton_2)  # True


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""


class UserSession:
    _instance = None

    id: str = None
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
        return f"{self.id}, {self.username}, {self.name}, {self.email}"

    def remove_data(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None


session_1 = UserSession()
print(session_1.get_user())
# None, None, None, None

session_1.set_user(1, "nlarrea", "Naia", "naia@gmail.com")
print(session_1.get_user())
# 1, nlarrea, Naia, naia@gmail.com

session_2 = UserSession()
print(session_2.get_user())
# 1, nlarrea, Naia, naia@gmail.com

session_3 = UserSession()
session_3.remove_data()
print(session_3.get_user())
# None, None, None, None
print(session_1.get_user())
# None, None, None, None
