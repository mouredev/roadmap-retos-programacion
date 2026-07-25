#HERENCIA

#Superclase
class Animal:

    def __init__(self, name:str):
        self.name = name

    def sound(self):
        pass

#Subclases
class Dog(Animal):
    
    def sound(self):
        print("Guau!")

class Cat(Animal):
    
    def sound(self):
        print("Miau!")

def print_sound(animal:Animal):
    animal.sound()

my_animal = Animal("Animal")
my_animal.sound()
print_sound(my_animal)
my_dog = Dog("Perro")
my_dog.sound()
print_sound(my_dog)
my_cat = Cat("Gato")
my_cat.sound()
print_sound(my_cat)


#EJERCICIO EXTRA

#Superclase
class Empleado():

    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
        self.empleados = []

    def agregaEmpleado(self, empleado):
        self.empleados.append(empleado)

    def printEmpleados(self):
        for i in self.empleados:
            print(i.name)

#Subclases
class Gerente(Empleado):
    
    def function(self):
        print("Soy un Gerente")


class GerenteProyecto(Empleado):

    def __init__(self, id:str, name:str, proyect: str):
        super().__init__(id, name)
        self.proyect = proyect
    
    def function(self):
        print("Soy un Gerente de Proyectos")

class Programador(Empleado):

    def __init__(self, id:str, name:str, language: str):
        super().__init__(id, name)
        self.languaje = language
    
    def function(self):
        print(f"Soy un Programador programando en {self.languaje}")

    def agregaEmpleado(self, empleado):
        print("El Programador no puede agregar empleados")

my_gerente = Gerente(1, "Victor")
my_gerente_proyecto1 = GerenteProyecto(2, "Pepe", "Proyecto 1")
my_gerente_proyecto2 = GerenteProyecto(3, "Paco", "Proyecto 2")
my_programador1 = Programador(4, "Control", "Java")
my_programador2 = Programador(5, "Ros", "Cobol")
my_programador3 = Programador(6, "Busi", "Python")
my_programador4 = Programador(7, "Naso", "Dart")

my_gerente.agregaEmpleado(my_gerente_proyecto1)
my_gerente.agregaEmpleado(my_gerente_proyecto2)

my_gerente_proyecto1.agregaEmpleado(my_programador1)
my_gerente_proyecto1.agregaEmpleado(my_programador2)


my_gerente_proyecto2.agregaEmpleado(my_programador3)
my_gerente_proyecto2.agregaEmpleado(my_programador4)

my_programador1.agregaEmpleado(my_programador2)

my_programador1.function()
my_gerente_proyecto1.function()
my_gerente.function()

my_gerente.printEmpleados()