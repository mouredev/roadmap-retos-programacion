'''
 EJERCICIO:
* Explora el patrón de diseño "singleton" y muestra cómo crearlo
* con un ejemplo genérico.
'''
class Singleton:
    _instancia = None  # Aquí se guarda la única instancia

    def __new__(cls):
        # Crea la instancia solo la primera vez
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        # Las llamadas siguientes devuelven la misma instancia
        return cls._instancia


# Ambas variables apuntan al mismo objeto
objeto1 = Singleton()
objeto2 = Singleton()

print(objeto1 is objeto2)  # True

'''
* DIFICULTAD EXTRA (opcional):
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión.
'''

class UserSession:
    _instance = None  # Guarda la única instancia

    def __new__(cls):
        # Crea la instancia solo si aún no existe
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user_data = None  # Estado inicial de la sesión

        # Devuelve siempre la misma instancia
        return cls._instance

    def set_user(self, user_id, username, name, email):
        # Guarda los datos del usuario en la sesión
        self.user_data = {
            "id": user_id,
            "username": username,
            "name": name,
            "email": email,
        }

    def get_user(self):
        # Devuelve los datos guardados, o None si no hay usuario
        return self.user_data

    def clear_session(self):
        # Borra los datos de la sesión
        self.user_data = None


# Ejemplo de uso
session1 = UserSession()
session1.set_user(1, "ana", "Ana Pérez", "ana@example.com")

session2 = UserSession()

print(session1 is session2)  # True
print(session2.get_user())   # Los datos guardados desde session1
Usuario1 = UserSession()
Usuario1.set_user(1, "jdoe", "John Doe", "john.doe@example.com")
print(Usuario1.get_user())
Usuario2 = UserSession()
Usuario2.set_user(2, "jsmith", "Jane Smith", "jane.smith@example.com")
print(Usuario2.get_user())
print(Usuario1.get_user())  
Usuario1.clear_session()
print(Usuario1.get_user())
print(Usuario2.get_user())
Usuario3 = UserSession()
Usuario3.set_user(3, "jwilson", "John Wilson", "john.wilson@example.com")
print(Usuario3.get_user())

print(Usuario1 is Usuario3)  # True
print(Usuario2.get_user())  # Los datos guardados desde Usuario3

#El patrón singleton asegura que todas las instancias de UserSession compartan el mismo estado, 
#por lo que cualquier cambio en una instancia afecta a todas las demás.