"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
"""

import asyncio
from datetime import datetime, timedelta


async def my_async_function(sleep_time: int, name: str) -> None:
    starts_at = datetime.now()
    ends_at = starts_at + timedelta(0, sleep_time)
    print(
        f"{name:-^60}",
        f"starts_at={starts_at.strftime("%c")}",
        f"duration={sleep_time}",
        f"ends_at={ends_at.strftime("%c")}",
        sep="\n"
    )
    await asyncio.sleep(sleep_time)
    ends_at = datetime.now().strftime("%c")
    print(f"{name} - Finshed at {ends_at}")


async def main():
    task_1 = asyncio.create_task(my_async_function(5, "first"))
    task_2 = asyncio.create_task(my_async_function(3, "second"))
    task_3 = asyncio.create_task(my_async_function(7, "third"))

    await task_1
    await task_2
    await task_3


asyncio.run(main())


"""
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

print("-" * 60)

async def extra():
    await asyncio.gather(
        my_async_function(3, "C"),
        my_async_function(2, "B"),
        my_async_function(1, "A")
    )

    await my_async_function(1, "D")

asyncio.run(extra())