'''EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.
DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.'''

# Superclase: una superclase es una clase de la que se heredan otras clases.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self): # Método que se hereda a las subclases
        pass # Este método se define en las subclases. Pass es una palabra clave que no hace nada.

# Subclases: una subclase es una clase que hereda de una superclase.
class Dog(Animal):
    def sonido(self):
        print('Guau')

class Cat(Animal):
    def sonido(self):
        print('Miau')

def sonido_animal(animal: Animal): 
    animal.sonido() # Llama al método sonido de la clase animal

mi_animal = Animal('Animal')
sonido_animal(mi_animal)
mi_perro = Dog('Perro')
sonido_animal(mi_perro)
mi_gato = Cat('Gato')
sonido_animal(mi_gato)

# EXTRA
class Empleado:
    def __init__(self, id:int, nombre:str):
        self.id = id
        self.nombre = nombre
        self.employees=[]
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def print_employees(self):
        for employee in self.employees:
            print(employee.nombre)

class Gerente(Empleado):
    def coordinate_projects(self):
        print(f"{self.nombre} está coordinando todos los proyectos de la empresa.")

class GerenteProyecto(Empleado):
    def __init__(self, id:int, nombre:str, project:str):
        super().__init__(id, nombre)
        self.project = project
    
    def coordinate_project(self):
        print(f"{self.nombre} está coordinando el proyecto {self.project}.")

class Programador(Empleado):
    def __init__(self, id:int, nombre:str, lenguaje:str):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje
    
    def code(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")
    
    def add(self, employee:Empleado):
        print(f"Un programador no tiene empleados a su cargo. {employee.nombre} no se añadirá.")

# Crear empleados
mi_gerente = Gerente(1, 'Santiago Bailleres')
mi_project_manager = GerenteProyecto(2, 'Juan Perez', 'Proyecto 1')
mi_project_manager2 = GerenteProyecto(3, 'Pedro Lopez', 'Proyecto 2')
mi_programador = Programador(4, 'Maria Garcia', 'Python')
mi_programador2 = Programador(5, 'Ana Martinez', 'Java')
mi_programador3 = Programador(6, 'Luis Ramirez', 'C++')
mi_programador4 = Programador(7, 'Carlos Sanchez', 'JavaScript')

mi_gerente.add_employee(mi_project_manager)
mi_gerente.add_employee(mi_project_manager2)

mi_project_manager.add_employee(mi_programador)
mi_project_manager.add_employee(mi_programador2)
mi_project_manager2.add_employee(mi_programador3)
mi_project_manager2.add_employee(mi_programador4)

mi_programador.add(mi_programador4)

mi_programador.code()
mi_project_manager.coordinate_project()
mi_gerente.coordinate_projects()
mi_gerente.print_employees()
mi_project_manager.print_employees()
mi_programador.print_employees()