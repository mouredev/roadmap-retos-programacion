"""
    Explora el concepto de callback en tu lenguaje creando un ejemplo
    simple (a tu elección) que muestre su funcionamiento.
"""

import random
import time


def saludar(nombre):
    print(f"Hola {nombre}")


def EntradaUsuario(callback):
    nombre = input("Ingresa tu nombre: ")
    callback(nombre)


EntradaUsuario(saludar)

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

def confirm(dish):
    print(f"Pedido confirmado: {dish}")


def ready(dish):
    print(f"Plato listo: {dish}")


def deliver(dish):
    print(f"Pedido entregado: {dish}")

# Función que procesa los pedidos


def process(dish, confirm, ready, deliver):
    # Confirmar el pedido
    confirm(dish)

    # Simula el tiempo de preparación
    prep_time = random.randint(1, 10)
    time.sleep(prep_time)
    ready(dish)

    # Simula el tiempo de entrega
    delivery_time = random.randint(1, 10)
    time.sleep(delivery_time)
    deliver(dish)


# Simular el procesamiento de un pedido
dish = input("¿Que desea ordenar? ")
process(dish, confirm, ready, deliver)
