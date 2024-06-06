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
 * actividad, y almacena los empleados a su cargo.
 */
"""


class Animal():

    def __init__(self) -> None:
        pass

class Perro(Animal):

    def __init__(self) -> None:
        super().__init__()

    def sonido(self):
        print("Guau!!!")

class Gato(Animal):

    def __init__(self) -> None:
        super().__init__()

    def sonido(self):
        print("Miau!!!")

print(Perro.__bases__)
print(Animal.__subclasses__())
mi_perro = Perro()
mi_perro.sonido()

"""
Extra
"""

class Empleados():

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.empleado = []

    def new_empleado(self, empleado):
        self.empleado.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleado:
            print (empleado.name)


    
class Gerente(Empleados):

    def coordinador(self):
        print(f"{self.name}, es el coordinador de proyectos.")


class Gerente_Proyectos(Empleados):

    def __init__(self, id: int, name: str, proyecto: str):
        super().__init__(id, name)
        self.proyecto = proyecto

    def coordinador_proyecto(self):
        print(f"{self.name}, esta coordinando este proyecto.")


class Programadores(Empleados):

    def __init__(self, id: int, name: str, lenguaje:str):
        super().__init__(id, name)
        self.lenguaje = lenguaje
        

    def programando(self):
        print(f"{self.name}, esta programando en {self.lenguaje}")

    def añadir(self, empleado:Empleados):
        print(f"Un programador no puede añadir nuevos empleados. {empleado.name} no se puede añadir. ")

    






empleado_1 = Empleados(1107,"Antonio")
print(empleado_1.id)
print(empleado_1.name)
empleado_2 = Gerente(1108,"Ezequiel")
empleado_2.coordinador()
empleado_3 = Gerente_Proyectos(1109,"Miguel","Thermo_1")
empleado_3.coordinador_proyecto()
empleado_4 = Programadores(1215, "Enrique","Python")
empleado_4.programando()