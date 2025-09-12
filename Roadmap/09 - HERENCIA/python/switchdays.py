"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""

# Superclase:
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

# Subclases:
class Perro(Animal):
    def sonido(self):
        print(f"El perro {self.nombre} hace guau")

class Gato(Animal):
    def sonido(self):
        print(f"El gato {self.nombre} hace miau")

perro = Perro("Toby")
gato = Gato("Michi")

perro.sonido()
gato.sonido()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Gerente(Empleado):
    def __init__(self, id, nombre, salario):
        super().__init__(id, nombre)
        self.salario = salario
        self.personas_a_cargo = []

    def empleados_a_cargo(self, empleado):
        self.personas_a_cargo.append(empleado)
        print(f"Empleados a cargo de {self.nombre}: {self.personas_a_cargo}")


    def actividad(self):
        print(f"El gerente {self.nombre}, con identificador {self.id}, gestiona el departamente correspondiente.")

class Gerente_de_proyectos(Empleado):
    def __init__(self, id, nombre, salario):
        super().__init__(id, nombre)
        self.salario = salario
        self.personas_a_cargo = []

    def empleados_a_cargo(self, empleado):
        self.personas_a_cargo.append(empleado)
        print(f"Empleados a cargo de {self.nombre}: {self.personas_a_cargo}")


    def actividad(self):
        print(f"El gerente de proyectos {self.nombre}, con identificador {self.id}, gestiona el departamente de proyectos.")

class Programador(Empleado):
    def __init__(self, id, nombre, salario):
        super().__init__(id, nombre)
        self.salario = salario
        self.personas_a_cargo = []

# El programador no tiene personas a su cargo.


    def actividad(self):
        print(f"El programador {self.nombre}, con identificador {self.id}, se encarga de desarrollar la web de la empresa.")

gerente = Gerente(12345, "Manoleke", 10000)
gerente.actividad()
gerente.empleados_a_cargo("Gustavo")

gerente_de_proyectos = Gerente_de_proyectos(98765, "Pakito", 20000)
gerente_de_proyectos.actividad()
gerente_de_proyectos.empleados_a_cargo("Patricio")

programador = Programador(34567, "Pepe", 30000)
programador.actividad()