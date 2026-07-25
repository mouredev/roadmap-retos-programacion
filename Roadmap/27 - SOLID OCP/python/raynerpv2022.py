# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *


# Incorrect
class Shape:
    def __init__(self,s: str,a,b : int) -> None:
        self.shape = s
        self.a = a
        self.b = b
        self.area = 0
        

    def Area(self):
        if self.shape == "r":
            self.area = self.a*self.b
        if self.shape == "q":
            self.area = self.a**2
        if self.shape == "t":
            self.area = self.a*self.b/2
    
    def result(self):
        if self.area ==0:
            print("there is not Area calculated")
            return
        print(f" Area is {self.area}")

print("incorrect")
shape = [Shape("r",12,23),Shape("t", 34,7),Shape("q",12,12)]
 

for i in shape:
    i.Area()
    i.result()

# correct

from abc import ABC, abstractmethod
from functools import reduce

class Shape(ABC):
    def __init__(self,name: str) -> None:
        self.name = name
        self.area = 0
        super().__init__()
    
    @abstractmethod
    def Area(self):
        """Método abstracto que calcula el área de la figura. Obliga a redefinirlo"""
        pass

    def Result(self):
        print(f"Shape {self.name} with Area   {self.area}")
     

class square(Shape):
    def __init__(self, a : int) -> None:
        self.a = a
        super().__init__("square")
    
    def Area(self):
        self.area = self.a **2
         
    
class triangle(Shape):
    def __init__(self, a,b :int) -> None:
        self.a = a
        self.b = b
        super().__init__("triangle")

    def Area(self):
        self.area = self.a*self.b/2
         
    
class rectangle(Shape):
    def __init__(self, a,b: int) -> None:
        super().__init__("Rectangle")
        self.a = a
        self.b = b
        

    def Area(self):
        self.area = self.a*self.b
         
        
print("Correct")
shape = [triangle(12,13),square(12),triangle(34,55),square(99), rectangle(12,13)]
for i in shape:
    i.Area()
    i.Result()


    # Extra

    #  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
#  * Requisitos:
#  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
#  * Instrucciones:
#  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
#  * 2. Comprueba que el sistema funciona.
#  * 3. Agrega una quinta operación para calcular potencias.
#  * 4. Comprueba que se cumple el OCP.
#  */


# version sencilla

class Calculator(ABC):
    @abstractmethod
    def operator(self, *a ):
        pass

class Sum(Calculator):
    def operator(self, *a):
        return sum(a)

class Rest(Calculator):
    def operator(self, *a):
        return reduce(lambda x,y:x-y,a)
    
class Mult(Calculator):
    def operator(self, *a):
        return  reduce(lambda x,y:x*y,a)
    
class Div(Calculator): 
    # no DIV 0 checked
    def operator(self, *a):
        return reduce(lambda x,y:x/y,a)
class Power(Calculator):
    def operator(self, *a):
        return reduce(lambda x,y:x**y,a)

SUMA1 = print(Sum.operator(12,13,12,3,4))
RESTA1 = print(Rest.operator(1,2,3,4,5,6,7,8,9))
MULT1 = print(Mult.operator(1,2,3,4,5,6,7,8,9))
DIV1 = print(Div.operator(1,2,3,4,5,6,7,8,9))
POWER1 = print(Power.operator(1,2,3 ))


# Version complicada
# clase base para calculadora
class Calculator(ABC) :
    def __init__(self,symbol: str,n1,n2: float) -> None:
        self.n1 = n1 
        self.n2 = n2
        self.result = 0
        self.symbol = symbol
        
        super().__init__()
    
    @abstractmethod
    def Execute(self):
        pass
     
# clase para operacion suma, solo executa la suma
class Sum(Calculator):
    def __init__(self, n1 = None, n2 = None) -> None:
        super().__init__("+",n1,n2)
        
    def Execute(self):
        self.result = self.n1+self.n2
    
# # clase similar a suma
class Rest(Calculator):
    def __init__(self, n1 = None, n2 = None) -> None:
        super().__init__("-", n1, n2)

    def Execute(self):
        self.result = self.n1-self.n2
    
class Mult(Calculator):
    def __init__(self, n1 = None, n2 = None) -> None:
        super().__init__("*", n1, n2)

    def Execute(self):
        self.result = self.n1*self.n2

class Div(Calculator):
    def __init__(self, n1 = None, n2 = None) -> None:
        super().__init__("/", n1, n2)

    def Execute(self):
        if self.n2 == 0:
             self.result = None # div por 0 lo pongo None
        else:
            self.result = self.n1/self.n2

class Power(Calculator):
    def __init__(self, n1 = None, n2 = None) -> None:
        super().__init__("^", n1, n2)

    def Execute(self):
            self.result = self.n1**self.n2


# clase para imprimir resultados
class Result:
    def Print_result(self, c :Calculator):
        print(f" {c.n1} {c.symbol} {c.n2} = {c.result} ")

    def Print_error(self, o: str):
        print(o)

# clase para validar la entrada  
class Validate_Operation:
    def __init__(self) -> None:
        self.n1, self.n2,self.op = None,None,None
  
    def validate(self,op):
         match = re.match(r"(-?\d+)([+^\-*/])(-?\d+)", op)
         if match:
            self.n1 = int(match.group(1))
            self.op = match.group(2)
            self.n2 = int(match.group(3))
             
    def get_validation(self):
        return self.n1, self.op, self.n2

# clase para registrar los operadores permitidos
class Registry_Operation:
    def __init__(self) -> None:
        self.registry = {}

    def add_operation(self, key, value):
        self.registry[key] = value

    def get_registry(self, key):
        return self.registry.get(key,None)


result = Result()
registry = Registry_Operation()

# Nueva operacion ? adicionar aqui
registry.add_operation("+",Sum)
registry.add_operation("-",Rest)
registry.add_operation("*",Mult)
registry.add_operation("/",Div)
registry.add_operation("^",Power)

while True:
    print("Calculator v1")

    print("calc> ")
    op = input()
    if op == "exit":
        break
    op = op.strip()
    validate_operation = Validate_Operation()
    validate_operation.validate(op)
    n1,op,n2 = validate_operation.get_validation()

    if not op:
        result.Print_error("Error de  sintaxis , debe ser (n1 operador n2) ejemplo 2+4")
        continue
    
    if   not  registry.get_registry(op):
        result.Print_error(f"Error operation {op} not yet allowed")
        continue

    operation_class = registry.get_registry(op)
    actual_operation = operation_class(n1,n2) 
    actual_operation.Execute()
    
    result.Print_result(actual_operation)


    

    
    
   

     


