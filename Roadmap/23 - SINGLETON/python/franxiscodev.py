'''
Patrones de diseño
SINGLETON
Compartir una misma instancia de un objeto
ejemplo al llamar la sesión de usuario
'''


class My_Singleton:
    _my_instance = None

    def __new__(cls):
        if not cls._my_instance:
            cls._my_instance = super(My_Singleton, cls).__new__(cls)

        return cls._my_instance


singleton1 = My_Singleton()
singleton2 = My_Singleton()
print(singleton1 is singleton2)


'''
Extra
'''


class UserSession:

    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)

        return cls._instance

    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id},{self.username},{self.name},{self.email}"

    def clear_user(self):
        self.id: int = None
        self.username: str = None
        self.name: str = None
        self.email: str = None


session1 = UserSession()
session1.set_user(11, "franxiscodev", "Francisco A R",
                  "franxiscodev@gmail.com")
print(session1.get_user())

# simular navegación
session2 = UserSession()

print(session2.get_user())

# logout
session3 = UserSession()
session3.clear_user()
print(session1.get_user())
