"""
    * #15 ASINCRONÍA
"""

import asyncio


async def ejecutar_tarea(nombre, duracion):
    print(f"Tarea {nombre} iniciada")
    await asyncio.sleep(duracion)
    print(f"Tarea {nombre} finalizada")


"""
    * DIFICULTAD EXTRA
"""


async def main():
    tarea_c = ejecutar_tarea("C", 3)
    tarea_b = ejecutar_tarea("B", 2)
    tarea_a = ejecutar_tarea("A", 1)

    await asyncio.gather(tarea_c, tarea_b, tarea_a)
    print("Tareas A, B y C finalizadas. Iniciando tarea D...")
    await ejecutar_tarea("D", 1)


if __name__ == "__main__":
    asyncio.run(main())
