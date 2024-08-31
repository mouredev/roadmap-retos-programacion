"""
 EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 
"""

class Animal:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def imprimirSonido(self):
        pass

class Perro(Animal):
    def imprimirSonido(self):
        print(f"soy {self.nombre} y hago GUAU")

class Gato(Animal):
    def imprimirSonido(self):
        print(f"soy {self.nombre} y hago MIAU")


#Ejemplo:
perro = Perro('ComoTu')
gato = Gato('Minino')
perro.imprimirSonido()
gato.imprimirSonido()


""" * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Empleado:
    def __init__(self, identificador:int, nombre:str):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados=[]
    def add_empleados(self,empleados):
        self.empleados.append(empleados)
    def imprimir_empleados(self):
        for empleado in self.empleados:
            print(f"{empleado.nombre} esta bajo ordenes de {self.nombre}")
    
class Gerente(Empleado):
    def supervision(self):
        print(f"{self.nombre} esta supervisando")

class GerenteProyecto(Empleado):
    def __init__(self, identificador:int, nombre:str, proyecto:str):
        super().__init__(identificador, nombre)
        self.proyecto = proyecto
    def coordinar_proyectos(self):
        print(f"{self.nombre} esta coordinado su proyecto {self.proyecto}")

class Programador(Empleado):
    def __init__(self, identificador:int, nombre:str, lenguaje:str, proyecto:str):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje
        self.proyecto = proyecto
    def programar(self):
        print(f"{self.nombre} esta programando el proyecto {self.proyecto} en {self.lenguaje}")
    def add(self, empleado: Empleado):
        print(
            f"Un programador no tiene empleados a su cargo. {empleado.name} no se añadirá.")

gerente=Gerente(0, "Thony")
gerente_de_proyectos=GerenteProyecto(1, "Juan", "Proyecto A")
gerente_de_proyectos2=GerenteProyecto(2, "Pedro", "Proyecto B")
programador1=Programador(3, "Carlos", "Python", "Proyecto A")
programador2=Programador(4, "Luis", "Java", "Proyecto A")
programador3=Programador(5, "Maria", "C++", "Proyecto B")
gerente.add_empleados(gerente_de_proyectos)
gerente.add_empleados(gerente_de_proyectos2)
gerente_de_proyectos.add_empleados(programador1)
gerente_de_proyectos.add_empleados(programador2)
gerente_de_proyectos2.add_empleados(programador3)
gerente.imprimir_empleados()
gerente_de_proyectos.imprimir_empleados()
gerente_de_proyectos2.imprimir_empleados()
programador1.imprimir_empleados()
programador2.imprimir_empleados()
programador3.imprimir_empleados()
gerente_de_proyectos.coordinar_proyectos()
gerente_de_proyectos2.coordinar_proyectos()
programador1.programar()
programador2.programar()
programador3.programar()