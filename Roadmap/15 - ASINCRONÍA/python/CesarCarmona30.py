import asyncio
import datetime

async def async_function(function_name, time):
    start_time = datetime.datetime.now()
    print(f"Start function {function_name}")
    print(f"{function_name} will take {time} seconds")
    while (datetime.datetime.now() - start_time).total_seconds() < time:
        current_time = datetime.datetime.now()
        elapsed_time = (current_time - start_time).total_seconds()
        print(f"{function_name} - Sec {int(elapsed_time) + 1}")
        await asyncio.sleep(1)
    print(f"{function_name} was completed after {time} seconds")

async def tasks():
    # Crear y ejecutar tareas asíncronas
    task_1 = async_function("Task 1", 10)
    task_2 = async_function("Task 2", 5)
    await asyncio.gather(task_1, task_2)

# Ejecutar el bucle de eventos de asyncio
asyncio.run(tasks())

async def main():
    # Ejecutar las funciones C, B y A en paralelo
    task_c = async_function("Function C", 3)
    task_b = async_function("Function B", 2)
    task_a = async_function("Function A", 1)
    await asyncio.gather(task_c, task_b, task_a)
    
    # Cuando C, B y A han terminado, ejecutar la función D
    task_d = async_function("Function D", 1)
    await task_d

# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())