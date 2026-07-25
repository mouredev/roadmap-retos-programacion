# 07

# stacks - LIFO
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)   # [1, 2, 3]

pila.pop()    # saca el 3
print(pila)   # [1, 2]

pila.pop()    # saca el 2
print(pila)   # [1]

pila.pop()    # saca el 1
print(pila)   # []

# queue - FIFO

cola = []
cola.append('A')
cola.append('B')
cola.append('C')
print(cola)  # ['A', 'B', 'C']

# Quitar del principio
primero = cola.pop(0)
print(primero)  # 'A'
print(cola)     # ['B', 'C']

"""- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web."""

def navegador():
    lista_webs = ["Google", "Youtube", "Facebook", "Pinterest" ]
    posicion = 0
    opciones = [1, 2, 3, 4]
    # Mensaje de inicio
    print(f"\nEstas en la pagina {lista_webs[posicion]}\n")

    def opcion_1():
        nonlocal posicion
        posicion += 1
        try:
            print(f"\nAvanzate a la pagina {lista_webs[posicion]}")
            pantalla()
        except IndexError:
            print("Índice fuera del rango, no hay mas elementos adelante.")
            pantalla()
        
    def opcion_2():
        nonlocal posicion
        posicion -= 1
        print(f"\nRetrocediste a la pagina {lista_webs[posicion]}")
        pantalla()

    def opcion_3():
        nonlocal posicion
        nueva_web = input("\nEscribe el nombre de la web: ")
        lista_webs.append(nueva_web)

        posicion = len(lista_webs) - 1
        print(f"\nAhora te encuentras en la pagina {lista_webs[posicion]}")

        pantalla()
    
    def opcion_4():
        print("Saliendo del programa...")
        exit()
         
    acciones = {
    1: opcion_1,
    2: opcion_2,
    3: opcion_3,
    4: opcion_4,
    }
    def pantalla():
            while True:
                try:
                    x = int(input("\nElige la accion deseas realizar para cambiar de pagina:\
                            \n1. Adelante\n" \
                            "2. Atras\n3. Nombre de la Pagina que deseas digirirte\n4. Salir\n" \
                            "Indique una opción: "))
                    if x in opciones:
                        accion = acciones.get(x, lambda: print("Opción no válida"))
                        accion()
                        break
                    else:
                        print("\nBoludo es del 1 al 4\n")
                except ValueError:
                    print("\nSolo se permiten numeros\n")

    pantalla()

navegador()

"""* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos."""

def impresora():
    lista_webs = []
    posicion = 0
    opciones = ["imprimir", "salir"]
    
    def opcion_1():
        nonlocal posicion
        print(f"\nImprimiendo archivo: {lista_webs[posicion]}")
        lista_webs.pop(0)
        pantalla()
    
    def opcion_2():
        print("\nSaliendo del programa...\n")
        exit()

    def opcion_3(word):
        lista_webs.append(word)
        print(f"\nArchivo agregado a la cola {word}")
        pantalla()

    acciones = {
    "imprimir": opcion_1,
    "salir": opcion_2,
    "document": opcion_3,
    }
    def pantalla():
            while True:
                try:
                    x = input("\nEscribe la palabra 'imprimir' si deseas imprimir de lo contrario se tomara como documento: \nEscribe salir para terminar el programa: ")
                    minimizar = x.lower()
                    if minimizar in opciones:
                        accion = acciones.get(minimizar, lambda: print("Opción no válida 1"))
                        accion()
                        break
                    else:
                        accion = acciones.get("document", lambda: print("Opción no válida"))
                        accion(minimizar)
                        break
                except ValueError:
                    print("\nSolo se permite texto\n")

    pantalla()

impresora()