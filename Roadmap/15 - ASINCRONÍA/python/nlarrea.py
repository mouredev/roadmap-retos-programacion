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
from datetime import datetime


async def print_parameters(seconds: int, name: str) -> None:
    print(f"Task: {name}\nTime: {seconds}\nStart: {datetime.now()}\n")
    await asyncio.sleep(seconds)
    print(f"Task: {name}\nEnd: {datetime.now()}\n")


async def main():
    await asyncio.gather(
        print_parameters(5, "task 1"),
        print_parameters(8, "task 2"),
        print_parameters(1, "task 3"),
        print_parameters(15, "task 4"),
    )


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


async def run():
    tasks = [
        print_parameters(3, "C"),
        print_parameters(2, "B"),
        print_parameters(1, "A"),
    ]
    await asyncio.gather(*tasks)

    await print_parameters(1, "D")


asyncio.run(run())
