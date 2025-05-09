""" /*
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
 */ """

import random
import time

#EJERCICIO

def greeting_process(name: str, callback):
    callback(name)

def greet_callback(name: str):
    print(f"Hola {name}.")

greeting_process("David", greet_callback)


#DIFICULTAD EXTRA

def order(dish_name: str, confirmation_callback, ready_callback, delivered_callback):
    dish_name = input("¿Qué quieres pedir?: ").lower()
    confirmation_callback(dish_name)
    time.sleep(random.randint(1, 10))
    ready_callback(dish_name)
    time.sleep(random.randint(1, 10))
    delivered_callback(dish_name)

def order_confirmation(dish_name: str):
    print(f"Tu pedido {dish_name.lower()} ha sido confirmado.")


def order_ready(dish_name: str):
    print(f"Tu pedido {dish_name.lower()} está listo.")

def order_delivered(dish_name: str):
    print(f"Tu pedido {dish_name.lower()} ha sido entregado.")

order("", order_confirmation, order_ready, order_delivered)