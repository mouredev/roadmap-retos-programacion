import asyncio
import datetime

# Ejercicio función asincrona


async def async_task(name: str, duration: int):
    print(
        f"Comienza la tarea {name}. Duración de {duration} segundos. Hora de comienzo {datetime.datetime.now().strftime('%H:%M:%S')}"
    )
    await asyncio.sleep(duration)
    print(
        f"Finaliza la tarea {name}. Hora de finalización {datetime.datetime.now().strftime('%H:%M:%S')}"
    )


# Dificultad extra
async def async_tasks():
    await asyncio.gather(async_task("C", 3), async_task("B", 2), async_task("A", 1))
    await async_task("D", 1)


if __name__ == "__main__":
    asyncio.run(async_task("Tarea 1", 2))

    asyncio.run(async_tasks())
