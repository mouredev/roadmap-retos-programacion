import asyncio
import datetime

async def my_func(name, duration):
    print(f"Nombre de la función: {name}. Duración: {duration} segundos. Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Nombre de la función: {name}. Fin: {datetime.datetime.now()}")

asyncio.run(my_func("A", 2))

"""
DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.

"""
# EJECUCIÓN EN PARALELO (GATHER)

async def async_funcs():
    await asyncio.gather(my_func("C", 3),my_func("B", 2),my_func("A", 1))
    await my_func("D", 1)
asyncio.run(async_funcs())

