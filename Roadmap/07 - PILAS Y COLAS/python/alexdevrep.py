'''
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
'''

'''
Las pilas son tipos abstactos de datos que se encuentran en un formato de tipo lista
a cuyos elementos se accede de una forma particular (LIFO) Last In First Out que se puede 
traducir como "Lo último en entrar será lo último en salir"
'''
from collections import deque # Librería para las colas


#Creamos un pila de elementos
mi_list=["Hola","Python","Alexdevrep"]
print(mi_list)

# Introducción de un elemento en una pila
mi_list.append("Mundo")
print(mi_list)

#Recuperación del último elemento de la pila
print(mi_list.pop())
print(mi_list)


print("-----------------------------------------")

'''
Las colas son los colecciones de elementos ordenados que únicamente permiten dos acciones 
-Añadir un elemento a la cola
-Sacar un elemento de la cola
La peculiaridad es que el primer elemento en entrar es el primero en salir (FIFO) First In First Out
'''

#Creamos una cola de elementos
cola = deque(["Mundo","Python","Alexdevrep"])
print(cola)

#Introducimos un elemento a la cola
cola.append("Hola")
print(cola)

#Recuperación el primer elemento de la cola en este caso "Mundo"
print(cola.popleft())
print(cola)

print("-----------------------------------------")

#Dificultad EXTRA


# Ejercicio Pilas 

pila_web = []

print("###---NAVEGADOR WEB---###")
print("Pestaña nueva:")

while True:
    def accion(arg):
        if arg == "ADELANTE":
            web = input("Por favor indique a qué web quiere acceder: ")
            pila_web.append(web)
            print(f'Ahora estás viendo {pila_web[-1]}')

        elif arg == "ATRAS":
            if len(pila_web) > 1:
                pila_web.pop()
                print(f'Ahora estás viendo {pila_web[-1]}')
            else:
                print("No hay historial de navegación para retroceder.")

        elif arg == "SALIR":
            print("Cerrando el navegador web.")
            

        else:
            print("Comando no reconocido.")

    arg = input("Por favor escriba ADELANTE si quiere acceder a una URL nueva, ATRAS si quiere cerrar la última URL, o SALIR para salir: ")
    accion(arg)
    if arg == "SALIR":
        break


# Ejercicio Colas

documentos = deque([])

while True:
    def impresora(archivo):
        if archivo == "IMPRIMIR":
            if len(documentos)>=1:
                print(f'Imprimiendo archivo {documentos.popleft()}')
            else:
                print ("No hay archivos para imprimir")
        elif archivo == "SALIR":
            print ("Apagando la impresora")
            exit()
        else :
            documentos.append(archivo)
            print("Documento añadido a la cola de impresión")
    
    archivo = input("Por favor escriba el nombre del archivo para añadirlo a la cola de la impresión , IMPRIMIR para imprimirlo y SALIR para apagar la impresora: ")
    impresora(archivo)
        
    













