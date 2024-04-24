"""
CLASES EN PYTHON 🐍
"""
class MyFirstClass:
    """ My first class in Python"""
    atributo_int :int
    atributo_str :str
    
    # En el init le he puesto valores por defecto a los parametros :)  
    def __init__(self, cantidad=0, texto="vacio") -> None:
        self.atributo_int = cantidad
        self.atributo_str = texto
    
    def print(self):
        print(f"\t- cantidad: {self.atributo_int}\t- texto: {self.atributo_str} ")


myObjectEmpty = MyFirstClass()
myObjectEmpty.print()

myObject = MyFirstClass(99, "Patatin")
myObject.print()

myObject.atributo_int = 55
myObject.atributo_str = "otro texto"
myObject.print()


"""
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
    retornar el número de elementos e imprimir todo su contenido.
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

# Pila / Stack

class Stack:
    
    data = []
    
    def __init__(self) -> None:
        data = []
    
    def push(self, item) -> None:
        self.data.append(item)
    
    def pop(self):
        if(len(self.data) == 0):
            print("WARN: empty stack!")
        else:
            return self.data.pop()
    
    def size(self):
        return len(self.data)
    
    def print(self):
        print("heap")
        print("  ↓")
        print(self.data[::-1])

def test_stack():
    pila = Stack()
    pila.push("A")
    pila.push("B")
    pila.push("C")
    pila.print()

    print(f"pop: {pila.pop()}")
    pila.print()
    print(f"pop: {pila.pop()}")
    pila.print()
    print(f"pop: {pila.pop()}")
    pila.print()
    print(f"pop: {pila.pop()}")
    pila.print()

test_stack()
