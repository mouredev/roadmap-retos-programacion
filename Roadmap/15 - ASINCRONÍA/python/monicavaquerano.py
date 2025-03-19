# 15 ASINCRONÍA
# Monica Vaquerano
# https://monicavaquerano.dev

"""/*
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
 */"""

import asyncio, time


async def main(tiempo: int):
    print(f"started at {time.strftime('%X')}")

    print("Soy una ...")
    await asyncio.sleep(tiempo)
    print("... función asíncrona!")

    print(f"finished at {time.strftime('%X')}")


async def asincrona(tarea: str = "Default", tiempo: int = 1):
    print(
        f"Tarea: {tarea} Comienzo: {time.strftime('%X')} Duración: {tiempo} segundo(s)"
    )
    await asyncio.sleep(tiempo)
    print(f"... Tarea: {tarea} Final: {time.strftime('%X')}")


inicio = time.time()
asyncio.run(main(3))
fin = time.time()

print(f"\nLa función se demoró {(fin - inicio):.02f} segundos.\n")

inicio = time.time()
asyncio.run(asincrona("Prueba", 2))
fin = time.time()

print(f"\nLa función se demoró {(fin - inicio):.02f} segundos.\n")

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han
#  *   finalizado.


async def asincronizadas():
    await asyncio.gather(asincrona("A", 1), asincrona("B", 2), asincrona("C", 3))
    await asincrona("D", 1)


inicio = time.time()
asyncio.run(asincronizadas())
fin = time.time()

print(f"\nLa función se demoró {(fin - inicio):.02f} segundos.\n")
