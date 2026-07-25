# ╔═════════════════════════════════════╗
# ║ Autor:  h4ckxel                     ║
# ║ GitHub: https://github.com/h4ckxel  ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * PATRONES DE DISEÑO: SINGLETON
# -----------------------------------

"""
* EJERCICIO #1:
* Explora el patrón de diseño "singleton" y muestra cómo crearlo
* con un ejemplo genérico.
"""

class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

singleton1 = Singleton()
# singleton2 accede a la misma instancia que singleton1.
singleton2 = Singleton()
print(singleton1 is singleton2)

"""
* EJERCICIO #2:
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión.
"""

class UserSession:
    __instance = None
    __user_id: int = None
    __user_name: str = None
    __name: str = None
    __email: str = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def set_user(self, user_id, user_name, name, email):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__name = name
        self.__email = email

    def get_user(self) -> dict:
        return {
            "id": self.__user_id,
            "username": self.__user_name,
            "name": self.__name,
            "email": self.__email
        }
    
    def logout(self):
        self.__instance = None
        self.__user_id = None
        self.__user_name = None
        self.__name = None
        self.__email = None

login_user1 = UserSession()
login_user1.set_user(1, "Zoe_1", "Zoe", "Zoe@gm.com")
print(login_user1.get_user())
login_user1.logout()

login_user2 = UserSession()
login_user2.set_user(1, "Ben_1", "Ben", "Ben@gm.com")
print(login_user2.get_user())
login_user2.logout()

