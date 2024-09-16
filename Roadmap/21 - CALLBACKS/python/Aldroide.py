"""
    Explora el concepto de callback en tu lenguaje creando un ejemplo
    simple (a tu elección) que muestre su funcionamiento.
"""

import random
import time
import threading


def saludar(nombre, callback):
    print("Ejecutando saludo...")
    callback(nombre)


def EntradaUsuario(nombre):
    print(f"Hola, {nombre}!")


saludar("aldo", EntradaUsuario)

"""DIFICULTAD EXTRA (opcional):
    Crea un simulador de pedidos de un restaurante utilizando callbacks.
    Estará formado por una función que procesa pedidos.
    - Debe aceptar el nombre del plato, una callback de confirmación, una de listo y otra de entrega.
    - Debe imprimir un confirmación cuando empiece el procesamiento.
    - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre procesos.
    - Debe invocar a cada callback siguiendo un orden de procesado.
    - Debe notificar que el plato está listo o ha sido entregado.
"""


# Definir las funciones callback
def order_process(dish, confirm_callback, ready_callback, delivered_callback):
    def process():
        confirm_callback(dish)
        # Simula el tiempo de preparación
        prep_time = random.randint(1, 10)
        time.sleep(prep_time)
        ready_callback(dish)
        # Simula el tiempo de entrega
        delivery_time = random.randint(1, 10)
        time.sleep(delivery_time)
        delivered_callback(dish)
    threading.Thread(target=process).start()


def confirm(dish: str):
    print(f"Pedido confirmado: {dish}")


def ready(dish: str):
    print(f"Plato listo: {dish}")


def delivered(dish: str):
    print(f"Pedido entregado: {dish}")

# Función que procesa los pedidos


# Simular el procesamiento de un pedido
dish = input("¿Que desea ordenar? ")
order_process("Limon", confirm, ready, delivered)
