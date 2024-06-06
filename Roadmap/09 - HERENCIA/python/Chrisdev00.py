"""
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


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido (self):
        pass

class Perro (Animal):
    def sonido(self):
        return "Guauu"
    
class Gato (Animal):
    def sonido(self):
        return "Miauu"
    
mi_perro = Perro("Rufo")
mi_gato = Gato("Bigotes")

print(mi_perro.nombre)
print(mi_perro.sonido())

print(mi_gato.nombre)
print(mi_gato.sonido())


########  ---------------------- EXTRA -------------------------------  ##########


class Empleado:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre}"


class Gerente(Empleado):
    def __init__(self, identificador, nombre, departamento):
        super().__init__(identificador, nombre)
        self.departamento = departamento

    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Departamento: {self.departamento}"


class GerenteProyecto(Gerente):
    def __init__(self, identificador, nombre, departamento, proyectos):
        super().__init__(identificador, nombre, departamento)
        self.proyectos = proyectos

    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Departamento: {self.departamento}, Proyectos: {self.proyectos}"


class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje

    def __str__(self):
        return f"ID: {self.identificador}, Nombre: {self.nombre}, Lenguaje: {self.lenguaje}"


gerente_proyecto = GerenteProyecto(1, "Juan", "Desarrollo", ["Proyecto A", "Proyecto B"])
programador = Programador(2, "Pedro", "Python")

print(gerente_proyecto)
print(programador)


    