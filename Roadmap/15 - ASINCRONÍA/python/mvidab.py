from datetime import datetime
import time
import asyncio

'''
Ejercicio
'''

async def function(name : str, duration_sec: int):
    
    print(f"Función: {name}. Duración: {duration_sec} s. Inicio; {datetime.now()}")
    await asyncio.sleep(duration_sec)
    print(f"Función: {name}. Fin; {datetime.now()}")


asyncio.run(function("Ejercicio", 5))


'''
Ejercicio extra
'''
#function("D", 1) 
async def async_tasks():
    await asyncio.gather(function("C", 3), function("B", 2), function("A", 1))  # Ejecución en paralelo
    await function("D", 1)

asyncio.run(async_tasks())

