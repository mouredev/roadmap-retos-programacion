# 21 - Callbacks

import asyncio
import random

def end_process():
    print("Proceso terminado.")

def count_number(num, fun):
    for i in range(num):
        print(i+1)
    fun()

count_number(6,end_process)

def greeting_process(callback, name):
    print("Ejecutando el proceso de saludo....")
    callback(name)

def greet_callback(name: str):
    print(f"Hola {name}!")

greeting_process(greet_callback, "Gordo Master")

"""
Ejercicio Extra
"""

async def confir(name):
    print(f"Pedido de: {name} confirmado")

async def order_ok(name):
    print(f"Pedido de: {name} esta listo")

async def delivered(name):
    print(f"Pedido de: {name} fue entregado")

async def order(name,confir_callback,order_ok_callback,delivered_callback):
    await confir_callback(name)
    await asyncio.sleep(random.randint(1,10))
    
    await order_ok_callback(name)
    await asyncio.sleep(random.randint(1,10))
    
    await delivered_callback(name)

async def main():
    await asyncio.gather(
    order("Hamburguesa",confir,order_ok,delivered),
    order("Papas fritas",confir,order_ok,delivered),
    order("Gaseosa",confir,order_ok,delivered),
    order("Helado",confir,order_ok,delivered)
    )

asyncio.run(main())