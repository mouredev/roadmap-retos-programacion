# EJERCICIO:
# Explora el patrón de diseño "singleton" y muestra cómo crearlo
# con un ejemplo genérico.

class Singlenton:
    _instance = None  # Variable de clase para guardar la instancia
    
    def __new__(cls):
        # Si no existe una instancia se crerara
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance # Siempre devolvemos la misma instancia
    def __init__(self, value=None):
        # Solo inicializamos una vez
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.value = value
            


# DIFICULTAD EXTRA (opcional):
# Utiliza el patrón de diseño "singleton" para representar una clase que
# haga referencia a la sesión de usuario de una aplicación ficticia.
# La sesión debe permitir asignar un usuario (id, username, nombre y email),
# recuperar los datos del usuario y borrar los datos de la sesión.

class User:
    _instance = None
    
    
    def __new__(cls,*args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, id, username, name, mail):
        self.id: int = id
        self.username: str = username
        self.name: str = name.capitalize()
        self.mail: str = mail
    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Nombre: {self.name}, Email: {self.mail}"
    
    def clear_session(self):
        self.id = None
        self.username = None
        self.name = None
        self.mail = None


edu = User(23, "vastmind", "eduardo", "cocinas_del_sur@cds.com")
sundy = User(24, "bruja", "sundy", "buja@witch.com")

print(edu.__str__())