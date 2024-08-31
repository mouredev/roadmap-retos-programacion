# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

'''
- EJERCICIO:
Explora el patrón de diseño "singleton" y muestra cómo crearlo
con un ejemplo genérico.

- DIFICULTAD EXTRA (opcional):
Utiliza el patrón de diseño "singleton" para representar una clase que
haga referencia a la sesión de usuario de una aplicación ficticia.
La sesión debe permitir asignar un usuario (id, username, nombre y email),
recuperar los datos del usuario y borrar los datos de la sesión.
'''

##################################################
################# EJERCICIO 1 ####################
##################################################

class Not_Duplicity:
    _instance = { }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

obj1 = Not_Duplicity()
obj2 = Not_Duplicity()

print(f"ID Objeto 1 => { id(obj1) }")
print(f"ID Objeto 2 => { id(obj2) }")
print(f"¿Los objetos 1 y dos son iguales? { id(obj1) == id(obj2) }")

print("\n********************************\n")


##################################################
############### EJERCICIO EXTRA ##################
##################################################

class UserSession:
    _instance = None
    _user_data = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, user_id, username, name, email):
        self._user_data = {
            'id': user_id,
            'username': username,
            'name': name,
            'email': email
        }

    def get_user(self):
        return self._user_data

    def clear_user(self):
        self._user_data = None

# Ejemplo de uso:
session = UserSession()
session.set_user(1, 'hectorio23', 'Adán', 'adan_example@example.com')

print(session.get_user())  # Muestra los datos del usuario

session.clear_user()

print(session.get_user())  # Muestra None, ya que los datos han sido borrados

# Verificación de singleton:
another_session = UserSession()
print(session is another_session)  # True, ambas variables apuntan a la misma instancia
