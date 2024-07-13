 EJERCICIO:
 Explora el patrón de diseño "singleton" y muestra cómo crearlo
 con un ejemplo genérico.

 DIFICULTAD EXTRA (opcional):
 Utiliza el patrón de diseño "singleton" para representar una clase que
 haga referencia a la sesión de usuario de una aplicación ficticia.
 La sesión debe permitir asignar un usuario (id, username, nombre y email),
 recuperar los datos del usuario y borrar los datos de la sesión.
"""

from threading import Lock

class SingletonMeta(type):
    _instancias = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instancias:
                instancia = super().__call__(*args, **kwargs)
                cls._instancias[cls]= instancia
        return cls._instancias[cls]

class ContadorSingleton(metaclass=SingletonMeta):
    valor: int = None
    def __init__ (self, valor: int):
        self.valor = valor
        return None
    def get(self):
        return self.valor
    def incrementar(self):
        self.valor+=1
    def decrementar(self):
        self.valor-=1
class SessionSingleton(metaclass=SingletonMeta):
    id =None
    username = None
    nombre = None
    email = None
    def __init__(self, id, username, nombre, email):
        self.id= id
        self.username= username
        self.nombre= nombre
        self.email= email
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
    def delete(self):
        self.id =None
        self.username = None
        self.nombre = None
        self.email = None
    def __str__(self):
        mostrar = "La session id: {} es del username: {}, nombre:{} email: {}".format(self.id, self.username, self.nombre, self.email)
        return mostrar

contador = ContadorSingleton(10)
print("el contador tiene: {}".format(contador.get()))

contador.decrementar()

contador2 = ContadorSingleton(20)
print("contador= {}  y contador2={}".format(contador.get(), contador2.get()))

contador2.decrementar()
print("contador= {}  y contador2={}".format(contador.get(), contador2.get()))


s1=SessionSingleton(5, 'pepe', 'Juan', 'juan@gmail.com')
s2=SessionSingleton(66, 'thor', 'Thor Pedo', 'thor@gmail.com')

print(s1)
print(s2)


