import asyncio, datetime # importando paquetes

# funcion asincrona
async def funcion_asincrona(tiempo:float, task_name:str):
    inicio = datetime.datetime.now() # tiempo y hora de inicio
    print(f"tarea: {task_name} iniciada el {inicio}")

    await asyncio.sleep(tiempo) # esperar x cantidad de tiempo

    fin = datetime.datetime.now() # tiempo y hora de fin
    print(f"{task_name} terminado el {fin}")

    transcurrido = fin - inicio # diferencia entre inicio y fin
    print(f"Tiempo transcurrido: {transcurrido}")

asyncio.run(funcion_asincrona(5, "ir al baño")) # ejecucion de la funcion asincrona

# ---- DIFICULTAD EXTRA ----

async def funcion(nombre:str, espera:float):
    print(f"Funcion {nombre} comenzada")

    await asyncio.sleep(espera)

    print(f"Funcion {nombre} terminada ({espera} segundos)")

async def main():
    await asyncio.gather(funcion("C", 3),
                         funcion("B", 2),
                         funcion("A", 1))

    await funcion("D", 1)

asyncio.run(main())