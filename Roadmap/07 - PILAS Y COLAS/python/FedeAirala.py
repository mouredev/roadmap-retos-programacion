# 07 Pilas y Colas con Python

"""
    Breve resumen: las pilas y las colas son estructuras de datos en el orden en que ingresan y en el que salen de 
    la misma tiene un orden. Los datos entran a la estructura de manera ordena y el orden en el que salen en una pila
    es de forma descendente, esto quiere decir que el último en ingresar es el primero en salir en cambio en las colas
    es de forma ascendente, el primero en entrar es el primero en salir, todo esto hasta que no queden datos por
    recorrer en la estructura.

"""


# Ejemplo de Cola deque

from collections import deque  # Librería en Python para tratar las pilas y colas

cola = deque()     # Estructura de tipo cola
cola.append(0)     # Con append se insertan datos a la cola
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)

print (f" Cola completa: {cola}") # Impresión de cola completa


for i in range (len(cola)):
    sacar_datos = cola.popleft()              # popleft va retirando los datos de la cola de manera ascendente
    print (f"Dato extraído: {sacar_datos}")
    print (f"Datos que quedan en la cola: {cola}")

# Ejemplo de cola con listas
    

cola=[]
cola.append(0)
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)

for i in range (len(cola)):
    print (cola[i])
    

# Ejemplo de Pilas deque
    
pila = deque()     # Estructura de tipo pila
pila.append(0)     # Con append se insertan datos a la pila
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)

print (f" Pila completa: {pila}") # Impresión de pila completa


for i in range (len(pila)):
    sacar_datos = pila.pop()              # pop va retirando los datos de la pila de manera descendente
    print (f"Dato extraído: {sacar_datos}")
    print (f"Datos que quedan en la cola: {pila}")

"""Otras formas de trabajar con pilas y colas es con la estructiura de listas, ya que estas se pueden tratar
    con el concepto de las mismas variando en cuestios """

# Ejemplo de pilas con listas

#Pilas

pila = []
pila.append (0)
pila.append (1)
pila.append (2)
pila.append (3)
pila.append (4)

n = len(pila)

for i in range (n):
    print (pila[n-i-1])

   



""" * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

# Primer ejercicio de dificulta extra: Pila

list_web = []
index=0

def list_empty(list_web):
    if len(list_web)==0:
        print ("Lista vacía")
        return True
    else:
        return False

def navegador_web():
    while True:
        accion = input (" 1 Buscar web  !  2 Atrás  ! 3 Adelante  ! 4 Listar Web's  ! 5 Sacar web de lista  !  6 Salir")
        global index
        match accion:
                case "1":
                    web = input("Ingrese nombre de la web:")
                    list_web.append(web)
                    index+=1
                    print(list_web)
                
                case "2":
                    if  not list_empty(list_web):
                        if index==1:
                            print (f"Estás en la primer página: {list_web[index-1]}")
                        else:
                            index-=1
                            print (list_web[index-1])
                        
                case "3":
                    if  not list_empty(list_web):
                        if index == (len(list_web)):
                            print (f"Estás en la última página: {list_web[index-1]}")

                        else:
                            index+=1
                            print (list_web[index-1])
                       
                case "4":
                    print (f"Listado de web ingresadas: {list_web}")
                
                case "5":
                    if  not list_empty(list_web):
                        list_web.pop()
                        print (list_web)
                        index -= 1
                    
                case "6":
                    print("Saliendo de la aplicación.")
                    break
                    
                case _:
                    print("Opción no válida. Elige una opción del 1 al 5.")
                  
navegador_web()

# Segundo ejercicio dificultad extra: Cola

doc_print = deque() 

index_2 = 0
doc = 0
doc_impresos = []
def doc_empty(doc_print):
    if len(doc_print)==0:
        print ("No hay documentos en la cola de impresión")
        return True
    else:
        return False

def print_doc():
    while True:
        accion = input (" 1 Imprimir  !  2 Ingresar Documento   ! 3 Listar Documentos    !  4 Documentos impresos  !  5 Salir")
        global index_2,doc

        match accion:

            case "1":
                index_2 -= 1
                if not doc_empty(doc_print):
                    print(doc_print[index])
                    doc_impresos.append(doc_print[index])
                    doc_print.popleft()

            case "2":
                print ("Ingreso de documento a la cola de impresión")
                doc+=1
                doc_print.append(doc)
                print (doc_print)
                
            case "3":
                 print (f"En cola de impresión: {doc_print}")
            
            case "4":
                print (doc_impresos)
                 
            case "5":
                print ("Saliendo de impresión")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 4.")

print_doc()               


