"""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
"""

# EJERCICIO:


class Singleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)

# DIFICULTAD EXTRA:


class Sesion:
    _id = ""
    _username = ""
    _nombre = ""
    _email = ""

    def __init__(self, id, username, nombre, email):
        self._id = id
        self._username = username
        self._nombre = nombre
        self._email = email

    def get_id(self):
        return self._id

    def get_username(self):
        return self._username

    def get_name(self):
        return self._nombre

    def get_email(self):
        return self._email

    def delete_data(self):
        self._id = ""
        self._username = ""
        self._nombre = ""
        self._email = ""
        return self


sesion1 = Sesion(id="1", username="test1",
                 nombre="Agustin", email="test@gmail.com")

print(f"User: {sesion1.get_username()}")
print(f"Eliminando datos: {sesion1.delete_data()}")
print(f"User id: {sesion1.get_id()}")
