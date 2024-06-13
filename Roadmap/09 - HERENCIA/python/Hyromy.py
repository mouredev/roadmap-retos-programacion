# clase padre
class Animal:

    # contructor de la clase padre
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    # metodos comunes

    def mostrar(self):
        print(f"Soy un {self.nombre} {self.tamaño}")

    def comer(self):
        print(f"{self.nombre} está comiendo")

# clase perro que hereda de animal
class Perro(Animal):

    # constructor para la clase perro (similar al constructor de la clase padre)
    def __init__(self, nombre, tamaño, raza):
        super().__init__(nombre, tamaño) # super hace referencia al padre o a la super clase
        self.raza = raza # atributo de la clase perro

    # metodos propios

    def sonido(self):
        print("Guau!")

    def mostrar_raza(self):
        print(f"Soy un {self.raza}")

# clase gato que hereda de animal (diferente a perro)
class Gato(Animal):

    # constructor para la clase gato (similar al constructor de la clase padre )
    def __init__(self, nombre, tamaño, pelaje):
        super().__init__(nombre, tamaño) # heredando las mismas propiedades de animal
        self.pelaje = pelaje # atributo propio de la clase gato

    def sonido(self):
        print("Miau")

    def tocar_pelaje(self):
        print(f"{self.nombre} tiene un pelaje {self.pelaje}")

# instanciar objetos de cada clase
freddy = Animal("oso", "grande")
firulais = Perro("Firulais", "mediano", "Shiba Inu")
michi = Gato("micchi", "pequeño", "suave")

# metodo mostrar
freddy.mostrar()
firulais.mostrar()
michi.mostrar()

# metodo comer
freddy.comer()
firulais.comer()
michi.comer()

# metodo sonido
#freddy.sonido() # Animal no puede porque no esta definido el metodo sonido
firulais.sonido() # Perro.sonido() => Guau
michi.sonido() # Gato.sonido() => Miau

# metodo mostrar_raza
firulais.mostrar_raza() # Animal y Gato no poseen dicho metodo

# metetodo tocar_pelaje
michi.tocar_pelaje() # Animal y Perro no poseen dicho metodo

"""
 ---- DIFICULTAD EXTRA ----
"""

from abc import ABC, abstractmethod

class Empleado(ABC): # clase abstracta
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    # metodo comun
    def presentarse(self):
        print(f"Me llamo {self.nombre}, tengo {self.edad}. Mi matricula es {self.matricula}")

    # metodo abstracto
    @abstractmethod
    def trabajar(self):
        pass


class Programador(Empleado):
    def __init__(self, nombre, edad, matricula, lenguaje):
        super().__init__(nombre, edad, matricula)
        self.lenguaje = lenguaje

    def trabajar(self):
        print(f"{self.nombre} esta trabajando en {self.lenguaje}")

class Gerente(Empleado):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad, matricula)
        self.programadores = []

    def trabajar(self):
        if len(self.empleados_matricula) > 0:
            print(f"El gerente {self.nombre} esta trabajando con los programadores: {self.programadores}")
        else:
            print(f"El gerente {self.nombre} no tiene empleados a cargo")

    def agregar_programador(self, programador):
        self.programadores.append(programador)

    def quitar_programador(self, index = -1):
        if len(self.programadores) > 0:
            self.programadores.pop(index)
        else:
            print("No hay programadores por remover")

class Gerente_P(Empleado):
    def __init__(self, nombre, edad, matricula, proyecto):
        super().__init__(nombre, edad, matricula)
        self.proyecto = proyecto

    def trabajar(self):
        print(f"El gerente {self.nombre} está trabajando en el proyecto {self.proyecto}")

    def dormir(self):
        print(f"{self.nombre} se durmió xd")