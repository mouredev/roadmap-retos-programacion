#LIFO último en entrar primero en salir
def stacks(arg1, arg2, arg3, arg4):
    stack = []

    #Añaden valores a la pila
    stack.append(arg1)
    stack.append(arg2)
    stack.append(arg3)
    stack.append(arg4)
    
    print(f"Pila de cosas a hacer durante el día {stack}")
    
    print(f"Último elemento en entrar {stack[len(stack)-1]}")
    
    print(f"Primer elemento en salir {stack.pop()}")
    print(f"Pila de cosas a hacer {stack}")

stacks("Pintar", "Comer", "Ver Tv", "Dormir")

#FIFO Primero en entrar, primero en salir
def queue(arg1, arg2, arg3):
    queue = []
    queue.append(arg1)
    queue.append(arg2)
    queue.append(arg3)
    
    print(f"Lista de tareas a realizar: {queue}")
    
    print(f"Primera tarea de la lista: {queue[0]}")
    
    print(f"Terminada la primera tarea de la lista se elimina de ella: {queue.pop(0)}")
    
    print(f"Lista de tareas a realizar: {queue}")


queue("Desayunar", "Estudiar", "Hacer ejercicio")

#EXTRA
print("---------------------")

def simulation_web():
    browser_web = []
    forward = []
    status = True

    while status:
        order = input("Indica el nombre del sitio web, adelante, atras o salir: ")

        #Comparamos la orden introducida por consola
        if order.lower() == "adelante":
            #Si browser_web esta vacia abre nueva pestaña e introducimos el nombre del sitio web y lo almacena en la lista browser_web
            if len(browser_web) == 0:
                print("Nueva Pestaña")
                web_name = input("Indique el nombre del sitio web a acceder: ")
                browser_web.append(web_name)
                print(f"Estas en el sitio web -> {browser_web[len(browser_web) - 1]}")
            #Si la lista forward no esta vacia mostrará el último resultado de la lista que hace de historial y añade el valor a browser_web
            elif len(forward) > 0:
                print(f"Estas en el sitio web -> {forward[len(forward) - 1]}")
                browser_web.append(forward[len(forward) - 1])
                forward.pop()
            #Si no muestra la posición actual de la lista browser_web
            else:
                print(f"Estas en el sitio web -> {browser_web[len(browser_web) - 1]}")
        elif order.lower() == "atras":
            #Si browser_web es mayor que 1 borramos el último valor de la lista y la añadimos a la lista forward y se muestra la última posición de browser_web
            if len(browser_web) > 1:
                back = browser_web.pop()
                forward.append(back)
                print(f"Estas en el sitio web -> {browser_web[len(browser_web) - 1]}")
            #Si no indicamos que el historial está vacio
            else: 
                print("El historial esta vacio, no se puede retroceder")
                print(f"adelante {forward}")
        elif order.lower() == "salir":
            print("Cerrando el navegador")
            status = False
        else:
            browser_web.append(order)
            print(f"Estas en el sitio web -> {browser_web[len(browser_web) - 1]}")


simulation_web()

def printer():
    queue_printer = []
    status = True

    while status:
        order = input("Indica el nombre del fichero ha añadir a la cola de impresion, imprimir o salir: ")
        #Si indicamos que queremos imprimir comprobamos que la lista no este vacia, si es así lo indicamos y se vuelve a pedir la orden anterior
        #Si la lista no esta vacia se muestra la impresión de los documentos y cuando se finaliza se limpia la cola de impresión
        if order.lower() == "imprimir":
            if len(queue_printer) == 0:
                print("No hay documentos a imprimir")
            else:    
                for i in queue_printer:
                    print (f"Imprimiendo el documento imprimir {i}")
                queue_printer.clear()
        #Si indicamos que queremos salir, se muestra un mensaje que indica que se esta cerrando el programa y cambiamos la variable status para que no pida mas instruciones        
        elif order.lower() == "salir":
            print("Cerrando programa de cola de impresión...")
            status = False
        #Si no se indica que deseamos imprimir o salir, lo introducido por comando se añade a la cola de impresión    
        else:
            queue_printer.append(order)

printer()