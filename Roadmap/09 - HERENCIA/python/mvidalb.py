'''
Ejercicio
'''
# Superclase

class Animal:
    
    def __init__(self, name: str) -> None:
        self.name = name

    def sound(self):
        print("Este animal emite un sonido no determinado")


#Subclases

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
my_animal = Dog("Perro")
print_sound(my_animal)
my_animal = Cat("Gato")
print_sound(my_animal)


'''
Ejercicio extra
'''

class Employee():
    
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):

    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")


class ProjectManager(Employee):

    def __init__(self, id: int, name: str, project: str) -> None:
        super().__init__(id,name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando  su proyecto.")


class Programmer(Employee):
    
    def __init__(self, id: int, name: str, language: str) -> None:
        super().__init__(id,name)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}.")
        
    def add_employee(self, employee):   # Se crea la función para que este empleado no pueda añadir ninún empleado
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")


my_manager = Manager(1, "MarioDev")
my_project_manager = ProjectManager(2, "Mario", "Proyecto 1")
my_project_manager2 = ProjectManager(3, "Marcos", "Proyecto 2")
my_programmer = Programmer(4, "Mai", "Python")
my_programmer2 = Programmer(5, "Angy", "Java")
my_programmer3 = Programmer(6, "Moure", "Python")
my_programmer4 = Programmer(7, "Jose", "C#")

my_manager.add_employee(my_project_manager)
my_manager.add_employee(my_project_manager2)

my_project_manager. add_employee(my_programmer)
my_project_manager. add_employee(my_programmer2)
my_project_manager2. add_employee(my_programmer3)
my_project_manager2. add_employee(my_programmer4)

my_programmer.add_employee(my_programmer2)

my_programmer.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()
