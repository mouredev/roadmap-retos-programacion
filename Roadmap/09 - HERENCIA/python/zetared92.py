# Reto 09 HERENCIA Y POLIMORFISMO

# SUPERCLASE

class Animal:

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

# SUBCLASES

class Dog(Animal):

    def sound(self):
        print("Guau!")

class Cat(Animal):

    def sound(self):
        print("Miau!")


def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("Pet:")
print_sound(my_animal)
my_dog = Dog("Dog")
print_sound(my_dog)
my_cat = Cat("Cat")
print_sound(my_cat)


# Extra

print("🧩 DIFICULTAD EXTRA - JERARQUÍA DE EMPRESA 🧩")

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
        print(f"{self.name} is coordinating the projects")

class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} is supervising the projects")

class Programmer(Employee):

    def __init__(self, id: int, name: str, program: str):
        super().__init__(id, name)
        self.program = program

    def code(self):
        print(f"{self.name} is programming in {self.program}")

    def add(self, employee: Employee):
        print( f"A programmer does not have employees under his supervision. {employee.name} not add")

my_manager = Manager(1, "Johnny")
my_project_manager = ProjectManager(2, "Zeta", "Projekt X")
my_project_manager2 = ProjectManager(3, "V", "Projekt Z")
my_programmer = Programmer(4, "Judy", "BrainDance")
my_programmer2 = Programmer(5, "Panam", "Neurostimulus")
my_programmer3 = Programmer(6, "Alt", "Soulkiller")
my_programmer4 = Programmer(7, "Rache", "R.A.B.I.D.S.")

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