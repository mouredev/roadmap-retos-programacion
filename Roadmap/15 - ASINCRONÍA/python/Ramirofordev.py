import datetime
import time
import asyncio

async def task(name: str, duration: int):
    print(f"Tarea: {name}. Duracion: {duration}s. Inicio: {datetime.datetime.now()}")
    time.sleep(duration)
    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}")

asyncio.run(task("1", 2))

'''
Dificultad extra:
Utilizando el concepto de asincronia y la funcion anterior, crea el siguiente programa que ejecuta en este orden:
    * Una funcion C que dura 3 segundos
    * Una funcion B que dura 2 segundos
    * Una funcion A que dura 1 segundo
    * Una funcion D que dura 1 segundo
        * Las funciones C, B y A se ejecutan en paralelo.
        * La funcion D comienza su ejecucion cuando las tres anteriores han finalizado
'''

async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

asyncio.run(async_tasks())

'''
Mi forma de hacerlo: 

async def a():
    print(f"Incio de la funcion a: {datetime.datetime.now()}")
    time.sleep(1)
    print(f"Fin de la funcion a: {datetime.datetime.now()}")

async def b():
    print(f"Inicio de la funcion b: {datetime.datetime.now()}")
    time.sleep(2)
    print(f"Fin de la funcion b: {datetime.datetime.now()}")

async def c():
    print(f"Inicio de la funcion c: {datetime.datetime.now()}")
    time.sleep(3)
    print(f"Fin de la funcion c: {datetime.datetime.now()}")

async def d():
    print(f"Inicio de la funcion d: {datetime.datetime.now()}")
    await asyncio.sleep(1)
    print(f"Fin de la funcion d: {datetime.datetime.now()}")

async def main():
    # Tasks
    tA = asyncio.create_task(a())
    tB = asyncio.create_task(b())
    tC = asyncio.create_task(c())

    # Esperamos a que terminen
    await asyncio.wait([tA, tB, tC])

    # Llamamos a D para que inicie
    await d()


asyncio.run(main())

'''