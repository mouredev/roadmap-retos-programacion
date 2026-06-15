'''
Ejercicio:
Explora el patron de diseño "singleton" y muestra como crearlo con un ejemplo generico.

Singleton es un patron de diseño creacional que garantiza que tan solo exista un objeto de su tipo y propociona un unico punto de acceso a el para cualquier otro codigo
Caracteristicas principales: 
    * Instancia unica: Asegura que solo exista un objeto de la clase en toda la aplicacion
    * Punto de acceso global: Proporciona una forma unica y global de acceder a esa instancia.
    * Constructor privado: Se declara el constructor de la clase como privado para evitar que se creen otras instancias
    * Metodo de acceso estatico: Se crea un metodo publico y estatico, que se encarga de crear la instancia la primera vez y devolver la misma instancia en llamadas posteriores.
'''

class Singleton:
    _instance = None # Variable de clase para guardar la unica instancia.

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # Crear la instancia por primera vez
            print("Instancia creada.")
        else:
            print("Instancia ya existente, reutilizando")
        return cls._instance
    
a = Singleton()
b = Singleton()

print(a is b) # True


'''
Dificultad extra:
Utiliza el patron de diseño "singleton" para representar una clase que haga referencia a la sesion de usuario de una aplicacion ficticia.

La sesion debe permitir asginar un usuario (id, username, nombre y email), recuperar los datos del usuario y borrar los datos de la sesion
'''

class UserSession:

    # Creamos un diccionario para almacenar los datos del usuario
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def asignar_usuario(self):
        self.id = int(input("Inserte su ID por favor: "))
        self.username = input("Inserte su username por favor: ")
        self.nombre = input("Inserte su nombre porfavor: ").title()
        self.email = input("Inserte su email por favor: ")

    def obtener_usuario(self):
        return {
            "id": self.id,
            "username": self.username,
            "nombre": self.nombre,
            "email": self.email
        }
    
    def cerrar_sesion(self):
        self.id = None
        self.username = None
        self.nombre = None
        self.email = None


user = UserSession()
user.asignar_usuario()
print(user.obtener_usuario())
user.cerrar_sesion()