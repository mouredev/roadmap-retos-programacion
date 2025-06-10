"""
#23 - Patron de diseño Singleton
"""
# Es un patron de diseño que se asegura que una clase solamente tenga una instancia
# Proporciona un punto de acceso global a esa instancia
# En pocas palabras es tener algo que todos usan
# Ejemplo: Un telefono fijo en la casa

"""
Estrucutra basica
"""
# _instance: Variable para guardar un objeto unico
# __new__: Controla si ya existe un objeto o si hay que crearlo
# Si hay un objeto, no se crea otro, solo se devuelve

class AlgoUnico:
    _instance = None # Caja donde guardamos el objeto unico

    def __new__(cls): # Funcion que decide que hacer
        if cls._instance is None: # Si la caja esta vacia
            cls._instance = super().__new__(cls) # Crea el objeto si no existe
        return cls._instance # Devuelve lo que hay en la caja
    
"""
Como se compone
"""
# La clase: Define que cosa unica estamos creando(telefono, una impresora...)
# Variable estatica _instance: Almacena el unico objeto y compoartida por toda la clase
# Control de creacion __new__: Asegura que no se hagan copias extras
# Atributos o metodos: Lo que quiero que haga el Singleton


"""
Para que se usa
"""
# Cuando se necesita un solo recurso compartido en todo el programa
# Se quiere que todos accedan a lo mismo y vean los mismo cambios
# Evitar desperdiciar memoria creando muchas copias innecesarias


"""
Ejemplo 1
"""
# Cafetera compartida en una oficina

class Cafetera:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tipo_cafe = 'expresso' # Sabor inicial
        return cls._instance
    
    def cambiar_cafe(self, nuevo_tipo):
        self.tipo_cafe = nuevo_tipo
        print(f'La cafetera ahora tiene {self.tipo_cafe}')

cafetera1 = Cafetera()
cafetera2 = Cafetera()

print(cafetera1.tipo_cafe)
cafetera2.cambiar_cafe('Americano')
print(cafetera1.tipo_cafe)
print(cafetera1 is cafetera2)


"""
Ejemplo 2
"""
# Control tv en casa

class ControlTv:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.volumen_tv = 10
        return cls._instance
    
    def subir_volumen(self):
        self.volumen_tv += 5
        print(f'El volumen ahora es de {self.volumen_tv}')


control1 = ControlTv()
control2 = ControlTv()

print(control1.subir_volumen())
print(control2.subir_volumen())


"""
Extra
"""

class SesionUsuario:
    _instance = None

    id: int = None
    uesername: str = None
    name: str = None
    mail: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SesionUsuario, cls).__new__(cls)
        return cls._instance

    
    def set_user(self, id, username, name, mail):
        self.id = id
        self.uesername = username
        self.name = name
        self.mail = mail

    def get_user(self):
        return f'ID: {self.id}, Username: {self.uesername}, Nombre: {self.name}, Email: {self.mail}'
    
    def clear_user(self):
        self.id = None
        self.uesername = None
        self.name = None
        self.mail = None


session1 = SesionUsuario()
print(session1.get_user())
session1.set_user(1, "mouredev", "Brais Moure", "mouredev@gmail.com")
print(session1.get_user())

session2 = SesionUsuario()
print(session2.get_user())

session3 = SesionUsuario()
session3.clear_user()
print(session3.get_user())