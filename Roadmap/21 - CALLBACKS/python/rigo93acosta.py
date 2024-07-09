'''
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */
'''

## Programación Asíncrona principal saludo.

def greeting_process(name: str, callback):
    print('Ejecutando el proceso de saludo...')
    callback(name)

def greet_callback(names: str):
    print(f'Hola, {names}!')

greeting_process('Rigo', greet_callback)

'''
Extra
'''
import random
import time
import threading

def order_process(dish_name: str, confirm_callbackm, ready_callback, delivered_callback):
    def process():   
        confirm_callbackm(dish_name)
        time.sleep(random.randint(1, 10))    
        ready_callback(dish_name)
        time.sleep(random.randint(1, 10))
        delivered_callback(dish_name)
    
    threading.Thread(target=process).start()


def confirm_order(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido confirmado.")

def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name} está listo.")

def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name} ha sido entregado.")

order_process("Pizza Barbacoa", confirm_order, order_ready, order_delivered)
order_process("Pizza 4 Quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Margarita", confirm_order, order_ready, order_delivered)
order_process("Pizza con Piña", confirm_order, order_ready, order_delivered)
