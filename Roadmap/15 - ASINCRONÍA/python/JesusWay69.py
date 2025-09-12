import os
os.system('cls')
from datetime import datetime as DT
import time
import asyncio

""" * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
"""

def asynchrone (wait_seconds:int,name:str):
    start_time = DT.now()
    print(f"La ejecución de {name} durará {wait_seconds} segundos")
    print("La ejecución comienza a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    time.sleep(wait_seconds)
    print("Ejecución de ",name," terminada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    end_time = DT.now()
    print("Duración de la ejecución: ", end_time-start_time, "\n")
asynchrone(4,"\'Hola Mundo\'")

""" * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado."""

async def C ():
    print("Función C iniciada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    await asyncio.sleep(3)
    print("Función C terminada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
async def B ():
    print("Función B iniciada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    await asyncio.sleep(2)
    print("Función B terminada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    
async def A ():
    print("Función A iniciada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    await asyncio.sleep(1)
    print("Función A terminada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    
def D ():
    print("Función D iniciada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))
    time.sleep(1)
    print("Función D terminada a las {}:{}:{}".format(DT.now().hour,DT.now().minute,DT.now().second))

async def paralllel_funtcions():
    funtc_C = asyncio.create_task(C())
    funtc_B = asyncio.create_task(B())
    funtc_A = asyncio.create_task(A())
    await asyncio.gather(funtc_C,funtc_B,funtc_A)
asyncio.run(paralllel_funtcions())
D()

    




    