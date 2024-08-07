import random


class Session:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def __init__(self, id=None, username=None, name=None, email=None):
        if not hasattr(self, 'id'):
            self.id = id
        if not hasattr(self, 'username'):
            self.username = username
        if not hasattr(self, 'name'):
            self.name = name
        if not hasattr(self, 'email'):
            self.email = email

    @classmethod
    def clear_session(cls):
        cls._instance = None


def main():
    print("Iniciando sesión...")
    name = input("Nombre: ")
    username = input("Username: ")
    email = input("Email: ")

    session = Session(random.randint(1, 1000), username, name, email)

    quit = False

    while not quit:
        print("\nSeleccione una opción: "
              "\n1- Ver datos de sesión"
              "\n2- Borrar sesión\n")

        choice = input("> ")

        match choice:
            case "1":
                print(f"Id: {session.id}")
                print(f"Username: {session.username}")
                print(f"Name: {session.name}")
                print(f"Email: {session.email}")
            case "2":
                Session.clear_session()
                quit = True
                print("Hasta pronto")
            case _:
                print("Opción no válida")


if __name__ == '__main__':
    main()
