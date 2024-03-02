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


class Dog(Animal):

    def __init__(self, name: str, age:int, breed: str):
        super().__init__(name, age, species="Canis lupus")
        self.breed = breed

    def sound(self):
        print("Guau!") 

    def movement(self):
        print("Camina en 4 patas")

    def describe(self):
        return super().describe()
    

class Cat(Animal):

    def __init__(self, name: str, age:int, breed: str):
        super().__init__(name, age, species="Felis silvestris catus")
        self.breed = breed

    def sound(self):
        print("Miau!") 

    def movement(self):
        print("Camina en 4 patas")

    def describe(self):
        return super().describe()


my_animal = Animal("Bolo", "chango", 11)
my_animal.sound()
my_animal2 = Dog("Cleo", 7, "Westie")
my_animal2.describe()
my_animal2.sound()
my_animal3 = Cat("Silvestre", 12, "Spynx")
my_animal3.describe()
my_animal3.sound()


"""
Extra
"""
class Employee():

    def __init__(self, ID:int, name:str):
        self.ID = ID
        self.name = name
        self.jobtitle = type(self).__name__
        

    def print(self):
            mesage = f"Nombre: {self.name} | ID: {self.ID} | JT: {self.jobtitle} "
            print(mesage)


class Programer(Employee):

    def __init__(self, ID:int, name:str):
        super().__init__(ID, name)
        self.jobtitle = type(self).__name__

    def program(self):
        print("Programar")
        

    def print(self):
            mesage = f"Nombre: {self.name} | ID: {self.ID} | JT: {self.jobtitle} "
            print(mesage)
 

class Manager(Employee):
    
    def __init__(self, ID: int, name: str):
        super().__init__(ID, name)
        self.jobtitle = type(self).__name__
        self.team = []

    def manage(self):
        print("Generar facturas, Generar sueldos, Administar proyectos, Administrar empleados")

    def print(self):
        return super().print()
    
    def groups(self, *args):
        self.team.append(args)
    
    def in_charge(self):
        for person in self.team:
            print(person)


class Proyect_Manager(Manager, Employee):
    
    def __init__(self, ID: int, name: str):
        super().__init__(ID, name)
        self.jobtitle = type(self).__name__
        self.team = []

    def manage(self):
        mesage = "Administar proyectos, Administrar empleados"
        print(mesage)

    def print(self):
        return super().print()
    
    def groups(self, *args):
        return super().groups(args)
    
    def in_charge(self):
        return super().in_charge()
       
    
print()
my_emp = Programer(1, "Adrian")
my_emp.print()
my_emp.program()
my_emp2 = Proyect_Manager(2, "Fernando")
my_emp2.print()
my_emp2.manage()
my_emp2.groups(my_emp)
my_emp2.in_charge()
my_emp3 = Manager(3, "Brais")
my_emp3.print()
my_emp3.manage()
my_emp3.groups(my_emp, my_emp2)
my_emp3.in_charge()