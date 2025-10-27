#  * EJERCICIO:
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.

import asyncio
from datetime import datetime
async def funcion_asincronia():
    print(f"Comenzando a la hora {datetime.now().strftime('%H:%M:%S')}")
    await asyncio.sleep(2) #simulamos 2 segundos de espera
    print(f"Finalizando a las {datetime.now().strftime('%H:%M:%S')}")

asyncio.run(funcion_asincronia())

print("-"*60)

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han
#  *   finalizado.

print("Dificultad extra\n")
print(f"Las funciones se empezaran a ejecutar a las: {datetime.now().strftime('%H:%M:%S')}")
async def funcion_c():
    await asyncio.sleep(3)
    return print(f"Funcion C termino a las: {datetime.now().strftime('%H:%M:%S')}")
async def funcion_b():
    await asyncio.sleep(2)
    return print(f"Funcion B termino a las: {datetime.now().strftime('%H:%M:%S')}")

async def funcion_a():
    await asyncio.sleep(1)
    return print(f"Funcion A termino a las: {datetime.now().strftime('%H:%M:%S')}")

async def conjuncion():
    task_a= asyncio.create_task(funcion_a())
    task_b= asyncio.create_task(funcion_b())
    task_c= asyncio.create_task(funcion_c())
    await asyncio.gather(task_a,task_b,task_c)

async def funcion_d():
    await asyncio.sleep(1)
    return print(f"Funcion D termino a las {datetime.now().strftime('%H:%M:%S')}")

asyncio.run(conjuncion())
asyncio.run(funcion_d())
print("-"*60)



