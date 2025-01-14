import asyncio
from datetime import datetime

async def async_task(nombre, duracion):
    print(f"{datetime.now()}: La tarea '{nombre}' empieza. Durará {duracion} segundos.")
    await asyncio.sleep(duracion)
    print(f"{datetime.now()}: La tarea '{nombre} ha terminado.")

async def main():
    tarea1 = asyncio.create_task(async_task("Tarea 1", 3))
    tarea2 = asyncio.create_task(async_task("Tarea 2", 5))
    tarea3 = asyncio.create_task(async_task("Tarea 3", 2))
    await   asyncio.gather(tarea1, tarea2, tarea3)

asyncio.run(main())

### Ejercicio Extra ###

async def final_task(nombre, duracion):
    print(f"{datetime.now()}: La tarea '{nombre}' empieza. Durará {duracion} segundos.")
    await asyncio.sleep(2)
    print(f"{datetime.now()}: La tarea '{nombre} ha terminado.")
    

async def main_extra():
    tareas = [
    asyncio.create_task(async_task("Función C", 3)),
    asyncio.create_task(async_task("Función B", 2)),
    asyncio.create_task(async_task("Función A", 1)),
    ]
    await asyncio.wait(tareas)

    await final_task("Función D", 1)

asyncio.run(main_extra())