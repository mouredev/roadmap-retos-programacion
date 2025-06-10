""" EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal."""

class Animal:
    def __init__(self, especie: str):
        self.especie = especie

    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        print(f"{self.especie}: Ladra")


class Gato(Animal):
    def sonido(self):
        print(f"{self.especie}: Maulla")

def print_sonido(animal: Animal):
    animal.sonido()

my_animal = Animal(":c")
my_perro = Perro("Perro")
print_sonido(my_perro)

my_gato = Gato("Gato")
print_sonido(my_gato)


""" DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cadaepleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo. """

class Empleados:
    def __init__(self, id: int, nombre: str) :
        self.nombre = nombre
        self.id = id
        self.empleados = []

    def responsabilidades(self):
        pass

    def add(self, empleado):
        self.empleados.append(empleado)
    
    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.nombre)


class Gerente(Empleados):
    def responsabilidades(self):
        print(f"{self.nombre} Esta a cargo del Departemento de Desarrollo")


class Manager(Empleados):
    def responsabilidades(self):
        print(f"{self.nombre} Lidera al equipo")


class Programador(Empleados):

    def __init__(self, id: int, nombre: str, language: str):
        super().__init__(id, nombre)
        self.language = language

    def responsabilidades(self):
        print(f"{self.nombre} Esta encargado de Programar en {self.language}")


def responsablidad(empleado: Empleados):
    empleado.responsabilidades()


gerenteTI = Gerente(1, "José Figueroa")
responsablidad(gerenteTI)

managerTI = Manager(121, "Pepito Alvarez")
responsablidad(managerTI)

programador = Programador(131, "Menganito Rodriguez", "Python")
responsablidad(programador)


managerTI.add(programador)
managerTI.print_empleados()

programador.add(managerTI)
programador.print_empleados()