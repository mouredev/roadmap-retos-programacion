
print("\n\n=======================================EJERCICIO=======================================\n\n")

"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra como crearlo
 * con un ejemplo genérico.
"""
"""
 * El patron Singleton es un patrón de creación 
 * Los patrones de creación abstraen la forma en la que se crean los objetos, 
 * permitiendo tratar las clases a crear de forma genérica dejando para mas 
 * tarde la decisión de que clases crear o como crearlas.
 
 * El patrón Singleton asegura que una clase tenga solo una instancia 
 * y proporciona un punto de acceso global a ella
"""

class Singleton:

    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__new__(cls)
            
        return cls.__instance
            


instance1 = Singleton()
instance2 = Singleton()

print("Comprobando que las dos instancias son la misma instancia:\n")
print(instance1 is instance2)





print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

# Clase para definir el Singleton
class User_Session:
    
    __instance = None
    __user_data = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(User_Session, cls).__new__(cls)
            
        return cls.__instance
    
    # Funcion para establecer los datos de los usuarios y marcar como abrir sesion    
    def new_user(self, id, username, name, email):
        if self.__user_data is None:
            self.__user_data = {
                'id': id,
                'username': username,
                'name': name,
                'email': email
            }
            print(f"El usuario con el\n\tid: {id}\n\tusername: {username}\n\tname: {name}\n\temail:{email}\nHa iniciado sesion")
        else:
            print(f"Ya hay una sesion activa con el usuario {self.__user_data['username']}. Cierra la sesion actual antes de iniciar una nueva.")
            return
    
    # Devolvemos los datos del usuario que esta activo        
    def get_user(self):
        return self.__user_data
    
    # Borramos los datos del usuario y marca como cerrar sesion
    def logout(self):
        if self.__user_data:
            print(f"El usuario {self.__user_data['username']} ha cerrado la sesion")
            self.__user_data = None
        else:
            print("No hay sesiones abiertas")
            
# Definimos la clase usuario
class User():
    def __init__(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email
        
# Damos nombre a la instancia de User_Session        
session = User_Session()

# Iniciamos sesion
def log_in(user):
    session.new_user(user.id, user.username, user.name, user.email)
    
# Cerramos sesion
def logout():
    session.logout()
    
    
# Operativa    
user1 = User(1, "Rantam", "Alex", "rantam@rantam.es")
log_in(user1)

# Sin este logout no se podría abrir sesion con el siguiente usuario
logout()       

user2 = User(2, "Junior", "Maria", "maria@rantam.es")
log_in(user2)

logout()
