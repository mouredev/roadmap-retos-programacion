"""
--------
HERENCIA
--------
EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.

DIFICULTAD EXTRA (Opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empreados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""
# Ejercicio

class Animal:
    def __init__(self, name: str, species: str):
        self.species = species
        self.name = name

    def speak():
        pass

    def describe(self):
        print(f"{self.name} un Animal {self.species} de la especie", type(self).__name__)

class Perro(Animal):
    def __init__(self, name):
        self.species = "mamífero"
        self.name = name
    def speak(self):
        print("Guau!")

    
class Gato(Animal):
    def __init__(self, name) -> None:
        self.species = "mamífero"
        self.name = name
    def speak(self):
        print("Miau!")

my_dog = Perro("Keta")
my_cat = Gato("Garfield")

my_dog.describe()
my_dog.speak()

my_cat.describe()
my_cat.speak()

# Extra

class Empleado:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.empleados: list = []

    def fichar(self):
        print(f"{self.name}, ha entrado a trabajar")

    def salir(self):
        print(f"{self.name}, ha salido de trabajar")
        
    def contratar(self, candidato):
        self.empleados.append(candidato.name)

    def despedir(self, candidato):
        self.empleados.remove(candidato.name)

    def print_empleados(self):
        print(f"{self.name} esta al cargo de: {self.empleados}")


class Gerente(Empleado):

    def coordinar_projectos(self):
        print(f"{self.name} está coordinando todos los proyectos")

class GerenteProyectos(Empleado):

    def coordinar_projectos(self):
        pass

    def coordinar_projecto(self):
        print(f"{self.name} está coordinando su proyecto")

class Programador(Empleado):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def programar(self):
        print(f"{self.name} está programando en {self.language}")

    def contratar(self):
        pass

    def despedir(self):
        pass

    def coordinar_projectos(self):
        pass

    def coordinar_projecto(self):
        pass
    
    def print_empleados(self):
        print(f"{self.name} no puede tener empleados a su cargo")

my_manager = Gerente(1, "Jokos")
my_project_manager = GerenteProyectos(2, "Sergio")
my_project_manager2 = GerenteProyectos(3, "David")
my_programmer = Programador(4, "Randy", "Python")
my_programmer2 = Programador(5, "José", "JavaScript")

my_manager.contratar(my_project_manager)
my_manager.contratar(my_project_manager2)
my_manager.print_empleados()
my_project_manager.contratar(my_programmer)
my_project_manager2.contratar(my_programmer2)
my_project_manager.print_empleados()
my_project_manager2.print_empleados()
my_programmer.print_empleados()

my_manager.coordinar_projectos()
my_project_manager.coordinar_projecto()
my_programmer.programar()