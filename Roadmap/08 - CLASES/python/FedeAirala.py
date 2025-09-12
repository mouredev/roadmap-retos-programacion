# Reto #08 Clases


"""
  EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 """

class Persona:                                                  # Se crea la clase Persona
                                                               
    def __init__(self, name, surname) -> None:                  # Se inicializa la clase
        self.name = name                                        # Creaciòn de atributos
        self.surname = surname
    
    def printer(self):                                          # Función para imprimir 
        print (f"Nombre y Apellido: {self.name}, {self.surname}")

p1 = Persona("Jhon","Python")                                   # Creación de un objeto de la clase Persona
p2 = Persona ("My","SQL")
p1.printer()                                                    # Llamada a función imprimir de la clase Persona
p2.printer()
p2.name = "María"                                               # Modificacón del objeto p2
p2.surname = "DB"
p2.printer()


"""   
 DIFICULTAD EXTRA (opcional):

 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
"""

class Stack():

    def __init__(self, items : list) -> list:
        self.items = items
    
    def add(self,items):
        self.items.append(items)

    def remove(self):
        if len (self.items) > 0:
            self.items.remove(self.items[-1])
        else:
            print ("Stack vacía")
    
    def elements(self):
        print (f"Cantidad de elementos en Stack: {len(self.items)}")
    
    def printer (self):
        print (f"Stack: {self.items}")

    

pila1 = Stack ([1,2,3])
pila1.printer()
pila1.elements()
pila1.add(4)
pila1.printer()
pila1.remove()
pila1.printer()
pila1.remove()
pila1.printer()
pila1.remove()
pila1.remove()
pila1.remove()
pila1.printer()
pila1.elements()

class Queue():
    def __init__(self, items : list) -> list:
        self.items = items
    
    def add(self,items):
        self.items.append(items)

    def remove(self):
        if len (self.items) > 0:
            self.items.remove(self.items[0])
        else:
            print ("Queue vacía")
    
    def elements(self):
        print (f"Cantidad de elementos en Queue: {len(self.items)}")
    
    def printer (self):
        print (f"Queue: {self.items}")

cola1 = Queue (["A","B","C"])
cola1.printer()
cola1.add("D")
cola1.printer()
cola1.remove()
cola1.printer()
cola1.remove()
cola1.printer()
cola1.remove()
cola1.remove()
cola1.remove()
cola1.printer()
cola1.elements()