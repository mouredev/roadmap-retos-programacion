"""
# #08 CLASES
> #### Dificultad: Fácil | Publicación: 19/02/24 | Corrección: 26/02/24

## Ejercicio

```
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
```
"""

class Automovil:

    origen: str = None

    def __init__(self,brand:str, year:int, type:list):
        self.brand=brand
        self.year=year
        self.type=type

    def print(self):
        print(f"Marca: {self.brand}, Año:{self.year}, tipo: {self.type}, Lugar de fabricación: {self.origen} " )


Auto01= Automovil("Toyota", 2009,["SUV","Citycar"])

Auto01.print()

Auto01.origen= "Aisa"

Auto01.print()

Auto01.brand="Honda"

Auto01.print()

## Extra

class Pila:

    def __init__(self):
        self.pila=[]

    def push(self,item):
        self.pila.append(item)
    def pop(self):
        if len(self.pila) == 0:
            return print("la pila esta vacia")
        return self.pila.pop()
    def count(self):
        return print(f"Logitud de la pila {len(self.pila)}")
    def print(self):
        return print(f"estos son los datos del pila {self.pila}")

Pila02= Pila()

Pila02.push(1)
Pila02.push(2)
Pila02.push(3)
Pila02.push("d")
Pila02.print()
Pila02.count()
Pila02.pop()
Pila02.print()
Pila02.count()
Pila02.pop()
Pila02.pop()
Pila02.pop()
Pila02.pop()
Pila02.print()
Pila02.count()


##Queue

class cola:

    def __init__(self):
        self.cola=[]

    def equeue(self,item):
        self.cola.append(item)
    def dequeue(self):
        if len(self.cola) == 0:
            return print("la cola esta vacia")
        return self.cola.pop(0)
    def count(self):
        return print(f"Logitud de la cola {len(self.cola)}")
    def print(self):
        return print(f"estos son los datos del cola {self.cola}")


Cola01= cola()

Cola01.equeue(1)
Cola01.equeue(2)
Cola01.equeue(3)
Cola01.equeue("d")
Cola01.print()
Cola01.count()
Cola01.dequeue()
Cola01.print()
Cola01.count()
Cola01.dequeue()
Cola01.dequeue()
Cola01.dequeue()
Cola01.dequeue()
Cola01.print()
Cola01.count()
