# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
"""

def greet(name):
    return f"Hello, {name}!"


def call_func(func, name):
    """Función de orden superior que recibe un callback greet y un nombre
    Args:
        func (function): function callback
        name (str): name to greet
    Returns:
        str: greeting message
    """

    return func(name)


print(call_func(greet, "Duban")) # Hello, Duban!

"""
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
"""

from typing import Callable
import random
import asyncio
from enum import Enum, verify, UNIQUE
from time import time

@verify(UNIQUE)
class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    READY = "ready"
    DELIVERED = "delivered"


async def process_order(
        dish: str,
        confirm_callback: Callable,
        ready_callback: Callable,
        deliver_callback: Callable,
        status: OrderStatus = OrderStatus.PENDING
    ):

    current_status = {
        OrderStatus.PENDING: "Pendiente",
        OrderStatus.CONFIRMED: "Confirmado",
        OrderStatus.READY: "Listo",
        OrderStatus.DELIVERED: "Entregado"
    }

    if not isinstance(dish, str) or dish == "":
        raise ValueError("Ingrese un nombre de plato valido")

    """Process an order""" 
    print(f"Procesando pedido del plato: {dish}, estado: {current_status[status]}")
    status = await confirm_callback()
    print(f"Pedido de {dish}, estado: {current_status[status]}")
    status = await ready_callback()
    print(f"Pedido de {dish}, estado: {current_status[status]}")
    status = await deliver_callback()
    print(f"Pedido de {dish}, estado: {current_status[status]}")


# Callback de confirmación
async def confirm_order(status: OrderStatus = OrderStatus.CONFIRMED):
    start_time = time()
    await asyncio.sleep(random.randint(1, 10))
    time_spend_in_task = time() - start_time
    print(f"Tiempo de espera {time_spend_in_task:.2f} segundos")
    return status

# Callback de listo
async def ready_order(status: OrderStatus = OrderStatus.READY):
    start_time = time()
    await asyncio.sleep(random.randint(1, 10))
    time_spend_in_task = time() - start_time
    print(f"Tiempo de espera {time_spend_in_task:.2f} segundos")
    return status


# Callback de entrega
async def deliver_order(status: OrderStatus = OrderStatus.DELIVERED):
    start_time = time()
    await asyncio.sleep(random.randint(1, 10))
    time_spend_in_task = time() - start_time
    print(f"Tiempo de espera {time_spend_in_task:.2f} segundos")
    return status


if __name__ == "__main__":
    dish = input("Ingrese el nombre del plato: ")

    try:
        asyncio.run(process_order(dish, confirm_order, ready_order, deliver_order))
    except ValueError as e:
        print(e)