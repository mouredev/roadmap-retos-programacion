# 23 PATRONES DE DISEÑO: SINGLETON

# Ejercicio

class SingletonMeta(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def __init__(self) -> None:
        super().__init__()


if __name__ == '__main__':

    singleton1 = Singleton()
    singleton2 = Singleton()
    singleton3 = Singleton()

    print(singleton1 is singleton2)
    print(singleton1 is singleton3)


# Extra
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            sesion_instance = instance
        else:
            sesion_instance = cls._instances[cls]
        return sesion_instance


class sesion_usuario(metaclass=SingletonMeta):
    def __init__(self, id, username, nombre, email):
        if not hasattr(self, 'inicializada'):
            self.sesion_instance = {
                "id": id,
                "username": username,
                "nombre": nombre,
                "email": email,
                "autenticacion": False
            }
        self.inicializada = True

    def autenticacion(self, password):
        self.sesion_instance["autenticacion"] = True
        print(f"Usuario {self.sesion_instance['username']} autenticado.")

    def desconexion(self):
        print(f"Usuario {self.sesion_instance['username']} desconectado.")
        self.sesion_instance["id"] = None
        self.sesion_instance["username"] = None
        self.sesion_instance["nombre"] = None
        self.sesion_instance["email"] = None
        self.sesion_instance["autenticacion"] = False

    def info_usuario(self):
        return self.sesion_instance


# Ejemplo de uso
sesion1 = sesion_usuario("1", "juani", "Juan", "juan@ejemplo.com")
# para corroborar que es una unica instancia
sesion2 = sesion_usuario("2", "juanita", "juana", "juana@ejemplo.com")

print(sesion1.info_usuario())
print(sesion2.info_usuario())

sesion1.autenticacion("password123")
print(sesion1.info_usuario())

sesion1.desconexion()
print(sesion1.info_usuario())
print(sesion1 is sesion2)
