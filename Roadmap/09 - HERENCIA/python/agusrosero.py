"""
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
"""

# EJERCICIO:


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print("zZzZ..")


class Perro(Animal):
    def sonido(self):
        print("Guau")


class Gato(Animal):
    def sonido(self):
        print("Miau")


animal = Animal("Buho")
animal.sonido()
perro = Perro("Perro")
perro.sonido()
gato = Gato("Gato")
gato.sonido()

# DIFICULTAD EXTRA:


class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def deber(self):
        print("Trabajo")


class Gerente(Empleado):
    def __init__(self, id, nombre, empleados):
        super().__init__(id, nombre)
        self.empleados = empleados

    def deber(self):
        print("Gerencia")


class GerenteDeProyecto(Gerente):
    def __init__(self, id, nombre, empleados):
        super().__init__(id, nombre, empleados)

    def deber(self):
        print("Proyecto")


class Programador(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def deber(self):
        print("Desarrollo")
        super().deber()


programador = Programador("1", "Agus")
programador.deber()
gerente = Gerente("2", "Hernan", ["1"])
gerente.deber()
gerente_proyecto = GerenteDeProyecto("3", "Hernan", ["1"])
gerente_proyecto.deber()
empleado = Empleado("4", "Hernan")
empleado.deber()
