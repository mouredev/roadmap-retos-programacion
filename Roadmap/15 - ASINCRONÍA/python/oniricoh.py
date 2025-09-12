import asyncio
import time

async def execute_task(name, seconds):
    print("\nEjecutando la tarea de forma asíncrona...")
    #obtiene el tiempo actual del sistema
    start_time = time.time()

    # Simulamos una tarea que tarda un cierto número de segundos
    await asyncio.sleep(seconds)
    
    #obtiene el tiempo actual del sistema (pasado los x segundos de espera)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Nombre '{name}'. Duración: {elapsed_time:.2f} segundos")

# async def main():
#     await execute_task("Daniel", 3)

# asyncio.run(main())



###############################################################################
## DIFICULTAD EXTRA
###############################################################################

async def main():
    tasks = [
        ("Task C", 3),
        ("Task B", 2),
        ("Task A", 1),
    ]
    
    for name, second in tasks:
        await execute_task(name, second)
    
    await execute_task("Task D", 1)

asyncio.run(main())
