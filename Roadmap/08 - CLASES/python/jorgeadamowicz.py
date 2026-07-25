"""
EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 """

### EJERCICIO: ###
class Persona:
    #metodo inicializador
    def __init__(self, nombre, edad, actividad):
        self.nombre = nombre
        self.edad = edad
        self.actividad = actividad
    
    #metodo para imprimir atributos de clase a traves del metodo __str__
    def __str__(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad} \nActividad: {self.actividad} \n"
    
    #metodo que muestra los atributos de clase
    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad} \nActividad: {self.actividad}\n")
    
#instancia de clases
persona1 = Persona("juank", 25 , "Programador")

#llamo al método mostrar_atributos
persona1.mostrar_atributos()

#modifico atributo de clase
persona1.nombre = "Juan Gabriel"

#llamo al método __str__
print(persona1)

### DIFICULTAD EXTRA: ###

## Pila (LIFO)##
class Pila:
    #metodo inicializador
    def __init__(self):
        self.pila = []
        
    #metodo 'Push' que añade un elemento a la pila    
    def añadir_elemento(self, elemento):
        self.pila.append(elemento)
        
    #metodo 'Pop' que elimina un elemento de la pila
    def eliminar_elemento(self):
        #verifica que la pila no este vacia
        if self.contar_elementos() == 0:
            #retorna None si la pila esta vacia
            return None
        return self.pila.pop()
        
    
    #metodo 'Count' que retorna el numero de elementos de la pila
    def contar_elementos(self):
        return len(self.pila)
    
    #metodo 'Print' que imprime el contenido de la pila
    def imprimir_elementos(self):
        #recorre la lista de manera inversa
        for elemento in reversed(self.pila): #reverse() invierte los valores de la secuencia dada 
            print(elemento)

#creo una instacia de la clase Pila
mi_pila = Pila()
#añado elementos a la pila
mi_pila.añadir_elemento("elemento 1")
mi_pila.añadir_elemento("elemento 2")
mi_pila.añadir_elemento("elemento 3")
mi_pila.añadir_elemento("elemento 4")
#muestro la lista de elementos
mi_pila.imprimir_elementos()
#muestro la cantidad de elementos
print(f"la cantidad de elementos es: {mi_pila.contar_elementos()}\n")

#elimino un elemento de la pila
mi_pila.eliminar_elemento()
#muestro la lista de elementos
mi_pila.imprimir_elementos()
#muestro la cantidad de elementos
print(f"la cantidad de elementos es: {mi_pila.contar_elementos()}\n")


## Cola (FIFO)##

class Cola:
    #metodo inicializador
    def __init__(self):
        self.cola = []
    
    #metodo 'enqueue' que añade un elemento a la cola
    def añadir_elemento(self, elemento):
        self.cola.append(elemento)
        
    #metodo 'dequeue' que elimina un elemento de la cola
    def eliminar_elemento(self):
        #verifica que la cola no este vacia
        if self.contar_elementos() == 0:
            #retorna None si la cola esta vacia
            return None
        #se elimina el primer elemento de la cola indicando el indice '0'
        return self.cola.pop(0)
    
    #metodo 'Count' que retorna el numero de elemntos de la cola
    def contar_elementos(self):
        return len(self.cola)
    
    #metodo 'Print' que imprime el contenido de la cola
    def imprimir_elementos(self):
        for elemntos in self.cola:
            print(elemntos)
            
#creo una instancia de la clase Cola
mi_cola = Cola()
#añado elementos a la cola
mi_cola.añadir_elemento("elemento 1")
mi_cola.añadir_elemento("elemento 2")
mi_cola.añadir_elemento("elemento 3")
mi_cola.añadir_elemento("elemento 4")

#muestro la lista de elementos
mi_cola.imprimir_elementos()
#muestro la cantidad de elementos
print(f"la cantidad de elementos es: {mi_cola.contar_elementos()}\n")

#elimino un elemento de la pila
mi_cola.eliminar_elemento()
#muestro la lista de elementos
mi_cola.imprimir_elementos()
#muestro la cantidad de elementos
print(f"la cantidad de elementos es: {mi_cola.contar_elementos()}\n")
    
    
    
    