"""
* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
"""
class Animal():
    def __init__(self) -> None:
        pass

class Dog(Animal):
    def bark(self):
        print("GUAU")

class Cat(Animal):
    def meow(self):
        print("MIAU")

my_dog = Dog()
my_dog.bark()

my_cat = Cat()
my_cat.meow()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
#Un poquito de humor =)
class Empleado():
    def __init__(self):
        self.worker = dict()
        self.worker = {"name":"default","id":0,"position":"default"}
        return None
    def work():
        print("Estoy trabajando")
    
class CEO(Empleado):
    def __init__(self):
        super().__init__()
        self.worker["name"] = "Melon Musk"
        self.worker["id"] = 1
        self.worker["position"] = "CEO"
        self.worker["employees"] = ["PHILIP","ANDY FENNEL","ANTONIO SANZ", "ALEX VALDERRAMA", "ALEJANDRO CENALMOR"]
        self.worker["bonus"] = ["coche","seguro privado premium","dietas"]
    
    def work(self):
        print("Estoy gerenciando")

    def ceos_lunch(self):
        print("Me voy a comer con otros CEOs")

class ProjectManager(Empleado):
    def __init__(self):
        super().__init__()
        self.worker["name"] = "PHILIP"
        self.worker["id"] = 3
        self.worker["position"] = "PM"
        self.worker["employees"] = ["ALEX VALDERRAMA", "ALEJANDRO CENALMOR"]
        self.worker["bonus"] = ["seguro privado normal","dietas"]
    
    def work(self):
        print("Estoy gerenciando proyectos y viendo una peli en KODI")

    def smoke(self):
        print("Me salgo a fumar")

class Programmer(Empleado):
    def __init__(self):
        super().__init__()
        self.worker["name"] = "Alex Valderrama"
        self.worker["id"] = 1231323223
        self.worker["position"] = "Umpa Lumpa"
    
    def work(self):
        print("Estoy picando sin parar y cobrando poco")

    def take_breath(self):
        print("Voy a tomarme 30 segundos para respirar")

my_ceo = CEO()
print(my_ceo.worker)
my_ceo.work()
my_ceo.ceos_lunch()
my_pm = ProjectManager()
print(my_pm.worker)
my_pm.work()
my_pm.smoke()
my_programmer = Programmer()
print(my_programmer.worker)
my_programmer.work()
my_programmer.take_breath()
