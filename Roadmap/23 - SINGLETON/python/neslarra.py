"""
 EJERCICIO:
 Explora el patrón de diseño "singleton" y muestra cómo crearlo
 con un ejemplo genérico.

 DIFICULTAD EXTRA (opcional):
 Utiliza el patrón de diseño "singleton" para representar una clase que
 haga referencia a la sesión de usuario de una aplicación ficticia.
 La sesión debe permitir asignar un usuario (id, username, nombre y email),
 recuperar los datos del usuario y borrar los datos de la sesión.
"""
from time import sleep

print(f"{'#' * 47}")
print(f"##  Explicación  {'#' * 30}")
print(f"{'#' * 47}")

print(r"""
Singleton es un patrón de diseño que sirve para garantizar que una clase tendrá "una y sola una" instancia de la misma.

class Singleton(object):
    single_object = None

    def __new__(cls, *args, **kwargs):
        if cls.single_object is None:
            cls.single_object = super().__new__(cls)
            cls.single_object._initialized = False
        return cls.single_object

    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


obj1 = Singleton(17)
obj2 = Singleton("Mundo")
obj3 = Singleton([1, 2, 3])

print(f"obj1, obj2 y obj3 ¿Son el mismo objeto? <=> {id(obj1) == id(obj2) == id(obj3)}")
print(f"obj1 type = {obj1.__class__.__name__} value = {obj1.get_value()}")
print(f"obj2 type = {obj2.__class__.__name__} value = {obj2.get_value()}")
print(f"obj3 type = {obj3.__class__.__name__} value = {obj3.get_value()}")

obj1, obj2 y obj3 ¿Son el mismo objeto? <=> True
obj1 type = int value = 17  \
obj2 type = int value = 17   |---> tomó SOLAMENTE el primer objeto en instanciar (probar cambiando el orden)
obj3 type = int value = 17  /

Opero sobre el objeto
obj2.set_value(obj2.get_value() * 3)
obj3.set_value(obj3.get_value() - 2)
obj1.set_value(pow(obj1.get_value(), 0.5))
print(f"obj1, obj2 y obj3 ¿Son el mismo objeto? <=> {id(obj1) == id(obj2) == id(obj3)}")
print(f"obj1 type = {obj1.__class__.__name__} value = {obj1.get_value()}")
print(f"obj2 type = {obj2.__class__.__name__} value = {obj2.get_value()}")
print(f"obj3 type = {obj3.__class__.__name__} value = {obj3.get_value()}")

obj1, obj2 y obj3 ¿Son el mismo objeto? <=> True
obj1 type = int value = 7.0  \
obj2 type = int value = 7.0   |---> operé sobre obj1, 2 y 3 PERO, como es el MISMO objeto, fue una operación equivalente a raíz_2(17 * 3 - 2) = 7
obj3 type = int value = 7.0  /
""")


print(f"{'#' * 63}")
print(f"##  Dificultad extra 1 - Logger  {'#' * 30}")
print(f"{'#' * 63}\n")



class Singleton(object):
    single_object = None

    def __new__(cls, *args, **kwargs):
        if cls.single_object is None:
            cls.single_object = super().__new__(cls)
            cls.single_object._initialized = False
        return cls.single_object

    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Logger(Singleton):

    def add_entry(self, message):
        from datetime import datetime
        self.set_value(self.get_logger()  + datetime.now().strftime("%Y-%b-%d %H%M%S.%f")[:-3] + ": " + message + "\n")

    def get_logger(self):
        return self.get_value()


class Task:
    def __init__(self, username: str, task: str = "Starting logger"):
        from datetime import datetime
        self.username = username
        self.logger = Logger(datetime.now().strftime("%Y-%b-%d %H%M%S.%f")[:-3] + ": " + self.username + " - " + task + "\n")
        self.add_task("Login")

    def add_task(self, task:str):
        self.logger.add_entry(self.username + " - " + task)

    def view_tasks(self):
        return self.logger.get_logger()


task_nestor = Task("Nestor")
sleep(0.25)
task_nestor.add_task("Formatear disco G")
sleep(0.25)
task_neslarra = Task("Neslarra")
sleep(0.25)
task_nestor.add_task("Copiar ISOs a disco G")
sleep(0.25)
task_nestor.add_task("Hacer flash booteable con ISO Linux Mint")
sleep(0.25)
task_neslarra.add_task("Cargar SO Linux Mint en laptop AX103")
sleep(0.25)
task_delivery = Task("Delivery")
sleep(0.25)
task_neslarra.add_task("Bootear laptop AX103")
sleep(0.25)
task_nestor.add_task("Registar laptop AX103 como OK")
sleep(0.25)
task_delivery.add_task("Retiro de laptop AX103 para entrega")

print(f"Contenido del logger: \n{task_nestor.view_tasks()}")

print(f"¿Son las instancias de 'Task.logger' la misma instancia? <=> {id(task_nestor.logger) == id(task_neslarra.logger) == id(task_delivery.logger)}")

print(f"\n{'#' * 63}")
print(f"##  Dificultad extra 2 - UserId  {'#' * 30}")
print(f"{'#' * 63}\n")

class Login(Singleton):
    _id = 1000

    def user_login(self, username: str, name: str, email: str):
        from datetime import datetime
        data = {"username": username,
                "name": name,
                "email": email,
                "login_time": datetime.now().strftime("%Y-%b-%d %H%M%S.%f")[:-3],
                "session_id": self.get_session_id()
                }
        self.get_logged_users().append(data)

    def get_logged_users(self):
        return self.get_value()

    @classmethod
    def get_session_id(cls):
        cls._id += 1
        return cls._id


class User:

    def __init__(self, username: str, name: str, email: str):
        self.username = username
        self.name = name
        self.email = email
        self.user = Login([])
        self.add_user()

    def add_user(self):
        self.user.user_login(self.username, self.name, self.email)

    def view_logged_users(self):
        return self.user.get_logged_users()


nestor = User("nestor", "Nestor Larralde", "nestor.larralde@yahoo.com")
sleep(1.27)
neslarra = User("neslarra", "Nestor Omar Larralde", "neslarra@ibm.com")
sleep(0.98)
otro = User("otro)", "Otro Nestor", "otro_mail@turulo.net")

print(f"¿Son los objetos User.user iguales? <=> {id(nestor.user) == id(neslarra.user) == id(otro.user)}")

for lu in nestor.view_logged_users():
    print(f"\n")
    for k, v in lu.items():
        print(f"\t{k}: {v}")

print("""
En los tres casos (el de la explicación y las dos dificultades extra (Logger y User) se usó la misma clase Singleton: en la explicación instanció
un entero, en el Logger un string y en el User un dict. 
""")
