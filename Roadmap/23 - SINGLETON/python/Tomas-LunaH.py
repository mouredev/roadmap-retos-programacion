#  * EJERCICIO:
#  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
#  * con un ejemplo genérico.

class System_Cam:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, name, password):
        
        if hasattr(self, 'inicializado'): 
            print("Error al agregar Ya hay un equipo")
            return
        self.name = name
        self.password = password
        self.inicializado = True
        print(f"Cámara {self.name} configurada con su contraseña correctamente.")
    def conect_to (self):
        c = input("Ingrese la contrasena para conectarse: ")
        if c == self.password:
            print(f"Conectando su pantalla a la camara: {self.name}")
        else:
            print("contrasena incorrecta")   

pantalla1 = System_Cam("Equipo de tomy", "123456")
pantalla2 = System_Cam("Equipo de tomy", "838493")
pantalla3 = pantalla1 
print(pantalla2 == pantalla1)
print(pantalla2 == pantalla3)
print(pantalla3.name)
print(pantalla3.password)
# pantalla1.conect_to()
# pantalla2.conect_to()

# DIFICULTAD EXTRA (opcional):
#  * Utiliza el patrón de diseño "singleton" para representar una clase que
#  * haga referencia a la sesión de usuario de una aplicación ficticia.
#  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
#  * recuperar los datos del usuario y borrar los datos de la sesión.

class Sesion_User:
    __instancia = None
    def __new__(cls, *args, **kargs):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def __init__(self, username, name, id, email):
        if hasattr (self, "inicializado"):
            print("Ya hay una sesion activa")
            return
        self.username = username
        self.name = name
        self.id = id
        self.email = email
        self.inicializado = True

    def get_data(self):
        if self.username is None:
            print("No hay una sesion activa")
            return
        print(f"La sesion del usuario {self.username} con el nombre {self.name} , el id {self.id} y el correo {self.email}")
    def close_sesion(self):
        self.username = None
        self.name = None
        self.id = None
        self.email = None
        del self.inicializado 
        print("Se ha cerrado la sesion con exito, datos a salvo ")
    
user1 = Sesion_User("Tomy", "Angel", 92034, "tomy.pruebagmial.com")
user1.get_data()
user1.close_sesion()
user1.get_data()
user2 = Sesion_User("Juanito", "pancho", 39494, "elpanchogmail.com")
user2.get_data()
user2.close_sesion()


