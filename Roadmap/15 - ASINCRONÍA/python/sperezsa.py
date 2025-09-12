import datetime
import asyncio

async def test(segundos, nombre):
    print(f"Comienza tarea '{nombre}', tiempo de espera {segundos} segundos: {datetime.datetime.now()}")
    await asyncio.sleep(segundos) 
    print(f"Acaba tarea '{nombre}': {datetime.datetime.now()}")

asyncio.run(test(3,"espera"))


"""
Extra
"""

async def async_tasks():
    await asyncio.gather(test(3,"C"), test(2,"B"), test(1,"A"))
    await test(1,"D")

asyncio.run(async_tasks())

