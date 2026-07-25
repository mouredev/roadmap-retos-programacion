from collections import deque
import queue
# Pilas - LIFO

pila = ["hola", 1, 2, 7]

# Agregando elemento al dinal de la pila
pila.append(10)
pila.append("Final")
print(pila)

# Sacando elemento del final
pila.pop()
print(pila)

# Colas - FIFO

cola = ["Raul", "Ivan", "Mario"]

# Agregando elementos al final
cola.append("Maria")

print(cola)

# Sacando el primer elemento -> Principio cola
cola.pop(0)

print(cola)

# Con modulo collections - deque

cola2 = ["Mario", "Luis", "Ivan"]
cola2 = deque(cola2)
cola2.popleft()
print(cola2)

# Con modulo queue
cola3 = queue.Queue()
cola3.put("Elemento 1")
cola3.put("Elemento 2")
cola3.put("Elemento 3")

# Sacando el primer elemento
primer_elemento = cola3.get()
print(primer_elemento)

# Ver cuantos elementos quedan en la cola
print(cola3.qsize())


#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.
#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#  */


# Navegacion web
pilaAtras = ["atras"]
pilaAdelante = ["Prueba pag"]
pagina_actual = "misitio.com"


def navegacion_web(accion):
    global pagina_actual
    if accion == "adelante":
        if pilaAdelante:
            pilaAtras.append(pagina_actual)
            pagina_actual = pilaAdelante.pop()
        else:
            print("No hay paginas adelante")
    elif accion == "atras":
        if pilaAtras:
            pilaAdelante.append(pagina_actual)
            pagina_actual = pilaAtras.pop()
        else:
            print("No hay historial atras")
    else:
        pilaAtras.append(pagina_actual)
        pagina_actual = accion
        pilaAdelante.clear()

    print(f"Pagina actual: {pagina_actual}")
    print(f"Historial atras: {pilaAtras}")
    print(f"Historial adelante: {pilaAdelante}")


navegacion = navegacion_web("adelante")


# Impersora compartida
documentos = deque(["prueba", "nueva"])


def impresora(accion):
    if accion == "imprimir":
        impreso = documentos.popleft()
        print(f"Imprimiendo: {impreso}")
        print(f"Documentos restantes: {list(documentos)}")
    else:
        documentos.append(accion)
        print(f"Se ha agregado el documento: {list(documentos)}")


impresora("imprimir")
