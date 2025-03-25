'''
EJERCICIO:
Explora el concepto de Herencia segun tu lenguaje. Crea un ejemplo 
que implemente una superclase Animal y un par de subclases Perro y 
Gato, junto con una función que sirva para imprimir el sonido que 
emite cada Animal.
'''

class Animal: # Superclase Animal

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        print('Sonido desconocido')

# Subclase Perro
def Dog(Animal): 

    def sound(self):
        print('Guau!')

# Subclase Gato
def Cat(Animal): 

    def sound(self):
        print('Miau!')

def print_sound(animal: Animal):
    animal.sound()
    
my_animal = Animal('????') 
my_dog = Dog('Shena')
my_cat = Cat('Lucas')


'''
DIFICULTAD EXTRA (opcional):
- Implementa la jerarquía de una empresa de desarrollo formada por 
Empleados que pueden ser Gerentes, Gerentes de Proyectos o 
Programadores.
- Cada empleado tiene un identificador y un nombre.
- Dependiendo de su labor, tienen propiedades y funciones exclusivas 
de su actividad, y almacenan los empleados a su cargo.
'''

print('\n\n\n--- EJERCICIO EXTRA ---\n')

# Superclase Empleado
class Employee:

    def __init__(self, ID: int, name: str):
        self.ID = ID
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print('Nombre:', employee.name, '| ID:', employee.ID)

# Subclase Gerente
class Manager(Employee):
    
    def coordinate_projects(self):
        print(f'{self.name} está coordinando todos los proyectos de la empresa.')
    
    def add(self, employee):
        self.employees.append(employee)

# Subclase Gerente de Proyectos
class ProjectManager(Manager, Employee): 
    
    def __init__(self, ID: int, name: str, project: str):
        super().__init__(ID, name) # Llama al inicializador de Gerente
        self.project = project
        
    def coordinate_project(self):
        print(f'{self.name} está coordinando su proyecto.')
        

# Subclase Programador
class Programmer(Employee):
    
    def __init__(self, ID: int, name: str, language):
        super().__init__(ID, name) # Llama al inicializador de Gerente
        self.language = language
        
    def code(self):
        print(f'{self.name} está programando en {self.language}.')

    def add(self, employee: Employee):
        print(f'Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.')

# Crear Gerente
my_manager = Manager(1, 'MoureDev')

# Crear Gerentes de Proyectos
my_project_manager = ProjectManager(2, 'Fernando', 'Proyecto MotoGP')
my_project_manager2 = ProjectManager(3, 'Javier', 'Proyecto Formula 1')

# Crear Programadores
my_programmer = Programmer(4, 'Paco', 'python')
my_programmer2 = Programmer(5, 'Fran', 'python')
my_programmer3 = Programmer(6, 'Victor', 'java')
my_programmer4 = Programmer(7, 'Jose Andres', 'java')
my_programmer5 = Programmer(8, 'Eduardo', 'HTML&CSS')

# Empleados del Gerente
my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

# Empleados del Gerente de Proyectos
my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)
my_project_manager2.add(my_programmer4)
my_project_manager2.add(my_programmer5)

# Empleados del Programador
my_programmer.add(my_programmer2)

# Tareas de cada EMPLEADO
my_programmer2.code()
my_project_manager.coordinate_project()
my_manager.coordinate_projects()
my_manager.print_employees()
my_project_manager2.print_employees()
my_programmer.print_employees()
