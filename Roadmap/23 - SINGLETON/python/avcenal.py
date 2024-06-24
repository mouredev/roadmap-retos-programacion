"""
EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class Singleton (object):
    instance = None       
    def __new__(cls): 
        if cls.instance is None:
            print("Creo la instancia")
            cls.instance = object.__new__(cls)
            #sin añadir object que es algo que en Python 3 no es necesario, sería cls.instance = super(Singleton,cls).__new__(cls)
        else:
            print("No creo la instancia")
        return cls.instance

test = Singleton()
test2 = Singleton()

print(test == test2)

"""
DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class Session():
    instance = None

    id: int = 0
    username:str = None
    name:str = None
    email:str = None

    def __new__(cls): 
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance
    
    def set_user(self,id:int,username:str,name:str,email:str):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_data(self):
        print(f"- ID: {self.id}\n- Username: {self.username}\n- Nombre: {self.name}\n- Email: {self.email}")

    def erase_data(self):
            self.id = 0
            self.username = None
            self.name = None
            self.email = None
            print(f"Usuario borrado")


my_session = Session()
my_session.set_user(117,"avcenal","Alex Valderrama","a@a.com")
my_session.get_data()
my_session_2 = Session() #No crea la instancia con estos datos
my_session_2.get_data()
my_session_2.erase_data()
my_session.get_data()

