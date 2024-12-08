from os import name


class Singleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

""" Ejrcicio """


class Sesion:

    _instance = None
    id: str = None
    name: str = None
    username: str = None
    email: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Sesion, cls).__new__(cls)

        return cls._instance

    def set_user(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def get_user(self):
        return f"{self.id},{self.username},{self.name},{self.email}"

    def clear_user(self):
        self.id = None
        self.name = None
        self.username = None
        self.email = None


sesion1 = Sesion()

sesion1.set_user("1", "lucas", "lucasdev", "lucasdev@gmail.com")
print(sesion1.get_user())

sesion2 = Sesion()
print(sesion2.get_user())

sesion3 = Sesion()
sesion3.clear_user()
print(sesion3.get_user())
