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
