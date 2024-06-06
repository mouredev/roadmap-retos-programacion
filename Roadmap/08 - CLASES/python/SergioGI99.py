"""
------
CLASES
------
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.

DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
  retornar el número de elementos e imprimir todo su contenido.
"""
# Ejercicio

class BankAcc:
    
    def __init__(self,id: int, saldo: float):
        self.saldo = saldo
        self.id = id

    def deposit(self, amount: float):
        self.saldo += amount

    def imprimir(self):
        print("Tu balance actual es de: ", self.saldo)

my_account = BankAcc(1, 0)

my_account.deposit(100)

my_account.imprimir()

# Extra

class Pila: # Stack LIFO
    
    def __init__(self):
        self.pila = []
        
    def push(self, add):
        (self.pila).append(add)
        print(f"Se ha añadido {add} a la pila")
        
    def pop(self):
        if len(self.pila) == 0:
            return None
        return print("Se ha eliminado: ", (self.pila).pop())
        
    def count(self):
        print("El tamaño de la pila es: ", len(self.pila))
        
    def print(self):
        for item in reversed(self.pila):
            print(item)
        
my_pila = Pila()

my_pila.push("uno")
my_pila.push("dos")
my_pila.push("tres")

my_pila.count()

my_pila.pop()

my_pila.print()

class Cola: # Queue FIFO
    
    def __init__(self):
        self.cola = []
        
    def enqueue(self, add):
        (self.cola).append(add)
        print(f"Se ha añadido {add} a la cola")
        
    def dequeue(self):
        if len(self.cola) == 0:
            return None
        return print("Se ha eliminado: ", (self.cola).pop(0))
        
    def count(self):
        print("El tamaño de la cola es: ", len(self.cola))
        
    def print(self):
        for item in self.cola:
            print(item)
        
my_cola = Cola()

my_cola.enqueue("uno")
my_cola.enqueue("dos")
my_cola.enqueue("tres")

my_cola.count()

my_cola.dequeue()

my_cola.print()