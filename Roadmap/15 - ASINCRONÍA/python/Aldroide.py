# Ejercicio
"""
    Ejecutar una programa capaz de ejecutar de manera asíncrona una función
    que tardará en finalizar un numero concreto de segundos parametrizables
    Tambien debes poder asignarle un nombre
    La función imprime su nombre, cuando empieza, el tiempo que durara la ejecución
    y cuando finaliza
"""
import asyncio
import datetime


async def asyncHello(name: str, seconds: int):
    print(f"""La función {name}, dura {seconds} segundos
              Inica en {datetime.datetime.now().strftime('%H:%M:%S')}""")
    await asyncio.sleep(seconds)
    print(
        f"La función {name} ha finalizado en: {datetime.datetime.now().strftime('%H:%M:%S')}")

asyncio.run(asyncHello("Test", 5))


# Ejercicio extra
"""
  Utilizando el concepto de asincronía y la función anterior, crea
  el siguiente programa que ejecuta en este orden:
  - Una función C que dura 3 segundos.
  - Una función B que dura 2 segundos.
  - Una función A que dura 1 segundo.
  - Una función D que dura 1 segundo.
  - Las funciones C, B y A se ejecutan en paralelo.
  - La función D comienza su ejecución cuando las 3 anteriores han
  finalizado.
"""


async def ejercicioExtra():
    await asyncio.gather(
        asyncHello("C", 3),
        asyncHello("B", 2),
        asyncHello("A", 1),
    )


asyncio.run(ejercicioExtra())
