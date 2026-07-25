# RETO 15 ASINCRONÍA

import datetime
import asyncio

"""
PROGRAMA QUE EJECUTE UNA FUNCIÓN ASÍNCRONA
"""

async def task(name: str, duration: int):
    print(
        f"Task: {name}. Duration: {duration}sec. Start: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(
        f"Task: {name}. End: {datetime.datetime.now()}")
    

asyncio.run(task("1", 2))



# Extra

print("🧩 DIFICULTAD EXTRA - 10 MANERAS DE MOSTRAR LA FECHA 🧩")

"""
Utilizando el concepto de asincronía y la función anterior, crea
el siguiente programa que ejecuta en este orden:
Una función C que dura 3 segundos.
Una función B que dura 2 segundos.
Una función A que dura 1 segundo.
Una función D que dura 1 segundo.
Las funciones C, B y A se ejecutan en paralelo.
La función D comienza su ejecución cuando las 3 anteriores han
finalizado.
"""

async def async_task():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1), task("D", 1))

asyncio.run(async_task())