# 09 HERENCIA Y POLIMORFISMO
# Monica Vaquerano
# https://monicavaquerano.dev


"""
EJERCICIO:
Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
implemente una superclase Animal y un par de subclases Perro y Gato,
junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
print("Herencia y polimorfismo\n")
# La herencia es un mecanismo que permite que una clase (llamada subclase o clase derivada) herede atributos y métodos de otra clase (llamada superclase o clase base).
# Esto permite la reutilización de código y la creación de una jerarquía de clases.


# Superclase
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  # Método abstracto, será implementado por las subclases

    def make_sound(self):
        print(f"{self.name}: {self.sound()}")

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


# Subclases
class Perro(Animal):
    def sound(self):
        return "¡Guau!"


class Gato(Animal):
    def sound(self):
        return "¡Miau!"


print("Instancias de las sublases:")
# Crear instancias de las subclases
snoopy = Perro("Snoopy")
garfield = Gato("Garfield")

# Imprimir el sonido de cada animal
print(snoopy)
print(garfield)
snoopy.make_sound()
garfield.make_sound()


"""
DIFICULTAD EXTRA (opcional):
Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
pueden ser Gerentes, Gerentes de Proyectos o Programadores.
Cada empleado tiene un identificador y un nombre.
Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
actividad, y almacenan los empleados a su cargo.
"""
print("\nDIFICULTAD EXTRA (opcional):")


class Empleado:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def actividades(self):
        pass

    def imprimir_informacion(self):
        print(
            f"--- {self.__class__.__name__} ---\nid: {self.id}\nnombre: {self.nombre}"
        )

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} - ID: {self.id}"


class Gerente(Empleado):
    def __init__(self, id, nombre, departamento):
        super().__init__(id, nombre)
        self.departamento = departamento
        self.empleados_a_cargo = []

    def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

    def actividades(self):
        return f"Gestionar el departamento de {self.departamento}"

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"departamento: {self.departamento}\nactividades: {self.actividades()}")

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"


class GerenteProyecto(Gerente):
    def __init__(self, id, nombre, departamento, proyectos_asignados):
        super().__init__(id, nombre, departamento)
        self.proyectos_asignados = proyectos_asignados

    def actividades(self):
        return f"Gestionar los proyectos: {', '.join(self.proyectos_asignados)} del departamento de {self.departamento}"

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"proyectos asignados: {', '.join(self.proyectos_asignados)}")

    def __str__(self):
        return (
            super().__str__()
            + f", Proyectos asignados: {', '.join(self.proyectos_asignados)}"
        )


class Programador(Empleado):
    def __init__(self, id, nombre, lenguajes):
        super().__init__(id, nombre)
        self.lenguajes = lenguajes

    def actividades(self):
        return f"Programar aplicaciones en: {', '.join(self.lenguajes)}"

    def imprimir_informacion(self):
        super().imprimir_informacion()
        print(f"lenguajes: {', '.join(self.lenguajes)}")

    def __str__(self):
        return super().__str__() + f", Lenguajes: {', '.join(self.lenguajes)}"


alice = Gerente(1, "Alice", "Ventas")
bob = GerenteProyecto(2, "Bob", "Ventas", ["Proyecto 1", "Proyecto 2", "Proyecto 3"])
charlie = Programador(3, "Charlie", ["Python", "JavaScript"])

alice.imprimir_informacion()
bob.imprimir_informacion()
charlie.imprimir_informacion()

alice.agregar_empleado(bob)
alice.agregar_empleado(charlie)

print(f"\n{alice.nombre} tiene a cargo los siguientes empleados:")
for empleado in alice.empleados_a_cargo:
    print("\t", empleado)
