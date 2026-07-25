#Ejercicio

class Singleton:
    _instance = None

    def __new__(cls):
        #Si no hay instancia se crea una
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        #Devolvemos la instancia
        return cls._instance
    
s1 = Singleton()
print(f"s1: {s1}")
s2 = Singleton()
print(f"s2: {s2}")
print(f"Es s1 igual que s2: {s1 is  s2}")

#Extra

class UserSession():
    _instance = None

    _id: int = None
    _username: str = None
    _name: str = None
    _email: str = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set_user(self, id, username, name, email):
        self._id = id
        self._username = username
        self._name = name
        self._email = email

    def get_user(self):
        print(f"ID: {self._id}\nUsername: {self._username}\nNombre: {self._name}\nEmail: {self._email}")

    def delete_user(self):
        self._id = None
        self._username = None
        self._name = None
        self._email = None

session1= UserSession()
session1.set_user(1, "mariovelascodev", "Mario", "mario@mario.com")
session1.get_user()

session2 = UserSession()
session2.get_user()
session2.delete_user()
session2.get_user()