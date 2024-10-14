"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Ejemplo de uso
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Esto imprimirá True, ya que ambas variables apuntan a la misma instancia


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class UserSession:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls, *args, **kwargs)
            cls._instance.user_data = None
        return cls._instance

    def set_user(self, user_id, username, name, email):
        self.user_data = {
            'id': user_id,
            'username': username,
            'name': name,
            'email': email
        }

    def get_user(self):
        return self.user_data

    def clear_session(self):
        self.user_data = None

# Ejemplo de uso
session1 = UserSession()
session2 = UserSession()

# Asignar un usuario a la sesión
session1.set_user(1, 'jdoe', 'John Doe', 'jdoe@example.com')

# Recuperar los datos del usuario
print(session1.get_user())  # {'id': 1, 'username': 'jdoe', 'name': 'John Doe', 'email': 'jdoe@example.com'}

# Verificar que session1 y session2 son la misma instancia
print(session1 is session2)  # True

# Borrar los datos de la sesión
session2.clear_session()
print(session1.get_user())  # None
