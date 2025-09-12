# PILAS Y COLAS 

# PILAS / STACK (LIFO -> Last Input First Output)

stack = ["pelota roja", "pelota azul"]
print(stack)


# Añadir un nuevo elemento a la pila
stack.append("pelota verde")
print(stack)

# Acceder al último elemento, que es el primero en salir y eliminarlo
print(stack[-1])
del stack[-1]
print(stack)

# Hacemos lo mismo con el método pop de python
stack.append("pelota verde")
print(stack)
stack.pop()
print(stack)

# COLAS /QUEUE (FIFO -> First Input First Output)

queue = ["pelota roja", "pelota azul", "pelota verde"]

# Acceder al primer elemento, que es el primero en salir y eliminarlo
print(queue[0])
del queue[0]
print(queue)
queue.insert(0,"pelota roja")

# Hacemos lo mismo con el método pop de python
print(queue)
print(queue.pop(0))
print(queue)


# EJERCICIO EXTRA
"""
- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""
page_history = ["www.elmundo.es", "elpais.es", "www.abc.es"]

def menu():
    
    position = 0
    while True:
        user_option = input("Introduzca una opción: 'atras', 'adelante' o diga salir. Cualquier otra opción se añadirá como sitio web ")
        if user_option == "adelante":
            print("Ha elegido adelante")
            position += 1
            if position > len(page_history) - 1:
                "No hay más páginas que mostrar"
                print(f"Estás en la página:  {page_history[-1]}")
            else:
                print(page_history[position])
        elif user_option == "atras":
            print("Ha elegido atrás")
            position -= 1
            if position < 0: 
                print("Estás en la página de inicio")
                print(f"Estás en la página:  {page_history[0]}")
            else: 
                print(page_history[position])
        elif user_option == "salir":
            print("Ha salido exitosamente del programa")
            break
        else: 
            print(f"se añadirá la siguiente web: {user_option} ")
            page_history.append(user_option)

#menu()

# SEGUNDO EJERCICIO 

"""- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos."""


def printer():
    print_queue = []
    while True:
        option = input("Introduce una opción: imprimir o salir ")
        if option == "imprimir":
            if len(print_queue) == 0:
                print("No hay documentos en la cola de impresión")
            else:
                print(f"Imprimiendo... {print_queue.pop(0)} ")
                print(f"Documentos en la impresora: {print_queue}")
        elif option == "salir":
            print("Has salido exitosamente del programa")
            break
        else:
            print("Documento añadido a la cola de impresión")
            print_queue.append(option)
            print(f"Documentos en la impresora: {print_queue}")

printer()