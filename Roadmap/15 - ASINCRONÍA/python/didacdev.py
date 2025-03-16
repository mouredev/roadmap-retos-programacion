import time
from datetime import datetime
import asyncio


async def main():
    # await asyn_function(3)
    await asyncio.gather(C(), B(), A())
    await D()


async def asyn_function(seconds: int):
    start = datetime.now()
    print(f"Ejecutando la funcion asyn_function")
    print(f"Comienzo: {start}")
    asyncio.sleep(seconds)
    finish = datetime.now()
    print(f"Fin: {finish}")
    print(f"Duración: {round((finish - start).seconds, 0)} segundos")


async def A():
    await asyncio.sleep(1)
    print("Función A finalizada")


async def B():
    await asyncio.sleep(2)
    print("Función B finalizada")


async def C():
    await asyncio.sleep(3)
    print("Función C finalizada")


async def D():
    await asyncio.sleep(1)
    print("Función D finalizada")


if __name__ == "__main__":
    asyncio.run(main())
