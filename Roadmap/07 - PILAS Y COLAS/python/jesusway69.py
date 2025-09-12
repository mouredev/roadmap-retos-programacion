import os
#os.system('clear') #MAC/LINUX
os.system('cls') #WINDOWS
import collections

"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
"""


#MÉTODO PILA (LIFO)
def pila (my_list):
 for i in range (1,11):# Generamos números del 1 al 10
    my_list.append(i)# Los añadimos a la lista
 print(my_list)# Imprimimos la lista con los 10 números
 eliminado = my_list.pop()# El método pop elimina el último elemento de la lista si no le pasamos ningún índice
 print("Eliminamos el número", eliminado)# Mostramos el número eliminado
 print(my_list,"\n")# imprimimos la lista con el último elemento eliminado


#MÉTODO COLA (FIFO)
def cola (my_list):
  for i in range (1,11):# Generamos números del 1 al 10
    my_list.append(i)# Los añadimos a la lista
  print(my_list)# Imprimimos la lista con los 10 números
  eliminado = my_list.pop(0)# El método pop elimina el elemento de la lista cuyo índice le pasemos
  print("Eliminamos el número", eliminado)# Mostramos el número eliminado
  print(my_list,"\n")# imprimimos la lista con el primer elemento eliminado

#MËTODO COLA (FIFO) CON MÉTODO DEQUE
def cola_deque (my_list):
  my_list = collections.deque(range(1,11))# Generamos y añadimos números del 1 al 10
  print(my_list)# Imprimimos la lista con los 10 números
  eliminado = my_list.popleft()# El método popleft elimina el primer elemento de la lista (no admite argumentos)
  print("Eliminamos el número", eliminado)# Mostramos el número eliminado
  print(my_list,"\n")# imprimimos la lista con el primer elemento eliminado

my_list = []
pila(my_list)
my_list = []
cola(my_list)
my_list = []
cola_deque(my_list)


"""
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def browser(my_list: list):
 
 while len(my_list)>=1:
   print("Estás en la web:",my_list[len(my_list)-1])
   order = input("Introduzca web o escriba back para retroceder:")
   order = order.lower()
   print()

   if order == "back":
     my_list.pop()

   else:
     my_list.append(order)

my_list = ["inicio.com"]
browser(my_list)

def printer ():
 
  while len(my_list)>=0:
    print("\nLista de documentos a imprimir:", my_list, "\n")
    order = input("Introduzca un documento , escriba print para imprimir o exit para salir:")
    order = order.lower()
    print()

    if order != "print" and order != "exit":
      my_list.append(order)

    elif order == "exit":
     print("Fin del programa")
     return
    
    elif len(my_list)==0:
      print ("\nCola de impresión vacía, añada un documento o escriba exit para salir")

    elif order == "print" and len(my_list)>0:
      print("\nimprimiendo el documento:",my_list.pop(0))
     
    
    
my_list = []
printer()