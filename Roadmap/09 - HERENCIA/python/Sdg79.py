
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")

mi_perro = Perro("Mora")
mi_perro.sonido()
mi_gato = Gato("Moña")
mi_gato.sonido()
        

#DIFICULTAD EXTRA:

class Empleados:
    def __init__(self, ID: int, nombre: str):
        self.ID = ID
        self.nombre = nombre
        self.a_cargo = []
    def agregar(self, empleado):
        self.a_cargo.append(empleado)

    def imprimir_empleados(self):
        for empleado in self.a_cargo:
            print(empleado.nombre)
    
class Gerentes(Empleados):
    def funciones_G(self):
        print("Funciones y tareas del Gerente")

class Gerentes_de_Proyectos(Empleados):
    def __init__(self, ID: int, nombre: str, proyecto: str):
        super().__init__(ID, nombre)
        self.proyecto = proyecto

    def funciones_GP(self):    
        print("Funciones y tareas del Gerente de Proyectos")

class Programadores(Empleados):
    def __init__(self, ID: int, nombre: str, lenguaje: str):
        super().__init__(ID, nombre)
        self.lenguaje = lenguaje
    
    def codificar(self):
        print("Funciones y tareas del Programador")

gerente = Gerentes(1, "Sergio")
gerenteP1 = Gerentes_de_Proyectos(2, "Laura", "Proyecto1")
gerenteP2 = Gerentes_de_Proyectos(3, "Vicky", "Proyecto2")
programador1 = Programadores(4, "Damian", "Python")
programador2 = Programadores(5, "María", "C++")
programador3 = Programadores(6, "Micaela", "VisualBasic")
programador4 = Programadores(7, "Sol", "Cobol")

gerente.agregar(gerenteP1)
gerente.agregar(gerenteP2)

gerenteP1.agregar(programador1)
gerenteP1.agregar(programador2)
gerenteP2.agregar(programador3)
gerenteP2.agregar(programador4)

gerente.funciones_G()
gerenteP1.funciones_GP()
gerenteP2.funciones_GP()
programador1.codificar()

gerente.imprimir_empleados()
gerenteP1.imprimir_empleados()
gerenteP2.imprimir_empleados()

