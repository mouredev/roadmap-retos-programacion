""" /*
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
 */ """

""" Pilas / Stacks  --> LIFO """

""" En python no existen las pilas o colas como tal pero usando listas se puede suplir ese
    requerimiento."""

pila = ["Lunes", "Martes"]

""" Por ejemplo: un push se podria ver como un ... """

pila.append("miercoles")
print(pila)

""" Un pop se veria como: """

print(pila.pop())
print(pila)


""" Colas / Queues  --> FIFO"""

cola = ["Manzana", "Pera"]

""" Un queue item seria igual """

cola.append("Sandia")
print(cola)

""" un unqueue item seria """

print(cola.pop(0))
print(cola)


""" * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */  """


def navegador():

    historial = []
    actual = 0
    print("Salir - Para salir del sistema")
    print("adelante - Para avanzar en el hisotrial")
    print("atras - Para retroceder en el hisotrial")
    print("URL - Para navegar a la URL")
    print("----------------------------------------")

    while 1:

        command = input("Ingrese un comando.")
        print("")

        match command:
            case "salir":
                print("Saliendo del sistema ...")
                break

            case "adelante":

                actual += 1

                if actual - 1 >= len(historial):
                    actual = len(historial)
                    print("Ya no se puede avanzar mas")
                    print("------------------------------------------")
                else:
                    print(f"Se avanzo a la pagina {historial[actual-1]}")
                    print("------------------------------------------")

            case "atras":

                if actual <= 1:
                    actual = 0
                    print("Ya no se puede retroceder mas")
                    print("------------------------------------------")
                else:
                    actual -= 1
                    print(f"Se retrocedio a la pagina {historial[actual-1]}")
                    print("------------------------------------------")

            case _:

                historial = historial[0:actual]
                historial.append(command)

                actual += 1

                print(f"Se navego al pagina {historial[actual-1]}")
                print("------------------------------------------")


# navegador()


def impresora():

    cola = []
    while 1:

        op = input("Ingrese operacion [nombre_documento|imprimir]\n")

        match op:
            case "salir":
                print("Saliendo ...")
                break
            
            case "imprimir":

                if len(cola) > 0:
                    documento = cola.pop(0)
                    print(f"Imprimiendo docuemnto '{documento}' ...")
                else:
                    print("No hay nada que imprimir ...")

            case _:
                cola.append(op)
                print(f"Documento '{op}' ingresado en cola")

impresora()