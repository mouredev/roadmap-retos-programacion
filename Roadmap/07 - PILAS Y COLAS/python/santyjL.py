#07 - PILAS Y COLAS
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
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */
"""

# PILAS #
"""
lo que pasa con las pilas es que utilizan la siguiente idea 'Ultimo en entrar ,
primero en salir' lo que tambien se conoce como 'LIFO',para estructuras de datos
"""
pila = []

# Añadir elementos a la pila
pila.append("Plato1")
pila.append("Plato2")
pila.append("Plato3")

# Recuperar el elemento en la cima sin quitarlo
elemento_en_cima = pila[-1]



print("Pila actual:", pila)
plato_retirado = pila.pop()# Sacar el elemento más reciente
print("Plato retirado:", plato_retirado)
print("Pila después de retirar:", pila)
print("Elemento en la cima de la pila:", elemento_en_cima)

# COLAS #
"""
lo que pasa con las colas es que utilizan la siguiente idea 'primero en entrar,
primero en salir' , lo que tambien se conoce como LIFO para estructuras de datos
"""


cola = []

def añadir(cola, item):
    cola.append(item)

def retirar(cola):
    if not len(cola) == 0:
        return cola.pop(0)
    else:
        print("La cola está vacía.")

añadir(cola , "plato1")
añadir(cola , "plato2")
añadir(cola , "plato3")

elemento_en_el_fondo = cola[0]

print("cola actual:", cola)
print("Elemento en el fondo de la cola:", elemento_en_cima)

cola_tirada = retirar(cola)
print("Plato retirado:", cola_tirada)
print("cola después de retirar:", cola)



# Simulación de Navegador Web
def simulador_navegador():
    historial = []
    pagina_actual = ""

    while True:
        comando = input("Ingresa un comando ('adelante', 'atrás' , 'el nombre de una web' o 'salir'): ")

        if comando == "adelante":
            if not len(historial) == 0:
                pagina_actual = historial.pop()
                print(f"Navegando adelante a: {pagina_actual}")
            else:
                print("No hay historial adelante.")

        elif comando == "atras":
            if pagina_actual:
                historial.append(pagina_actual)
                print(f"Navegando atrás a la página anterior.")
                pagina_actual = ""
            else:
                print("No hay historial atrás.")

        elif comando == "salir":
            print("has salido")
            break

        else:
            if pagina_actual:
                historial.append(pagina_actual)
            pagina_actual = comando
            print(f"Navegando a la página: {pagina_actual}")

def simulador_impresora():
    cola_impresion = []

    while True:
        comando = input("Ingresa un comando ('imprimir' o el nombre de un documento): ")

        if comando == "imprimir":
            documento = retirar(cola_impresion)
            if documento:
                print(f"Imprimiendo documento: {documento}")
            else:
                print("No hay documentos para imprimir.")

        elif comando == "salir":
            print("has salido")
            break
        else:
            añadir(cola_impresion, comando)
            print(f"Documento '{comando}' agregado a la cola de impresión.")


simulador_navegador()

simulador_impresora()