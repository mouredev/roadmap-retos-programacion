# Pila/Stack (LIFO)
stack = []
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

del stack[len(stack) - 1]
print(stack)

print(stack.pop()) # printea el Last In

# Cola/Queue (FIFO)
queue = []
queue.append("1")
queue.append("2")
queue.append("3")
print(queue)

del queue[0]
print(queue)

print(queue.pop(0)) # printea el First In

'''
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''
print("\nEjercicio de dificultad extra\n")

salir = 1
nw = 1
impr = 1

while(salir):
    opcion = int(input("Elige entre:\n1. Navegador web\n2. Impresora\n3.Salir\n"))
    if opcion == 1:
        web = ["google.com"]
        i = len(web)
        print(web)
        while(nw):
            accion = int(input("\nElige:\n1. Desplazar hacia delante\n2. Desplazar hacia atrás\n3. Navegar a otra página\n4. Salir\n"))
            if accion == 1:
                if i == len(web) - 1:
                    print("No se puede avanzar más hacia delante.\n")
                else:
                    i += 1
                print(web[i])
            elif accion == 2:
                if i == 0:
                    print("No se puede avanzar más hacia atrás.\n")
                else:
                    i -= 1
                print(web[i])
            elif accion == 3:
                pagina = str(input("Escriba el nombre de la nueva página: "))
                web.append(pagina)
                print(web)
            elif accion == 4:
                nw = 0
            else:
                print("No ha elegido una opción válida.\n")
    elif opcion == 2:
        impresora = ["Mapa"]
        print(impresora)
        while(impr):
            accion = int(input("\nElige:\n1. Imprimir\n2. Añadir archivo\n3. Salir\n"))
            if accion == 1:
                if len(impresora) == 0:
                    print("No hay nada que imprimir.\n")
                else:
                    print("Imprimiendo " + impresora[0])
                    del impresora[0]                    
            elif accion == 2:
                archivo = str(input("Escriba el nombre del nuevo archivo: "))
                impresora.append(archivo)
                print(impresora)
            elif accion == 3:
                impr = 0
            else:
                print("No ha elegido una opción válida.\n")
    elif opcion == 3:
        salir = 0
    else:
        opcion = int(input("Elige entre:\n1. Navegador web\n2. Impresora\n3.Salir\n"))