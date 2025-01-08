'''
* EJERCICIO:
* Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
* atributos y una funciÃ³n que los imprima (teniendo en cuenta las posibilidades
* de tu lenguaje).
* Una vez implementada, crÃ©ala,w establece sus parÃ¡metros, modifÃ­calos e imprÃ­melos
* utilizando su funciÃ³n.
'''

class Car:
    def __init__ (self, marca, modelo, aÃ±o):
        self.marca = marca
        self.modelo = modelo
        self.aÃ±o = aÃ±o
        
    def car_of_the_year(self):
        return f"El premio coche del aÃ±o en {self.aÃ±o} fue para el {self.marca} {self.modelo}"
        

my_first_car = Car("seat", "1430", 1975)
my_last_car = Car("ford", "Mustang Shelby", 2020)
print(my_first_car.car_of_the_year())
print(my_last_car.car_of_the_year())


'''
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio nÃºmero 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para aÃ±adir, eliminar,
*   retornar el nÃºmero de elementos e imprimir todo su contenido.
'''

class Stack:
    
    def __init__(self):
        self.my_stack = []
        
    def len_items(self):
        return len(self.my_stack)

    def add(self, name):
        self.my_stack.append(name)
        return self.my_stack
        
    def pop(self):
        if len(self.my_stack) > 0:
            self.my_stack.pop()
            return self.my_stack
        else:
            return "No hay elementos para eliminar la lista estÃ¡ vacÃ­a"
            
pila = Stack()
print(pila.len_items())   
print(pila.add("Juan"))
print(pila.add("Pedro"))
print(pila.add("MarÃ­a"))
print(pila.len_items()) 
print(pila.pop())
print(pila.len_items()) 
print(pila.pop())
print(pila.len_items()) 
print(pila.pop())
print(pila.len_items())
print(pila.pop())

 
class Queue:
    def __init__(self):
        self.my_queue = []
        
    def len_items(self):
        return len(self.my_queue)
    
    def add(self,name):
        self.my_queue.append(name)
        return self.my_queue
    def pop(self):
        if len(self.my_queue) > 0:
            self.my_queue.pop(0)
            return self.my_queue
        else:
            return "No hay elementos para eliminar"

cola = Queue()
print(cola.len_items())
print(cola.add("Juan"))
print(cola.add("Pedro"))
print(cola.add("MarÃ­a"))
print(cola.len_items())    
print(cola.pop()) 
print(cola.len_items())  
print(cola.pop()) 
print(cola.len_items()) 
print(cola.pop()) 
print(cola.len_items()) 
print(cola.pop())      

