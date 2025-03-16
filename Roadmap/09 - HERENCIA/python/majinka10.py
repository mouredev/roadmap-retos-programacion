from typing import Any


class Animal():
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def emitirSonido(self):
        print(f"Hola, soy {self.nombre} y hago algún sonido")

class Perro(Animal):
    def  emitirSonido(self):
        print(f"Hola, soy {self.nombre} y hago Guau!")

class Gato(Animal):
    def  emitirSonido(self):
        print(f"Hola, soy {self.nombre} y hago Miau!")

mi_perro = Perro("Tony")
mi_perro.emitirSonido()

mi_gato = Gato("Tom")
mi_gato.emitirSonido()

# Ejercicio EXTRA

print("\nEjercicio con la jerarquía de una empresa de desarrollo.\n")

class Empleado():
    def __init__(self, nombre: str, ID: str, listaEmpleados: list = None) -> None:
        self.nombre = nombre
        self.ID = ID
        self.listaEmpleados = listaEmpleados

    def funcion(self):
        print(f"Hola, soy {self.nombre} con ID {self.ID} y trabajo en esta empresa.")

    def añadirEmpleadoACargo(self, empleado):
        self.listaEmpleados.append(empleado)

    def empleadosACargo(self):
        print(f"Los empleados a cargo de {self.nombre} son:")
        for empleado in self.listaEmpleados:
            print(empleado.getNombre())
    
    def eleminarEmpleadoACargo(self, empleado):
        self.listaEmpleados.remove(empleado)
        print(f"Se ha eliminado al empleado {empleado.getNombre()} de los empleados a cargo de {self.nombre}")

    def getNombre(self) -> str:
        return self.nombre

class Gerente(Empleado):
    auto = "Mercedes Benz"
    def funcion(self):
        print(f"Hola, soy el gerente {self.nombre} con ID {self.ID}, tengo un {self.auto} y administro la empresa.")

class ProjectManager(Empleado):
    bici = "GW Roja"
    def funcion(self):
        print(f"Hola, soy el gerente de proyectos {self.nombre} con ID {self.ID}, tengo una {self.bici} y gestiono los proyectos de la empresa.")

class Programador(Empleado):
    patin = "Xiaomi Electric Scooter 4"
    def funcion(self):
        print(f"Hola, soy  el programador {self.nombre} con ID {self.ID}, tengo un {self.patin} y escribo código!")

empleado1 = ProjectManager("Juan", "102", [])
empleado2 = Gerente("Pedro", "101", [empleado1])
empleado3 = Programador("Jose", "103")
empleado4 = Programador("Maria", "105")

empleado2.funcion() # Mostrar que hace este empleado.
empleado2.añadirEmpleadoACargo(empleado4) # Añadir un empleado a sus empleados a cargo.
empleado2.empleadosACargo() # Mostrar los empleados a su cargo.
empleado1.añadirEmpleadoACargo(empleado3) # Añadir un empleado a sus empleados a cargo.
empleado1.funcion() # Mostrar qué hace este empleado.
empleado1.empleadosACargo() # Mostrar los empleados a su cargo.
empleado3.funcion() # Mostrar qué hace este empleado.
empleado2.eleminarEmpleadoACargo(empleado1) # Eliminar un empleado a su cargo.
empleado2.empleadosACargo() # Mostrar los empleados a su cargo.