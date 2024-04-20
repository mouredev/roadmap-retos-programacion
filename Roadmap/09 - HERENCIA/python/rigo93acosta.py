'''
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
'''

class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def sonido(self):
        pass

# Subclases
class Perro(Animal):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)

    def sonido(self):
        return f"{self.nombre} Guau!"
    
class Gato(Animal):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)

    def sonido(self):
        return f"{self.nombre} Miau!"

floki = Gato("Floki")
animal = Animal("Animal")
dog = Perro("Dog")
print(floki.sonido())

# Empleo de Polimorfismo
def print_sonido(animal: Animal):
    print(animal.sonido())

print_sonido(floki)
print_sonido(dog)
print_sonido(animal)

'''
Ejercicio Extra
'''
class Empleado: 
    def __init__(self, nombre: str, id: int) -> None:
        self.nombre = nombre
        self.id = id
        self.empleados = []

    def contratar(self, empleado: 'Empleado'):
        self.empleados.append(empleado)
    
    def print_empleados(self):
        for empleado in self.empleados:
            print(empleado.nombre)

class Gerente(Empleado):
    def __init__(self, nombre: str, id: int) -> None:
        super().__init__(nombre, id)

    def coordinar_proyecto(self):
        print(f'{self.nombre} está coordinando todos los proyectos.')
    
class GerenteProyecto(Empleado):
    def __init__(self, nombre: str, id: int, proyecto: str) -> None:
        super().__init__(nombre, id)
        self.empleados = []
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f'{self.nombre} está coordinando el proyecto {self.proyecto}.')

class Programador(Empleado):
    def __init__(self, nombre: str, id: int, language: str) -> None:
        super().__init__(nombre, id)
        self.language = language

    def programar(self):
        print(f'{self.nombre} está programando en {self.language}.')

    def contratar(self, empleado: Empleado):
        print(f'No puedes contratar al empleado {empleado.nombre}, {self.nombre}.')

gerente = Gerente("Gerente", 1)
gerenteProyecto = GerenteProyecto("Gerente Proyecto", 2, 'Proyecto 1')
programador = Programador("Programador", 3, "Python")
programador2 = Programador("Programador 2", 4, "Java")

gerente.contratar(gerenteProyecto)
gerenteProyecto.contratar(programador)
programador.contratar(programador2)

gerente.print_empleados()
gerenteProyecto.print_empleados()

programador.programar()

