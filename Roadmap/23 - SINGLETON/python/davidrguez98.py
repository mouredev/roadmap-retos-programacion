""" /*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */ """

#EJERCICIO

class Singleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        
        return  cls._instance
    
Singleton1 = Singleton()
print(Singleton1)
Singleton2 = Singleton()
print(Singleton2)

print(Singleton1 is Singleton2)

#DIFICULTAD EXTRA

class user:

    instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(user, cls).__new__(cls)
        
        return  cls.instance
    
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

session1 = user()
session1.set_user(00, "davidrguez98", "David Rodríguez", "david@gmail.com")
print(session1.get_user())

session2 = user()
print(session2.get_user())

session3 = user()
session3.clear_user()
print(session3.get_user())