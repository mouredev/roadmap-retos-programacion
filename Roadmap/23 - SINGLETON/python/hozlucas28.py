# pylint: disable=pointless-string-statement,missing-class-docstring,missing-function-docstring

"""
    Singleton pattern...
"""

from typing import Any, Self


print("Singleton pattern...")


class SingletonMeta(type):
    __instances: dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls.__instances:
            instance: Any = super().__call__(*args, **kwds)
            cls.__instances[cls] = instance

        return cls.__instances[cls]


class Counter(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.__count: int = 0

    def get_count(self) -> int:
        return self.__count

    def increment(self) -> Self:
        self.__count += 1
        return self

    def decrement(self) -> Self:
        self.__count -= 1
        return self


counter_01: Counter = Counter()
counter_02: Counter = Counter()

print(
    "\nAre `counter_01` and `counter_02` the same instance of `Counter` class?"
    + f" {counter_01 == counter_02}",
)

print("\nMethod call of `counter_01` instance...")

counter_01.increment().increment().increment()
print("\ncounter01.increment().increment().increment()")

print(f"\nCount attribute of `counter_01` instance --> {counter_01.get_count()}")


print("\nMethod call of `counter_02` instance...")

counter_02.decrement()
print("\ncounter02.decrement()")

print(f"\nCount attribute of `counter_02` instance --> {counter_02.get_count()}")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)


"""
    Additional challenge...
"""

print("Additional challenge...")


class UserSession(metaclass=SingletonMeta):
    __email: str
    __uid: str
    __name: str
    __user_name: str

    def __init__(self, *, email="", uid="", name="", user_name="") -> None:
        self.__email = email
        self.__uid = uid
        self.__name = name
        self.__user_name = user_name

    def get_email(self) -> str:
        return self.__email

    def get_uid(self) -> str:
        return self.__uid

    def get_name(self) -> str:
        return self.__name

    def get_user_name(self) -> str:
        return self.__user_name

    def set_email(self, new_email: str) -> Self:
        self.__email = new_email
        return self

    def set_uid(self, new_uid: str) -> Self:
        self.__uid = new_uid
        return self

    def set_name(self, new_name: str) -> Self:
        self.__name = new_name
        return self

    def set_user_name(self, new_user_name: str) -> Self:
        self.__user_name = new_user_name
        return self

    def delete_data(self) -> Self:
        self.__email = ""
        self.__uid = ""
        self.__name = ""
        self.__user_name = ""
        return self


user_session: UserSession = UserSession(
    email="juansmith16@gmail.com",
    name="Juan",
    uid="15H4G-A5D-1Y7",
    user_name="JuanGamer16",
)

print(
    "\nUser: "
    + f"{user_session.get_uid()} {user_session.get_name()} "
    + f"{user_session.get_user_name()} {user_session.get_email()}"
)

user_session.delete_data()
print("\nUser data deleted!")

print(
    "\nUser: "
    + f"{user_session.get_uid()} {user_session.get_name()} "
    + f"{user_session.get_user_name()} {user_session.get_email()}"
)
