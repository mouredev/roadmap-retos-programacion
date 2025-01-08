"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Vehiculo:
    def __init__(self, tipo: str, modelo: str, color: str, ruedas: int):
        self.tipo = tipo
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"El vehiculo {self.tipo} es modelo {self.modelo}, con color {self.color} y de {self.ruedas} ruedas"

    
auto = Vehiculo('automovil', 'classic', 'gris', 4)
print(auto)
moto = Vehiculo('motocicleta', 'scooter', 'negro', 2)
print(moto)
auto.color = 'azul'
print("Se modifico el color del auto: ")
print(auto)
moto.modelo = 'motocross'
print("Se modifico el modelo de la moto")
print(moto)

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */"""

class Stack:
    def __init__(self):
        self.stack = []

    def add_element(self,element):
        return f"Se agrego el elemento a la pila: {self.stack.append(element)}"
        

    def remove_element(self):
        return f"Se elimino el ultimo elemento ingresado: {self.stack.pop()}"

    def size(self):
        return f"La pila tiene {len(self.stack)} elementos"

    def __str__(self):
        for element in self.stack[::-1]:
            return element

stack1 = Stack()

class Queue:
    def __init__(self):
        self.queue = []

    def add_element(self, element):
        return f"Se agrego el elemento a la cola: {self.queue.insert(0,element)}"
        
    def remove_element(self):
        return f"Se elimino el primer elemento que ingreso a la cola: {self.queue.pop()}"

    def size(self):
        return f"La cola tiene {len(self.queue)} elementos"

    def __str__(self):
        for element in self.queue[::-1]:
            return element
            
queue = Queue()