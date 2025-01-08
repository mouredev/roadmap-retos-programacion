import asyncio
import datetime

async def esperar(nombre: str, duracion: int):
    print(f"nombre: {nombre}, duracion: {duracion}, comienzo: {datetime.datetime.now()}")
    await asyncio.sleep(duracion)
    print(f"Fin: {datetime.datetime.now()}")
    
asyncio.run(esperar("Sorubadguy", 1))

#!Extra
    
async def tareas():
    await asyncio.gather(task("A",1))
    await asyncio.run(D)
    
asyncio.run(tareas())