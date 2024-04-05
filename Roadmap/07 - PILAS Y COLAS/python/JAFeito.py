# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).
 
 # DIFICULTAD EXTRA (opcional):
 #- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 #   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 #   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 #   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 #   el nombre de una nueva web.
 # - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 #   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 #   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 #   interpretan como nombres de documentos.
 
 #Solo dificultad extra
lista_pag = ["www.goggle.es","www.microsoft.es","www.youtube.com"]

def navegate (lista_pag):
    posicion = 0
    continuar = True
    while continuar :
        eleccion = input("Escriba 'adelante' o 'atras' para navegar, el nombre de la nueva web o 'exit' para salir:")
        if eleccion == "atras":
            if posicion == 0:
                print (f" {lista_pag[posicion]} es la primera. ")
            else:
                posicion -= 1
                print (lista_pag[posicion])
        elif eleccion == "adelante":
            if posicion == len(lista_pag) - 1:
                print (f" {lista_pag[posicion]} es la ultima. ") 
            else:
                posicion += 1
                print (lista_pag[posicion])
        elif eleccion == "exit":
            continuar = False
            
        else:
            lista_pag.append(eleccion)
            print (f" {eleccion} se ha añadido a la lista.")
navegate(lista_pag)
print(lista_pag)
