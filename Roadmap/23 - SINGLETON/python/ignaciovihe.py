"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class Singleton:
    _instance = None    # Aqui se guarda la instancia. Sera unica y todos los que intenten crear un Singleton se les devolvera esta.

    def __new__(cls):   # Se ejecuta antes de init.
        if cls._instance == None:                                   # Si la instancia no esta creada.
            cls._instance = super(Singleton, cls).__new__(cls)      # Lo creo usando en metodo new de su clase superior y pasandole cls
        return cls._instance                                        # Devuelvo la instancia. Siempre la misma.  

a = Singleton()
print(a)
b = Singleton()
print(b)  
print(a is b)


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""
# Version simple con una sola clase. Si queremos hacer otras clases singleton deberemos modificar su metodo new en cada una
class UserSession():
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(UserSession, cls).__new__(cls)
            cls._instance.user = None # Se crea un atributo de instacia desde new para no usar init cada vez y tener que controlar la inicialización con un flag.
        return cls._instance
    
    def set_user(self, id, username, name, email):
            self.user = {
                "id": id,
                "username": username,
                "name": name,
                "email": email
            }

    def get_user_data(self):
        if self.user:
            return f"{self.user["id"]} - {self.user["username"]} - {self.user["name"]} - {self.user["email"]}"
        else:
            print("Sesión sin usuario")
        
    def delete_session(self):
        self.user = None

print("------------------con clase simple-------------------------")
session1 = UserSession()
print(session1.get_user_data())
session1.set_user(1, "culiembres", "ignacio", "email@email.com")
print(session1.get_user_data())

session2 = UserSession()
print(session2.get_user_data())

session3 = UserSession()
session3.set_user(2, "pepeluis", "Pepe", "mielamil@email.com")
print(session3.get_user_data())

session3.delete_session()
session3.get_user_data()


# Version con metaclase para varias clases singleton. Siguiento las indicaciones de https://refactoring.guru/

class SingletonMeta(type):                              # Se utiliza una metaclase para modificar el comportamiento de call
                                                        # Todas las clases tienen la metaclase type por defecto
    _instances = {}                                     # Se crea un dict para guardas las instacias unicas de las clases que queremos que sean singleton.

    def __call__(cls, *args, **kwds):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)  # Creamos la instancia llamando al metodo call de type(metaclase base)
            cls._instances[cls] = instance              # internamente type.call llama a los metodos new y init de las clases(ej:UsserConnection, BBDDconnection)
        return cls._instances[cls]
    

class UserConnection(metaclass=SingletonMeta):          # Le indicamos que la calse tiene una metaclase definida opor nosotros(por defecto seria type)

    def __init__(self):
        self.user = None

    def set_user(self, id, username, name, email):
        self.user = {
            "id": id,
            "username": username,
            "name": name,
            "email": email
        }

    def get_user_data(self):
        if self.user:
            return f"{self.user['id']} - {self.user['username']} - {self.user['name']} - {self.user['email']}"
        else:
            return "Sesión sin usuario"

    def delete_session(self):
        self.user = None


class BBDDConnection(metaclass=SingletonMeta):
    
    def __init__(self):
        self.bbdd = {
            "name": "Pedro",
            "edad": 35
        }

    def get_data(self):
        return self.bbdd
    


print("------------------con metaclass------------------------")
    
connection1 = UserConnection()
connection1.set_user(1, "pepito", "Pepe", "pepe@email.com")
print(connection1.get_user_data())

connection2 = UserConnection()
print(connection2.get_user_data())

print(connection1 is connection2)

bbddc1 = BBDDConnection()
print(bbddc1.get_data())

bbddc2 = BBDDConnection()
print(bbddc2.get_data())

print(bbddc1 is bbddc2)


