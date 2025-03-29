# Singleton

# Patron de diseño, donde la clase solo genera una instancia, que es unica y tenga un punto acceso global 

"""
Sirve para:
1- Gestión de configuración
2- Conexión a base de datos
3- Registro de logs
4- Controladores de cache
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    

obj_1 = Singleton()
obj_2 = Singleton()

print(obj_1 is obj_2)


"""
Ejercicio extra
"""

class UserSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
            cls._instance.init_data()
        return cls._instance
    
    def init_data(self):
        self._id = None
        self.user_name = None
        self._name = None
        self.email = None
    
    def set(self, _id, user_name, _name, email):
        self._id = _id
        self.user_name = user_name
        self._name = _name
        self.email = email

    def get_data(self):
        print("Datos del usuario: ")
        print(f"Id: {self._id}")
        print(f"User name: {self.user_name}")
        print(f"Name: {self._name}")
        print(f"Email: {self.email}")

    def close_session(cls):
        print("Cerrando sesión...")
        cls.init_data()

sesion1 = UserSession()
sesion1.set("01","Gordo-Master","Gordo","gordomaster@gmail.com")
sesion1.get_data()

print("Prueba con otro")
sesion2 = UserSession()
sesion2.get_data()

sesion1.close_session()
sesion1.get_data()
print(sesion1)



