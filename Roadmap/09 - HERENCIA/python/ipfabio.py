"""
Ejercicio
"""

class Animal:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def sonido(self):
        ...

# Herencia
class Perro(Animal):
    
    def sonido(self):
        print(f"{self.nombre} hace: Guau Guau")

class Gato(Animal):
    
    def sonido(self):
        print(f"{self.nombre} hace: Miaaaaau")

# Polimorfismo -> Sobrecarga en compilación
def print_sound(animal: Animal):
    animal.sonido()

perro = Perro("Perro Lindo")
print_sound(perro)
gato = Gato("Gato Bello")
print_sound(gato)

"""
Extra
"""

class Empleado():
    def __init__(self, id:int, name: str) -> None:
        self.id = id
        self.name = name
        self.employees = []
    
    # Toma por defecto employee: Employee
    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
        

class Manager(Empleado):
    
    def coordintae_project(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")

class ProjectManager(Empleado):

    def __init__(self, id: int, name: str, project: str) -> None:
        super().__init__(id, name)
        self.project = project
    
    def coordintae_project(self):
        print(f"{self.name} está coordinando su proyecto.")

class Programmer(Empleado):
    
    def __init__(self, id: int, name: str, language: str) -> None:
        super().__init__(id, name)
        self.lenguage = language
    
    def code(self):
        print(f"{self.name} está programando en {self.lenguage}")
    
    def add(self, employee: Empleado):
        print(f"Un programador no tiene empleados a su cargo. {employee} no se añadirá.")
    
    def print_employees(self):
        print(f"{self.name} no tiene empleados a su cargo.")
        

my_manager = Manager(1, "Marco")
my_project_manager = ProjectManager(2, "Polo", "Proyecto 1")
my_project_manager_2 = ProjectManager(3, "Daniel", "Proyecto 2")
my_programmer = Programmer(4, "Kain", "C++")
my_programmer2 = Programmer(5, "Abel", "C#")
my_programmer3 = Programmer(6, "Ron", "C")
my_programmer4 = Programmer(7, "Mon", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager_2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)

my_project_manager_2.add(my_programmer3)
my_project_manager_2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordintae_project()
my_manager.coordintae_project()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()
