## 23 - SINGLETON
'''
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
'''
## refactoring -- guru

## SINGLETON: unica instancia de una clase
'''
Ejercicio
'''


class Singleton:

    _instance = None

    def __new__(cls):
        # Estructura común para implementar Singleton
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance
    
singleton_1 = Singleton()
singleton_2 = Singleton()

print(singleton_1 is singleton_2) # Es la misma clase

'''
Extra
'''

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
    
    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

sesssion1 = UserSession()
print(sesssion1)
sesssion1.set_user(1, "rigo93", "Rigo", "rigo93acosta@gmail.com")
print(sesssion1.get_user())

sesssion2 = UserSession()
print(sesssion2.get_user())

sesssion3 = UserSession()
sesssion3.clear_user()
print(sesssion3.get_user())