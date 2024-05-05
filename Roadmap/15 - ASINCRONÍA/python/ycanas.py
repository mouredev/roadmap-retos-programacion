import asyncio
import datetime

# ------ I. Ejercicio

async def my_async_function(name: str, time: int) -> None:
    print(f"{name}, duración: {time}s, inicio: {datetime.datetime.now()}")
    await asyncio.sleep(time)
    print(f"{name} fin {datetime.datetime.now()}")


asyncio.run(my_async_function("task1", 5))


# ------ II. Extra

async def async_functions():
    await asyncio.gather(
        my_async_function("TaskC", 3),
        my_async_function("TaskB", 2),
        my_async_function("TaskA", 1),
    )
    await my_async_function("TaskD", 1)


asyncio.run(async_functions())
