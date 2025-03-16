'''
/*
 * EJERCICIO:
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
 */
'''

# Declaramos una clase en Python
class ejemplo:
    #Inicializamos la clase 
    def __init__(self, saludo,nombre):
        #Atributos de la clase
        self.saludo= saludo
        self.nombre= nombre
    
    def saludar(self): #Esta es la función que va a imprimir los atributos de la clase tambien llamado método
        print(f'{self.saludo},{self.nombre}')

#Creamos instancias de la clase ejemplo 
saludo = ejemplo("Hola","Alexdevrep")
saludo.saludar()
#Modificamos los atributos de la clase 
saludo.nombre = "Python"
saludo.saludar() #instancia (saludo).método(saludar)()



#Dificultad EXTRA
#Pilas
class Pila:
    def __init__(self):
        self.elementos = []
    
    def añadir(self, elemento):
        self.elementos.append(elemento)
    
    def eliminar(self):
        if len(self.elementos) == 0:
            print("La pila está vacía")
            return
        else:
            return self.elementos.pop()
    
    def imprimirTodo(self):
        if len(self.elementos)==0:
            print("La pila está vacía")
            return
        else:
            print("Contenido de la pila")
            for index, elemento in enumerate(self.elementos, start=1) :
                print(index,elemento)
                

    def numeroElementos(self):
        return len(self.elementos)


#Creamos la instancia de la clase 
miPila= Pila()

#Añadimos elementos a la pila

miPila.añadir("Objeto 1")
miPila.añadir("Objeto 2")
miPila.añadir("Objeto 3")

miPila.imprimirTodo()

#Eliminamos el último elemento añadido en la Pila
miPila.eliminar()
miPila.imprimirTodo()

#Comprobamos que el número de elementos en la pila es el correcto (2)
numero=miPila.numeroElementos()
print(f'El número de elementos que hay en la Pila es {numero}')

#Colas
#Importamos las librerías necesarias
from collections import deque

class Cola:
    def __init__(self):
        self.objetos =deque([])
    def insertar(self, objeto):
        self.objetos.append(objeto)
    def borrar(self):
        if len(self.objetos)==0:
            print("La cola está vacía")
            return
        else:
            return self.objetos.popleft()
    def imprimir(self):
        if len(self.objetos)==0:
            print("La cola está vacía")
            return
        else:
            print("Contenido de la Cola")
            for index , objeto in enumerate(self.objetos, start=1):
                print(index,objeto)
    
    def numeroObjetos(self):
        return len(self.objetos)


#Creamos una nueva instancia
miCola = Cola()

miCola.insertar("Objeto 1")
miCola.insertar("Objeto 2")
miCola.insertar("Objeto 3")

#Imprimimos los objetos que hay en la cola
miCola.imprimir()

#Vamos a eliminar el primer objeto añadido a la cola 
miCola.borrar()
miCola.imprimir()

#Comprobamos que la cola tiene los objetos deseados despues de la modificación (2)
numeroObjetos=miCola.numeroObjetos()
print(f'El número de objetos que hay en la cola es: {numeroObjetos}')


        

            



        