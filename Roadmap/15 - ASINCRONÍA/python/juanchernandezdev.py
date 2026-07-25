### Async Python ###
import asyncio
import time

async def first_function(name: str, seconds: int):
  print(f'{name}, function started, run time will be {seconds}.')
  start = time.time()
  await asyncio.sleep(seconds)
  timelapse = time.time() - start
  print(f'execution time: {timelapse:.2f}s')

async def test():
  await first_function('my test function', 2)

asyncio.run(test())

#! Optional Challenge

async def function_a():
  start = time.time()
  await asyncio.sleep(1)
  timelapse = time.time() - start
  print(f'Function A execution time: {timelapse:.2f}s')
  
async def function_b():
  start = time.time()
  await asyncio.sleep(2)
  timelapse = time.time() - start
  print(f'Function B execution time: {timelapse:.2f}s')

async def function_c():
  start = time.time()
  await asyncio.sleep(3)
  timelapse = time.time() - start 
  print(f'Function C execution time: {timelapse:.2f}s')
  
async def function_d():
  start = time.time()
  await asyncio.sleep(1)
  timelapse = time.time() - start
  print(f'Function D execution time: {timelapse:.2f}s')
  
async def main():
  await asyncio.gather(function_a(), function_b(), function_c())
  await function_d()
  
asyncio.run(main())
