# #09 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
# Definimos la superclase Animal
class Animal:
    def hacer_sonido(self):
        raise NotImplemented("Este método debe ser implementado por las subclases")

# Definimos la subclase Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "El perro dice: ¡Guau Guau!"

# Definimos la subclase Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "El gato dice: ¡Miau Miau!"

# Definimos la subclase Pájaro
class Pajaro(Animal):
    def hacer_sonido(self):
        return "El pájaro dice: ¡Pio Pio!"

# Función para imprimir el sonido de cualquier animal
def imprimir_sonido(animal):
    print(f"{animal.hacer_sonido()}")

# Crear instancias
perro = Perro()
gato = Gato()
pajaro = Pajaro()

imprimir_sonido(perro)
imprimir_sonido(gato)
imprimir_sonido(pajaro)



"""
EXTRA
"""
# Creando la superclase
class Employ:
    _contador_id = 1  # Contador de ID estático

    def __init__(self, nombre):
        self.id = Employ._contador_id
        Employ._contador_id += 1
        self.nombre = nombre

    def show_details(self):
        print(f"\nID: {self.id}, Nombre: {self.nombre}")

# Creando la clase Gerente
class Manager(Employ):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.empleados_a_cargo = []

    def add_employ(self, empleados):
        self.empleados_a_cargo.append(empleados)

    def show_details(self):
        super().show_details()
        print("\nEmpleados a cargo:")
        for empleado in self.empleados_a_cargo:
            empleado.show_details()

# Creando la clase Gerente de Proyecto
class ProjectManager(Employ):
    def __init__(self, nombre, proyectos):
        super().__init__(nombre)
        self.proyectos = proyectos

    def show_details(self):
        super().show_details()
        print(f"Proyectos: {', '.join(self.proyectos)}")

# Creando la clase Programador
class Programmer(Employ):
    def __init__(self, nombre, lenguaje):
        super().__init__(nombre)
        self.lenguaje = lenguaje

    def show_details(self):
        super().show_details()
        print(f"Lenguaje: {self.lenguaje}")

# Ejecutar
# Crear Gerente
gerente = Manager("Jesus")

# Crear Gerentes de Proyecto
gerente_proyecto1 = ProjectManager("Antonio", ["Proyecto 1"])
gerente_proyecto2 = ProjectManager("Faty", ["Proyecto 2"])

# Crear Programadores
programmer1 = Programmer("Adolfo", "Python")
programmer2 = Programmer("Naty", "C#")
programmer3 = Programmer("Ruben", "Kotlin")
programmer4 = Programmer("Axel", "JavaScript")

# Agregar empleados a cargo del gerente
gerente.add_employ(gerente_proyecto1)
gerente.add_employ(gerente_proyecto2)
gerente.add_employ(programmer1)
gerente.add_employ(programmer2)
gerente.add_employ(programmer3)
gerente.add_employ(programmer4)

# Mostrar detalle de los empleados
gerente.show_details()
gerente_proyecto1.show_details()
gerente_proyecto2.show_details()
programmer1.show_details()
programmer2.show_details()
programmer3.show_details()