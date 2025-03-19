# Singleton
from dataclasses import dataclass


# With Class method
class MySingleton:
    __instance = None

    @classmethod
    def build(cls, *args, **kwargs):
        if cls.__instance is not None:
            return cls.__instance

        cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


obj1 = MySingleton.build(1, 2, 3, one=1, two=2, three=3)
print(f"{obj1.__dict__ = }")

obj2 = MySingleton.build(4, 5, 6)
print(f"{obj2.__dict__ = }")
print(f"{obj1.__dict__ = }")

print(f"{obj1 is obj2 = }")
print("__innit__ doesnt call again on second build, so gets old data")

print()
print()


class MyOtherSingleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is not None:
            return cls.__instance

        cls.__instance = super(MyOtherSingleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


obj1 = MyOtherSingleton(1, 2, 3, one=1, two=2, three=3)
print(f"{obj1.__dict__ = }")

obj2 = MyOtherSingleton(4, 5, 6)
print(f"{obj2.__dict__ = }")
print(f"{obj1.__dict__ = }")

print(f"{obj1 is obj2 = }")
print("__innit__ called again on second build, so gets new data")


# EXTRA
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass()
class Session(metaclass=Singleton):
    id: int
    username: str
    name: str
    email: str

    def asign__user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def recover(self):
        print(self.__dict__)

    def clean(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None


session = Session(1, "ggilperez", "Guillermo", "ggilperezalcazar@gmail.com")
session.recover()
session.clean()
session.recover()

session2 = Session(2, "mouredev", "Brais", "mouredev@gmail.com")
session2.recover()
print("With singleton as metaclass, innit is not called again so new values are not set")
session2.asign__user(2, "mouredev", "Brais", "mouredev@gmail.com")
session2.recover()
