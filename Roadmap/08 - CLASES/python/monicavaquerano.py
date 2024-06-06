# 08 CLASES
# Monica Vaquerano
# https://monicavaquerano.dev

"""
Ejercicio:

Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).

Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función. 
"""


# Clases (Classes)
#  En Python, una clase es una plantilla para crear objetos que comparten atributos y métodos comunes. Los objetos son instancias de una clase.
class Auto:
    # Inicializador (__init__)
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    # Método para imprimir los atributos
    def imprimir_informacion(self):
        print(
            f"--- Auto ---\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}"
        )

    # La función __str__(): esta controla lo que debe ser retornado cuando el objeto de clase se representa como una string.
    def __str__(self):
        return f"{self.marca}, {self.modelo} ({self.ano})"


print("08 CLASES\n")
# Crear una instancia de la clase Persona
print("* Instanciando:\n")
print('auto1 = Auto("Toyota", "Yaris", 2024)\n')
auto1 = Auto("Toyota", "Yaris", 2024)
# Llamar al método para imprimir los atributos
print("* Llamado al método:\nauto1.imprimir_informacion()\n")
auto1.imprimir_informacion()
# Llamar al método __str__()
print("\n* Usando el método __str__():\n")
print(auto1)
# Modificando los valores o atributos del objeto
print("\n* Modificando sus atributos:\n")
print('auto1.marca = "Volkswagen"\nauto1.modelo = "T-Roc"')
auto1.marca = "Volkswagen"
auto1.modelo = "T-Roc"
# Llamar nuevamente al método para imprimir los atributos
print("\n* Llamado nuevamente al método:\nauto1.imprimir_informacion()\n")
auto1.imprimir_informacion()
# Llamar nuevamente al método __str__()
print("\n* Usando nuevamente el método __str__():\n")
print(auto1)

"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)

- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""
print("\nDIFICULTAD EXTRA (opcional):\n")


# Pilas (Stacks):
# Una pila es una estructura de datos en la que el último elemento añadido es el primero en ser eliminado (LIFO - Last In, First Out).
class Stack:
    def __init__(self):
        self.stack = []

    def addIn(self, item):
        self.stack.append(item)

    def popOut(self):
        popped = self.stack.pop()
        return popped

    def __str__(self):
        return str(self.stack)

    def ver_stack(self):
        print(
            f"--- Estado Stack ---\nStack actual: {self.stack}\nSiguiente elemento a salir: {self.stack[-1]}"
        )


print("* Pilas (Stacks)")
# Instanciar Stack
stack1 = Stack()
# Usar método add()
stack1.addIn(1)
stack1.addIn(2)
stack1.addIn(3)
stack1.addIn(4)
# Usando método ver_stack()
stack1.ver_stack()
# Usar método popOut()
popped = stack1.popOut()
print("Elemento sacado =>", popped)
# Usando método __str__()
print("Stack después del pop:", stack1)


class Queue:
    def __init__(self):
        self.queue = []

    def addIn(self, item):
        self.queue.append(item)

    def popOut(self):
        popped = self.queue.pop(0)
        return popped

    def __str__(self):
        return str(self.queue)

    def ver_queue(self):
        print(
            f"--- Estado Queue ---\nQueue actual: {self.queue}\nSiguiente elemento a salir: {self.queue[0]}"
        )


print("\n* Colas (Queues)")
# Instanciar Queue
queue1 = Queue()
# Usar método add()
queue1.addIn(1)
queue1.addIn(2)
queue1.addIn(3)
queue1.addIn(4)
# Usando método ver_queue()
queue1.ver_queue()
# Usar método popOut()
popped = queue1.popOut()
print("Elemento sacado =>", popped)
# Usando método __str__()
print("Queue después del pop:", queue1)
