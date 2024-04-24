import asyncio

async def asyncFunction(name, seconds):
  print(f"Inicia la ejecucion de {name}")
  print(f"Duracion de {name}: {seconds} segundos")
  await asyncio.sleep(seconds)
  print(f"Finaliza la ejecucion de {name}")

# asyncio.run(asyncFunction("Test", 3))


# DIFICULTAD EXTRA

async def multipleFunctions():
  await asyncio.gather(asyncFunction("C", 3), asyncFunction("B", 2), asyncFunction("A", 1))
  await asyncFunction("D", 1)

asyncio.run(multipleFunctions())