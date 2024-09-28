# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.
#  *
import asyncio
from datetime import datetime

async def my_asyn_func(time, name):
    start = datetime.now()
    print(f"Task:{name} Start: {start.strftime("%H:%M:%S")} ")
    await asyncio.sleep(time)
    end = datetime.now()
   
    print(f"Task:{name} End:{end.strftime("%H:%M:%S")} Duration:{time}")

 

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
#  */


async def main():
        
        await asyncio.gather(my_asyn_func(10,"Aufgabe A"),my_asyn_func(7,"Aufgabe B"), my_asyn_func(3,"Aufgabe C"))
        await my_asyn_func(1,"Aufgabe D")

asyncio.run(main())