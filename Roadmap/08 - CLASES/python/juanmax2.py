"""
Clases
"""

class Persona():
    
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def saludar(self):
        print(f"Saludos soy {self.nombre} tengo {self.edad} años y soy {self.profesion}")

# Caso de uso

persona1 = Persona("Juanma", 32, "Programador")

persona1.saludar()

# Modificar un parametro

persona1.edad = 33

persona1.saludar()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Pila():
    
    def __init__(self):
        self.stack = []

    def push(self, archivo):
        self.stack.append(archivo)   
        
    def pop(self):
        if self.count() == 0:
            return None
        else:
            return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)
        
class Cola():
    
    def __init__(self):
        self.cola = []
    
    def push(self, archivo):
        self.cola.append(archivo)
        
    def pop(self):
        if self.count() == 0:
            return None
        else:
            return self.cola.pop(0)
    
    def count(self):
        return len(self.cola)
    
    def print(self):
        for item in self.cola:
            print(item)
        
my_stack = Pila()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

my_stack.print()
print(my_stack.count())
print("-----------------")
my_stack.pop()
print("-----------------")
my_stack.print()
print(my_stack.count())

print("-----------------")
print("-----------------")
cola = Cola()
cola.push("A")
cola.push("B")
cola.push("C")

cola.print()
print(cola.count())
print("-----------------")
print("-----------------")
cola.pop()
cola.print()
print(cola.count())