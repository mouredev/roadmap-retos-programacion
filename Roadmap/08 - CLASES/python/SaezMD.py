#08 CLASES
"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador, atributos y una función que los imprima (teniendo en cuenta las posibilidades de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido.
"""

#Attribute references
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.i)

#Class instantiation 
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

#another example:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Saez", 36)

print(p1.name)
print(p1.age)
p1.name = "MD"
print(p1.name)

#EXTRA

class Queue:
    def __init__(self):
        self.listOfObjects = []

    def addItem(self,toAdd):
        self.listOfObjects.append(toAdd)
    
    def removeItem(self):
        try:
            return self.listOfObjects.pop(0)
        except IndexError:
            print("Empty queue!")
    
    def lenght(self):
        return len(self.listOfObjects)
    
    def printAll(self):
        for item in self.listOfObjects:
            print(item)

d = Queue()
d.addItem("cap01")
d.addItem("cap02")
d.addItem("cap03")
d.addItem("cap04")
d.removeItem()
print(d.lenght())
d.printAll()

class Stack: #LIFO
    def __init__(self):
        self.listOfObjects = []

    def addItem(self,toAdd):
        self.listOfObjects.append(toAdd)
    
    def removeItem(self):
        try:
            self.listOfObjects.pop()
        except IndexError:
            print("Stack is empty!")
    
    def lenght(self):
        return len(self.listOfObjects)
    
    def printAll(self):
        for item in reversed(self.listOfObjects):
            print(item)

s = Stack()
s.addItem("show01")
s.addItem("show02")
s.addItem("show03")
s.addItem("show04")
s.removeItem()
print(s.lenght())
s.printAll()


        


