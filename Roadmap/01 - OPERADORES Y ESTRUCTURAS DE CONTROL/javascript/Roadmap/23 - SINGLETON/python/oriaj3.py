"""
23 - SINGLETON
Autor de la solución: Oriaj3

Teoría:
El patrón Singleton es un patrón de diseño creacional que garantiza que una clase
tiene una única instancia y proporciona un punto de acceso global a ella.

El patrón Singleton se utiliza cuando se necesita una única instancia de una clase
en todo el programa. Por ejemplo, se puede utilizar para representar una conexión
a una base de datos o un archivo de registro.

El patrón Singleton se implementa creando una clase con un método estático que
devuelve una instancia única de la clase. La instancia única se crea la primera
vez que se llama al método estático y se reutiliza en llamadas posteriores al
método.

Ejemplo de patrón Singleton:
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


"""

"""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class Unica:
    _instancia = None
    
    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
            print("Creado Objeto")
        else:
            print("El objeto ya existe")
        return cls._instancia

ins1 = Unica()
ins2 = Unica()
print(ins1)
print(ins2)

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
"""

class Sesion_usuario:
    _instancia = None 
    id: int
    usuario: str
    name: str
    email: str
    
    
    
    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email 
        
    def get_user(self):
        return f"{self.id}, {self.username}, {self.name}, {self.email}"
    
    def cerrar_sesion(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
    
sesion1 = Sesion_usuario()
sesion1.set_user(1, "oriaj", "Jairo", "oriaj@gmail.com")    

print(sesion1.get_user())

sesion2 = Sesion_usuario()
print(sesion2.get_user())

sesion1.cerrar_sesion()
print(sesion2.get_user())

