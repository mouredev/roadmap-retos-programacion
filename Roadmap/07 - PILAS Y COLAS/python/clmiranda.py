# PILAS Y COLAS

# PILA/STACK (LIFO: LAST IN, FIRST OUT)
stack = [15, 83]

# PUSH
stack.append(100)
stack.append("Hola Mundo")
stack.append(False)
print(stack)

# POP
stack.pop()
stack.pop()
print(stack)


# COLA/QUEUE (FIFO: FIRST IN, FIRST OUT)
queue = ["Python", 78]

# ENQUEUE
queue.append(5)
queue.append(19)
print(queue)

# DEQUEUE
queue.pop(0)
print(queue)


# EJERCICIO - DIFICULTAD EXTRA

# NAVEGADOR WEB
def navegador_web():
    pila = []
    index = -1
    while True:
        valor = input("\nIngrese una opción (nombre de la web, adelante, atrás, salir): ")
        if valor:
            try:
                match valor:
                    case "adelante":
                        print(f"Adelantando a la web: {pila[index]}")
                        index -= 1
                    case "atras":
                        if len(pila) > 0:
                            last = pila.pop()
                            print(f"Volviendo a la web: {last}")
                        else:
                            print("Página de inicio")
                    case "salir":
                        print("Saliendo del navegador web")
                        break
                    case _:
                        pila.append(valor)
                        print(f"Navegando a la web: {valor}")
            except:
                print("No se puede adelantar a otra página")
        else:
            print("Debe ingresar alguna de las opciones")

navegador_web()


# IMPRESORA
def impresora():
    cola = []
    while True:
        valor = input("\nIngrese una opción (nombre del documento, imprimir, salir): ")
        match valor:
            case "imprimir":
                if len(cola) > 0:
                    first = cola.pop(0)
                    print(f"Imprimiendo documento: {first}")
                else:
                    print("No hay documentos para imprimir")
            case "salir":
                print("Saliendo de la aplicación")
                break
            case _:
                cola.append(valor)

        print(f"Cola de impresión: {cola}")

impresora()