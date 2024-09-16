""" Reto 09: Herencia y Polimorfismo """

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
my_animal.sound()
print_sound(my_animal)

my_dog = Dog("Frida")
my_dog.sound()
print_sound(my_dog)

my_cat = Cat("Gordo")
my_cat.sound()
print_sound(my_cat)



""" Reto extra """

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

    def coordinate_projects(self):
        print(f"{self.name} está coordinando su proyecto.")

class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

my_manager = Manager(1, "Tomu")
my_project_manager1 = ProjectManager(2, "Jere", "Project 1")
my_project_manager2 = ProjectManager(3, "Cris", "Project 2")
my_programer1 = Programmer(4, "Celeste", "CSS")
my_programer2 = Programmer(5, "Benja", "Python")
my_programer3 = Programmer(6, "Pancho", "Java")
my_programer4 = Programmer(7, "Claudia", "C++")

my_manager.add(my_project_manager1)
my_manager.add(my_project_manager2)

my_project_manager1.add(my_programer1)
my_project_manager1.add(my_programer4)
my_project_manager2.add(my_programer2)
my_project_manager2.add(my_programer3)

my_programer4.add(my_programer1)

my_programer1.code()
my_project_manager1.coordinate_projects()
my_manager.coordinate_projects()

my_manager.print_employees()
my_project_manager1.print_employees()
my_programer4.print_employees()
