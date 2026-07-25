## Pilas y Colas

#Pilas/Stacks es una estructura de datos que sigue el principio LIFO (Last In, First Out), es decir, el último elemento en entrar es el primero en salir.

#Colas/Queues es una estructura de datos que sigue el principio FIFO (First In, First Out), es decir, el primer elemento en entrar es el primero en salir.

# Pilas/Stacks

stacks = []

# Agregar elementos a la pila

stacks.append(1)
stacks.append(2)
stacks.append(3)
stacks.append(4)
print(stacks)

# Eliminar elementos de la pila

# Opcion 1: usando del y len(), pero es menos común y no recomendado
item = stacks[len(stacks) -1]
del stacks[len(stacks) -1]
print(item)

print(stacks)

# Opcion 2: usando pop(), que es una funcion propia del lenguaje y es la forma recomendada
item = stacks.pop()
print(item)

print(stacks)

#Colas/Queues

queues = []

# Agregar elementos a la cola
queues.append(1)
queues.append(2)
queues.append(3)
queues.append(4)
print(queues)

# Eliminar elementos de la cola

# Opcion 1
item_queue = queues[0]
del queues[0]
print(item_queue)

print(queues)

# Opcion 2: usando pop(0), pasandole el indice en la posicion 0 para eliminar el primer elemento
item_queue = queues.pop(0)
print(item_queue)

print(queues)

##Extra

"""Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web."""

# Implementacion de pila para el historial del navegador


def navegador():
    print("Bienvenido al navegador web simulado.")

    historial = []
    pagina_actual = None

    while True:
        # Muestra la página actual para que el usuario sepa dónde está
        if pagina_actual:
            print(f"\nEstás en: {pagina_actual}")
        else:
            print("\nEstás en la página de inicio.")

        accion = input("Ingresa una URL, 'atras', 'adelante', o 'salir': ").lower()

        if accion == "salir":
            print("Saliendo del navegador...")
            break

        elif accion == "atras":
            # Si hay elementos en el historial de atrás, se puede retroceder
            if historial:
                # Se navega a la última página del historial de atrás
                pagina_actual = historial.pop()
                print(f"Navegando hacia atrás a: {pagina_actual}")
            else:
                pagina_actual = None
                #print("No hay páginas para retroceder.")

        elif accion == "adelante":
                print("No hay páginas para avanzar.")

        else: # Se considera que el usuario ingresó una nueva URL
            # La página actual se guarda en el historial
            if pagina_actual:
                historial.append(pagina_actual)

            pagina_actual = accion
            print(f"Visitando nueva página: {pagina_actual}")

navegador()

"""En la implementacion anterior, la accion adelante no tiene funcionalidad ya que no se
guarda un historial de páginas hacia adelante. Para implementar esta funcionalidad, se puede
utilizar una segunda pila que almacene las páginas hacia adelante cuando se navega hacia atrás."""



"""Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos."""

# Implementacion de cola para la impresora compartida

def impresora():
    
    print("Bienvenido a la impresora compartida simulada.")
    
    cola_impresion = []
    
    while True:
        accion = input("Ingrese el nombre del documento, 'imprimir' o 'salir':  ").lower()
        
        if accion == "salir":
            print("Saliendo de la impresora...")
            break
        elif accion == "imprimir":
            if cola_impresion:
                documento = cola_impresion.pop(0)
                print(f"Imprimiendo documento: {documento}")
            else:
                print("No hay documentos en la cola de impresion")
        else:
            cola_impresion.append(accion)
            print(f"Documento '{accion}' agregado a la cola de impresion.")
            
        print(f"Cola de impresion actual: {cola_impresion}")   
            
impresora()