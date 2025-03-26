"""
Callbacks
"""

# Es una funcion que pasa como argumento a otra
# La ultima funcion llama de vuelta a la otra funcion
# Es una forma de manejar tareas asincronicas

# Un callback serai como darle una tareas a un amigo y que este me avise cuando termino

def saludar(nombre: str):
    print(f'Hola {nombre}.')

def ejecutar_callback(funcion, argumento):
    print('Voy a ejecutar el callback ...')
    funcion(argumento)

ejecutar_callback(saludar, 'Juan')


"""
Usos
"""

# Programación asíncrona: Por ejemplo, en manejo de eventos o cuando esperas que algo termine (como una descarga).
# Librerías o frameworks: Piensa en una interfaz gráfica (como Tkinter) donde defines qué pasa cuando haces clic en un botón.
# Procesamiento de datos: Como aplicar una función personalizada a cada elemento de una lista.


"""
Ejemplo:

Supóngamos que pedimos una pizza por teléfono. La pizzería nos dice: "Te llamamos cuando la pizza esté lista". Aquí, no sabes exactamente cuándo va a estar lista, pero confíamos en que nos avisarán. Ese "te llamamos" es el callback.
"""

# Creamos la funcion que prepara la pizza y nos avisa cuando este lista
def pedir_pizza(callback):
    print('Preparando la pizza...')
    for _ in range(3):
        print('Hornenando la pizza...')
    callback()

# Creamos la funcion que avisa cuando la pizza este lista
def pizza_lista():
    print('La pizza esta lista, ven a recogerla.')

# Le damos la orden a la pizzeria de preparla y de avisarnos 
pedir_pizza(pizza_lista)


"""
Extra
"""

import random
import time
import threading


def proceso_pedidos():
    nombre_plato = input('Hola, ingresa el nombre del plato que deseas: ')
    print(f'El plato que elegiste fue {nombre_plato}')
    confirmacion(nombre_plato)
    time.sleep(random.randint(1, 10))
    listo(nombre_plato)
    time.sleep(random.randint(1, 10))
    entrega(nombre_plato)

    threading.Thread(target=proceso_pedidos).start()

def confirmacion(nombre_plato):
        print(f'Tu plato {nombre_plato} esta en preparacion.')

def listo(nombre_plato):
        print(f'Tu pedido de {nombre_plato} esta listo.')
        print('Lo estamos empacando')

def entrega(nombre_plato):
        print(f'Gracias por tu espera. Tu plato {nombre_plato} ha sido entregado.')


proceso_pedidos() 