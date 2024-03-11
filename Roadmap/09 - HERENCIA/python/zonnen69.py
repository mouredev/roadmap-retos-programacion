
# /*
#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.
#  */


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
    if isinstance(animal, Animal):
        print(f"{animal.nombre} hace {animal.hacer_sonido()}")
    else:
        print("Error: El objeto no es una instancia de Animal.")

# Ejemplo de uso
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")

imprimir_sonido(mi_perro)  # Salida: Buddy hace ¡Guau!
imprimir_sonido(mi_gato)   # Salida: Whiskers hace ¡Miau!


class Empleado:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.identificador})"


class Gerente(Empleado):
    def __init__(self, identificador, nombre, departamento):
        super().__init__(identificador, nombre)
        self.departamento = departamento
        self.empleados_a_cargo = []

    def asignar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def listar_empleados(self):
        print(f"Empleados a cargo de {self.nombre}:")
        for empleado in self.empleados_a_cargo:
            print(empleado)


class GerenteProyecto(Gerente):
    def __init__(self, identificador, nombre, departamento, proyecto):
        super().__init__(identificador, nombre, departamento)
        self.proyecto = proyecto

    def asignar_programador(self, programador):
        self.empleados_a_cargo.append(programador)


class Programador(Empleado):
    def __init__(self, identificador, nombre, lenguaje):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje


# Ejemplo de uso
if __name__ == "__main__":
    # Crear empleados
    empleado1 = Programador(1, "Juan", "Python")
    empleado2 = Programador(2, "Maria", "JavaScript")

    gerente_proyecto = GerenteProyecto(3, "Pedro", "Desarrollo", "Proyecto X")
    gerente_proyecto.asignar_empleado(empleado1)
    gerente_proyecto.asignar_empleado(empleado2)

    print("Empleados del gerente de proyecto:")
    gerente_proyecto.listar_empleados()
