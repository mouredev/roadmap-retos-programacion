"""
EJERCICIO:
Explora el concepto de Herencia segun tu lenguaje. Crea un ejemplo 
que implemente una superclase Animal y un par de subclases Perro y 
Gato, junto con una función que sirva para imprimir el sonido que 
emite cada Animal.

DIFICULTAD EXTRA (opcional):
- Implementa la jerarquía de una empresa de desarrollo formada por 
Empleados que pueden ser Gerentes, Gerentes de Proyectos o 
Programadores.
- Cada empleado tiene un identificador y un nombre.
- Dependiendo de su labor, tienen propiedades y funciones exclusivas 
de su actividad, y almacenan los empleados a su cargo.

by adra-dev.
"""

"""
Herencia:
    La herencia permite definir nuevas clases a partir de clases 
    existentes. A la clase de la que se hereda se le denomina 
    <<clase madre>> o <<super clase>>. A la clase que hereda se le 
    denomina <<clase hija>> o <<sub clase>>. La clase hija <<hereda>>
    todas las propiedades de la clase madre y nos permite redefinir 
    metodos y atributos o anadir nuevos. La ventaja fundamental que 
    aporta el mecanismo de herencia a la programacion es la capacidad
    de reutilizar el codigo. Asi, un conjunto de clases que comparten
    atributos y metodos pueden heredar de una superclase donde se 
    definan esos metodos y atributos.
"""

# Superclase

class Animal():

    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.species = species
        self.age = age

    def sound(self):
        pass

    def movement(self):
        pass

    def describe(self):
        print("Soy un Animal del tipo", type(self).__name__)

# Subclases

class Dog(Animal):

    def __init__(self, name: str, age:int, breed: str):
        super().__init__(name, age, species="Canis lupus")
        self.breed = breed

    def sound(self):
        print("Guau!") 

    def movement(self):
        print("Camina en 4 patas")

    def describe(self):
        print(f"Soy un Animal del tipo {self.species},de la raza {self.breed}")
    
        
class Cat(Animal):

    def __init__(self, name: str, age:int, breed: str):
        super().__init__(name, age, species="Felis silvestris catus")
        self.breed = breed

    def sound(self):
        print("Miau!") 

    def movement(self):
        print("Camina en 4 patas")

    def describe(self):
        print(f"Soy un Animal del tipo {self.species}, de la raza {self.breed}")

def print_sound(animal: Animal):
    animal.sound()

my_animal = Animal("Bolo", "chango", 11)
print_sound(my_animal)
my_dog = Dog("Cleo", 7, "Westie")
my_dog.describe()
print_sound(my_dog)
my_cat = Cat("Silvestre", 12, "Spynx")
my_cat.describe()
print_sound(my_cat)


"""
Extra
"""
class Employee():

    def __init__(self, ID:int, name:str):
        self.ID = ID
        self.name = name
        self.employees = []
        self.jobtitle = type(self).__name__
        

    def print(self):
            mesage = f"Nombre: {self.name} | ID: {self.ID} | JT: {self.jobtitle} "
            print(mesage)

    def add(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(employee.name)


class Manager(Employee):
    
    def coordinate_projects(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa.")

    def print(self):
        return super().print()


class ProjectManager(Manager, Employee):
    
    def __init__(self, ID: int, name: str, project: str):
        super().__init__(ID, name)
        self.project = project

    def coordinate_project(self):
        print(f"{self.name} está coordinando su proyecto.")


class Programmer(Employee):

    def __init__(self, ID:int, name:str, language):
        super().__init__(ID, name)
        self.jobtitle = type(self).__name__
        self.language = language


    def code(self):
        print(f"{self.name} está programando en {self.language}.")

    def add(self, employee: Employee):
        print(
            f"Un programador no tiene empleados a su cargo. {employee.name} no se añadirá.")
        

       
    
print()
my_emp = Programmer(1, "Adrian", "python")
my_emp.print()
my_emp.code()

my_emp2 = ProjectManager(2, "Fernando", "Proyecto1")
my_emp2.print()
my_emp2.add(my_emp)
my_emp2.coordinate_project()

my_emp.add(my_emp2)
my_emp3 = Manager(3, "Brais")
my_emp3.print()
my_emp3.coordinate_projects()
my_emp3.add(my_emp)
my_emp3.add(my_emp2)
my_emp3.print_employees()