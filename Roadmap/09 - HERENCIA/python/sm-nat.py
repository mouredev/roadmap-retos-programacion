class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        pass

#SUBCLASS

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"
    
# Creando instancias de las clases derivadas
perro = Perro("Firulais")
gato = Gato("Pepita")

print(f"{perro.nombre} dice {perro.sonido()}")
print(f"{gato.nombre} dice {gato.sonido()}")

#EXTRA
"""Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Empleado:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados_a_cargo = []

    def asignar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def mostrar_informacion(self):
        print(f"Identificador: {self.identificador}")
        print(f"Nombre: {self.nombre}")
        print("Empleados a cargo:")
        for empleado in self.empleados_a_cargo:
            print(f"- {empleado.nombre}")


class Gerente(Empleado):
    def __init__(self, identificador, nombre, departamento):
        Empleado.__init__(self, identificador, nombre)
        self.departamento = departamento

    def gestionar_equipo(self):
        print(f"El gerente {self.nombre} está gestionando el departamento {self.departamento}.")


class GerenteProyecto(Empleado):
    def __init__(self, identificador, nombre, proyecto):
        Empleado.__init__(self, identificador, nombre)
        self.proyecto = proyecto

    def supervisar_proyecto(self):
        print(f"El gerente de proyecto {self.nombre} está supervisando el proyecto {self.proyecto}.")


class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje):
        Empleado.__init__(self, identificador, nombre)
        self.lenguaje = lenguaje

    def desarrollar_codigo(self):
        print(f"El programador {self.nombre} está desarrollando código en {self.lenguaje}.")


if __name__ == "__main__":
    # Crear empleados
    juan = Gerente("G001", "Juan", "IT")
    maria = GerenteProyecto("GP001", "Maria", "Sistema de Gestión")
    pedro = Programador("P001", "Pedro", "Python")

    # Asignar empleados a cargo
    juan.asignar_empleado(maria)
    juan.asignar_empleado(pedro)

    # Mostrar información de los empleados
    juan.mostrar_informacion()
    print("\n")
    maria.mostrar_informacion()
    print("\n")
    pedro.mostrar_informacion()
