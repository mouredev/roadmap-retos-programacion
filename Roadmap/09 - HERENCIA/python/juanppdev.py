"""
EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
#  la herencia es un concepto fundamental en la programación orientada a objetos. Permite que una clase (subclase) herede atributos y métodos de otra clase (superclase).

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

def imprimir_sonido(animal):
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

# Ejemplo de uso
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")

imprimir_sonido(mi_perro)  # Salida: Buddy dice: ¡Guau!
imprimir_sonido(mi_gato)   # Salida: Whiskers dice: ¡Miau!


"""
DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Empleado:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def trabajar(self):
        pass

class Gerente(Empleado):
    def __init__(self, identificador, nombre, departamento):
        super().__init__(identificador, nombre)
        self.departamento = departamento
        self.empleados_a_cargo = []

    def asignar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def trabajar(self):
        print(f"{self.nombre} está supervisando el departamento {self.departamento}")

class GerenteProyecto(Gerente):
    def __init__(self, identificador, nombre, departamento, proyecto):
        super().__init__(identificador, nombre, departamento)
        self.proyecto = proyecto

    def trabajar(self):
        print(f"{self.nombre} está supervisando el proyecto {self.proyecto}")

class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje

    def codificar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}")

# Ejemplo de uso
gerente1 = Gerente(1, "Juan", "Desarrollo")
gerente2 = GerenteProyecto(2, "Maria", "Desarrollo", "Sistema de Gestión")
programador1 = Programador(3, "Pedro", "Python")
programador2 = Programador(4, "Ana", "JavaScript")

gerente1.asignar_empleado(programador1)
gerente1.asignar_empleado(programador2)

gerente1.trabajar()
for empleado in gerente1.empleados_a_cargo:
    empleado.trabajar()
