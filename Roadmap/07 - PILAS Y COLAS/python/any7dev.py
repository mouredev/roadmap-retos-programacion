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

# EJERCICIO

# Pilas
pila = [1, 2, 3, 4, 5]
print(pila)
# Añadir elemento a la pila, el último
pila.append(6)
print(pila)
# Quitar elemento, el último
pila.pop()
print(pila)
del pila[-1]
print(pila)

# Colas
cola = [6, 7, 8, 9, 10]
print(cola)
# Añadir elemento, el último
cola.append(11)
print(cola)
# Quitar elemento, el primero
cola.pop(0)
print(cola)
del cola[0]
print(cola)

# DIFICULTAD EXTRA

# Navegador web
pila = []

def navegador():
    contador = -1
    while True:
        opcion = input(f"\nEscribe cualquier página o: \n\t·atras --> Para ir a la página web anterior \n\t·adelante --> Para ir a la página web anterior \n\t·salir --> Para salir \n -->")
        match opcion:
            case "salir":
                print(f"Saliendo\n")
                break            
            case "atras":                
                if not pila:
                    print("Historial Vacío")
                elif contador == 0:
                    actual = pila[contador]
                    print(f"Estás en la primera página {actual}")
                else:
                    contador -= 1 
                    actual = pila[contador]
                    print(f"Estás en la página web {actual}")                                   
            case "adelante":
                if not pila:
                    print("Historial Vacío")
                elif contador+1 == len(pila):
                    actual = pila[contador]
                    print(f"Esta es la última web visitada {actual}, no se puede avanzar")
                else:
                    contador += 1
                    actual = pila[contador]
                    print(f"Estás en la página web {actual}")                    
            case _:
                www = opcion
                pila.append(www)
                print(f"Estás en la página web {www}")
                contador += 1            

navegador()

# Impresora
cola = []

def impresora():
    contador = -1
    while True:
        opcion = input(f"\nEscribe el nombre del documento, imprimir para imprimer el primer documento o salir para salir: \n-->")
        match opcion:
            case "salir":
                print(f"Saliendo\n")
                break
            case "imprimir":
                if not cola:
                    print("Cola de impresión vacía")
                else:
                    doc = cola[0]
                    print(f"Imprimiendo el documento con nombre {doc}")
                    cola.pop(0)
                    contador -= 1
            case _:
                cola.append(opcion)
                contador += 1

impresora()

