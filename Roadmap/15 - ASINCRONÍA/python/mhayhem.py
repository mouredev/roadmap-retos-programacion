from time import sleep
import time
import asyncio

# EJERCICIO:
# Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# asíncrona una función que tardará en finalizar un número concreto de
# segundos parametrizables. También debes poder asignarle un nombre.
# La función imprime su nombre, cuándo empieza, el tiempo que durará
# su ejecución y cuando finaliza.

async def task(name: str, seconds: int):
    print(f"Iniciando {name}.")
    await asyncio.sleep(seconds)
    print(f"{name} tardara {seconds} segundos.")
    return f"{name} termino."

async def main():
    start = time.time()

    answer = await asyncio.gather(
        task("Descarga", 6),
        task("Inicialización", 3),
        task("Petición http", 2)
    )
    
    end = time.time()
    print(f"\n Respuestas: {answer}")
    print(f"Tiempo de ejecución del programa: {end - start} s.")

# asyncio.run(main())

# DIFICULTAD EXTRA (opcional):
# Utilizando el concepto de asincronía y la función anterior, crea
# el siguiente programa que ejecuta en este orden:
# - Una función C que dura 3 segundos.
# - Una función B que dura 2 segundos.
# - Una función A que dura 1 segundo.
# - Una función D que dura 1 segundo.
# - Las funciones C, B y A se ejecutan en paralelo.
# - La función D comienza su ejecución cuando las 3 anteriores han
#   finalizado.
    
async def extra():
    await asyncio.gather(
        task("Función C", 3),
        task("Función B", 2),
        task("Función A", 1)
    )
    await task("Función D", 1)
    
asyncio.run(extra())