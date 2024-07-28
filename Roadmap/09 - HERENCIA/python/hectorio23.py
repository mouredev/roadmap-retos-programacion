# Autor: Héctor Adán 
# GitHub: https://github.com/hectorio23

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


# Clase base Animal
class Animal:
    def __init__(self, nombre, alimentacion, habitad_natural, edad):
        self.nombre = nombre
        self.alimentacion = alimentacion
        self.habitad_natural = habitad_natural
        self.edad = edad

    # Método para hacer sonido del animal
    def hacer_sonido(self):
        print("Sonido de la clase Animal")

    # Método para mostrar los detalles del animal
    def get_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Alimentación: {self.alimentacion}")
        print(f"Hábitat: {self.habitad_natural}")
        print(f"Edad: {self.edad}")

# Clase derivada Perro
class Perro(Animal):
    def __init__(self, nombre, alimentacion, habitad_natural, edad):
        super().__init__(nombre, alimentacion, habitad_natural, edad)

    # Método para hacer sonido del perro
    def hacer_sonido(self):
        print("¡Woow Woow!")

# Clase derivada Gato
class Gato(Animal):
    def __init__(self, nombre, alimentacion, habitad_natural, edad):
        super().__init__(nombre, alimentacion, habitad_natural, edad)

    # Método para hacer sonido del gato
    def hacer_sonido(self):
        print("¡Miauu Miauu!")

# Clase base Empleado
class Empleado:
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.identificador = identificador

    # Método para mostrar detalles del empleado
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, ID: {self.identificador}")

# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, identificador):
        super().__init__(nombre, identificador)
        self.empleados_a_cargo = []

    # Método para asignar empleado a cargo
    def asignar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    # Método para mostrar detalles del gerente y empleados a cargo
    def mostrar_detalles(self):
        print(f"Gerente - Nombre: {self.nombre}, ID: {self.identificador}")
        print("Empleados a cargo:")
        for empleado in self.empleados_a_cargo:
            empleado.mostrar_detalles()

# Clase derivada GerenteProyecto
class GerenteProyecto(Gerente):
    def __init__(self, nombre, identificador):
        super().__init__(nombre, identificador)

    # Método para mostrar detalles del gerente de proyecto
    def mostrar_detalles(self):
        print(f"Gerente de Proyecto - Nombre: {self.nombre}, ID: {self.identificador}")
        print("Empleados a cargo:")
        for empleado in self.empleados_a_cargo:
            empleado.mostrar_detalles()

# Clase derivada Programador
class Programador(Empleado):
    def __init__(self, nombre, identificador):
        super().__init__(nombre, identificador)

    # Método para mostrar detalles del programador
    def mostrar_detalles(self):
        print(f"Programador - Nombre: {self.nombre}, ID: {self.identificador}")

# Programa principal
if __name__ == "__main__":
    # Creación de un gato
    print("Instancia de la clase GATO:")
    g1 = Gato("Musides", "Omnívoro", "Hogar", 1)
    g1.hacer_sonido()  # Emite el sonido del gato
    g1.get_info()  # Muestra los detalles del gato

    print("------------------------------------")

    # Creación de un perro
    print("Instancia de la clase PERRO:")
    p1 = Perro("Rufus", "Carnívoro", "Hogar", 2)
    p1.hacer_sonido()  # Emite el sonido del perro
    p1.get_info()  # Muestra los detalles del perro

    print("\n\n**********************************\n\n")

    # Ejercicio Extra: Creación de empleados y un gerente de proyecto
    gerente_proyecto = GerenteProyecto("Juan", 1001)
    programador1 = Programador("Pedro", 2001)
    programador2 = Programador("Maria", 2002)

    # Asignación de empleados al gerente de proyecto
    gerente_proyecto.asignar_empleado(programador1)
    gerente_proyecto.asignar_empleado(programador2)

    # Mostrar detalles del gerente de proyecto y empleados a su cargo
    gerente_proyecto.mostrar_detalles()
