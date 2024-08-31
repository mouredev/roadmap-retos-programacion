"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
"""

class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kgargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance
    
s1 = Singleton()
print(f"First instance: {s1}")
s2 = Singleton()
print(f"Second instance: {s2}")
print(f"s1 is s2?: {s1 is s2}")


"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class User:
    _instance = None

    def __new__(cls, id: str, username: str, name: str, email: str):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls.id = id
            cls.name = name
            cls.username = username
            cls.email = email

        return cls._instance
    

    # These are instance attributes. If __init__ exist, get_user() method will point to these instance attributes istead the class attributes.
    """
    def __init__(self, id: str, username: str, name: str, email: str):
        print("Inside init")
        self.id = id
        self.username= username
        self.name = name
        self.email = email
    """


    def get_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email,
        }
    
    def clean_user(self):
        User._instance = None


###################
# Testing the class
###################

print("")
print("### Testing: Dificultad extra\n")

luis = User(id= "01", username="LuisOlivares", name="Luis", email="alfonso@dev")
print(f"User luis: {luis.get_user()}")

print("Trying to create a new user...")
luis2 = User("1", "2", "3", "4")

print(f"luis is luis2?: {luis is luis2}")

print(f"User luis: {luis.get_user()}")
print(f"User luis2: {luis2.get_user()}")

print("\nUsing clear_user method...:\n")
luis.clean_user()
oscar = User("2", "OscarOlivares", "Oscar", "oscar@Dev")
print(f"User oscar: {oscar.get_user()}")
