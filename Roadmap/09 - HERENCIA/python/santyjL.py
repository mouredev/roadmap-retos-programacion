#09 - HERENCIA

"""
/*
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
 */
"""

class Animal:
    def __init__(self ,nombre) -> None:
        self.nombre = nombre

    def sonido (self) -> str:
        pass


class Perro(Animal):
    def __init__(self , nombre):
        super().__init__(nombre)

        self.nombre = nombre

    def sonido(self, sonido):
        print(f"el perro {self.nombre} hace {sonido}")


class Gato(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

        self.nombre = nombre

    def sonido(self, sonido: str) -> str:
        print(f"El gato {self.nombre} hace {sonido}")


perro = Perro("Gaston")
perro.sonido("guau")
gato = Gato("Cachito")
gato.sonido("miau")

###Extra###
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def deber(self):
        pass

    def sueldo(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}, Edad: {self.edad}"


class Gerente(Empleado):
    def __init__(self, nombre, edad, empleados, salario):
        super().__init__(nombre, edad)
        self.empleados = empleados
        self.salario = salario

    def deber(self):
        print(f"El gerente tiene el deber de manejar, controlar y planificar el trabajo de sus empleados que son: {', '.join(self.empleados)}")

    def sueldo(self):
        print(f"El gerente tiene un sueldo de {self.salario}$.")


class GerenteDeProyecto(Empleado):
    def __init__(self, nombre, edad, proyectos):
        super().__init__(nombre, edad)
        self.proyectos = proyectos

    def deber(self):
        print(f"El Gerente de Proyecto tiene el deber de supervisar y coordinar proyectos como: {', '.join(self.proyectos)}")

    def sueldo(self):
        print("El sueldo del Gerente de Proyecto depende del éxito de los proyectos.")


class Programador(Empleado):
    def __init__(self, nombre, edad, lenguajes):
        super().__init__(nombre, edad)
        self.lenguajes = lenguajes

    def deber(self):
        print(f"El Programador tiene el deber de desarrollar software utilizando los siguientes lenguajes: {', '.join(self.lenguajes)}")

    def sueldo(self):
        print("El sueldo del Programador se basa en su experiencia y habilidades técnicas.")


# Llamadas en el código principal

gerente = Gerente("Julian", 38, ["Fernando", "Cesar"], 6000)
print(gerente)
gerente.deber()
gerente.sueldo()

gerente_proyecto = GerenteDeProyecto("Ana", 32, ["Proyecto A", "Proyecto B"])
print(gerente_proyecto)
gerente_proyecto.deber()
gerente_proyecto.sueldo()

programador = Programador("Carlos", 25, ["Python", "JavaScript"])
print(programador)
programador.deber()
programador.sueldo()