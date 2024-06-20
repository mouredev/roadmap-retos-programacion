import datetime
import time
import asyncio
"""
Ejercicio
"""


async def tarea(nombre: str, duracion: int):
    print(f"Tarea: {nombre} duración: {duracion}s. Inicio {datetime.datetime.now()} ")
    await asyncio.sleep(duracion)
    print(f"Tarea: {nombre} Fin: {datetime.datetime.now()} ")

#asyncio.run(tarea("1", 5))

"""
Extra
"""

async def tareas_asincronas():
    await asyncio.gather(tarea("C", 5),
    tarea("B", 2),
    tarea("A", 1)
    )
    await tarea("D", 1)
    

 
asyncio.run(tareas_asincronas())
