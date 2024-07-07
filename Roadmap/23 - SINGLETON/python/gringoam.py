"""
Ejercicio
"""

class Singleton:
    _instancia= None

    def __new__(cls):
        if not cls._instancia:
            cls._instancia= super(Singleton, cls).__new__(cls)
        return cls._instancia
    
singleton1= Singleton()
print(singleton1)
singleton2=Singleton()
print(singleton2)


class Sesion:
    _instancia= None
    id=None
    nombre_usuario=None
    nombre= None
    email=None
            
    def __new__(cls):
        if not cls._instancia:
            cls._instancia= super(Sesion, cls).__new__(cls)
            
        return cls._instancia
    
    def cargar_usuario(self, id, nombre_usurio, nombre, email):
        self.id=id
        self.nombre_usuario=nombre_usurio
        self.nombre=nombre
        self.email= email

    def obter_datos_usuario(self):
        print(f"id: {self.id} usuario: {self.nombre_usuario} nombre: {self.nombre} email: {self.email}")

    def cerrar_sesion(self):
        self.cargar_usuario_instancia= None
        self.id=None
        self.nombre_usuario=None
        self.nombre= None
        self.email=None

sesion1=Sesion()

sesion1.cargar_usuario(1, "gringoam","Diego", "diego@gemil.com")
sesion1.obter_datos_usuario()
sesion1.cerrar_sesion()
sesion1.obter_datos_usuario()

