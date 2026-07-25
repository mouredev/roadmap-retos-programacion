import datetime
import asyncio

async def task(name: str, duration: int):
    print(f"Task: {name}. Duration: {duration}s. Start: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Task: {name}. End: {datetime.datetime.now()}")

#asyncio.run(task("1", 4))



#Extra Exercise

async def async_tasks():
    await asyncio.gather(task("c", 3), task("B", 2), task("A", 1))

    await task("D", 1)

#asyncio.run(async_tasks())

async def main():
    await task("1", 4) #part 1

    await async_tasks() #part2
    

asyncio.run(main())