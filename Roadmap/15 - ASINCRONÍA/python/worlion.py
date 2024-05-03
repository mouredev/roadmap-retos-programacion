import asyncio
from datetime import datetime

"""
    EJERCICIO: Asincronía
"""

async def sleeper(name: str, seconds: int):
    now = datetime.now().strftime("%X")
    print(f"me llamo {name}, son las {now} y me voy a echar {seconds} segunditos... 🥱")    
    await asyncio.sleep(seconds)
    now = datetime.now().strftime("%X")
    print( f"me llamo {name}, ahora son las {now} y ya he terminado ⏰"    )

async def asynchronous_task(tasks):
    start_time = datetime.now()
    
    # tasks = [sleeper('Pepe', 3), sleeper('Juan', 5), sleeper('Manolo', 2)]
    await asyncio.gather(*tasks)
    
    end_time = datetime.now()
    print('Duration async: {}'.format(end_time - start_time))
        
asyncio.run(asynchronous_task([sleeper('Pepe', 3), sleeper('Juan', 5), sleeper('Manolo', 2)]))

"""
    DIFICULTAD EXTRA (opcional):
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")


async def main():
    tasks = [
        sleeper('C', 3), 
        sleeper('B', 2), 
        sleeper('A', 1), 
        sleeper('D', 1)
    ]
    await asyncio.gather(*tasks[:3])
    await tasks[3]
    
asyncio.run(main())