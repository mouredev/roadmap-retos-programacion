#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.

class Animal:
    def __init__(self, name):
        self.name = name

    def sonido(self):
        return "Cada animal hace un sonido"
    

class Perro(Animal):
    def sonido(self):
        return 'Guau'
    
class Gato(Animal):
    def sonido(self):
        return 'Miau'
    
animales = [Perro('Tito'), Gato('Liro')]
for animal in animales:
    print(f'{animal.name} hace {animal.sonido()}')

print("/" * 50)
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.


class Empleado():
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def imprimir_empleados(self):
        for empleado in self.empleados:
            print(empleado.nombre)

    
class Gerentes(Empleado):    
    def coordinar_proyectos(self):
        print(f'{self.nombre} coordina todos los proyectos abiertos')


class GerenteProyectos(Empleado):
    def __init__(self, nombre, id, proyecto):
        super().__init__(nombre, id)
        self.proyecto = proyecto

    def coordinar_proyecto(self):
        print(f'{self.nombre} coodina los proyectos asignados')

class Programadores(Empleado):   
    def __init__(self, nombre, id, lenguaje):
        super().__init__(nombre, id)
        self.lenguaje = lenguaje

    def programar(self):
        print(f"{self.nombre} esta programando en {self.lenguaje}")

    def agregar_empleado(self, empleado: Empleado):
        print(f'Los programadores no tienen empleados a cargo, {empleado.nombre} no agregado')


# creamos los objetos de clases
manager = Gerentes("Tito", 1234)
proyect_manager = GerenteProyectos("Ana", 4567, 'Proyecto Granada')
proyect_manager2 = GerenteProyectos("Fefi", 4569, 'Proyecto Motril')
programador = Programadores('Alvaro', 9876, 'Python')
programador2 = Programadores('Pepe', 345, 'C++')
programador3 = Programadores('Juan', 544, 'Java')
programador4 = Programadores('Luis', 765, 'Swift')

# usamos el metodo de agregar a listados de cada objeto
manager.agregar_empleado(proyect_manager)
proyect_manager.agregar_empleado(programador)
proyect_manager.agregar_empleado(programador2)
proyect_manager2.agregar_empleado(programador3)
proyect_manager2.agregar_empleado(programador4)
programador.agregar_empleado(programador2)

# verificamos los demas metodos de subclases
manager.coordinar_proyectos()
proyect_manager.coordinar_proyecto()
proyect_manager2.coordinar_proyecto()
programador.programar()
programador2.programar()
programador3.programar()
programador4.programar()

# usamos el metodo de impresion de empleados
manager.imprimir_empleados()
proyect_manager.imprimir_empleados()
proyect_manager2.imprimir_empleados()
programador.agregar_empleado(programador2)
programador.imprimir_empleados() # los programadores no pueden tener empleados a cargo por lo tanto no printea nada