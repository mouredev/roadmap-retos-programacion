#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.

class ClasePrincipal:
    def __init__(self, atributo1, atributo2, atributo3):
        self.atributo = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3

    def impresion(self):
        print(f'{self.atributo},{self.atributo2} o {self.atributo3}...una...dos...tres!')

opciones = ClasePrincipal('piedra','piedra', 'tijera') # creamos el objeto de clase, agregamos los atributos

opciones.impresion() # usamos la funcion de la clase, para la impresion
opciones.atributo2 = 'papel' # modificamos atributo
opciones.impresion() 

print('/' * 50)
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.

class Pila():
    def __init__(self):
        self.listado = []
    
    def agregar_elementos(self, elemento):
        if elemento in self.listado:
            print('Ese elemento ya esta en la lista')
        else:
            print(f'Elemento {elemento} agregado a la lista')
            self.listado.append(elemento)
    
    def eliminar_elementos(self):
        if self.contar_elementos == 0:
            print('Lista vacias')
        else:
            print(f'Elemento {self.listado[-1]} eliminado de la lista')
            return self.listado.pop()

    def contar_elementos(self):
        return len(self.listado)
    
    def impresion_lista(self):
        print('Listado actual:')
        for elemento in self.listado[::-1]:
            print(elemento)

pila = Pila()

pila.agregar_elementos('A')
pila.agregar_elementos('B')
print(pila.contar_elementos())
pila.agregar_elementos('C')
print(pila.contar_elementos())
pila.impresion_lista()

pila.eliminar_elementos()
pila.impresion_lista()
pila.eliminar_elementos()
pila.impresion_lista()

print('--------------------------------------------------------------------------------')
class Cola():
    def __init__(self):
        self.listado_cola = []
    
    def agregar_elementos(self, elemento):
        if elemento in self.listado_cola:
            print('Ese elemento ya esta en la lista')
        else:
            print(f'Elemento {elemento} agregado a la lista')
            self.listado_cola.append(elemento)
    
    def eliminar_elementos(self):
        if self.contar_elementos == 0:
            print('Lista vacias')
        else:
            print(f'Elemento {self.listado_cola[-1]} eliminado de la lista')
            return self.listado_cola.pop(0)

    def contar_elementos(self):
        return len(self.listado_cola)
    
    def impresion_lista(self):
        print('Listado actual:')
        for elemento in self.listado_cola:
            print(elemento)

cola = Cola()

cola.agregar_elementos('A')
cola.agregar_elementos('B')
print(cola.contar_elementos())
cola.agregar_elementos('C')
print(cola.contar_elementos())
cola.impresion_lista()

cola.eliminar_elementos()
cola.impresion_lista()
cola.eliminar_elementos()
cola.impresion_lista()