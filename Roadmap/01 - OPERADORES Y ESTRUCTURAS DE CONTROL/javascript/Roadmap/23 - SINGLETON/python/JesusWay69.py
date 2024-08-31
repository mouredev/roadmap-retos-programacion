import os, platform
from importlib import reload 

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
"""


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
       
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton1(metaclass=SingletonMeta):
    def print_logic(self):
     print("Creando objeto..", self)

if __name__ == "__main__":
        Singleton1().print_logic()
        instance1 = Singleton1()
        instance2 = Singleton1()
        print ("Instancia 1 = ", instance1)
        print ("Instancia 2 = ", instance2)
        print("\n")


""" * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión."""


def singleton (class_instance):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_instance == None:
            instances.clear()
            instances[class_instance] = class_instance(*args, **kwargs)
            return instances[class_instance]
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args, **kwargs)
            return instances[class_instance]
        if class_instance in instances:
            return instances[class_instance]
        
    return get_instance

def singleton_off(singleton:singleton):
    singleton = None
    Session(singleton)
    return singleton

@singleton
class Session:
    def __init__(self,id=None,username=None,name=None,email=None):
            self.id = id
            self.username = username
            self.name = name
            self.email = email
    def setter(self,id=None,username=None,name=None,email=None):
            self.id = id
            self.username = username
            self.name = name
            self.email = email

jesus = Session(1, "Jesusway69", "Jesus", "jesusway60@midominio.es")
jose = Session(2, "Pepe84", "Jose", "pepepepe@midominio.es")
print(f"Jesus = id: {jesus.id}, username: {jesus.username}, name: {jesus.name}, email: {jesus.email}")
print(f"Jose = id: {jose.id}, username: {jose.username}, name: {jose.name}, email: {jose.email}")
print("Sesión de jesus: ", jesus)
print("Sesión de jose: ", jose)
jesus = singleton_off(jesus)
print("Eliminando sesión de jesus...")
print("Sesión de jesus: ", jesus)
jesus = singleton(jesus)
print("Nueva sesión de jesus: ", jesus)
ana = Session()
ana.setter(3, "Ana57", "Ana", "anagarcia@midominio.es")
print(f"Ana = id:{ana.id}, username: {ana.username}, name: {ana.name}, email: {ana.email}, sesión singleton: {ana}")
