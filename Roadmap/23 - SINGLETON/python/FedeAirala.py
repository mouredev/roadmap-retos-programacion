# #23 PATRONES DE DISEÑO: SINGLETON
"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class Singleton:
    instance = None
    
    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance
    
sesion1 = Singleton()
print (sesion1)
sesion2 = Singleton()
print (sesion2)
print (sesion1 is sesion2)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class User:
    
    instance = None
    
    id : int = None
    name : str = None
    email: str = None
    
    def __new__(cls):
        if not cls.instance:
            cls.instance = super(User,cls).__new__(cls)
        return cls.instance
    
    def set_user(self,id,name,email) -> None:
        self.id = id
        self.name = name
        self.email = email
    
    def get_user(self):
        return f"{self.id}, {self.name}, {self.email}"
    
    def clear_user(self):
        self.id = None
        self.name = None
        self.email = None
    

user1 = User()
user1.set_user(1,"Fede","fede@gmail.com")
user2 = User()

print (user1.name)
print (user2.get_user())
user2.clear_user()
print (user1.get_user())