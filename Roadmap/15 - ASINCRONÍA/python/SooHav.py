# 15 ASINCRONÍA

# Ejercicio

import asyncio
import time


async def ejecutar_tarea(tarea: str, duracion: int):
    """
    Ejecuta una tarea asíncrona que espera durante un tiempo especificado.
    Parametros:
    - tarea (str): Nombre de la tarea.
    - duracion (int): Duración en segundos que tarda la tarea.
    """
    print(f'[{tarea}] Empieza la ejecución')
    inicio = time.time()
    await asyncio.sleep(duracion)
    fin = time.time()
    print(f'[{tarea}] Tiene una duración de {fin - inicio:.2f} segundos')
    print(f'[{tarea}] Termina la ejecución.')


async def ejecutar_programa() -> None:
    await asyncio.create_task(ejecutar_tarea('Tarea 1', 3))

asyncio.run(ejecutar_programa())

# Ejercicio Extra


async def ejecutar_tarea_2(tarea: str, duracion: int) -> None:
    """
    Ejecuta una tarea asíncrona que espera durante un tiempo especificado.
    Parametros:
    - tarea (str): Nombre de la tarea.
    - duracion (int): Duración en segundos que tarda la tarea.
    """
    try:
        print(f'[{tarea}] Empieza la ejecución')
        inicio = time.time()
        await asyncio.sleep(duracion)
        fin = time.time()
        print(f'[{tarea}] Tiene una duración de {fin - inicio:.2f} segundos')
    except Exception as e:
        print(f'[{tarea}] Error: {e}')
    finally:
        print(f'[{tarea}] Termina la ejecución.')


async def ejecutar_programa_2() -> None:
    tareas = [
        asyncio.create_task(ejecutar_tarea_2('C', 3)),
        asyncio.create_task(ejecutar_tarea_2('B', 2)),
        asyncio.create_task(ejecutar_tarea_2('A', 1))
    ]
    await asyncio.gather(*tareas)
    await asyncio.create_task(ejecutar_tarea_2('D', 1))

asyncio.run(ejecutar_programa_2())
