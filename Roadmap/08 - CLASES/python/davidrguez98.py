""" /*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */ """

#EJERCICIO

class programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")

my_programmer = programmer("David", 26, ["Python", "HTML", "CSS"])
my_programmer.print()
my_programmer.surname = "Rodríguez"
my_programmer.print()

my_programmer.age = 27
my_programmer.print()

#DIFICULTAD EXTRA

#Pila

class pila:

    def __init__(self):
        self.pila = []

    def add(self, item):
        self.pila.append(item)

    def delete(self):
        return self.pila.pop()

    def count(self):
        print(len(self.pila))

    def print(self):
        for item in reversed(self.pila):
            print(item)


my_pila = pila()
my_pila.add("1")
my_pila.add("2")
my_pila.add("3")
my_pila.count()
my_pila.print()

my_pila.delete()
my_pila.count()
my_pila.print()

#Cola

class cola:

    def __init__(self):
        self.cola = []

    def add(self, item2):
        self.cola.append(item2)

    def delete(self):
        return self.cola.pop(0)

    def count(self):
        print(len(self.cola))

    def print(self):
        for item2 in reversed(self.cola):
            print(item2)


my_cola = cola()
my_cola.add("1")
my_cola.add("2")
my_cola.add("3")
my_cola.count()
my_cola.print()

my_cola.delete()
my_cola.count()
my_cola.print()