"""
Herencia y polimorfismo
"""

class Animal:
    
    def __init__(self, name):
        self.name = name
        self.sound = "desconocido"
    
    def call_sound(self):
        print(f"El sonido que hace {self.name} es: {self.sound}")

class Perro(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "guau guau"

class Gato(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "miau miau"

def print_sound(animal: Animal):
    animal.call_sound()


my_animal = Animal("pepe")
my_perro = Perro("Doggie")
my_perro.call_sound()
my_gato = Gato("Michael")
my_gato.call_sound()

print_sound(my_animal)
print_sound(my_perro)
print_sound(my_gato)




"""
Ejercicio Extra
"""

class Empleado:
    def __init__(self, identificador, name: str):
        self.id = identificador
        self.name = name
        self.empleados = []

    def agregar(self, empleado):
        self.empleados.append(empleado)

    def print_empleados(self):
        if len(self.empleados) > 0:
            print(f"{self.name} esta acargo de los siguientes empleados: ")
            for empleados in self.empleados:
                print(empleados.name)
        else:
            print(f"{self.name} no tiene empleados a su cargo")


class Gerentes(Empleado):
    
    def coordinar_proyectos(self):
        print(f"{self.name} está coordinando todos los proyectos de la empresa")
    
    


class GerentesDeProyectos(Empleado):

    def __init__(self, identificador, name: str, proyecto: str):
        super().__init__(identificador, name)
        self.proyecto = proyecto
    
    def coordinar_proyecto(self):
        print(f"{self.name} está coordinando el siguiente proyecto: {self.proyecto}")


class Programadores(Empleado):

    def __init__(self, identificador, name: str, language: str):
        super().__init__(identificador, name)
        self.language = language
    
    def programar(self):
        print(f"{self.name} esta programando en {self.language}")

    def agregar(self, empleado: Empleado):
        print(f"Un programador no tiene empleados a su cargo. {empleado.name} no se añadirá")


my_manager = Gerentes(1, "Gordo-Master")
my_proyect_manager = GerentesDeProyectos(2, "Gordo", "Proyecto 1")
my_proyect_manager2 = GerentesDeProyectos(3, "Master", "Proyecto 2")
my_programer = Programadores(4, "Franco", "C++")
my_programer2 = Programadores(5, "José", "JavaScript")
my_programer3 = Programadores(6, "Luis", "Python")
my_programer4 = Programadores(7, "Alberto", "Java")

my_manager.agregar(my_proyect_manager)
my_manager.agregar(my_proyect_manager2)
my_proyect_manager.agregar(my_programer)
my_proyect_manager.agregar(my_programer2)
my_proyect_manager2.agregar(my_programer3)
my_proyect_manager2.agregar(my_programer4)

my_programer.agregar(my_programer2)

# my_programer.programar()
my_programer2.programar()
# my_programer3.programar()
# my_programer4.programar()

# my_proyect_manager.coordinar_proyecto()
my_proyect_manager2.coordinar_proyecto()

my_manager.coordinar_proyectos()

my_manager.print_empleados()
my_proyect_manager.print_empleados()
my_programer4.print_empleados()