class Persona:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def printer(self):
        print(f"{self.name} is {self.age} years old!")
    
p1= Persona("Jose Miguel Gallo Zuno",23)
p2= Persona("Monica Gabriela Zuno Ramirez", 55)
p1.printer()
p2.printer()
p1.name=("Gallolobo")
p1.age=(24)
p1.printer()

"""   
 DIFICULTAD EXTRA (opcional):

 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
"""
class Pila:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def print_content(self):
        print("Pila:", self.items)


class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def print_content(self):
        print("Cola:", self.items)

#Pruebas
pilates= Pila()
pilates.push("Gallolobo")
pilates.push("tontito")
pilates.push("Hola")
pilates.print_content()
pilates.pop()
pilates.print_content()

popola=Cola()
