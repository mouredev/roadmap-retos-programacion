'''EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
o lista (dependiendo de las posibilidades de tu lenguaje).'''
from collections import deque
# La lista en python funciona por defecto como pila, es más eficiente que una pila o cola


# pila / stack
lista = []              
lista.append(11)        # Inserción al final de la lista
lista.append(13)        # se le llama push a añadir, a apilar
lista.append(15)
print (lista)           # [11, 13, 15]
lista.pop (1)           # elimino el index 1 que es el 13
print (lista)           # [11, 15]
                        #la longitud de la lista es 3 pero en index son 2 (0,1,2) de ahí el -1 en la posición
num_desapilar = lista[len(lista)-1] 
print (num_desapilar)   # 15
                        # Eliminar elementos de la pila (pop) El último en entrar es el primero en salir LIFO 
del lista[len(lista)-1] # elimino el último por índice, el 15   "desapilar"
print (lista)           # [11]
lista.pop ()            # elimino por defecto el último añadido, el 11   
print (lista)           # []
print()


# cola / queue  FIFO Lista doblemente finalizada, fácil para insertar/eliminar en principios o finales
mi_deque = deque()
mi_deque.append(1)      # push / inserción igual que en la pila
mi_deque.append(2)      # pero se le llama encolar = enqueue
mi_deque.append(3)
print (mi_deque)        # deque([1, 2, 3])  
mi_deque.appendleft(5)  # inserta al principio
print (mi_deque)        # deque([5, 1, 2, 3]) 
print("Posición 1: ", mi_deque[1]) 
                        # la posicioon 1 es el 1, la 0 es el 5 que acabamos de añadir
mi_deque.pop()          # desencolar / dequeue / elimina el último que es el 3 / actúa como pila
print (mi_deque)        # deque([5, 1, 2]) 
mi_deque.popleft()      #elimina el primero que es el 5
print(mi_deque)         # deque([1, 2])
print()


''' DIFICULTAD EXTRA (opcional):
* Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
* Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.'''



'''No conseguía desplazarme por los items de la lista, quería que se fueran imprimiendo una tras otra, pero en el ejercicio
resuelto de Moure se introduce la web completa, quedando la lista así:
['moure.dev', 'moure.dev/inicio', 'moure.dev/inicio/cursos'] '''

def navega ():
    stack =[]
    while True:        # Bucle infinito 
        
        print ("""*********************************\nAdvertencia: Esto es un simulador no un navegador.\nIntroduce 'adelante/atras/salir' o el nombre de la web donde quieres ir.\nPor ejemplo: moure.dev/inicio/cursos/python ... etc.\nNo es necesario introducir 'http://'  pero recuerda incluir la web completa :\n*********************************""")
        introducido = input ()
        
        if introducido == "adelante":
            # No se puede solucinar con una pila, porque al ir atrás he borrado el último y no tengo ninguno al que avanzar
            print()
            print ( "---> Error 404 Página no encontrada") 
                    
        elif introducido == "atras":
            if len (stack) == 1:
                print()
                print ("---> Estás en la página principal no puedes volver atrás.")

            elif len (stack) > 1:
                stack.pop()
                   
        elif introducido == "salir":
            print()
            print ("---> Has terminado de navegar. Adiós.")
            break
        else:
            stack.append(introducido)

        print()                   
        print (f"---> Estás en la web: http://{stack[len(stack)-1]}")    # imprimo el último de la fila
        
navega()

def impresora ():
    lista_documentos :list = []
    while True:

        print ("""*********************************\nIntroduce el nombre del documento a imprimir o 'salir'.\nPor ejemplo: factura.psd\nCuando quieras empezar la impresión escribe 'imprimir' para imprimir en orden, o 'imprimir' seguido del docuemnto que desee.\n*********************************""")
        a_imprimir = input ()
        
        if a_imprimir == "imprimir":
            if len(lista_documentos) >0:
                print(f"---> Se está imprimiendo el archivo {lista_documentos.pop(0)}")
                if len(lista_documentos) ==0:
                    print ("---> No quedan documentos a imprimir. Lista vacía")
            else:
                print ("---> No quedan documentos a imprimir. Lista vacía")
                
        elif "imprimir" in a_imprimir:
            if len(lista_documentos) >0:
                nombre_concreto = a_imprimir.strip("imprimir ")
                # print ("Nombre concreto:" + nombre_concreto)  #comprobación ok
                if nombre_concreto in lista_documentos:
                    print()
                    print (f"---> Se está imprimiendo el archivo {nombre_concreto}")
                    lista_documentos.remove(nombre_concreto)
                    if len(lista_documentos) ==0:
                        print ("---> No quedan documentos a imprimir. Lista vacía")
                else:
                    print ("---> Archivo no encontrado. Comprueba si está en la cola de impresión.")
            
        elif a_imprimir == "salir":
            print()
            print ("---> Impresión terminada. Adiós.")
            break
        else:
            lista_documentos.append(a_imprimir)
        print()
        print (f"---> Cola de impresión pendiente: {lista_documentos}")  
        
impresora ()

# Fin del ejercicio

#-----------------------------------------------------------------------------------------
# mis pruebas de salida para ver el formato
mi_web: list = ["index"]
mi_web.append ("segunda")
inicio : str =mi_web[0]
print()
print("http://" + inicio)               # http://index  
print ("http://", mi_web)               # http:// ['index', 'segunda']
print (f"http://", {inicio})            # http:// {'index'}
print ("http://",mi_web[0:])            # http:// ['index', 'segunda']
temp=str(mi_web[0:])
print(f"http://" + temp)                # http://['index', 'segunda']  Ya no hay espacio, pero sigue saliendo [] y '
print(f"http://" + temp.strip(("[']"))) # http://index', 'segunda      Sigue saliendo '
mi_web.pop()
print(f"http://" + str(mi_web[0:]))     # http://['index']  Ya no hay espacio, pero sigue saliendo [] y '
print()

#def imprime_web (mi_web):
#   for pagina in mi_web:
#        print (f"Estás en esta página http://" + pagina ) # Aquí se imprime con index limpio pero una línea por cada página
#imprime_web (mi_web)