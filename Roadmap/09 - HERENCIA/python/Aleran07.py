#09

"""* EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal."""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "Este animal habla"
    
class Perro(Animal):
    def hablar(self):
        return "Guau"
    
class Gato(Animal):
    def hablar(self):
        return "Miau"
    
lista_animales = [Perro("Toby"), Gato("Michi")]

for x in lista_animales:
    print(x.nombre, "dice", x.hablar())


""" * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo."""

class Persona:
    def __init__(self, nombre, id):
        self.nombre = nombre
       
        self.id = id

    def presentarse(self):
        print(f"Buen dia, soy {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, id, cargo):
        super().__init__(nombre, id)
        self.cargo = cargo
        self.empleados_a_cargo = []
    
    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def mostrar_empleados(self):
        if not self.empleados_a_cargo:
            print(f"{self.nombre} no tiene empleados a su cargo.")
            return

        print(f"Empleados a cargo de {self.nombre}:")
        for emp in self.empleados_a_cargo:
            print(f" - {emp.nombre} ({emp.__class__.__name__})")

    def mostrar_empleo(self):
        print(f"{self.nombre} trabaja como {self.cargo}")
    
    def informacion(self):
        print(f"[{self.__class__.__name__}] ID: {self.id}, Nombre: {self.nombre}")

class Gerente(Empleado):
    def __init__(self, nombre, id, cargo):
        super().__init__(nombre, id, cargo)

    def supervisar(self):
        print(f"{self.nombre} esta supervisando")

    

class GerenteDeProyectos(Empleado):
    def __init__(self, nombre, id, cargo):
        super().__init__(nombre, id, cargo)

    def administrar(self):
        print(f"{self.nombre} esta administrando el proyecto")

    def informacion(self):
        super().informacion()
        print(f"Proyecto: {self.proyecto}")

class Programador(Empleado):
    def __init__(self, nombre, id, cargo):
        super().__init__(nombre, id, cargo)

    def programar(self):
        print(f"{self.nombre} esta programando")
    
    def informacion(self):
        super().informacion()
        print(f"Lenguaje principal: {self.lenguaje}")


# Crear empleados
g1 = Gerente("Sofía", 1, "Desarrollo")
gp1 = GerenteDeProyectos("Carlos", 2, "App Bancaria")
p1 = Programador("Laura", 3, "Python")
p2 = Programador("Diego", 4, "Java")

# Relacionar jerarquía
g1.agregar_empleado(gp1)
g1.agregar_empleado(p1)

gp1.agregar_empleado(p2)

# Mostrar información
g1.informacion()
g1.mostrar_empleados()

print("\n--- Acciones específicas ---")
g1.supervisar()
gp1.administrar()
p1.programar()
