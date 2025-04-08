
# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *


class Figura:
    def __init__(self ):
        pass

    
    def Area(self):
        pass
        


class Rectangle(Figura):
    def __init__(self, x, y):
         if  x<= 0 and y <= 0:
             raise ValueError("Valores deben ser mayores q que 0")
         self.x = x
         self.y = y

    
    
    
    def Area(self):
         
        return self.x*self.y
         
            
    

class Square(Figura):
    def __init__(self, x):
        if  x <= 0 :
             raise ValueError("Valores deben ser mayoresq que 0")
        self.x = x
     
    
    def Area(self):
         return self.x ** 2
         
        
class Circle(Figura):
    def __init__(self, r):
        if  r <= 0 :
            raise ValueError("Valores deben ser mayores q que 0")
        self.r = r
    
    def Area(self):
            return 3.14*self.r ** 2
         
            
        
def Calcular_Area(f: Figura):
    print(f.Area())
    
R =  Rectangle(12,14) 
S =  Square(7) 

C = Circle(10)




Figurillas = [R,S,C]
for i in Figurillas:
    Calcular_Area(i)


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
#  * cumplir el LSP.
#  * Instrucciones:
#  * 1. Crea la clase Vehículo.
#  * 2. Añade tres subclases de Vehículo.
#  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
#  * 4. Desarrolla un código que compruebe que se cumple el LSP.
#  */

class Vehiculo:
    def __init__(self, speed = 0):
        self.speed = speed

    def acelerar(self, i):
        self.speed += i

    def frenar(self, d):
        self.speed -= d
        if self.speed <= 0 :
            self.speed = 0
            
        

class carricoche(Vehiculo):
    def __init__(self, speed=0):
        super().__init__(speed)
    
    def acelerar(self,i):
        super().acelerar(i)
        return f" Carricoche ACELERAR Velocidad {self.speed}"

    def frenar(self,d):
       super().frenar(d)
       return f" Carricoche FRENO Velocidad {self.speed}"

    
class riquimbili(Vehiculo):
     def __init__(self, speed=0):
        super().__init__(speed)
    
     def acelerar(self, i):
        super().acelerar(i)
        return f" Rikimbili ACELERAR Velocidad {self.speed}"

     def frenar(self,d):
       super().frenar(d)
       return f" Rikimbili FRENO Velocidad {self.speed}"

C = carricoche()
R = riquimbili()
V = [C,R]

def test_LSP(v: Vehiculo):
    print(v.acelerar(100))
    print(v.acelerar(12))
    print(v.acelerar(1))
    print(v.acelerar(45))
    print(v.frenar(34))



print("EXTRA")
 

test_LSP(C)    
test_LSP(R )
test_LSP(C )
test_LSP(C )
test_LSP(R )
