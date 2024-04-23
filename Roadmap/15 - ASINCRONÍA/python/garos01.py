import asyncio


async def ejecutar_tarea(nombre, segundos):
    print(f"{nombre}: Comenzando la tarea.")
    await asyncio.sleep(segundos)
    print(f"{nombre}: Tarea completada después de {segundos} segundos.")


async def main():
    # Definir las tareas que se ejecutarán de manera asíncrona
    tarea1 = ejecutar_tarea("Tarea 1", 3)
    tarea2 = ejecutar_tarea("Tarea 2", 5)
    tarea3 = ejecutar_tarea("Tarea 3", 2)

    # Ejecutar las tareas de manera simultánea
    await asyncio.gather(tarea1, tarea2, tarea3)


# Iniciar el bucle de eventos de asyncio y ejecutar el programa
asyncio.run(main())


# Ejercicio extra


async def funcion_a():
    print("Función A: Comenzando la ejecución.")
    await asyncio.sleep(1)
    print("Función A: Finalizada.")


async def funcion_b():
    print("Función B: Comenzando la ejecución.")
    await asyncio.sleep(2)
    print("Función B: Finalizada.")


async def funcion_c():
    print("Función C: Comenzando la ejecución.")
    await asyncio.sleep(3)
    print("Función C: Finalizada.")


async def funcion_d():
    print("Función D: Esperando a que finalicen las funciones C, B y A.")
    await asyncio.gather(funcion_c(), funcion_b(), funcion_a())
    print(
        "Función D: Todas las funciones C, B y A han finalizado. Comenzando ejecución."
    )
    await asyncio.sleep(1)
    print("Función D: Finalizada.")


async def main():
    await asyncio.gather(funcion_c(), funcion_b(), funcion_a(), funcion_d())


asyncio.run(main())
