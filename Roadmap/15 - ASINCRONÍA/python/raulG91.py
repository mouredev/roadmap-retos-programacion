
import asyncio
import time

async def function(seconds:float,name:str):
    await asyncio.sleep(seconds)
    print(f'Hello {name}')
    
asyncio.run(function(3,"Raul"))  

#Extra
async def functionC():
    print("Starting function C")
    await asyncio.sleep(3)
    print("Ending function C")
async def functionB():
    print("Starting function B")
    await asyncio.sleep(2)
    print("Ending function B")
async def functionA():
    print("Starting function A")
    await asyncio.sleep(1)
    print("Ending function A")
async def functionD():
    print("Starting function D")
    await asyncio.sleep(1)  
    print("Ending function D")  
    
#Group all async functions into main    
async def main():
    print(f"started at {time.strftime('%X')}")
    async with  asyncio.TaskGroup() as tg:
      #it will wait until all tasks in the group are completed
      task1= tg.create_task(functionC())
      task2 = tg.create_task(functionB())
      task3 = tg.create_task(functionA())
    #Now run functionD
    await functionD()
      
    print(f"finished at {time.strftime('%X')}")
asyncio.run(main())    