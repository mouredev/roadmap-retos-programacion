#CLASES en PYHTON

class Developer:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        
    def saludar(self):
        print(f"Hola soy el desarrollador {self.name} y tengo {self.age} años")
        

desarrollador_1 = Developer("Juan", 22)
desarrollador_1.saludar()
desarrollador_1.name = "Pablo"
desarrollador_1.age= 25
desarrollador_1.saludar()


#EJERCICIO EXTRA


class Pila:
    
    def __init__(self):
        self.stack = []
        
    def apilar(self, item):
        self.stack.append(item)
    
    def desapilar(self):
        if self.contador() == 0:
            return None
        return self.stack.pop()
    
    def contador(self):
        return len(self.stack)
    
    def listar(self):
        for i in reversed(self.stack):
            print(i)

# mi_pila = Pila()
# mi_pila.apilar("ITEM1")
# mi_pila.apilar("ITEM2")
# mi_pila.apilar("ITEM3")
# mi_pila.contador()
# mi_pila.listar()
# mi_pila.desapilar()
# print("-------------------")
# mi_pila.contador()
# mi_pila.listar()

class Cola:
    def __init__(self):
        self.line = []
        
    def encolar(self, item):
        self.line.append(item)
    
    def desencolar(self):
        if self.contador() == 0:
            return None
        return self.line.pop(0)
    
    def contador(self):
        return len(self.line)
    
    def listar(self):
        for i in (self.line):
            print(i)

cola_1 = Cola()
cola_1.encolar("ITEM1")
cola_1.encolar("ITEM2")
cola_1.encolar("ITEM3")
print(cola_1.contador())
cola_1.listar()
cola_1.desencolar()