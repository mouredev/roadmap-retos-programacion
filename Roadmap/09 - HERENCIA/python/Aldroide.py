"""
Ejercicio crear un ejemplo que implemente una superclase animal 
y subclases de perro y gato junto a una función que imprima
el sonido que emite cada animal
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Perro(Animal):

    def sound(self):
        print(f"El {self.name} hace Guau!")


class Gato(Animal):

    def sound(self):
        print(f"El {self.name} hace Miau!")


def print_sound(animal: Animal):
    animal.sound()


mi_animal = Animal("Animal")
print_sound(mi_animal)
mi_perro = Perro("Perro")
print_sound(mi_perro)
mi_gato = Gato("Gato")
print_sound(mi_gato)


"""
* DIFICULTAD EXTRA :
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */
"""


class Empleado:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.empleados = []

    def añadir(self, empleado):
        self.empleados.append(empleado)

    def imprime(self):
        for empleado in self.empleados:
            print(empleado.name)


class Gerente(Empleado):
    def Cor_proyectos(self):
        print(f"{self.name} está coordinando todos los proyectos")


class Gerente_proyectos (Empleado):
    def __init__(self, id: int, name: str, proyecto: str):
        super().__init__(id, name)
        self.proyecto = proyecto

    def Cor_proyecto(self):
        print(f"{self.name} esta cordinando su proyecto.")


class Programador(Empleado):
    def __init__(self, id: int, name: str, lenguaje: str):
        super().__init__(id, name)
        self.lenguaje = lenguaje

    def codigo(self):
        print(f"{self.name} programa un proyecto en {self.lenguaje}")

    def añadir(self, empleado: Empleado):
        print(
            f"El progamador tiene empleados a su cargo. {empleado.name} no se unirá")


Gerente1 = Gerente(1, "Aldroide")
Gerente_proyectos1 = Gerente_proyectos(2, "Samira", "Proyecto gatitos")
Gerente_proyectos2 = Gerente_proyectos(3, "Sebastian", "Proyecto perritos")
Progamador1 = Programador(4, "Erwin", "Swift")
Progamador2 = Programador(5, "Emmanuel", "Cobol")
Progamador3 = Programador(6, "Anahi", "Dart")
Progamador4 = Programador(7, "Yubesny", "Python")

Gerente1.añadir(Gerente_proyectos1)
Gerente1.añadir(Gerente_proyectos2)

Gerente_proyectos1.añadir(Progamador1)
Gerente_proyectos1.añadir(Progamador2)
Gerente_proyectos2.añadir(Progamador3)
Gerente_proyectos2.añadir(Progamador4)

Progamador1.añadir(Progamador2)

Progamador1.codigo()
Gerente_proyectos1.Cor_proyecto()
Gerente1.Cor_proyectos()
Gerente1.imprime()
Gerente_proyectos1.imprime()
Progamador1.imprime()
