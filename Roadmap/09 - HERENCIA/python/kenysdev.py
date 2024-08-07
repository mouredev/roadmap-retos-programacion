# ╔══════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado               ║
# ║ GitHub: https://github.com/Kenysdev  ║
# ║ 2024 -  Python                       ║
# ╚══════════════════════════════════════╝

# ----------------------------------------
# Herencia
# ----------------------------------------
# - Permite definir una clase que hereda atributos y métodos de una 
#   clase existente, para reutilización y organización.
# - La clase que hereda se conoce como “subclase” o “clase hija”.
# - La clase de la que hereda se conoce como “superclase” o “clase padre”.

# Polimorfismo:
# ----------------------------------------
# - Los objetos de diferentes clases pueden ser accedidos utilizando el 
#   mismo interfaz, mostrando un comportamiento distinto 
#   (tomando diferentes formas) según cómo sean accedidos.

# superclase:
class Animal: 
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} hace: {self.sound}")

# subclases:
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

# crear instancias y llamar a sus métodos
dog = Dog("Max")
cat = Cat("Milo")
dog.make_sound()
cat.make_sound()

#__________________________________________
# Ejercicio usando herencia y Polimorfismo.
"""
- Implementa la jerarquía de una empresa de desarrollo formada por 
  empleados que pueden ser Gerentes, Gerentes de Proyectos o Programadores.
- Cada empleado tiene un identificador y un nombre.
- Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
  actividad, y almacenan los empleados a su cargo.
"""

class Employees:
    employees: list = []
    def __init__(self):
        self.identifier = ""
        self.tasks: tuple = ()
        self.staff: set = {}

    def add(self, names: tuple):
        for name in names:
            self.employees.append([self.identifier, name])

    def println(self):
        for employee in self.employees:
            if employee[0] == self.identifier:
                print(f"{employee[1]} -> {self.identifier}")

    def functions(self):
        print(f"\nFunciones de {self.identifier}")
        for task in self.tasks:
            print(task)
        print("--------------------")
    
    def subordinates(self):
        print(f"\nSubordinados de un {self.identifier}")
        for employee in self.employees:
            if employee[0] in self.staff:
                print(f"{employee[1]} -> {employee[0]}")
        print("--------------------")

class Manager(Employees):
    def __init__(self):
        super().__init__()
        self.identifier = "Gerente"
        self.tasks: tuple =(
            "- Supervisión", 
            "- Toma de decisiones")
        self.staff: set = {"Gerente de Proyecto", "Programador"}


class Project_Manager(Employees):
    def __init__(self):
        super().__init__()
        self.identifier = "Gerente de Proyecto"
        self.tasks: tuple =(
            "- Planificación", 
            "- Coordinación de proyectos")
        self.staff: set = {"Programador"}

class Programmer(Employees):
    def __init__(self):
        super().__init__()
        self.identifier = "Programador"
        self.tasks: tuple =(
            "- Desarrollo", 
            "- Mantenimiento de código")
        self.staff = {"No tiene subordinados"}

#__________________________________________
if __name__ == "__main__":
    manager = Manager()
    project_manager = Project_Manager()
    programmer = Programmer()

    manager.add(("Ben", "Dan"))
    project_manager.add(("Ray", "Joe"))
    programmer.add(("Leo", "Sam", "Zoe", "Ana"))

    manager.functions()
    project_manager.functions()
    programmer.functions()

    manager.subordinates()
    project_manager.subordinates()

    manager.println()
    project_manager.println()
