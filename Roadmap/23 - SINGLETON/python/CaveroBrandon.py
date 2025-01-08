""" EJERCICIO:
Explora el patrón de diseño "singleton" y muestra cómo crearlo
con un ejemplo genérico.
"""


class Door:
    _is_door_open = None
    _initialized = False

    def __new__(cls):
        if cls._is_door_open is None:
            cls._is_door_open = super(Door, cls).__new__(cls)
        return cls._is_door_open

    def __init__(self):
        if not self._initialized:
            self.value = None


person1 = Door()
person2 = Door()

person1.value = True  # Person 1 opens the door
print(f'Person 1 opens the door, door status = {person1.value}')
print(f'Person 2 checks the door, door status = {person2.value}')
person2.value = False
print(f'Person 2 close the door, door status = {person2.value}')
print(f'Person 1 checks the door, door status = {person1.value}')

"""
DIFICULTAD EXTRA (opcional):
Utiliza el patrón de diseño "singleton" para representar una clase que
haga referencia a la sesión de usuario de una aplicación ficticia.
La sesión debe permitir asignar un usuario (id, username, nombre y email),
recuperar los datos del usuario y borrar los datos de la sesión.
"""

print('\n---- Extra ----\n')
class UserSession:
    _instance = None
    user_id = None
    username = None
    name = None
    email = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def create_user_session(self, user_id: int, username: str, name: str, email: str):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email

    def get_user_session(self) -> dict:
        user_session = {'user_id': self.user_id, 'username': self.username, 'name': self.name, 'email': self.email}
        return user_session

    def clear_session(self):
        self.user_id = None
        self.username = None
        self.name = None
        self.email = None


session1 = UserSession()
print('Creating a user session...')
session1.create_user_session(user_id=123, username='Brandon123', name='Brandon', email='cc@gmail.com')
print(session1.get_user_session())

session2 = UserSession()
print('Overriding user session...')
session2.create_user_session(user_id=321, username='Cavero321', name='Andres', email='cavero.brandon94@gmail.com')
print(session2.get_user_session())

print('Clearing the user session')
session1.clear_session()
print(session1.get_user_session())
