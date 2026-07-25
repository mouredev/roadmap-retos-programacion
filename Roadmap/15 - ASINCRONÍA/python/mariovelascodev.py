import asyncio #importamos el modulo para poder utilizar asíncrnia
from datetime import datetime #importamos el modulo para trabajar con fechas y horas

#Creamos la función asíncrona
async def async_function(name, time):
    print(f"Iniciando función {name}: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
    await asyncio.sleep(time) #Hace una espera del tiempo indicado
    print(f"La función {name}, ha finalizado: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")

#Inicia el bucle de eventos y la corrutina
asyncio.run(async_function("test", 3))

print("---"*10,"\n")

#Extra
async def async_functions():
    #Ejecutamos de forma paralela las tres funciones
    await asyncio.gather(
        async_function("C", 3),
        async_function("B", 2),
        async_function("A", 1)
    )
    
    #Se ejecuta una vez han terminado de ejecutarse el bloque gather
    await async_function("D", 1)
    

asyncio.run(async_functions())