"""
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        if cls not in cls._instances:
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton trabajando, ambas variables contienen la misma instancia.")
        print(id(s1), id(s2))
    else:
        print("Singleton trabajando, ambas variables contienen diferentes instancias.")
        print(id(s1), id(s2))

### Otro ejemplo

class newSingleton():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(newSingleton, cls).__new__(cls)

        return cls._instance

s3 = newSingleton()
s4 = newSingleton()

print(id(s3), id(s4))   


#### EXTRA ####

class UserSession():
    id: int | None = None
    username: str | None = None
    name: str | None = None
    email: str | None = None

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def login(self, id: int, username: str, name: str, email: str):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def unlogin(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

    def show_user(self):
        return f"{self.id}\t{self.username}\t{self.name}\t{self.email}"

window1 = UserSession()
window2 = UserSession()
window3 = UserSession()

window1.login(197865541641927634917264391724693726493124369126491823649371264912764, "elmataviejitas500", "lorenzo", "lorenzo@dominio.io")
print(window2.show_user())
print(window3.show_user())

window4 = UserSession()
window4.unlogin()

print(window1.show_user())
print(window2.show_user())
print(window3.show_user())
print(window4.show_user())