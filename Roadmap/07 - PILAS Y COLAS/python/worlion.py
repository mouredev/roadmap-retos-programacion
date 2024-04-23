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
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

def navegador():

    # Pintar de colores... para el menú ^_^ 
    def red(skk): print("\033[91m {}\033[00m" .format(skk))
    def grey(skk): print("\033[97m {}\033[00m" .format(skk))
    def green(skk): print("\033[92m {}\033[00m" .format(skk))
    
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