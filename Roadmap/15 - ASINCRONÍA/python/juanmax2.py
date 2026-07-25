from datetime import datetime
import time
import asyncio
"""
Asincronía
"""

async def tarea(name: str, duration: int):
    print(
        f"Tarea: {name}. Duración: {duration}s. Inicio: {datetime.now()}"
    )
    await asyncio.sleep(duration)
    print(
        f"Tarea: {name}. Fin: {datetime.now()}"
    )
    

asyncio.run(tarea("1", 3))

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


async def async_tareas():
    await asyncio.gather(
    tarea("C", 3),
    tarea("B", 2),
    tarea("A", 1)
)
    await tarea("D", 1)
    
asyncio.run(async_tareas())
