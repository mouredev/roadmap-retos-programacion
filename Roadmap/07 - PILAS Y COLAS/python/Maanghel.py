"""
EJERCICIO:
Implementa los mecanismos de introducción y recuperación de elementos propios de las
    pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
    o lista (dependiendo de las posibilidades de tu lenguaje).

DIFICULTAD EXTRA (opcional):
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
    de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
    que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
    Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
    el nombre de una nueva web.
- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
    impresora compartida que recibe documentos y los imprime cuando así se le indica.
    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
    interpretan como nombres de documentos
"""

def stack_example():
    """Stacks example (LIFO)"""
    stack = []
    while True:
        print("\nSeleccione una opcion:")
        print("1. Ingresar dato\n2. Eliminar dato\n3. Mostrar stack\n4. Salir")
        option = input("\n-> ")

        match option:
            case "1":
                data = input("Ingrese el dato: ")
                stack.append(data)
            case "2":
                if stack:
                    print(stack.pop())
                else:
                    print("El stack está vacío.")
                input()
            case "3":
                print(f"Contenido del stack:\n{stack}")
                input()
            case "4":
                print("Saliendo del ejemplo de Stack")
                break

def queue_example():
    """Queue example (FIFO)"""
    queue = []
    while True:
        print("\nSeleccione una opcion:")
        print("1. Ingresar dato\n2. Eliminar dato\n3. Mostrar cola\n4. Salir")
        option = input("\n-> ")

        match option:
            case "1":
                data = input("Ingrese el dato: ")
                queue.append(data)
            case "2":
                if queue:
                    print(f"Se ha eliminado {queue.pop(0)}")
                else:
                    print("La queue está vacía.")
                input()
            case "3":
                print(f"Contenido de la queue:\n{queue}")
                input()
            case "4":
                print("Saliendo del ejemplo de queue")
                break

# queue_example()
# stack_example()

# EXTRA

def web_navigation():
    """Web navigation example"""
    historial = []
    adelante = []

    while True:
        option = input("Ingrese una URL o seleccione adelante/atras/salir: ").lower()

        if option == "salir":
            print("Saliendo del navegador web.")
            break
        elif option == "atras":
            if len(historial) > 1:
                adelante.append(historial.pop())
            else:
                print("No puedes ir más atrás.")
        elif option == "adelante":
            if adelante:
                historial.append(adelante.pop())
            else:
                print("No puedes ir más adelante.")
        else:
            historial.append(option)
            adelante.clear()

        if historial:
            print(f"Estás en: {historial[-1]}")
        else:
            print("Estás en la página de inicio.")

def printer():
    """shared printer example"""
    queue = []

    while True:
        option = input(
            "Añada un documento o seleccione imprimir/cola/salir: "
        ).lower()

        if option == "salir":
            print("Saliendo de la impresora.")
            break
        elif option == "imprimir":
            if queue:
                print(f"Imprimiendo {queue.pop(0)}")
            else:
                print("No hay documentos en la cola.")
        elif option == "cola":
            if len(queue) > 0:
                print(f"Cola de impresion:\n{queue}")
            else:
                print("No hay documentos en la cola.")
        else:
            queue.append(option)