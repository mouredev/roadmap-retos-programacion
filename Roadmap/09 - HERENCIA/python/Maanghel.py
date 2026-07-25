"""
EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
    implemente una superclase Animal y un par de subclases Perro y Gato,
    junto con una función que sirva para imprimir el sonido que emite cada Animal.

DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
    pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
    Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
    actividad, y almacenan los empleados a su cargo.
"""

# Superclass Animal
class Animal:
    """
    A base class representing an animal.
    
    Attributes:
        name (str): The name of the animal.
    """
    def __init__(self, name: str):
        """
        Initializes the animal with a given name.
        
        Args:
            name (str): The name of the animal.
        """
        self.name = name

    def make_sound(self):
        """
        Prints a generic message indicating the animal is making a sound.
        """
        print(f"{self.name} is making a sound")

# Subclasses
class Dog(Animal):
    """
    A class representing a dog, which is a type of animal.
    
    Inherits from the Animal class and overrides the make_sound method.
    """
    def make_sound(self):
        """
        Prints the sound made by a dog: "guau guau".
        """
        print("guau guau")


class Cat(Animal):
    """
    A class representing a cat, which is a type of animal.
    
    Inherits from the Animal class and overrides the make_sound method.
    """
    def make_sound(self):
        """
        Prints the sound made by a cat: "miau miau".
        """
        print("miau miau")

# Instantiate objects
my_animal = Animal("animal")
my_dog = Dog("Perro")
my_cat = Cat("gato")

my_dog.make_sound()
my_cat.make_sound()
my_animal.make_sound()

# EXTRA

class Employee:
    """
    A class representing an employee in a company.
    
    Attributes:
        id (int): The employee's ID.
        name (str): The employee's name.
        employees (list): A list of employees that report to this employee.
    """
    def __init__(self, id: int, name: str):
        """
        Initializes the employee with an ID and name.
        
        Args:
            id (int): The employee's ID.
            name (str): The employee's name.
        """
        self.id = id
        self.name = name
        self.employees = []

    def add_employee(self, employee) -> None:
        """
        Adds an employee to the list of employees under this employee.
        
        Args:
            employee (Employee): The employee to be added.
        """
        self.employees.append(employee)

    def print_employees(self) -> None:
        """
        Prints the list of employees under this employee's supervision.
        """
        print(f"\n{self.name} is managing:")
        for id, employee in enumerate(self.employees, 1):
            print(f"{id}.- {employee.name}")


class Manager(Employee):
    """
    A class representing a manager, a type of employee.
    
    Inherits from Employee and has the ability to coordinate projects.
    """
    def coordinate_projects(self) -> None:
        """
        Prints a message indicating the manager is coordinating the company.
        """
        print(f"\n{self.name} is coordinating the entire company.")


class ProjectManager(Employee):
    """
    A class representing a project manager, a type of employee.
    
    Inherits from Employee and coordinates a specific project.
    
    Attributes:
        project (str): The project that the project manager is overseeing.
    """
    def __init__(self, id, name, project: str):
        """
        Initializes the project manager with an ID, name, and project.
        
        Args:
            id (int): The project manager's ID.
            name (str): The project manager's name.
            project (str): The name of the project they are coordinating.
        """
        super().__init__(id, name)
        self.project = project

    def coordinate_project(self) -> None:
        """
        Prints a message indicating the project manager is coordinating a specific project.
        """
        print(f"\n{self.name} is coordinating the project '{self.project}'")


class Programmer(Employee):
    """
    A class representing a programmer, a type of employee.
    
    Inherits from Employee and has the ability to program in a specific language.
    
    Attributes:
        language (str): The programming language the programmer uses.
    """
    def __init__(self, id, name, language: str):
        """
        Initializes the programmer with an ID, name, and programming language.
        
        Args:
            id (int): The programmer's ID.
            name (str): The programmer's name.
            language (str): The programming language the programmer uses.
        """
        super().__init__(id, name)
        self.language = language

    def code(self) -> None:
        """
        Prints a message indicating the programmer is coding in a specific language.
        """
        print(f"\n{self.name} is coding in {self.language}")

    def add_employee(self, employee) -> None:
        """
        Prints a message indicating that programmers cannot have employees under their supervision.
        
        Args:
            employee (Employee): The employee to be added (will not be added for programmers).
        """
        print(f"\n{self.name} cannot have employees under their supervision.")

# Example usage
my_manager = Manager(1, "Manuel")
my_project_manajer = ProjectManager(2, "Angel", "Web Page")
my_project_manajer2 = ProjectManager(3, "Jose", "Desktop App")
my_programmer = Programmer(4, "Ana", "Python")
my_programmer2 = Programmer(5, "Juan", "Python")
my_programmer3 = Programmer(6, "Maria", "JavaScript")
my_programmer4 = Programmer(7, "Fer", "JavaScript")

my_manager.add_employee(my_project_manajer)
my_manager.add_employee(my_project_manajer2)
my_project_manajer.add_employee(my_programmer3)
my_project_manajer.add_employee(my_programmer4)
my_project_manajer2.add_employee(my_programmer)
my_project_manajer2.add_employee(my_programmer2)

my_manager.coordinate_projects()
my_manager.print_employees()

my_project_manajer.coordinate_project()
my_project_manajer.print_employees()

my_project_manajer2.coordinate_project()
my_project_manajer2.print_employees()

my_programmer.add_employee(my_programmer2)
my_programmer.code()
