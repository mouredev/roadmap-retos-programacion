# 15 - Asincronia

import asyncio
from datetime import datetime

async def call_name(name,time_to_wait):
    print(datetime.now().time().strftime(f"Comienza función: {name}: %X, durara {time_to_wait} segundos"))
    await asyncio.sleep(time_to_wait)
    print(datetime.now().time().strftime(f"Termina funcion {name}: %X"))

# asyncio.run(call_name("Gordo Master",2))

"""
Ejercicio Extra
"""
async def main():

    await asyncio.gather(
        call_name("C",3),
        call_name("B",2),
        call_name("A",1)
    )
    
    await call_name("D",1)

asyncio.run(main())
