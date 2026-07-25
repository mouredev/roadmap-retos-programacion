##########################  POO  ################################

'''
Llamamos clase a la representación abstracta de un concepto. Por ejemplo, “perro”, “número entero” o “servidor web”.
Las clases se componen de atributos y métodos.
Un objeto es cada una de las instancias de una clase.
Los atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas.
Un atributo de objeto se define dentro de un método y pertenece a un objeto determinado de la clase instanciada.
Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos.
'''

'''
Método constructor init

Los atributos de objetos no se crean hasta que no hemos ejecutado el método. 
Tenemos un método especial, llamado constructor init, que nos permite inicializar los atributos de objetos. 
Este método se llama cada vez que se crea una nueva instancia de la clase (objeto).
'''
'''
El método constructor, al igual que todos los métodos de cualquier clase, recibe como primer parámetro a la instancia 
sobre la que está trabajando. Por convención a ese primer parámetro se lo suele llamar self 
(que podríamos traducir como yo mismo), pero puede llamarse de cualquier forma.

Para referirse a los atributos de objetos hay que hacerlo a partir del objeto self.
'''

from math import sqrt

# Definición de Clases:

class Punto():
    '''
    Representación de un punto en el plano, los atributos son x e y que representan
    los valores de sus coordenadas cartesianas
    '''
    # Constructor
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
    
    def mostrar(self) -> str:
        return str(self.x) + ":" + str(self.y)
    
    def distancia(self, point):
        # Devuelve la distancia entre ambos puntos
        dx = self.x - point.x
        dy = self.y - point.y
        
        return sqrt((dx*dy + dy*dy))
    
# Instanciar objetos de la clase Punto
a = Punto()
b = Punto(4,6)

# Llamada a método de la clase en los objetos
print(a.mostrar())
print(b.mostrar())

print(a.distancia(b))

a.x = 10
a.y = 10

print(a.mostrar())
print(a.distancia(b))


##########################  FIN POO  ################################

##########################  EXTRA  ################################
class Stack():
    
    def __init__(self, stack: list = []) -> None:
        self.stack = stack

    def add(self, value) -> None:
        self.stack.append(value)
        print(f'Se ha añadido el elemento {value} a la pila')
        
    def print_elements(self):
        return self.stack if len(self.stack) > 0 else "No hay elementos en la pila"
    
    def count(self) -> int:
        return len(self.stack)

    def pop(self) -> None:
        if len(self.stack) > 0:
            print(f'Se ha eliminado {self.stack.pop()} de la pila')
        else:
            print('La pila está vacía')
            
    def get_value(self, position: int = 0):
        if position < len(self.stack) and position >= 0:
            return self.stack[position]

class Queue():
    
    def __init__(self, queue: list = [])-> None:
        self.queue = queue
    
    def add(self, value: int) -> None:
        if self.queue.insert(0,value):
            print(f'Se ha añadido el elemento {value} a la cola.')
    
    def count(self) -> int:
        return len(self.queue)

    def print_elements(self):
        return self.queue if len(self.queue) > 0 else "No hay elementos en la cola"
    
    def pop(self) -> None:
        if len(self.queue) > 0:
            print(f'Se extraido el elemento {self.queue.pop()} de la cola')
        else:
            print('No hay elementos en la cola')
            
    def get_value(self, position: int = 0):
        if position < len(self.queue) and position >= 0:
            return self.queue[position]


my_stack = Stack([i for i in range(1,11)])
print('Inicio de Pila')
print(my_stack.count())
print(my_stack.get_value(2))
my_stack.pop()
my_stack.add(55)
print(my_stack.print_elements())
my_stack.pop()
print(my_stack.print_elements())

my_queue = Queue([i for i in range(1,11)])

print('Inicio de Cola')
print(my_queue.count())
print(my_queue.get_value(2))
my_queue.pop()
my_queue.add(55)
print(my_queue.print_elements())
my_queue.pop()
print(my_queue.print_elements())
print('Fin de Cola')
##########################  FIN EXTRA  ################################
