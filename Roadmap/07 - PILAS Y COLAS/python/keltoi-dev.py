"""
* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
"""

# Implementacion de las pilas (stacks - LIFO)
pila = []  # Creamos la pila

# Le agregamos elementos
pila.append("Elemento 1")
pila.append("Elemento 2")
pila.append("Elemento 3")

print("Asi esta la pila: ", pila)

# Desapilamos elementos (Siempre sale primero el ultimo que ingresa)
pila.pop()
pila.pop()

print("Asi esta la pila: ", pila)

# Le agregamos mas elementos
pila.append("Elemento 4")
pila.append("Elemento 5")

print("Asi esta la pila: ", pila)

# Desapilamos elementos (Siempre sale primero el ultimo que ingresa)
pila.pop()
pila.pop()

print("Asi esta la pila: ", pila)

print("-" * 30)
# Implementacion de las pilas (stacks - LIFO)
cola = []  # Creamos la pila

# Le agregamos elementos
cola.append("Elemento 1")
cola.append("Elemento 2")
cola.append("Elemento 3")

print("Asi esta la cola: ", cola)

# Desapilamos elementos (Siempre sale primero el ultimo que ingresa)
cola.pop(0)
cola.pop(0)

print("Asi esta la cola: ", cola)

# Le agregamos mas elementos
cola.append("Elemento 4")
cola.append("Elemento 5")

print("Asi esta la cola: ", cola)

# Desapilamos elementos (Siempre sale primero el ultimo que ingresa)
cola.pop(0)
cola.pop(0)

print("Asi esta la cola: ", cola)


"""
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
"""

# NAVEGADOR WEB

print("\nSe inicia el navegador web...\n")

historial = []
indice = 0

while True:
    pagina = input("Ingrese una URL o navegar con: atras, adelante o salir: ").lower()
    if pagina == "salir":
        break
    elif pagina == "atras":
        if indice == (len(historial) - 1):
            print("No se puede ir mas atras")
        else:
            indice += 1
            print(historial[indice])
    elif pagina == "adelante":
        if indice == 0:
            print("No se puede ir mas adelante")
        else:
            indice -= 1
            print(historial[indice])
    else:
        historial.insert(0, pagina)
        indice = 0


# IMPRESORA

print("\nSe inicia la impresora compartida...\n")

buffer = []

while True:
    documento = input("Ingrese el nombre de un documento, imprimir o salir: ").lower()
    if documento == "imprimir":
        if buffer == []:
            print("No hay documentos por imprimir")
        else:
            print("Imprimiendo el documento:", buffer[0])
            buffer.pop(0)
    elif documento == "salir":
        break
    else:
        buffer.append(documento)
    print("Estado de la cola de impresion")
    print(buffer)
