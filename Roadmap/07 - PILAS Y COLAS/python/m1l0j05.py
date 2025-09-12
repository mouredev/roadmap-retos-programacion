# Teoria

# Pilas (Stacks - LIFO):
# 1. Una pila es una estructura de datos en la que los elementos
# se añaden y se eliminan siguiendo una política conocida como LIFO, 
# que significa "Last In, First Out" (último en entrar, primero en salir).
# 
# 2. Imagina una pila de platos: 
# El último plato que colocas sobre la pila será el primero en ser retirado.
# 
# 3. En Python, puedes implementar una pila utilizando una lista. 
# Puedes añadir elementos a la pila usando el método `append()` 
# y eliminar elementos usando el método `pop()`.

# Colas (Queue - FIFO):
# 1. Una cola es otra estructura de datos en la que los elementos se añaden y 
# se eliminan siguiendo una política conocida como FIFO, 
# que significa "First In, First Out" (primero en entrar, primero en salir).
#
# 2. Imagina una cola en una tienda: 
# La persona que llega primero es la primera en ser atendida.
# 
# 3. En Python, puedes implementar una cola utilizando la clase `deque` 
# del módulo `collections`. Puedes añadir elementos a la cola usando 
# el método `append()` y eliminar elementos usando el método `popleft()`.


# Ejercicio
import time
import random
from collections import  deque

def ejercicio():
    stack_lifo = []
    print(f'\n[+] Modificando elementos de la pila:')
    print(f'\n[+] Contenido de la pila {stack_lifo}')

    for i in range(1,6):
        stack_lifo.append(f'item_{i}')
        print(f'\n[+] Añadido un elemento al stack_LIFO')
        print(f'[+] Contenido de la pila {stack_lifo}')
        time.sleep(0.3)

    for i in range(0, len(stack_lifo)):
        stack_lifo.pop()
        print(f'\n[+] Eliminado un elemento al stack_LIFO')
        print(f'[+] Contenido de la pila {stack_lifo}')
        time.sleep(0.3)

    stack_fifo = deque()

    for i in range(1,6):
        stack_fifo.append(f'item_{i}')
        print(f'\n[+] Añadido un elemento al stack_FIFO')
        print(f'[+] Contenido de la pila {stack_fifo}')
        time.sleep(0.3)

    for i in range(0, len(stack_fifo)):
        stack_fifo.popleft()
        print(f'\n[+] Eliminado un elemento al stack_FIFO')
        print(f'[+] Contenido de la pila {stack_fifo}')
        time.sleep(0.3)


# Ejercicios Extra

web_history = []
url_anterior = ''
url_actual = ''
url_posterior = ''

def adelante(url):
    global url_actual
    global url_posterior
    global url_anterior
    
    if not url_posterior:
        print(f'[i] Se encuentra en el final')
    else:
        if url_anterior:
            url_anterior.append(web_history)
        url_anterior=url_actual
        url_actual=url_posterior
        url_posterior=''

def atras(url):
    global url_actual
    global url_posterior
    global url_anterior
    
    if not url_anterior:
        print(f'[i] No existe una URL anterior')
    else:
        url_posterior=url_actual
        url_actual=url_anterior
        if len(web_history) > 0:
            url_anterior=web_history.pop()
        else:
            url_anterior=''


def navegar(url):
    global url_actual
    global url_anterior
    if  url_actual and url_anterior:
        web_history.append(url_anterior)
    url_anterior = url_actual
    url_actual = url

    print(f'[+] Navegar: {url}')

def navegando():
    while True:
        user_intput = input("\nIngrese 'adelante', 'atras' o la URL de una nueva página:\n")
        if user_intput.lower() == "adelante":
            adelante(user_intput)
        elif user_intput.lower() == "atras":
            atras(user_intput)
        else:
            navegar(user_intput)
        
        print(f'\n[i] Informacion. ')
        print(f'[i] Historial: {web_history}')
        print(f'[i] Url_Anterior: {url_anterior}')
        print(f'[i] Url_Actual: {url_actual}')
        print(f'[i] Url_posterior: {url_posterior}')



# Ejercicio Extra 2

def impresora(cola_impresion):
    cont = 0
    imprimir = False
    while True:
        if not imprimir:
            documento = f'{cont}.txt'
            cola_impresion.append(documento)
            print(f'\n[i] Añadido documento {documento} a la cola de impresión')
            print(f'[i] Archivos en cola: {cola_impresion}\n\n') 
            time.sleep(0.5)
            if len(cola_impresion) > 3:
                imprimir = True
            else:
                num = random.randint(1, 5)
                if num % 2 != 0:
                    imprimir = True
            cont += 1
        else:
            try:
                print(f'[i] Imprimiendo {cola_impresion.popleft()}...')
            except IndexError:
                print('[i] No hay documentos en la cola para imprimir')
            imprimir = False

# Ejecucion de los ejercicios.
#ejercicio()
#navegando()
cola_impresion = deque()
impresora(cola_impresion)
