import datetime
import asyncio

# ejercicio

async def task(name: str, duration: int):
    print(f"Tarea:{name}. Duración: {duration}s. Inicio: {datetime.datetime.now().strftime("%H:%M:%S")}")
    await asyncio.sleep(duration)
    print(f"Tarea:{name}. Fin: {datetime.datetime.now().strftime("%H:%M:%S")}")
    
#asyncio.run(task("1", 2))

# EXTRA

async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)

#asyncio.run(async_tasks())

async def main():
    await task("1", 2)          # ejercicio
    await async_tasks()         # extra

if __name__ == "__main__":
    asyncio.run(main())



