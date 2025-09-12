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

""" Ejemplo de herencia """


class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def sonido(self):
        print("Un sonido desconocido ...")


class Perro(Animal):

    def sonido(self):
        print("Guau! Guau! ...")


class Gato(Animal):

    def sonido(self):
        print("Miau! Miauuu! ...")


""" Polimorfismo  """

animal_generico = Animal("????")
perro = Perro("Toby")
gato = Gato("Dorito")


def sonido_animal(animal: Animal):
    animal.sonido()


# sonido_animal(animal_generico)
# sonido_animal(perro)
# sonido_animal(gato)

""" * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */ """


class Empleado:

    def __init__(self, name: str, id: int) -> None:
        self.id = id
        self.name = name
        self.empleados_a_cargo: list[Empleado] = []

    def agregar(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def empleados(self):
        for e in self.empleados_a_cargo:
            print(f"{self.name} esta a cargo de {e.name}")


class Gerente(Empleado):

    def coordinar_projectos(self):
        print(f"{self.name} esta coordinando projectos de generales de empresa ...")


class Programador(Empleado):

    def __init__(self, name: str, id: int, lenguaje: str) -> None:
        super().__init__(name, id)
        self.lenguaje = lenguaje

    def codear(self):
        print(f"{self.name} esta codeando en {self.lenguaje}")

    def agregar(self, empleado: Empleado):
        print(f"No se puede agregar {empleado.name} a cargo de {self.name} ...")


class GereteProyecto(Empleado):

    def __init__(self, name: str, id: int, proyecto: str) -> None:
        super().__init__(name, id)
        self.proyecto = proyecto

    def coordinar_projectos(self):
        print(f"{self.name} esta coordinando el proyecto {self.proyecto} ...")


gerente = Gerente("Manuel", 1)
gerente_proyecto1 = GereteProyecto("Jose", 2, "Proyecto1")
gerente_proyecto2 = GereteProyecto("Maria", 3, "Proyecto2")
programador1 = Programador("Lucas", 4, "Python")
programador2 = Programador("David", 5, "Kobol")
programador3 = Programador("Sofia", 6, "Dart")
programador4 = Programador("Rosa", 7, "Java")
programador5 = Programador("Pedro", 8, "Ruby")

gerente.agregar(gerente_proyecto1)
gerente.agregar(gerente_proyecto2)
gerente_proyecto1.agregar(programador1)
gerente_proyecto1.agregar(programador2)
gerente_proyecto1.agregar(programador3)
gerente_proyecto2.agregar(programador4)
gerente_proyecto2.agregar(programador5)

programador1.agregar(programador2)

gerente.empleados()
gerente_proyecto1.empleados()
gerente_proyecto2.empleados()
