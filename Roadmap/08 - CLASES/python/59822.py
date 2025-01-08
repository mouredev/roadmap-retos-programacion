'''Una clase es un modelo que define un conjunto de atributos y métodos que tendrán 
los objetos que se creen a partir de ella. '''


## Los parametros de los metodos de instancia deben ser self,
# que es una referencia al objeto que invoca el metodo

class Persona:
    persona = "Persona es un ser humano"
    #M Persona es un atributo de la clase
    
    def __init__(self, nombre, apellido): # Metodo constructor
        self.nombre = nombre # Atributo de instancia
        self.apellido = apellido
        
    def hablar(self, mensaje):
        print(f"{self.nombre} dice {mensaje}")

isabel = Persona("Isabel", "García")
isabel.hablar("Hola, soy Isabel")
        
'''Dificultad'''
##  LIFO
class LIFO:
    
    def __init__(self):
        self.opciones = []
    
    def añadir(self, item):
        self.opciones.append(item)
        
    def quitar(self):
        if self.count() == 0: 
            return None
        else:
            return self.opciones.pop()
    
    def count(self):
        return len(self.opciones)
    
    def mostrar(self):       
        for item in self.opciones:
            print("Las opciones son:\n", item)

class Fifo:
    
    def __init__(self):
        self.fila = []
    
    def añadir(self, item):
        self.fila.append(item)
    
    def eliminar(self):
        if self.count() == 0:
            return None
        else:
            return self.fila.pop(0)
    
    def count(seLf):
        return len(self.fila)
    
    def mostrar(self):       
        for item in self.opciones:
            print("Las opciones son:\n", item)