#15 - Asincronía
"""
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
  La función imprime su nombre, cuándo empieza, el tiempo que durará su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""
from datetime import datetime 

import asyncio
async def nameAndWait(nameFunct: str, seconds: int) -> int:
    """function to wait"""

    print(f"Fucntion name: {nameFunct}")
    now = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
    print(f"{nameFunct} Starting at: {now}")
    print(f"{nameFunct} Wait for: {seconds} seconds.")
    await asyncio.sleep(seconds)
    print(f"{nameFunct} Ending at: {datetime.today().strftime('%d/%m/%Y %H:%M:%S')}")

asyncio.run(nameAndWait("Wait for five minutes...",1))
#asyncio.run(sumWithWait(20,2,2))

#EXTRA:
import time

async def main():
    """calling the functions together"""
    # testing
    await asyncio.gather(
        nameAndWait("C", 3),
        nameAndWait("B", 1),
        nameAndWait("A", 1)
    )

async def second():
    """calling more functions before"""
    await asyncio.gather(
        nameAndWait("D", 1)
    )

if __name__ == "__main__":
    init_time = time.time()

    # strating main function
    asyncio.run(main())
    asyncio.run(second())

    finish_time = time.time()

    print(f"\nAll Excecution took: {round(finish_time - init_time, 3)} seconds.")


