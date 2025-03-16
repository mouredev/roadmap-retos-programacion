# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * CALLBACKS
# -----------------------------------
# https://www.askpython.com/python/built-in-methods/callback-functions-in-python

"""
* EJERCICIO #1:
* Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu elección) que muestre su funcionamiento.
"""

def sum_numbers(a: int, b: int, callback: object):
    if isinstance(a, int) and isinstance(b, int):
        result = a + b
        callback((f"{a} + {b}"), result)

def my_callback(summands: str, result: int):
    if isinstance(summands, str) and isinstance(result, int):
        print(f"La suma de {summands} es: {result}")

print("EJERCICIO #1")
sum_numbers(6, 6, my_callback)
sum_numbers(5, 2, my_callback)

"""
* EJERCICIO #2:
* Crea un simulador de pedidos de un restaurante utilizando callbacks.
* Estará formado por una función que procesa pedidos.
* Debe aceptar el nombre del plato, una callback de confirmación, una
* de listo y otra de entrega.
* - Debe imprimir un confirmación cuando empiece el procesamiento.
* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
*   procesos.
* - Debe invocar a cada callback siguiendo un orden de procesado.
* - Debe notificar que el plato está listo o ha sido entregado.
"""

from random import randint
import asyncio

async def process_order(name: str, confirm, prepare, serving):
    print(f"-----\n* Procesando: '{name}' \n-----\n")
    await confirm(name)
    await prepare(name)
    await serving(name)

def time_random() -> int:
    return randint(1, 10)

async def confirm_order(name: str):
    time: int = time_random()
    print(f"* Confirmando {name}, espere {time} segundos.")
    await asyncio.sleep(time)
    print(f"- '{name}', ha sido confirmado.\n")

async def prepare_order(name: str):
    time: int = time_random()
    print(f"* Preparando, espere {time} segundos.")
    await asyncio.sleep(time)
    print(f"- '{name}', esta Listo.\n")

async def serving_order(name: str):
    time: int = time_random()
    print(f"* Sirviendo, espere {time} segundos.")
    await asyncio.sleep(time)
    print(f"- '{name}', ha sido entregado.\n")

async def order(dish_name: str):
    await process_order(
        dish_name, 
        confirm_order, 
        prepare_order, 
        serving_order
    )

async def orders_list():
    await order("Baleadas")
    await order("Tamales")
    await order("Enchiladas")


print("\nEJERCICIO #2")
asyncio.run(orders_list())
