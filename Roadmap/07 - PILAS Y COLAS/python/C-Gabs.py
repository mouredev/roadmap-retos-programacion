#Reto 07

'''Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.'''

#Pila
pila = [1,2,3,4,5,6]
print(pila)
pila.append(7)
print(pila)
print(pila.pop())
print(pila)


#Cola
cola = [1,2,3,4,5,6]
cola.insert(0,0)
print(cola)
print(cola.pop())
print(cola)


#Reto Extra

#Adelante/Atras
def navegacion_web():
    webs = []
    tope = []
    while True:
        texto = str(input("Introduzca Adelante/Atras para navegar entre las paginas web, introduzca una nueva web o introduzca 'Salir': \n"))
        if texto.lower() == "adelante":
            if len(tope) > 0:
                webs.append(tope.pop())
                print(f"Estas en la web: {webs[-1]}")
            else:
                print("No hay paginas webs mas recientes\n")
        elif texto.lower() == "atras":
            if len(webs) == 1:
                print("No hay paginas webs mas antiguas\n")
            else:
                tope.append(webs.pop())
                print(f"Estas en la web: {webs[-1]}")
        elif texto.lower() == "salir":
            print("Finaliza el programa")
            break
        else:
            if len(tope) > 0:
                tope.clear()
            webs.append(texto)
            print(f"estas en la web: {texto}")

navegacion_web()
#Imprimir

def impresora_compartida():
    impresora = []
    while True:
        texto = str(input("Introduzca 'imprimir' para imprimir un documento, introduzca un nuevo documento a la cola o introduzca 'Salir': \n"))
        if texto.lower() == "imprimir":
            if len(impresora) == 0:
                print("No hay documentos para imprimir")
            else:
                print(f"Se imprimió el documento: {impresora.pop()}")
        elif texto.lower() == "salir":
            print("Finaliza el programa")
            break
        else:
            print(f"Se añade el documento: '{texto}' a la cola de impresión")
            impresora.insert(0,texto)

impresora_compartida()