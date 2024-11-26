### CALLBACKS EN PYTHON

'''
Un callback es simplemente una función que:

Se pasa como argumento a otra función.
Es llamada dentro de esa función en un momento determinado.
'''

# Definimos una función callback
#def saludo(name: str) -> None:
#    print(f"Hola {name}")
#
## Función principal que usará el callback
#def procesar_saludo(name: str, my_callback) -> None:
#    print("Procesando saludo...")
#    my_callback(name)
#    print("Saludo procesado.")
#
#procesar_saludo("Brais", saludo)


### EJERCICIO EXTRA
import asyncio #Vamos a trabajar con procesos
from random import randint #Para generar los tiempo aleatorios

# Funciones callback
async def order_confirmed(plate_name: str) -> None:
    print(f"La comanda para el plato: {plate_name} está confirmada")
    await asyncio.sleep(randint(1,10)) # Generamos un tiempo aleatorio entre 1 y 10

async def order_ready(plate_name: str) -> None:
    print(f"La comanda para el plato: {plate_name} está lista")
    await asyncio.sleep(randint(1,10)) # Generamos un tiempo aleatorio entre 1 y 10

async def order_delivered(plate_name: str) -> None:
    print(f"La comanda para el plato: {plate_name} está entregada")
    await asyncio.sleep(randint(1,10)) # Generamos un tiempo aleatorio entre 1 y 10

# Función principal
async def procesar_pedido(plate_name: str, cb_confirmed, cb_ready, cb_delivered) -> None:
    print(f"Procesando pedido de {plate_name}...")
    #await asyncio.sleep(1)
    await cb_confirmed(plate_name)
    #await asyncio.sleep(1)
    await cb_ready(plate_name)
    #await asyncio.sleep(1)
    await cb_delivered(plate_name)
    #await asyncio.sleep(1)
    print(f"Pedido de {plate_name} procesado.")
    
# Ejecución asíncrona
async def main() -> None:
    await asyncio.gather(
        procesar_pedido("Pizza", order_confirmed, order_ready, order_delivered),
        procesar_pedido("Hamburguesa", order_confirmed, order_ready, order_delivered),
        procesar_pedido("Kebap", order_confirmed, order_ready, order_delivered)
    )

# Ejecutar la función principal
asyncio.run(main())
    
### FIN EJERCICIO EXTRA

### FIN CALLBACKS EN PYTHON

