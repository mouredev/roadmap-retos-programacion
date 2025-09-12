# CLASES
class Pala:
  def __init__(self, marca, modelo, precio, tiendas):
    self.marca = marca
    self.modelo = modelo
    self.precio = precio
    self.tiendas = tiendas
    
  def __str__(self):
    return f"{self.marca} {self.modelo} {self.precio} {self.tiendas}"
  
  def info(self):
    print(f"--- Pala ---\nMarca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio} €\nDisponible en: {self.tiendas}")

cosa = Pala("Varlion", "LW Carbon Hexagon", 200, ["El Corte Inglés", "Decathlon"])
cosa.info()
print(cosa)

"""
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""
class Stack:
    def __init__(self):
        self.stack = []

    def mete(self, item):
        self.stack.append(item)

    def saca(self):
        sacado = self.stack.pop()
        return sacado

    def __str__(self):
        return str(self.stack)

    def muestra(self):
        print(
            f"--- Stack (Pila) ---\nStack actual: {self.stack}\nSiguiente elemento a sacar: {self.stack[-1]}"
        )

stack1 = Stack()
stack1.mete(1)
stack1.mete(3)
stack1.mete(5)
stack1.mete(7)
# Usando método muestra()
stack1.muestra()
# Usar método saca()
sacado = stack1.saca()
print("Elemento sacado =>", sacado)
# Usando método __str__()
print("Stack después del pop:", stack1)


class Queue:
    def __init__(self):
        self.queue = []

    def mete(self, item):
        self.queue.append(item)

    def saca(self):
        sacado = self.queue.pop(0)
        return sacado

    def __str__(self):
        return str(self.queue)

    def muestra(self):
        print(
            f"--- Queue (Cola) ---\nQueue actual: {self.queue}\nSiguiente elemento a sacar: {self.queue[0]}"
        )


queue1 = Queue()
queue1.mete(1)
queue1.mete(3)
queue1.mete(5)
queue1.mete(7)
# Usando método muestra()
queue1.muestra()
# Usar método saca()
sacado = queue1.saca()
print("Elemento sacado =>", sacado)
# Usando método __str__()
print("Queue después del pop:", queue1)
