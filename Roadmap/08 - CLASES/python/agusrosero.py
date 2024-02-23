"""
/*
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
 */
"""

# EJERCICIO:


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

    def saludar(self):
        return f'¡Hola {self.nombre} {self.apellido}!'

    def despedir(self):
        return f'¡Adiós {self.nombre} {self.apellido}!'


objeto1 = Persona('Hernan', 'Rosero')
print(objeto1)
print(objeto1.saludar())
print(objeto1.despedir())

# DIFICULTAD EXTRA:


class Pila:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.append(value)
        print(self.items)

    def delete(self):
        elemento_eliminado = self.items.pop()
        return elemento_eliminado

    def number_of_elements(self):
        numero_de_elementos = len(self.items)
        if numero_de_elementos == 0:
            return 0
        else:
            return numero_de_elementos

    def get_information(self):
        print(self.items)


pila1 = Pila()
pila1.add(1)
pila1.add(2)
pila1.add(3)
print(pila1.delete())
print(pila1.number_of_elements())
pila1.get_information()


class Cola:
    def __init__(self):
        self.items = []

    def add(self, value):
        self.items.insert(0, value)
        print(self.items)

    def delete(self):
        elemento_eliminado = self.items.pop()
        return elemento_eliminado

    def number_of_elements(self):
        numero_de_elementos = len(self.items)
        if numero_de_elementos == 0:
            return 0
        else:
            return numero_de_elementos

    def get_information(self):
        print(self.items)


cola1 = Cola()
cola1.add(1)
cola1.add(2)
cola1.add(3)
print(cola1.delete())
print(cola1.number_of_elements())
cola1.get_information()
