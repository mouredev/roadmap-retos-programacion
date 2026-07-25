#### PATRONES DE DISEÑO: SINGLETON

'''
El patrón Singleton es un patrón de diseño que asegura que una clase tenga una única instancia en todo el programa 
y proporciona un punto de acceso global a esa instancia. Es útil en casos como la gestión de configuraciones, 
recursos compartidos (como conexiones a bases de datos) o registros de logs.

Python ofrece varias formas de implementar este patrón, la más sencilla es usando variables de clase
'''

# Implementación básica: usando variables de clase
class Configuration:
    _instance = None # Variable de clase para almacenar la única instancia
    
    # Método para controla la construcción de la instancia
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs) #Nueva instancia usando clase base
            cls._instance.settings = {} #Creamos un diccionario para almacenar nuestra configuración
        
        return cls._instance # Devolvemos la instáncia única (nueva o ya creada)
    
    def set(self, key, value):
        self.settings[key] = value
    
    def get(self, key):
        return self.settings.get(key, None)        

# Uso de singleton
config1 = Configuration()
config2 = Configuration()

config1.set("db_host", "192.168.20.10")
config1.set("db_name", "my_db")
config1.set("db_user", "user_db")
config1.set("port", 3306)

print(config1.get("db_host")) # 192.168.20.10
print(config2.get("db_host"))

print(config1 is config2)

### EJERCICIO EXTRA
class Session():
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            cls.__instance.username = None
            cls.__instance.session_id = None
            cls.__instance.name = None
            cls.__instance.email = None
        
        return cls.__instance
    
    def set_username(self, username):
        self.username = username
    
    def set_session_id(self, session_id):
        self.session_id = session_id
    
    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email
    
    def get_username(self):
        return self.username
    
    def get_session_id(self):
        return self.session_id
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def end_session(self):
        self.username = None
        self.session_id = None
        self.name = None
        self.email = None
        Session.__instance = None
        
        print("Sesión finalizada, con éxito...")
    
session1 = Session()    
session2 = Session()

session1.set_name('Manu')
session1.set_session_id(1)
session1.set_username("mrodara")
session1.set_email("manueljesus.rodriguez@iesalandalus.org")

print(session2.get_name())
print(session2.get_username())
print(session2.get_session_id())
print(session2.get_email())

session2.end_session()

print(session1.get_name())
print(session1.get_username())
print(session1.get_session_id())
print(session1.get_email())
    
### FIN EJERCICIO EXTRA

#### FIN PATRONES DE DISEÑO: SINGLETON
