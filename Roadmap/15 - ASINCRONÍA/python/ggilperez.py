# 15 Async
import asyncio
from datetime import datetime


async def async_function(sleep_time: int, name: str) -> None:
    print(f"Function {name}. Starting at: {datetime.utcnow()}. Duration {sleep_time}")

    await asyncio.sleep(sleep_time)

    print(f"Function {name}. Ending at: {datetime.utcnow()}")

asyncio.run(async_function(2, "slow_func"))

# Extra

async def run_tasks():
    await asyncio.gather(async_function(3, "C"), async_function(2, "B"), async_function(1, "A"))
    await async_function(1, "D")

asyncio.run(run_tasks())
