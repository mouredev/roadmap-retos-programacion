class MiClase():
    def __init__(self, nombre:str, apellido:str, edad:int, ciudad:str):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad

    def print(self): 
        print(f"Mi nombre es {self.nombre}; mi apellido es {self.apellido} y tengo {self.edad} años")

Yo = MiClase("Ricardo", "Ortega", 60, "Zamora")
Yo.print()
Yo.edad = 70
Yo.print()
print(Yo.ciudad)
Yo.ciudad = "Soria"
print(Yo.ciudad)

#Una clase que implemente a una pila LIFO

class Stack():
    def __init__(self):
        self.pila = []

    def apilar(self, item):
        self.pila.append(item)
    def desapilar(self):
        if self.contar() > 0:
            self.pila.pop()
        else:
            return None    
    def contar(self):
        return len(self.pila)
    def mostrar(self):
        return self.pila

MiPila = Stack()

MiPila.apilar(1)
MiPila.apilar(2)
MiPila.apilar(3)
MiPila.apilar("4")
print(MiPila.mostrar())
MiPila.desapilar()
print(MiPila.contar())    
MiPila.desapilar()
print(MiPila.mostrar())
MiPila.desapilar()
MiPila.desapilar()
MiPila.desapilar()
print(MiPila.mostrar())
print(MiPila.contar())

#Una clase que implemente a una cola FIFO

class Queue():
    def __init__(self):
        self.cola = []
    def encolar(self, item):
        self.cola.append(item)
    def desencolar(self):
        if self.contar() > 0:
            self.cola.pop(0)
        else:
            return None    
    def contar(self):
        return len(self.cola)
    def mostrar(self):
        return self.cola

MiCola = Queue()


MiCola.encolar("A")
MiCola.encolar(9)
MiCola.encolar(8)
MiCola.encolar(7)
print(MiCola.contar())
print(MiCola.mostrar())
MiCola.desencolar()
MiCola.desencolar()
print(MiCola.contar())
print(MiCola.mostrar())
MiCola.encolar("B")
print(MiCola.contar())
print(MiCola.mostrar())
MiCola.desencolar()
MiCola.desencolar()
MiCola.desencolar()
MiCola.desencolar()
print(MiCola.desencolar())
MiCola.desencolar()
print(MiCola.contar())
print(MiCola.mostrar())
