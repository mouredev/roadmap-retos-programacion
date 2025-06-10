"""* EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión."""

from tkinter import S

class Singleton:
    
    """Creamos un atributo de clase y lo declaramos a nulo."""
    instance = None
    
    """Constructor de clase"""
    def __new__(cls):
        """Si no existe una instancia de la clase, la creamos
        y la devolvemos. Si ya existe, devolvemos la instancia ya
        creada.
        """        
        if not cls.instance:
            """De no existir la instancia, la instanciamos enviando nuestra la
            clase como instancia de clase usando el contructor __new__."""
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

class Session:    
    instance = None
    
    id = None
    username = None
    name = None
    email = None
    
    def __new__(session):
        if not session.instance:            
            session.instance = super(Session, session).__new__(session)
        return session.instance
    
    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return self.id, self.username, self.name, self.email
    
    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

"""Login de usuario"""
user = Session()
print(user)
user.set_user(1, "Juan", "Juan", "jymtr1968@gmail.com")
print(user.get_user())

"""Datos de usuario logueado"""
user2 = Session()
print(user2)
print(user2.get_user())

"""Cerrar sesión"""
user3 = Session()
print(user3)
print(user3.get_user())
user3.clear_user()
print(user3.get_user())