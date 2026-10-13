#  * EJERCICIO:
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.

import time
import asyncio
from datetime import datetime 

async def download(name,wait_time):
    print(f"Ejecutando la función: {download.__name__}")
    print(f"Descargando archivo {name} .....")
    print(f"Tiempo de espera aproximado: {wait_time}")
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Tiempo de inicilizacion: {now}")
    await asyncio.sleep(wait_time)
    print("Archivo descargado")
    end = datetime.now().strftime("%H:%M:%S")
    print(f"Tiempo de finalizacion: {end}")


async def main():
    start_time = time.time()
    await asyncio.gather (download("C",3), download("B",2), download("A",1))
    await download("D", 1)
    finish_time = time.time() - start_time
    print(f"\n El tiempo total de la finalizacion de las descargas es de {finish_time:.2f} segundos")

asyncio.run(main())

# DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han
#  *   finalizado.


