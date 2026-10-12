"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
"""

import asyncio

async def funcion_asincrona(seconds = 1):
    print("funcion_asincrona")
    print("Empieza ahora...")
    print(f"Tardará {seconds} segundos...")
    await asyncio.sleep(seconds)
    print("Finaliza ahora...")

asyncio.run(funcion_asincrona(2))


import datetime, time
def task(name: str, duration: int) -> None:
    print(f"Tarea: {name}. Duración: {duration} s. Inicio: {datetime.datetime.now()}.")

    time.sleep(duration)
    
    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}.")

task("1", 2)

async def task(name: str, duration: int) -> None:
    print(f"Tarea: {name}. Duración: {duration} s. Inicio: {datetime.datetime.now()}.")

    await asyncio.sleep(duration)
    
    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}."); print()

asyncio.run(task("2", 2))

#### EXTRA ####

# Me confunde su forma de escribir, no coincido con las soluciones, lo que dice el escrito y lo que él dice en vídeo.


async def async_tasks():
    await asyncio.gather(
        task("C", 3),
        task("B", 2),
        task("A", 1)
    )
    await task("D", 1)

asyncio.run(async_tasks())