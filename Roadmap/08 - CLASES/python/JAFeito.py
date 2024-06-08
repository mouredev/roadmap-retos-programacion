class Pila:
    def __init__(self):
        self.pila =[]
        
    def push(self):
        elemento = input(f"Introduzca un elemento para añadir a la pila.\n")
        self.pila.append(elemento)
        
    def pop(self):
        if len(self.pila) == 0:
            return None
        return self.pila.pop()
            
    def count(self):
        return len(self.pila)    
        
    def imprime(self):
        print(self.pila)
      
      
class Cola:
    def __init__(self):
        self.cola = []
        
    def push(self):
        elemento = input(f"Introduzca un elemento para añadir a la pila.\n")
        self.cola.append(elemento)
        
    def pop(self):
        if len(self.cola) == 0:
            return None
        return self.cola.pop(0)
            
    def count(self):
        return len(self.cola)    
        
    def imprime(self):
        print(self.cola)    
        
                
        
mi_pila = Pila()     
mi_pila .push()
mi_pila .push()
mi_pila .push()
print(mi_pila.count())
mi_pila.imprime()
mi_pila.pop()
print(mi_pila.count())
mi_pila.imprime()

mi_cola = Cola()     
mi_cola .push()
mi_cola .push()
mi_cola .push()
print(mi_cola.count())
mi_cola.imprime()
mi_cola.pop()
print(mi_cola.count())
mi_cola.imprime()