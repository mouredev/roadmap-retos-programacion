""" /*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */ """

# EJERCICIO

class animal():
    def __init__(self, name):
        self.name = name

class dog(animal):
    
    def sound(self):
        print("Guau")

class cat(animal):

    def sound(self):
        print("Miau")

def print_sound(animal: animal):
    animal.sound()

my_dog = dog("Perro")
my_dog.sound()
my_cat = cat("Gato")
my_cat.sound()
print_sound(my_dog)
print_sound(my_cat)


#DIFICULTAD EXTRA

class empleados:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.empleado = []

    def añadir(self, empleados):
        self.empleado.append(empleados)
        
class gerente(empleados):

    def funcion(self):
        print(f"{self.name} está a cargo de todos los proyectos de la empresa.")

class gerente_proyecto(empleados):

    def __init__(self, id, name, proyecto):
        super().__init__(id, name)
        self.proyecto = proyecto

    def funcion(self):
        print(f"{self.name} está a cargo del proyecto {self.proyecto}.")

class programador(empleados):

    def __init__(self, id, name, lenguaje):
        super().__init__(id, name)
        self.lenguaje = lenguaje

    def codigo(self):
        print(f"{self.name} está programando en {self.lenguaje}")

mi_gerente = gerente(1, "David")
mi_gerente_proyecto = gerente_proyecto(2, "Miguel", "X")
mi_gerente_proyecto2 = gerente_proyecto(3, "Juan", "Y")
mi_programador = programador(4, "Marcos", "Python")
mi_programador2 = programador(5, "Yae", "JS")
mi_programador3 = programador(6, "Pedro", "Angular")
mi_programador4 = programador(7, "José", "React")

mi_gerente.añadir(mi_gerente_proyecto)
mi_gerente.añadir(mi_gerente_proyecto2)
mi_gerente_proyecto.añadir(mi_programador)
mi_gerente_proyecto.añadir(mi_programador2)
mi_gerente_proyecto2.añadir(mi_programador3)
mi_gerente_proyecto2.añadir(mi_programador4)

mi_gerente.funcion()
mi_gerente_proyecto.funcion()
mi_gerente_proyecto2.funcion()
mi_programador.codigo()
mi_programador2.codigo()
mi_programador3.codigo()
mi_programador4.codigo()