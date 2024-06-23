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

from typing import Any


class Singleton:
    class __Singleton:
        def __init__(self) -> None:
            self.nombre = None
    
        def __str__(self):
            return f"{self.nombre}"
        
    instance = None

    def __new__(cls):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance
    
    
my_singleton = Singleton()
my_singleton.nombre = "Alan Ramirez"
print(my_singleton)

# Extra
class UserSession:
    _instance = None
    id = None
    username = None
    nombre = None
    email = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    
                
    def setuser(self, id, username, nombre, email):
        self.id = id
        self.username = username
        self.nombre = nombre
        self.email = email        
        
    def getuser(self):
        return f"Sesion: {self.id}, {self.username}, {self.nombre}, {self.email}"
    
    def clearuser(self):
        self.id = None
        self.username = None
        self.nombre = None
        self.email = None
        
    
my_usersession = UserSession()
my_usersession.setuser(1, "alanshakir", "alan Ramirez", "alan2085@gmail.com")
print(my_usersession.getuser())
my_usersession.clearuser()
print(my_usersession.getuser())
