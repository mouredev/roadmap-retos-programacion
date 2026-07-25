
#Exercise
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

print(singleton1 is singleton2)


#Extra Exercise

class User_Session:

    _instance = None


    id: int = None
    username: str = None
    name: str = None
    email: str = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(User_Session, cls).__new__(cls)
        return cls._instance

    def create_user(self, id, username, name, email):
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


session1 = User_Session()
session1.create_user(1, "irene123", "Irene", "irene@mail.com")

print(session1.get_user())

# New variable but same object(Singleton)
session2 = User_Session()
print(session2.get_user()) #Same user

session2.clear_user()

print(session1.get_user())   #Cleared (None)
