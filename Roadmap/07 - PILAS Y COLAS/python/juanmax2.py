"""
Ejercicio
"""

# Pila/Stack

stack = []

# Push de elementos

stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

# Pop de elementos

stack_item = stack.pop()
print(stack)
print(stack_item)

# Cola

# Encolar
cola = []
cola.append("4")
cola.append("5")
cola.append("6")

print(cola)

# Desencolar

cola_item = cola.pop(0)
print(cola)
print(cola_item)


"""
* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.

"""

# Pila
def navegador_web():
    continuar = True
    historial = []
    historial_pop = []
    while continuar == True:
        
        do = input("Añade una url o interactúa con palabras adelante/atras/salir: ")
        
        if do == "adelante".upper() or do == "adelante".lower() \
            or do == "adelante".capitalize():
                historial.append(historial_pop.pop())
                print(historial[-1])
                
        elif do == "atras".upper() or do == "atras".lower() \
            or do == "atras".capitalize():
                if len(historial) > 0:
                    historial_pop.append(historial.pop())
                    print(historial[-1])
                else:
                    print("No hay mas webs en el historial")
                    
        elif do == "salir".upper() or do == "salir".lower() \
            or do == "salir".capitalize():
                print("Cerrando sesión...")
                continuar = False
        else:
            historial.append(do)
        
        print(f"Web acutal: {len(historial) - 1}")

navegador_web()

# Cola
""" * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos."""
 
def imprimir():
    continuar = True
    documentos = []
    documentos_impresos = []
    while continuar == True:
        
        do = input("""Introduce que quieres hacer:
                   Escribe el nombre del document para enviarlo
                   Escribe imprimir para imprimir
                   Escribe salir para salir   
                   """)
        
        if do == "imprimir".upper() or do == "imprimir".lower() \
            or do == "imprimir".capitalize():
                if len(documentos) <= 0:
                    print("No hay archivos para imprimir")
                else:
                    documentos_impresos.append(documentos.pop(0))
                    print(f"Imprimiendo documento {documentos_impresos[-1]}")
        elif do == "salir".upper() or do == "salir".lower() \
            or do == "salir".capitalize():
                print("Cerrando sesión...")
                continuar = False
        else:
            documentos.append(do)
            print(f"Documento {do} añadido a la cola de impresion")

                
imprimir()