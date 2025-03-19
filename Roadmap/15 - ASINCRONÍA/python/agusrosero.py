"""
/*
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
 */
"""
import asyncio

"""EJERCICIO:"""


async def main(seconds):
    print('Hernan ...')
    await asyncio.sleep(seconds)
    print('Fin de la ejecucion!')

asyncio.run(main(2))

"""DIFICULTAD EXTRA:"""


async def funcion_C():
    print('Funcion C')
    await asyncio.sleep(3)


async def funcion_B():
    print('Funcion B')
    await asyncio.sleep(2)


async def funcion_A():
    print('Funcion A')
    await asyncio.sleep(1)


async def funcion_D():
    print('Funcion D')
    await asyncio.sleep(1)


async def test():
    await asyncio.gather(funcion_C(), funcion_B(), funcion_A())
    await funcion_D()

asyncio.run(test())
