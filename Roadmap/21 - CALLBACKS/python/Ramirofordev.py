'''
Ejercicio: 
Explora el concepto de callback en tu lenguaje creando un ejemplo simple que muestre su funcionamiento.
'''

def al_cuadrado(number):
    return number ** 2

def apply_operation(func, value):
    return func(value)

result = apply_operation(al_cuadrado, 5)
print(result)

'''
Dificultad extra:
Crea un simulador de pedidos de un restaurante utilizando callbacks
Estara formado por una funcion que procesa pedidos.

Debe acpetar el nombre del plato, una callback de confirmacion, una de listo y otra de entrega
    * Debe imprimir una confirmacion cuando empiece el procesamiento
    * Debe simular un timpo aleatorio entre 1 a 10 segundos entre procesos
    * Debe invocar a cada callback siguiendo un orden procesado
    * Debe notificar que el plato esta listo o ha sido entregado
'''

import random
import asyncio

async def confirmar(plato):
    print(f"Confirmacion de tu pedido: '{plato}' ha sido recibido.")

async def listo(plato):
    print(f"El plato '{plato}' ya esta listo para servir.")

async def entregado(plato):
    print(f"El plato '{plato}' ha sido entregado, provecho!")

async def pedidos(plato, confirm, ready, serve):
    # Confirmar el pedido 
    await confirm(plato)
    await asyncio.sleep(random.randint(1, 10))

    # Plato listo
    await ready(plato)
    await asyncio.sleep(random.randint(1, 10))

    # Plato entregado
    await serve(plato)
    await asyncio.sleep(random.randint(1, 10))


def main():
    plato = input("Inserte el nombre del plato: ")
    asyncio.run(pedidos(plato, confirmar, listo, entregado))

main()