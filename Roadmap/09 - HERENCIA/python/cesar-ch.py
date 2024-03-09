"""
    #09 HERENCIA Y POLIMORFISMO
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Guau, guau!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Miau, miau!")


dog = Dog("Fido")
dog.sound()
cat = Cat("Garfield")
cat.sound()

"""
    DIFICULTAD EXTRA 
"""


class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def imprimir_empleados(self):
        print([empleado.nombre for empleado in self.empleados_a_cargo])


class Gerente(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def actividad(self):
        print("Gerente")


class GerenteProyecto(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def actividad(self):
        print("Gerente de Proyecto")


class Programador(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def actividad(self):
        print("Programador")


gerente = Gerente(1, "Juan")
gerente_proyecto = GerenteProyecto(2, "Pedro")
gerente_proyecto2 = GerenteProyecto(3, "Luis")
programador = Programador(4, "Maria")
programador2 = Programador(5, "Ana")
programador3 = Programador(6, "Jorge")
programador4 = Programador(7, "Carlos")

gerente.agregar_empleado(gerente_proyecto)
gerente.agregar_empleado(gerente_proyecto2)

gerente_proyecto.agregar_empleado(programador)
gerente_proyecto.agregar_empleado(programador2)
gerente_proyecto2.agregar_empleado(programador3)
gerente_proyecto2.agregar_empleado(programador4)

gerente.imprimir_empleados()
gerente_proyecto.imprimir_empleados()
gerente_proyecto2.imprimir_empleados()
programador.imprimir_empleados()

gerente.actividad()
gerente_proyecto.actividad()
programador.actividad()
