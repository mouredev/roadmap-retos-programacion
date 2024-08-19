""" * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje)."""

""" Creamos la Pila / Stack """
stack = []

""" Añadir elementos (LIFO) """
stack.append("primero")
print(stack)
stack.append("segundo")
print(stack)
stack.append("tercero")
print(stack)
stack.append("cuarto")
print(stack)


""" Eliminar / Desapilar elementos (LIFO) """
print(stack.pop()) # Utilizamos el método pop para quitar el ultimo elemento que haya entrado " len()-1 "
print(stack)
print(stack.pop())
print(stack)

print(stack[len(stack)-1])
del stack[len(stack)-1] # Estamos eliminado el elemeto en la ultima posición
print(stack)


""" Cola / Queue (FIFO) """
stack.append("Cola 1")
print(stack)
stack.append("Cola 2")
print(stack)
stack.append("Cola 3")
print(stack)


""" Eliminar / Desencolar 'Dequeue' """
print(stack.pop(0))
print(stack)
print(stack.pop(0))
print(stack)

print(stack[0])
del stack[0] # Estamos eliminado el elemeto en la primera posición
print(stack)


""" * DIFICULTAD EXTRA (opcional):
 *   Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web."""


def web_navegation():
    web = ["home"]
    restaurarWeb = []
    while True:
        action = input("Añade una url o interactua con palabras adelante/atrás/salir: ")
        match action: 
            case "salir":
                print("Cerraste el navegador.")
                break
            case "atrás":
                if len(web) > 1:
                    restaurarWeb.append(web.pop()) # Quitando el elemento de la web y guardandola en otra lista
                else:
                    print("Se encuentra en el inicio: ")
            case "adelante":
                if len(restaurarWeb) > 0:
                    web.append(restaurarWeb.pop()) # Devolviendo el elemento eliminado de la web
            case _:
                web.append(action) # "Navegando"
        print(web)
web_navegation()


""" *   Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
    *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
    *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
    *   interpretan como nombres de documentos."""

def printer_actions():
    documents = []
    while True:
        action = input("Añade un documento / ingresa (imprimir) ó (salir)")
        match action: 
            case "salir":
                print("Saliste de la impresora.")
                break
            case "imprimir":
                if len(documents) > 0:
                    print(f"Imprimiendo Documento: {documents.pop(0)}") # Quitando el elemento de la lista de documents
                else:
                    print("No tiene documentos en la cola de impresión")
            case _:
                documents.append(action) # "añadienod documento"
        print(f"Cola de impresión: {documents}")

printer_actions()