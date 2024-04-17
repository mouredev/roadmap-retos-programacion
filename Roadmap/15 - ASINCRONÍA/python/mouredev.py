import datetime
import asyncio

"""
Ejercicio
"""


async def task(name: str, duration: int):
    print(
        f"Tarea: {name}. Duración: {duration}s. Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(
        f"Tarea: {name}. Fin: {datetime.datetime.now()}")


asyncio.run(task("1", 2))

"""
Extra
"""


async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

asyncio.run(async_tasks())
