""" /*
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
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 */ """

import datetime
import time
import asyncio


async def task(duration: int, name: str):
    print(f"Tarea {name}: Duracion: {duration} Inicio: {datetime.datetime.now()}")

    await asyncio.sleep(duration)

    print(f"Tarea {name}: Fin: {datetime.datetime.now()}")


# asyncio.run(task(5, "Tarea 1"))

# asyncio.run(task(1,"Tarea 2"))
# asyncio.run(task(3,"Tarea 3"))

async def async_tasks():
    await asyncio.gather(task(3, "Funcion C"), task(2, "Funcion B"), task(1, "Funcion A"))
    await task(1, "Funcion D")

asyncio.run(async_tasks())

