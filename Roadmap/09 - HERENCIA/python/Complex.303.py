"""
Herencia y Polimorfismo
"""

# Superclase (clase base)
class Animal:
    # Constructor que recibe un nombre
    def __init__(self, name: str):
        self.name = name

    # Método que se espera que las subclases sobrescriban
    def sound(self):
        pass  # No hace nada aquí

# Subclase Dog que hereda de Animal
class Dog(Animal):
    # Sobreescribe el método sound()
    def sound(self):
        print("Guau!!")

# Subclase Cat que hereda de Animal
class Cat(Animal):
    # Sobreescribe el método sound()
    def sound(self):
        print("Miau!!")

# Función que recibe un objeto Animal (o sus subclases)
# y llama a su método sound()
def print_sound(animal: Animal):
    animal.sound()

# Creamos un objeto de tipo Animal
my_animal = Animal('Animal')
print_sound(my_animal)  # Como Animal.sound() está vacío (pass), no imprime nada

# Creamos un objeto de tipo Dog
my_dog = Dog('Perro')
print_sound(my_dog)  # Llama a Dog.sound() y muestra "Guau!!"

# Creamos un objeto de tipo Cat
my_cat = Cat('Gato')
print_sound(my_cat)  # Llama a Cat.sound() y muestra "Miau!!"


""" * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""



# Clase base Employee (Empleado)
class Employee:
    def __init__(self, id: int, name: str):
        self.id = id                    # ID del empleado
        self.name = name                # Nombre del empleado
        self.employee = []              # Lista para guardar empleados a su cargo

    def add(self, employee):
        # Método para agregar empleados a la lista
        self.employee.append(employee)

    def print_employee(self):
        # Método para mostrar los nombres de los empleados a su cargo
        for employee in self.employee:
            print(employee.name)

# Clase Manager que hereda de Employee
class Manager(Employee):
    def coordinate_projects(self):
        # Método específico del Manager
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")

# Clase ProjectManager que hereda de Employee
class ProjectManager(Employee):
    def __init__(self, id: int, name: str, proyecto: str):
        super().__init__(id, name)      # Llama al constructor de Employee
        self.proyecto = proyecto        # Proyecto a su cargo

    def coordinate_project(self):
        # Método específico del ProjectManager
        print(f"{self.name} está coordinando su proyecto.")

# Clase Programmer que hereda de Employee
class Programmer(Employee):
    def __init__(self, id: int, name: str, languaje: str):
        super().__init__(id, name)
        self.languaje = languaje        # Lenguaje de programación

    def code(self):
        # Método específico del Programmer
        print(f"{self.name} está programando en {self.languaje}.")

    def add(self, employee: Employee):
        # Sobreescritura de add(): los programadores no pueden tener empleados
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")

# ----------------- INSTANCIAS Y USO ----------------------

# Creamos un Manager
my_manager = Manager(1, 'Eddy')

# Creamos dos ProjectManagers
my_proyect_manager = ProjectManager(2, 'Raul', 'Proyecto1')
my_proyect_manager2 = ProjectManager(3, 'Maria', 'Proyecto2')

# Creamos cuatro Programadores
my_programmer = Programmer(4, 'Jose', 'Python')
my_programmer2 = Programmer(5, 'Duran', 'Kotlin')
my_programmer3 = Programmer(6, 'Migue', 'Java')
my_programmer4 = Programmer(7, 'Ana', 'C#')

# El Manager agrega a los ProjectManagers
my_manager.add(my_proyect_manager)
my_manager.add(my_proyect_manager2)

# Cada ProjectManager agrega programadores a su proyecto
my_proyect_manager.add(my_programmer)
my_proyect_manager.add(my_programmer2)
my_proyect_manager2.add(my_programmer3)
my_proyect_manager2.add(my_programmer4)

# Intentamos agregar un programador a otro programador (no permitido)
my_programmer.add(my_programmer4)

# Acciones de los empleados
my_programmer.code()                   # Jose está programando
my_proyect_manager.coordinate_project()# Raul coordina su proyecto
my_manager.coordinate_projects()       # Eddy coordina todo

# Ver lista de empleados de cada quien
my_manager.print_employee()            # Muestra a Raul y Maria
my_proyect_manager.print_employee()    # Muestra a Jose y Duran
my_programmer.print_employee()         # No tiene empleados



