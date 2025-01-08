# #07 PILAS Y COLAS
## Ejercicio
'''
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */
'''
class Stack: #LIFO 
    def __init__(self):#Constructor de la clase
        self.stack = [] #Inicializamos la pila como una lista vacía

    def push(self, item): #Metodo para añadir elementos a la pila
        self.stack.append(item) #Añadimos el elemento al final de la lista

    def pop(self): #Metodo para eliminar elementos de la pila
        return self.stack.pop() #Eliminamos el ultimo elemento de la lista y lo retornamos

    def __str__(self): #Metodo para imprimir la pila
        return str(self.stack)
    
class Queue: #FIFO
    def __init__(self): #Constructor de la clase
        self.queue = [] #Inicializamos la cola como una lista vacía

    def push(self, item): #Metodo para añadir elementos a la cola
        self.queue.append(item) #Añadimos el elemento al final de la lista

    def pop(self): #Metodo para eliminar elementos de la cola
        return self.queue.pop(0) #Eliminamos el primer elemento de la lista y lo retornamos

    def __str__(self): #Metodo para imprimir la cola
        return str(self.queue)   
        
'''
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''
class NavegadorWeb:
    def __init__(self): #Constructor de la clase
        self.back = Stack() #Inicializamos la pila de retroceso
        self.forward = Stack() #Inicializamos la pila de avance
        self.current = '' #Inicializamos la pagina actual
        
    def go_to(self, url): #Metodo para ir a una pagina
        self.back.push(self.current) #Añadimos la pagina actual a la pila de retroceso
        self.current = url #Cambiamos la pagina actual por la nueva
        self.forward = Stack() #Vaciamos la pila de avance
        
    def back(self): #Metodo para retroceder
        if not self.back.empty(): # Si la pila de retroceso no esta vacia
            self.forward.push(self.current) #Añadimos la pagina actual a la pila de avance
            self.current = self.back.pop() #Cambiamos la pagina actual por la ultima pagina visitada
    
    def forward(self): #Metodo para avanzar
        if not self.forward.empty(): #Si la pila de avance no esta vacia
            self.back.push(self.current) #Añadimos la pagina actual a la pila de retroceso
            self.current = self.forward.pop() #Cambiamos la pagina actual por la ultima pagina visitada
            
    def __str__(self): #Metodo para imprimir la pagina actual
        return self.current #Retornamos la pagina actual
    
class Impresora: #Clase impresora  
    def __init__(self): #Constructor de la clase
        self.queue = Queue() #Inicializamos la cola de impresion 
        
    def print(self, document): #Metodo para añadir documentos a la cola de impresion
        self.queue.push(document) #Añadimos el documento a la cola de impresion
        
    def print_next(self): #Metodo para imprimir el siguiente documento
        return self.queue.pop() #Eliminamos el primer documento de la cola de impresion y lo retornamos
    
    def __str__(self): #Metodo para imprimir la cola de impresion
        return self.queue.__str__() #Retornamos la cola de impresion
        