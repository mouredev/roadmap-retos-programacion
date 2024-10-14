#08 CLASES

"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class bici():

    def __init__(self, marca, modelo, talla) -> None:
        self.marca = marca
        self.modelo = modelo
        self.talla = talla

    def infobike(self):
        print(f"Bicicleta: {self.marca}, Modelo: {self.modelo}, Talla: {self.talla}")
    
nueva_bici = bici("Giant","Talon 2","L")
nueva_bici.infobike()

nueva_bici.talla = ["XL","L"]
nueva_bici.infobike()

nueva_bici.marca = "Trek"
nueva_bici.modelo = "Marlon 5"
nueva_bici.infobike()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class pila():

    def __init__(self) -> None:
        self.stack = []
    
    def añadir(self, value):
        self.stack.append(value)
    
    def eliminar(self):
        self.stack.pop()
    
    def infopila(self):
        if self.stack:
            print(self.stack)
        else:
            print("La pila está vacía, añada elementos")

x = pila()
x.añadir(1)
x.añadir(2)
x.añadir(3)
x.añadir(4)
x.infopila()
x.eliminar()
x.infopila()
x.eliminar()
x.infopila()
x.eliminar()
x.infopila()
x.eliminar()
x.infopila()

class cola():

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def infocola(self):
        if self.queue:
            print(self.queue)
        else:
            print("La cola está vacía, añada elementos")

y = cola()
y.enqueue("a") 
y.enqueue("b") 
y.enqueue("c") 
y.enqueue("d")
y.infocola()
y.dequeue()
y.infocola()
y.dequeue()
y.infocola()
y.dequeue()
y.infocola()
y.dequeue()
y.infocola()   