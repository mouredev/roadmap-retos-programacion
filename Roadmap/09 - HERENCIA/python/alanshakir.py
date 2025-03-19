"""
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
"""

class Animal:
    def __init__(self, especie, sonido) :
        self.especie = especie
        self.sonido = sonido
    
    def imprimir_sonido(self):
        pass
        #print(f"el sonido del animal {self.especie} es: {self.sonido}")

class Perro(Animal):
    def imprimir_sonido(self):
        print("Guauuu")

class Gato(Animal):
    def imprimir_sonido(self):
        print("Miauuu")

my_dog = Perro("mamifero", "ladra")
my_dog.imprimir_sonido()

my_cat = Gato("mamifero", "aulla")
my_cat.imprimir_sonido()

class Empleados:
    def __init__(self, identify, name):
        self.identify = identify
        self.name = name
        self.my_employee = []

    def add_employee(self, employee):
        self.my_employee.append(employee)

    def printer_employee(self):
        for n in self.my_employee:
            print(n.name)

class Gerente(Empleados):
    def projects(self):
        print(f"{self.name} coordina los proyectos")


class SubGerente(Empleados):
    def __init__(self, identify, name, my_projects):
        super().__init__(identify, name)
        self.my_projects = my_projects
    
    def projects(self):
        print(f"{self.name} coordina su proyecto")
    


class Programadores(Empleados):
    def __init__(self, identify, name, language):
        super().__init__(identify, name)
        self.language = language
    
    def my_language(self):
        print(f"{self.name} programa en el lenguaje {self.language}")

my_gerente = Gerente(1, "Alan")
my_gerente2 = Gerente(2, "Giselle")
my_subgerente =  SubGerente(3, "Nicolle", "pagina web")
my_subgerente2 = SubGerente(4, "Matheo", "servidores")
my_programador = Programadores(5, "Rodrigo", "Go")


my_gerente.add_employee(my_subgerente)
my_gerente2.add_employee(my_subgerente2)
my_subgerente.add_employee(my_programador)

my_gerente.printer_employee()
my_gerente2.printer_employee()
my_subgerente.printer_employee()

my_gerente.projects()
my_gerente2.projects()
my_subgerente.projects()
my_subgerente2.projects()
my_programador.my_language()
