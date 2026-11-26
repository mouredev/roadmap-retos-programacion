"""
SINGLETON
"""


class Singleton:
    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singleton1 = Singleton()
print(singleton1)
singleton2 = Singleton()
print(singleton2)

print(singleton1 is singleton2)


"""
    EXTRA EXERCISE
"""


class UserSession:
    _instance = None

    user_id: int
    username: str
    name: str
    email: str

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance

    def set_user(self, user_id, username, name, email):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.user_id}, {self.username}, {self.name}, {self.email}"

    def clear_user(self):
        self.user_id = None
        self.username = None
        self.name = None
        self.email = None


session1 = UserSession()
# print(session1.get_user())
session1.set_user(1, "elhdrond", "Sergio Cardo", "sergio@example.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())
