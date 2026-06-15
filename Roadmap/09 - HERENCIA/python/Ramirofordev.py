# Crea una superclase animal y un par de subclases Perro y Gato

class Animal:
    def __init__(self, nombre, patas, size, edad):
        self.nombre = nombre
        self.patas = patas
        self.size = size
        self.edad = edad


class Dog(Animal):
    def sound(self):
        print("Guau!")
    

class Cat(Animal):
    def sound(self):
        print("Miaw!")

mi_perro = Dog(nombre = "Firulais", patas = 4, size = "Mediano", edad = 3)
mi_gato = Cat(nombre = "Cartoon", patas = 4, size = "Mediano", edad = 8)

mi_perro.sound()
mi_gato.sound()

# Ejercicio extra

class Trabajador:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.empleados = []
        self.programadores = []


class Manager(Trabajador):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.empleados = []

    def add_empleado(self, empleado):
        self.empleados.append(empleado)

    def coordinate_projects(self):
        print(f"{self.nombre} esta coordinando todos los proyectos")

class ProjectManager(Trabajador):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.programadores = []

    def add_programador(self, programador):
        self.programadores.append(programador)

    def coordinate_project(self):
        print(f"{self.nombre} esta coordinado este proyecto")
    

class Programador(Trabajador):
    def __init__(self, id, nombre, language):
        super().__init__(id, nombre)
        self.language = language

    def code(self):
        print(f"{self.name} esta programando en {self.language}")

paco = Manager("Paco", 12354)
nacho = Programador(4456, "Nacho", "Python")
paco.add_empleado(nacho)