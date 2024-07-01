class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class Patata(metaclass=SingletonMeta):

    def __init__(self, size: int = 10, color: str = "yellow") -> None:
        self.size = size
        self.color = color

    def __str__(self) -> str:
        return f"Patata(s={self.size}, c='{self.color}')"


class User:

    def __init__(self, user_id: int, username: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"User(user_id={self.user_id}, username='{self.username}', name='{self.name}', email='{self.email}')"


class SingletonByUserMeta(type):
    __instances = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)

        def remove_user_from_instances(self) -> None:
            SingletonByUserMeta.delete(self.__class__, user=self.user)
            self.user = None

        obj.clear = remove_user_from_instances

        @property
        def instances(klass) -> list[str]:
            return [f"{klass.__name__}(user={u})" for u in SingletonByUserMeta.__instances[klass]]

        cls.instances = instances

        return obj

    def __call__(cls, user: User | None, *args, **kwargs):
        if user is None:
            return

        if cls not in cls.__instances:
            cls.__instances[cls] = {}

        if user.user_id not in cls.__instances[cls]:
            cls.__instances[cls][user.user_id] = super().__call__(user, *args, **kwargs)

        return cls.__instances[cls][user.user_id]

    def delete(cls, user: User) -> None:
        if cls not in cls.__instances or user.user_id not in cls.__instances[cls]:
            return

        return cls.__instances[cls].pop(user.user_id)


class Session(metaclass=SingletonByUserMeta):

    def __init__(self, user: User | None) -> None:
        self.user = user


def main():
    print("===== MAIN =====")
    print("Creamos un objeto de la clase Patata")
    print('>>> p1 = Patata()')
    p1 = Patata()
    print(f"p1 == {p1}")
    print("Intentamos crear una segunda Patata, inicializada con valores diferentes:")
    print('>>> p2 = Patata(size=20, color="red")')
    p2 = Patata(size=20, color="red")
    print("Sin embargo, p2 es idéntica a p1:")
    print(f"p2 == {p2}")
    print("Esto es porque Patata es una clase singleton, y por tanto p2 no se ha instanciado, sino tomado de p1:")
    print(">>> p1 is p2")
    print(p1 is p2)
    print("Cambiar un atributo de cualquiera de los dos objetos lo cambia en ambos:")
    print('p1.size = 100')
    p1.size = 100
    print(f"p2 == {p2}")
    print('>>> p2.color = "green"')
    p2.color = "green"
    print(f"p1 == {p1}")


def extra():
    print("\n===== EXTRA =====")

    print("Creamos un usuario:")
    print('>>> user1 = User(user_id=1, username="juan", name="Juan Andahalf", email="juan@example.com")')
    user1 = User(user_id=1, username="juan", name="Juan Andahalf", email="juan@example.com")

    print("Creamos una sesión para ese usuario:")
    print('>>> session1 = Session(user=user1)')
    session1 = Session(user=user1)

    print("Vemos que esta sesión se ha registrado:")
    print(">>> Session.instances")
    print(Session.instances)

    print("Intentamos crear otra sesión para ese usuario:")
    print('>>> session2 = Session(user=user1)')
    session2 = Session(user=user1)

    print("Sin embargo, esta es idéntica a la anterior (es session1):")
    print('>>> session2 is session1')
    print(session2 is session1)

    print("Podemos ver que sólo hay una sesión en total:")
    print(">>> Session.instances")
    print(Session.instances)

    print("Ahora creamos un segundo usuario:")
    print('>>> user2 = User(user_id=2, username="illo", name="Juan Otro", email="otro@example.com")')
    user2 = User(user_id=2, username="illo", name="Juan Otro", email="otro@example.com")

    print("Y también creamos una sesión para ese usuario:")
    print('>>> session3 = Session(user=user2)')
    session3 = Session(user=user2)

    print("Como el usuario es distinto, se ha creado una sesión distinta para él:")
    print('>>> session3 is session1')
    print(session3 is session1)

    print("En efecto, ahora las dos sesiones están registradas:")
    print(">>> Session.instances")
    print(Session.instances)

    print("Tal y como se requiere, podemos extraer la información de usuario de una sesión:")
    print('>>> session1.user')
    print(session1.user)

    print("También podemos borrar una sesión:")
    print('>>> session1.clear()')
    session1.clear()
    print("Ahora sólo estará registrada la tercera sesión (la del usuario 2):")
    print('>>> Session.instances')
    print(Session.instances)
    print("Y los objetos session1 Y TAMBIÉN session2 (puesto que son el mismo objeto) han sido vaciados:")
    print('>>> session1.user')
    print(session1.user)
    print('>>> session2.user')
    print(session2.user)

    print("Obviamente, podemos volver a generar una sesión para el usuario 1:")
    print('>>> session4 = Session(user1)')
    session4 = Session(user1)
    print(">>> Session.instances")
    print(Session.instances)


if __name__ == "__main__":
    main()
    extra()
