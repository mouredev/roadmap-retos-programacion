"""
Ejercicio
"""


class Sigleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Sigleton, cls).__new__(cls)
        return cls._instance


sigleton1 = Sigleton()
print(sigleton1)
sigleton2 = Sigleton()
print(sigleton2)

print(sigleton1 is sigleton2)

"""
Extra
"""


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
        return f"{self.id}, {self.username}, {self.name}, {self.email}"

    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None


session1 = UserSession()
print(session1.get_user())
session1.set_user(1, "mouredev", "Brais Moure", "mouredev@gmail.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())
