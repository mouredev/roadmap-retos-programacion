import asyncio

async def Segundos(nombre, segundos):
    print(f"La tarea '{nombre}' comenzó.")
    print(f"La tarea '{nombre}' durará {segundos} segundos.")
    await asyncio.sleep(segundos)
    print(f"La tarea '{nombre}' finalizó.")


async def ejecutar_tareas():
    nombre_func = input('Nombre de la función: ')
    actividades = [
        Segundos(nombre_func, 2),
    ]
    # Ejecutar las actividades
    await asyncio.gather(*actividades)

asyncio.run(ejecutar_tareas())

'''
EXTRA
'''

async def funcA(segundos):

    await asyncio.sleep(segundos)
    print('La función A ya finalizó')

async def funcB(segundos):

    await asyncio.sleep(segundos)
    print('La función B ya finalizó')

async def funcC(segundos):

    await asyncio.sleep(segundos)
    print('La función C ya finalizó')

async def funcD(segundos):

    await asyncio.sleep(segundos)
    print('La función D ya finalizó')


async def FuncsABCD():
    print('Las funciones A, B y C se estan ejecutandose')
    await asyncio.gather(funcA(1), funcB(2), funcC(3))
    print('Las funciones A, B y C finalizaron')
    await asyncio.gather(funcD(1))


asyncio.run(FuncsABCD())
