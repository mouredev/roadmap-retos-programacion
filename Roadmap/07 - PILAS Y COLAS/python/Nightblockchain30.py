'''
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
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
 *   interpretan como nombres de documentos.
 */
'''

# <<<< PILAS >>>>
pila =  [1,2,3,4,5]

## ¿Cómo puedo introducir elementos nuevos a mi pila?-> Método append()
pila.append(6)
print(pila)
## ¿Cómo puedo recuperar elementos de mi pila? Teniendo en cuenta el formata LIFO -> Método pop()
elemento_extraido_pila = pila.pop();
print(f"Estado pila: {pila}, Elemento extraido = {elemento_extraido_pila}")

# CASO DE USO
for i in range(len(pila)):
    elemento_target = pila.pop()
    print(pila)


# <<<< COLAS >>>>
cola = [1,2,3,4,5]
## ¿Cómo puedo introducir elementos nuevos a mi cola?-> Método append()
cola.append(6)
print(cola)
## ¿Cómo puedo recuperar elementos de mi cola? Teniendo en cuenta el formata FIFO -> Método pop()
elemento_extraido_cola = cola.pop(0)
print(f"Estado cola: {cola}, Elemento extraido = {elemento_extraido_cola}")

# CASO DE USO
for i in range(len(cola)):
    elemento_target = cola.pop(0)
    print(cola)




#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.

historial_navegación = []

while True:
    option = int(input("¿Qué deseas hacer en nuestro navegador? Ir a una página (1) | Adelante (2) | Atrás (3) | Salir (4) \n"))

    match option:
        case 1:
            path = str(input(f"Introduce la ruta a la cual deseas ir: \n"))
            #Agregamos al historial la web visitada
            historial_navegación.append(path)
        case 2:
            pass
        case 3:
                if len(historial_navegación) > 0:
                    historial_navegación.pop()
        case 4: 
            print("Saliendo del navegador web")
            break
    
    if len(historial_navegación) > 0:
        print(f"Estado Historial: {historial_navegación}")
    else:
        print("Estás en la página principal")

# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.

def shared_printer():
    queue = []

    while True:
        option = str(input("Introduce el documento que deseas añadir o la palabra 'imprimir' para imprimir o 'salir' \n"))
    
        if option == "salir":
            break
        elif option == "imprimir":
            print(f"Imprimiendo el documento {queue.pop(0)}")
        else:
            queue.append(option)

        if len(queue) > 0:
            print(queue)
        else:
            print("La cola de impresión esta vacía! ")


shared_printer()




