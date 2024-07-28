"""
Ejercicio
"""


# Superclase
class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass


# Subclases
class Dog(Animal):
    def sound(self):
        print("Guau")


class Cat(Animal):
    def sound(self):
        print("Miau")


def print_sound(animal: Animal):
    animal.sound()


my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
print_sound(my_dog)
my_cat = Cat("Gato")
print_sound(my_cat)

"""
Extra
"""


class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def equipment_supervision(self):
        print(f"{self.name} supervises and manages teams and resources")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def control_projects(self):
        print(f"{self.name} plans, executes and controls projects with {self.project}")


class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}")

    def add_employee(self, employee: Employee):
        print(f"{employee.name} no tiene cargos")


my_manager = Manager(
    1,
    "Marcos",
)
my_project_manager = ProjectManager(
    2,
    "Pedro",
    "Proyecto 1",
)
my_project_manager2 = ProjectManager(
    3,
    "Pepe",
    "Proyecto 2",
)

my_programmer = Programmer(4, "Raul", "Python")
my_programmer2 = Programmer(5, "Bruno", "Java")
my_programmer3 = Programmer(6, "Ana", "Python")


my_manager.add_employee(my_project_manager)
my_manager.add_employee(my_project_manager2)

my_project_manager.add_employee(my_programmer)

my_programmer2.code()

my_manager.print_employees()
