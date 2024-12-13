class SingletonMeta(type):

    _instances = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args,**kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]    
    def clear(cls):
        cls._instances.pop(cls)

class Singleton(metaclass=SingletonMeta):
    def syHello(self):
        print("Hello from Singleton class") 

s1 = Singleton()
s2 = Singleton() 

if id(s1) == id(s2):
    print("Both instances have same id")
else:
    print("Intances are different")    

class User(metaclass=SingletonMeta):
    def __init__(self,id,username,name,email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email 
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_username(self):
        return self.username     
    def get_email(self):
        return self.email
    def close_session(self):
        User.clear()
 

user = User(1,"user1","Juan","juan@test.com")
id1 = id(user)
print(f'Id for object: {id1}')
print(f'User Id {user.get_id()}')
print(f'User name {user.get_name()}')
user.close_session()
user2 = User(2,"user2","Luna","luna@test.com")
id2 = id(user2)
print(f'Id for object: {id2}')
print(f'User Id {user2.get_id()}')
print(f'User name {user2.get_name()}')
user2.close_session()