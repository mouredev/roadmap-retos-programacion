import asyncio
import datetime

async def asyncTask(name: str, seconds: int):
    print(f"Comienza la función {name}. Duración de {seconds} segundos. Hora de comienzo {datetime.datetime.now().strftime('%H:%M:%S')}")
    await asyncio.sleep(seconds)
    print(f"Finaliza la función {name}. Hora de finalización {datetime.datetime.now().strftime('%H:%M:%S')}")
    
asyncio.run(asyncTask("Test 1", 5))


# Extra

async def extra():
    await asyncio.gather(
        asyncTask("C", 3),
        asyncTask("B", 2),
        asyncTask("A", 1)
    )
    await asyncTask("D", 1)
    
asyncio.run(extra())