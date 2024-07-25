import asyncio
import time

"""
* EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
"""

async def async_func(secs,name):
    print(f"El nombre de la función es {name} y va a tardar {secs} segundos en ejecutarse")
    print(f"La hora de inicio es {time.strftime("%X")}")
    await asyncio.sleep(secs)
    print(f"La hora de fin es {time.strftime("%X")}")
    

asyncio.run(async_func(3,"test"))

"""
* DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
"""
async def A ():
    await asyncio.sleep(1)
    print(f"ejecutada función A a las {time.strftime("%X")}")
async def B ():
    await asyncio.sleep(2)
    print(f"ejecutada función B a las {time.strftime("%X")}")
async def C ():
    await asyncio.sleep(3)
    print(f"ejecutada función C a las {time.strftime("%X")}")

async def D():
    print(f"Inicio: {time.strftime("%X")}")
    task1 = asyncio.create_task(A())
    task2 = asyncio.create_task(B())
    task3 = asyncio.create_task(C())
    await task1
    await task2
    await task3
    print(f"ejecutada función D a las {time.strftime("%X")}")

asyncio.run(D())
