
#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).

# pilas
lista = [1,2,3]
print(lista)
elemento = lista.pop() # la funcion pop extrae el ultimo elemento que entro en la pila
print(lista)
print(elemento)

# colas
lista = [1,2,3]
print(lista)
elemento = lista.pop(0) # la funcion pop indicando el indice que queremos eliminar de la cola
print(lista)
print(elemento)


#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.

def navigation():
    historial = []

    while True:

        accion = input("Agrega una URL o si quieres desplazarte adelante/atras/salir: ")
        if accion == 'salir':
            print("Saliendo del programa")
            break
        elif accion == 'adelante':
            pass
        elif accion == "atras":
            if len(historial) > 0:
                historial.pop()
        else:
            historial.append(accion)

        if len(historial) > 0:
            print(f'Pagina actual {historial[len(historial)-1]}')
        else:
            print('Estas en la pagina de inicio')
        

navigation()


#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.

def impresora():
    cola_impresion = []
    while True:
        instruccion = input("Agrega un documento a la cola de impresion, o indica si quieres imprimir o salir: ")

        if instruccion == 'imprimir':
            if len(cola_impresion) >= 1:
                print(f'imprimiendo documento: {cola_impresion[0]}')
                cola_impresion.pop(0)
            else:
                print('no quedan documentos en cola')
        elif instruccion == 'salir':
            break
        else:
            cola_impresion.append(instruccion)

        if len(cola_impresion) >= 1:
            print('Documentos en cola')
            for doc in cola_impresion:
                print(doc)

impresora()