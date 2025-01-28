import datetime
import time
import asyncio

#Ejercicio

async def task(name:str, duration:int):
    print(f"Tarea: {name}. Duración: {duration}s. Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Fin {name}: {datetime.datetime.now()}")

#asyncio.run(task("1", 3))
#asyncio.run(task("2", 2))


#EJERCICIO EXTRA

async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

asyncio.run(async_tasks())