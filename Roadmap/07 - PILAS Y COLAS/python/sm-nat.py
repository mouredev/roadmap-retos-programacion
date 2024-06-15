#Pila (Stack - LIFO)
pila = []

pila.append(1)
pila.append(2)
pila.append(3)

print("Pila después de los push:", pila)  

ultimo_elemento = pila.pop()

print("Elemento eliminado (pop):", ultimo_elemento) 
print("Pila después del pop:", pila) 

#Cola (Queue - FIFO)
cola = []

cola.append(1)
cola.append(2)
cola.append(3)

print("Cola después de los enqueue:", cola) 

primer_elemento = cola.pop(0)

print("Elemento eliminado (dequeue):", primer_elemento)  
print("Cola después del dequeue:", cola)

#EXTRA
"""Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos."""


def navegador_web():
    historial = []  

    while True:
        comando = input("Introduce una página o 'adelante' o 'atrás' o 'salir': ").strip().lower()
        if comando == "salir":
            print("Saliendo...")
            break
        elif comando == "adelante":
           pass
        elif comando == "atrás":
            if len(historial) > 0:
                historial.pop()
            else:
                historial.append(comando)
                print("Página actual:", historial.len(historial[-1]))
            
        else:
            historial.append(comando)
            print("Página actual:", comando)

navegador_web()

#Impresora compartida

def impresora_compartida():
    cola_imprimir = []
    while True:
        comando = input("Introduce un documento o 'imprimir' o 'salir': ")
        if comando.lower() == "salir":
            print("Saliendo...")
            break
        elif comando.lower() == "imprimir":
            if len(cola_imprimir) > 0:
                print("Imprimiendo:", cola_imprimir.pop(0))
            else:
                cola_imprimir.append(comando)
        else:
            print("No hay documentos en la cola")