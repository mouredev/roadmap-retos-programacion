import asyncio
import datetime

"""
    ASYNCHRONOUS
"""


async def task(name: str, duration: int):
    print(f"Task: {name}. Duration: {duration}s. Start: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Task: {name}. End: {datetime.datetime.now()}")


asyncio.run(task("First async task", 2))

"""
    EXTRA EXERCISE
"""


async def async_tasks():
    await asyncio.gather(task("C", 3), task("B", 2), task("A", 1))
    await task("D", 1)


asyncio.run(async_tasks())
