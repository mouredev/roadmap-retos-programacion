# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
"""


# Implementación básica
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
    
sin1 = Singleton()
print(sin1)
sin2 = Singleton()
print(sin2)
print(sin1 is sin2) # True


"""* DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */"""

class UserSession():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creando nueva sesión de usuario!")
            cls._instance = super(UserSession, cls).__new__(cls)
            # Inicializar el estado de la sesión vacia
            cls._instance._user_data = None
        return  cls._instance

    def set_user(self, user_id, username, name, email):
        self._user_data = {
            "id": user_id,
            "username": username,
            "name": name,
            "email": email,
            "is_authenticated": True
        }
        
        print(f"Usuario {username} ha iniciado sesión.")
        return self._user_data
    
    def get_user(self):
        """Método para obtener los datos del usuario"""
        if not self._user_data:
            print("No hay ningún usuario en la sesión.")
            return None
        else:
            return self._user_data

    def is_authenticated(self):
        """Verifica si hay un usuario autenticado en la sesión"""
        return self._user_data is not None and self._user_data.get("is_authenticated", False)

    def logout(self):
        """Borra todos los datos de la sesión"""
        if self._user_data:
            username = self._user_data["username"]
            self._user_data.clear()
            print(f"Usuario {username} ha cerrado la sesión")
            return True
        else:
            return False

if __name__ == "__main__":

    # Caso de uso sesión usuario
    user1 = UserSession()
    print("Usuario Autenticado?:", user1.is_authenticated())

    # Establecemos un usuario
    user1.set_user(1, "johndoe", "John Doe", "johndoe@fake.com")
    print("Usuario Autenticado?:", user1.is_authenticated())
    print(user1.get_user())

    # Creamos otra instancia de la sesión (DEBE SER LA MISMA)
    user2 = UserSession()
    print("Sesión 1 es sesión 2?:", user1 is user2)

    print("Usuario en sesion 1:", user1.get_user()["username"])
    print("Usuario en sesion 2:", user2.get_user()["username"])

    # Cerramos sesión
    user2.logout()

    # Verificamos en ambas sesiones
    print("sesion 1 Autenticado?:", user1.is_authenticated())
    print("sesion 2 Autenticado?:", user2.is_authenticated())