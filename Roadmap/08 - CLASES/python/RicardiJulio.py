# EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  */

class Miclase():
    atributo1 = 'valor1'#---> Atributos de clase
    atributo2 = 'valor2'
    def __init__(self,argumento1):
        self.argumento1 = argumento1#---> Atributo de instancia
    def funcion1(self):#---> Funcion de clase
        print('Esta es la funcion 1')
    
objeto = Miclase('Primer argumento')

print(objeto.atributo1)
print(objeto.atributo2)
print(objeto.argumento1)
objeto.funcion1()

objeto.atributo1 = 'Valor modificado'
objeto.atributo2 = 'Valor modificado'
objeto.argumento1 = 'Primer valor modificado'

print(objeto.atributo1)
print(objeto.atributo2)
print(objeto.argumento1)

# DIFICULTAD EXTRA:

class Pila(): # Pila LIFO (Last In, First Out)
    pila = []
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def añadir(self,valor):
        self.pila.append(valor)
        print(f'Se ha añadido {valor} a {self.nombre}')
    
    def eliminar(self):
        print(f'Se ha eliminado {self.pila[-1]} de {self.nombre}')
        self.pila.pop()
    
    def retornar_elementos(self):
        print(f'El numero de elementos de {self.nombre} es {len(self.pila)}')
    
    def imprimir(self):
        print(self.pila)
        
pila = Pila('Mi pila')

pila.añadir('Elemento')
pila.añadir('Elemento1')
pila.añadir('Elemento2')
pila.añadir('Elemento3')

pila.imprimir()
pila.retornar_elementos()

pila.eliminar()

pila.imprimir()
pila.retornar_elementos()

class Cola():
    from collections import deque
    cola = deque([])
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def añadir(self,valor):
        self.cola.append(valor)
        print(f'Se ha añadido {valor} en {self.nombre}')
        
    def eliminar(self):
        print(f'Se ha eliminado {self.cola[0]} de {self.nombre}')
        self.cola.popleft()
    
    def retornar_elementos(self):
        print(f'El numero de elementos de {self.nombre} es {len(self.cola)}')
        
    def imprimir(self):
        print(self.cola) 
        
cola = Cola('Mi cola xD')

cola.añadir('Elemento')
cola.añadir('Elemento1')
cola.añadir('Elemento2')
cola.añadir('Elemento3')

cola.imprimir()
cola.retornar_elementos()

cola.eliminar()

cola.imprimir()
cola.retornar_elementos()
