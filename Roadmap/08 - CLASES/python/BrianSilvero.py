"""
Ejercicio
"""

class Programer:
    apellido:str = None
    
    def __init__(self,name: str, age: int, lenguaje: list):
        self.name = name
        self.age = age
        self.lenguaje = lenguaje
        
    def print(self):
        print(f"Nombre: {self.name} | Apellido: {self.apellido} Edad: {self.age} | Lenguaje: {self.lenguaje}")
        
my_programador = Programer("Brian", 27,["Python", "JavaScript"])
my_programador.print()
my_programador.apellido = "Silvero"
my_programador.print()
my_programador.age = 28
my_programador.print()


"""
Extra
"""

# LIFO

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)
            
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()

print("-----------------------------------------------------------")
# FIFO

class Cola:
    def __init__(self):
        self.cola = []
    
    def push(self,item):
        self.cola.append(item)
        
    def pop(self):
        if self.count() == 0:
            return None
        self.cola.pop(0)
        
    def count(self):
        return len(self.cola)
    
    def print(self):
        for item in self.cola:
            print(item)
            
my_cola = Cola()
my_cola.push("F")
my_cola.push("G")
my_cola.push("H")
print(my_cola.count())
my_cola.print()
my_cola.pop()
my_cola.pop()
my_cola.pop()
print(my_cola.count())
my_cola.print()