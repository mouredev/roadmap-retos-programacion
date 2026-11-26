'''
* Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
* y crea un ejemplo simple donde se muestre su funcionamiento
'''

class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        pass 

class Guitarra(Instrumento):
    def tocar(self):
        print(f"Tocando la guitarra: {self.nombre}")
class Piano(Instrumento):
    def tocar(self):
        print(f"Tocando el piano: {self.nombre}")
class Bateria(Instrumento):
    def tocar(self):
        print(f"Tocando la batería: {self.nombre}")
class Orquesta():
    def __init__(self):
        self.instrumentos = []

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)


    def eliminar_instrumento(self, instrumento):
        if instrumento in self.instrumentos:
            self.instrumentos.remove(instrumento)
            print(f"Se ha eliminado el instrumento {instrumento.nombre} de la orquesta")
        else:
            raise ValueError(f"El instrumento {instrumento.nombre} no está como objeto en la orquesta.")       

    def tocar_orquesta(self):
        for instrumento in self.instrumentos:
            instrumento.tocar()

orquesta = Orquesta()
guitarra = Guitarra("Alhambra")
orquesta.agregar_instrumento(Guitarra("Fender Stratocaster"))
orquesta.agregar_instrumento(guitarra)
orquesta.agregar_instrumento(Piano("Yamaha P125"))
orquesta.agregar_instrumento(Bateria("Pearl Export"))
orquesta.tocar_orquesta()
try:
    orquesta.eliminar_instrumento(guitarra)
    orquesta.eliminar_instrumento(Guitarra("Fender Stratocaster")) # Al ejecutar este método se vuelve a instanciar la clase 
    # Guitarra y deja de ser el mismo objeto aunque guarde igual atributo, la solución a esto es crear la instancia guitarra
    # sino de esta manera no se pueden eliminar.
except ValueError as e:
    print(e)
finally:          
    orquesta.tocar_orquesta()        

'''
* DIFICULTAD EXTRA (opcional):
* Desarrolla una Operdora que necesita realizar diversas operaciones matemáticas.
* Requisitos:
* - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
* Instrucciones:
* 1. Implementa las operaciones de suma, resta, multiplicación y división.
* 2. Comprueba que el sistema funciona.
* 3. Agrega una quinta operación para Operr potencias.
* 4. Comprueba que se cumple el OCP.
'''
from abc import ABC, abstractmethod

class Oper(ABC):
    @abstractmethod
    def opera (self, a, b):
        pass

class Suma(Oper):
    def opera(self, a, b):
        return a + b    
class Resta(Oper):
    def opera(self, a, b):
        return a - b
class Multiplica(Oper):
    def opera(self, a, b):
        return a * b 
class Divide(Oper):       
    def opera(self, a, b):
            return a / b 
class Potencia(Oper):       
    def opera(self, a, b):
            return a ** b     
class Calcula:
    def __init__(self):
        self.operaciones = {}

    def añade_oper(self, nombre ,operacion):
        self.operaciones[nombre] = operacion

    def elimina_oper(self, nombre):
        del self.operaciones[nombre]    

    def ejecuta(self, nombre, a, b):
        if nombre not in self.operaciones:
            raise ValueError (f"Error en la denominación de la operación {nombre}")
        else:
            return self.operaciones[nombre].opera(a, b)

calculadora = Calcula()
calculadora.añade_oper("suma", Suma())
calculadora.añade_oper("resta", Resta())    
calculadora.añade_oper("multiplica", Multiplica())
calculadora.añade_oper("divide", Divide())
calculadora.elimina_oper("divide") # Al ser un conjunto el objeto queda asociado a un nombre y se puede referenciar para su borrado
# no como en el ejemplo anterior. No se instancia otra vez como antes que había una lista de objetos en sí.
calculadora.añade_oper("divide", Divide())
calculadora.añade_oper("potencia", Potencia())

try:
    print(calculadora.ejecuta("suma", 5, 7))
    print(calculadora.ejecuta("resta", 5, 7))
    print(calculadora.ejecuta("multiplica", 5, 7))
    print(calculadora.ejecuta("divide", 5, 7))
    try:
        print(calculadora.ejecuta("potencia", 5, 7))
    except ValueError as e:
        print(e)   
except ValueError as e:
    print(e)
    

