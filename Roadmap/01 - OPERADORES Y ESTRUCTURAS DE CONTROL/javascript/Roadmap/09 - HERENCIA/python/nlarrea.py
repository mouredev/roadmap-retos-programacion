"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""


class Animal:
    def __init__(self, pet_name: str, animal_type: str) -> None:
        self.name = pet_name
        self.type = animal_type

    def __str__(self):
        return f"This is {self.name}. It is a {self.type}."

    def print_sound(self):
        pass


class Dog(Animal):
    def print_sound(self):
        print("Guau!")


class Cat(Animal):
    def print_sound(self):
        print("Miau!")


my_dog = Dog("Lagun", "dog")
print(my_dog)  # This is Lagun. It is a dog.
my_dog.print_sound()  # Guau!

my_cat = Cat("Kira", "cat")
print(my_cat)  # This is Kira. It is a cat.
my_cat.print_sound()  # Miau


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""


class Employee:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        print(f"\n{self.name}'s employees:")
        for employee in self.employees:
            print(f" - {employee.name}")


class Manager(Employee):
    def coordinate(self):
        print(f"\n{self.name} is coordinating all of the company's projects")


class ProjectManager(Employee):
    def __init__(self, id: int, name: str, project: str) -> None:
        super().__init__(id, name)
        self.project = project

    def coordinate(self):
        print(f"\n{self.name} is coordinating: {self.project}")


class Programmer(Employee):
    def __init__(self, id: int, name: str, language: str) -> None:
        super().__init__(id, name)
        self.language = language

    def code(self):
        print(f"\n{self.name} is programming using {self.language} language")

    def add(self, employee: Employee):
        print(
            f"\nA programmer has no employees.\n{employee.name} won't be added."
        )


# Initializing employees
my_manager = Manager(1, "ManagerName")
my_pm1 = ProjectManager(2, "PM1", "Project 1")
my_pm2 = ProjectManager(3, "PM2", "Project 2")
my_programmer1 = Programmer(4, "P1", "Python")
my_programmer2 = Programmer(5, "P2", "React")
my_programmer3 = Programmer(6, "P3", "JavaScript")
my_programmer4 = Programmer(7, "P4", "SQL")


# Adding employees
my_manager.add(my_pm1)
my_manager.add(my_pm2)

my_pm1.add(my_programmer1)
my_pm1.add(my_programmer2)

my_pm2.add(my_programmer3)
my_pm2.add(my_programmer4)

my_programmer1.add(my_programmer4)  # won't work
""" prints:
A programmer has no employees.
P4 won't be added.
"""


# Tasks
my_manager.coordinate()
# ManagerName is coordinating all of the company's projects
my_pm1.coordinate()
# PM1 is coordinating: Project 1
my_programmer1.code()
# P1 is programming using Python language
my_programmer2.code()
# P2 is programming using React language
my_pm1.print_employees()
"""
PM1's employees:
 - P1
 - P2
"""
my_manager.print_employees()
"""
ManagerName's employees:
 - PM1
 - PM2
 """
