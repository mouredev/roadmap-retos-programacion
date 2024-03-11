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
        print("Guau!")


class Cat(Animal):

    def sound(self):
        print("Miau!")


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

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto.")


class Programmer(Employee):

    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")


my_manager = Manager(1, "MoureDev")
my_project_manager = ProjectManager(2, "Brais", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Moure", "Proyecto 2")
my_programmer = Programmer(4, "Kontrol", "Swift")
my_programmer2 = Programmer(5, "Ros", "Cobol")
my_programmer3 = Programmer(6, "Bushi", "Dart")
my_programmer4 = Programmer(7, "Nasos", "Python")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()
