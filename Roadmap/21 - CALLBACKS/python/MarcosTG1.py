
"""
* EJERCICIO:
* Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu elección) que muestre su funcionamiento.
"""

def net_concept(name:str, callback):
    print("Iniciando proceso de salutaciones...")
    callback(name)
    
    

def saludar(name: str):
    print(f"Hola, {name}!")

net_concept("Marcos", saludar)

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
""" 
import asyncio
import random

# , callback_ready, callback_deliver
async def process_order(dish_name: str, callback_confirmation, callback_ready, callback_deliver):
    
    await callback_confirmation(dish_name)
    await asyncio.sleep(random.randint(1, 10))
    await callback_ready(dish_name)
    await asyncio.sleep(random.randint(1, 10))
    await callback_deliver(dish_name)

async def order_confirmed(dish_name: str):
    print(f"El plato {dish_name} está confirmado.")

async def order_ready(dish_name: str):
    print(f"El plato {dish_name} está listo.")

async def order_delivered(dish_name: str):
    print(f"El plato {dish_name} ha sido entregado.")

async def asign_tasks():
    await asyncio.gather(process_order("espaguetis", order_confirmed, order_ready, order_delivered), 
                         process_order("pizza", order_confirmed, order_ready, order_delivered),
                         process_order("tiramisú", order_confirmed, order_ready, order_delivered))

asyncio.run(asign_tasks())