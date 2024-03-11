#/*
# * EJERCICIO:
# * Implementa los mecanismos de introducción y recuperación de elementos propios de las
# * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# * o lista (dependiendo de las posibilidades de tu lenguaje).

# ====== Pilas ======
pila_de_libros = []

# introducción de elementos
pila_de_libros.append("Las mil y una noches")
pila_de_libros.append("Don Quijote de la Mancha")
pila_de_libros.append("Orgullo y prejuicio")
pila_de_libros.append("Frankenstein o el moderno Prometeo")
pila_de_libros.append("Los tres mosqueteros")

# recuperación de elementos
for libro in pila_de_libros:
    print(libro)

ultimo_libro = pila_de_libros.pop()
print(ultimo_libro)

# ====== Colas ======
from collections import deque

cola_de_personas = deque()

# introducción de elementos
cola_de_personas.append("Samanta")
cola_de_personas.append("Brais")
cola_de_personas.append("Roswell")
cola_de_personas.append("Andrea")
cola_de_personas.append("Jefferson")

# recuperación de elementos
for persona in cola_de_personas:
    print(persona)

primera_persona = cola_de_personas.popleft()
print(primera_persona)

# *
# * DIFICULTAD EXTRA (opcional):
# * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
# *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
# *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
# *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
# *   el nombre de una nueva web.

def navegador_web():
    print("========== navegador_web ==========")
    paginas = []
    index = 0

    while True:
        opcion = input(f"Ingrese la URL del sitio web que desea navegar o escribe una de las opiciones abajo: \n- adelante \n- atras \n- salir \n").lower()
        
        match opcion:
            case "adelante":
                if index + 1 <= len(paginas) - 1:
                    index += 1
                else:
                    print("Este es el sitio web actual")
                print("Sitio web actual: " + paginas[index] + "\n\n")
                pass
            case "atras":
                if index - 1 >= 0:
                    index -= 1
                else:
                    print("No hay ningún sitio web anterior al actual")
                print("Sitio web actual: " + paginas[index] + "\n\n")
                pass
            case "salir":
                print("===== Cerrando navegador_web =====")
                return
            case _:
                paginas.append(opcion)
                index = len(paginas) - 1
                print("Sitio web actual: " + paginas[index] + "\n\n")
                pass

navegador_web()


# * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
# *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
# *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
# *   interpretan como nombres de documentos.
# */

def impresora():
    print("========== impresora ==========")
    documentos = deque()

    while True:
        opcion = input("Ingrese el nombre del documento para cola de impresión \no escriba 'imprimir' para imprimir el siguiente documento en la cola: \n('salir' para cerrar la aplicación)")

        if (opcion == "salir"):
            print("========== Cerrando impresora ==========")
            return

        if (opcion == "imprimir"):
            if (len(documentos) == 0):
                print("No hay documentos para imprimir")
            else:
                documento_impreso = documentos.popleft()
                print("--> Imprimindo el documento: " + documento_impreso)
        else:
            documentos.append(opcion)
            print("-- cola de documentos para impresión --")
            for doc in documentos:
                print(doc)

impresora()