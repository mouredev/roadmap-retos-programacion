import asyncio
import time

# EJERCICIO:
# Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
# asíncrona una función que tardará en finalizar un número concreto de
# segundos parametrizables. También debes poder asignarle un nombre.
# La función imprime su nombre, cuándo empieza, el tiempo que durará
# su ejecución y cuando finaliza.

func_time_list = [('C', 3), ('B', 2), ('A', 1), ('D', 1)]

async def funcion_asincrona(nombre: str, segundos: int):
    inicio = time.perf_counter()
    print(f"Iniciando función {nombre} ({segundos}s)...")
    await asyncio.sleep(segundos)
    fin = time.perf_counter()
    print(f"Función {nombre} finalizó en {(fin - inicio):.2f} segundos.")

for n, s in func_time_list:
    asyncio.run(funcion_asincrona(n, s))
    print()

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

async def funciones_en_paralelo():
    await asyncio.gather(*(funcion_asincrona(n, s) for n, s in func_time_list[:-1]))
    print()

    await funcion_asincrona(*(func_time_list[-1]))
    print('\nTodas las funciones han finalizado')

asyncio.run(funciones_en_paralelo())