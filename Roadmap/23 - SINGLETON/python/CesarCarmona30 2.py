'''
    EJERCICIO
'''

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        print("Using instance")    
        return cls._instance

instance1 = Singleton()
instance2 = Singleton()

print(instance1 is instance2)

'''
    EXTRA
'''

class Session():
    _instance = None
    
    id = None
    username = None
    name = None
    email = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
        return cls._instance

    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f'User: {self.id}, {self.username}, {self.name}, {self.email}'
    
    def clear_user(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
    
session1 = Session()
print(session1.get_user())
session1.set_user(1, "leroy58", "César Leroy", "cesarcarmona@gmail.com")
print(session1.get_user())

session2 = Session()
print(session2.get_user())

session3 = Session()
session3.clear_user()
print(session3.get_user())