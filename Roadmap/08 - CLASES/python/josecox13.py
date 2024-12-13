'''
 EJERCICIO 8:
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
 */
'''
class Coche:
    def __init__(self, marca: str, años: int):
        self.marca = marca
        self.años = años
    def print(self):
        print(f'Marca: {self.marca}, Años: {self.años}')
coche1 = Coche('Seat', 5)

coche1.print()
coche1.marca = 'Renault'
coche1.print()

'''
Ejercicio extra
'''
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return('No hay elementos en la pila')
        return self.stack.pop()
    def contar(self):
        return len(self.stack)
    def print(self):
        print(self.stack)
mi_stack = Stack()
mi_stack.push(1)
mi_stack.push(2)
mi_stack.push(3)
print(mi_stack.contar())
mi_stack.print()
mi_stack.pop()
mi_stack.print()
mi_stack.pop()
mi_stack.pop()
mi_stack.print()

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return('No hay elementos en la cola')
        return self.queue.pop(0)
    def contar(self):
        return len(self.queue)
    def print(self):
        print(self.queue)

mi_queue = Queue()
mi_queue.enqueue(1)
mi_queue.enqueue(2)
mi_queue.enqueue(3)
print(mi_queue.contar())
mi_queue.print()
mi_queue.dequeue()
mi_queue.print()
mi_queue.dequeue()
mi_queue.dequeue()
mi_queue.print()
