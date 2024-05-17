class Animal:
    def __init__(self, especie, raza, color):
        self.especie = especie
        self.raza = raza
        self.color = color
    
    
    def sound(self, sonido: str):
        return print(f'El {self.especie} hace {sonido}')
        
    def print(self):
        print(f'Especie: {self.especie}, es de raza {self.raza}, y su color es {self.color}.')

class Gato(Animal):
    pass

class Perro(Animal):
    pass
        
my_dog = Perro('Canino', 'Pitbull', 'Blanco')
my_dog.print()

my_cat = Gato('Felino', 'Persa', 'Amarillo')
my_cat.print()

my_cat.sound('Miau')
my_dog.sound('Guau')

'''
Ejercicio
'''

class Employees():
    def __init__(self, identifier: int, name: str):
        self.identifier = identifier
        self.name = name
        self.employees = []
    
    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)

class Manager(Employees):
    def projects_coordination(self):
        print(f'{self.name} is the manager, they coordinate all of the company projects.')
        
class ProjectManager(Employees):
    def __init__(self, identifier:int, name: str, project: str):
        super().__init__(identifier, name)
        self.project = project
    
    def print_projects(self):
        print(f'{self.project} is one of the projects that {self.name} works on.')

class Programmer(Employees):
    def __init__(self, identifier: int, name: str, languages: list, expertise: int):
        super().__init__(identifier, name)
        self.languages = languages
        self.expertise = expertise        
        
    def print_programmer(self):
        print(f"The programmer {self.name} is one of the organizations programmers (ID:{self.identifier}). He manages {self.languages} properly and has {self.expertise} level of expertise in a 0 - 5 scale.")
    
    def add(self, employee: Employees):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")
    
manager1 = Manager(1, 'César Morán')
project_manager1 = ProjectManager(2,'Jesus Moran', 'Perfumery Web Page')
project_manager2 = ProjectManager(3,'Ruby Rose', 'Perfumery Web Page')
programmer1 = Programmer(4, 'Jose Moran', ['Ruby', 'Java', 'Python'], 3)
programmer2 = Programmer(5, 'Pucho Almendras', ['JavaScript', 'Python'], 4)
programmer3 = Programmer(6, 'Pelango Navaz', ['Python'], 5)
manager1.projects_coordination()
project_manager1.print_projects()
programmer1.print_programmer()

manager1.add(project_manager1)
manager1.add(project_manager2)

project_manager1.print_projects()
project_manager2.print_projects()

programmer3.add(programmer3)

programmer3.print_programmer()