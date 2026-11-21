# EJERCICIO

class Singleton:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
single1 = Singleton()
print(single1)

single2 = Singleton()
print(single2)

print(single1 is single2)

#EXTRA
class UserSession:
    
    _instance = None
   
    user_id: int | None = None
    username: str | None = None
    name: str | None = None
    email: str | None = None
          
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
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
session1.set_user(1, "Rick", "Rick Orellana", "lionheart7777@gmail.com")
print(session1.get_user())

session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
print(session3.get_user())
session3.clear_user()
print(session3.get_user())


"""
ALTERNATIVO


class Singleton:
    _instance = {}

    def __new__(cls):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]

class UserSession(Singleton):
    user_id: int | None = None
    username: str | None = None
    name: str | None = None
    email: str | None = None

    def set_user(self, user_id, username, name, email):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.user_id}, {self.username}, {self.name}, {self.email}"

    def clear_user(self):
        self.user_id = self.username = self.name = self.email = None
        
        
session1 = UserSession()

print(session1.get_user())
session1.set_user(1, "Rick", "Rick Orellana", "lionheart7777@gmail.com")
session2 = UserSession()
print(session2.get_user())

session3 = UserSession()
print(session3.get_user())
session3.clear_user()
print(session3.get_user()) 

u =UserSession()
print(type(u))
"""      