# EJERCICIO 07 - PILAS Y COLAS (by Worlion)

# Pila (stack)
stack = []

def initialize_stack():
    stack = []

def push(item):
    stack.append(item)

def pop():
    if(len(stack) == 0):
        raise Exception("Empty stack :(")
    # return item = stack.pop()      ¯\_(ツ)_/¯ 
    item = stack[len(stack)-1]
    del stack[len(stack)-1]
    return item;
    
print("Jugando con la pila...")
print("Añado 4 valores")
push(3)     
push(65)        
push(1)     
push(99)        
print(f"Stack: {stack}")

print("elimino el primero: ")
print(f"pop: {pop()}")
print(f"Stack: {stack}")
print("elimino otro: ")
print(f"pop: {pop()}")
print(f"Stack: {stack}")
print(f"pop: {pop()}")
# print(f"Stack: {stack}")
# print(f"pop: {pop()}")
# print(f"Stack: {stack}")
# print(f"pop: {pop()}")
# print(f"Stack: {stack}")

# Cola (queue)
queue = []

def put(item):
    queue.append(item)

def get():
    if(len(queue) == 0):
        raise Exception("Empty queue :(")
    item = queue[0]
    del queue[0]
    return item;

print("Jugando con la cola...")
print("Añado 4 valores")
put("a")     
put("b")     
put("c")     
put("d")     
        
print(f"Queue: {queue}")

print("elimino el primero: ")
print(f"get: {get()}")
print(f"Queue: {queue}")
print("elimino otro: ")
print(f"get: {get()}")
print(f"Queue: {queue}")
print(f"get: {get()}")
print(f"Queue: {queue}")
print(f"get: {get()}")
print(f"Queue: {queue}")
# print(f"get: {get()}") # Daría excepcion

"""
* DIFICULTAD EXTRA (opcional):
"""
# Pintar de colores... para el menú ^_^ 
def red(skk): print("\033[91m {}\033[00m" .format(skk))
def grey(skk): print("\033[97m {}\033[00m" .format(skk))
def green(skk): print("\033[92m {}\033[00m" .format(skk))

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

def navegador():

    back_history = []
    forward_history = []
    
    def navegar(page):
        
        forward_history.clear()
        back_history.append(page)
        
    def adelante():
        if(len(forward_history) == 0):
            print("No se puede ir hacia adelante")
            return
        # pop adelante y push atrás
        back_history.append(forward_history.pop())
        
    def atras():
        if(len(back_history) == 1):
            print("No se puede ir hacia atrás, estás en inicio.")
            return
        # pop adelante y push atrás
        forward_history.append(back_history.pop())

    def print_menu():
        print(f"\n\n\n -Página actual: '{back_history[len(back_history)-1]}'")
        print("\nElija una opción o escriba la url a la que quiere navegar:")
        
        if(len(forward_history) == 0):
            grey("\t - 1: Adelante")
        else: 
            green("\t - 1: Adelante")
            
        if(len(back_history) == 1):
            grey("\t - 2: Atrás")
        else:   
            green("\t - 2: Atrás")
        red("\t - 0: Salir")
        return input("¿qué desea hacer?")
    
    finish = False
    
    navegar("Inicio")
    
    while not finish :
        action = print_menu()
        if(action == "1" or  action.upper() == "ADELANTE" ):
            adelante()
        elif(action == "2" or  action.upper() == "ATRÁS"  or  action.upper() == "ATRAS" ):
            atras()
        elif(action == "0" or  action.upper() == "SALIR" ):
            finish = True
            print ("exit...")
        else:
            print(f"navegar a {action}")
            navegar(action)
                
navegador()

# Impresora

def impresora():
    
    option = 1
    
    impresora = []
    
    def put_impresora(doc_name):
        impresora.append(doc_name)
    
    def get_impresora():
        if(len(impresora) == 0):
            red("Cola vacía, no hay nada que imprimir.")
            return
        document = impresora[0]
        del impresora[0]
        green(f"Imprimiendo documento: '{document}'")
    
    def print_option_2():
        msg = "\t - Escriba 'Imprimir' para comenzar la impresión'"
        if(len(impresora) == 0):
            grey(msg)
        else:
            green(msg)
    
    def show_menu_impresora() -> str:
        print("\nOpciones: ")
        green("\t - Escriba el nombre del documento")
        print_option_2()
        red("\t - Escriba 'Salir' o '0' para salir de la aplicación'")
        return input("\n\t > ")
    
    def process_option(option: str):
        if option == "0" or option.upper() == "SALIR":
            return "0"
        elif option.upper() == "IMPRIMIR":
            get_impresora()
        else:
            put_impresora(option)
        return 1
    
    while(option != "0"):
        print(f"\n\n\nCola de impresión: {impresora}")
        option = process_option(show_menu_impresora())
    
impresora()
