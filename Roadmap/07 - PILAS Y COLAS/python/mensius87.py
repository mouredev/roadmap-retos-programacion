"""
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
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
"""


# FIFO - First In First Out
lista_fifo = []

def introducir_elemento(elem):
    lista_fifo.append(elem)
    print(lista_fifo)


def sacar_elemento():
    elem_sacado = lista_fifo.pop(0)
    print(f"Elemento eliminado: {elem_sacado}")


print("""
    Opciones:
        1 - Añadir elemento a la pila
        2 - Ver pila
        3 - Ver próximo elemento en salir
        4 - Sacar elemento de la pila
        5 - Salir
""")

opcion_elegida = input("Elige una opción: ")

while opcion_elegida != '5':
    match opcion_elegida:
        case '1':
            elem = input("Introduce un elemento: ")
            introducir_elemento(elem)
        case '2':
            print("Pila:", lista_fifo)
        case '3':
            if lista_fifo:
                print("Próximo elemento en salir:", lista_fifo[0])
            else:
                print("La pila está vacía.")
        case '4':
            sacar_elemento()
        case '5':
            print("Gracias por usar la pila.")
            break
        case _:
            print("Opción no válida.")

    opcion_elegida = input("Elige una opción: ")


# LIFO - Last In First Out
