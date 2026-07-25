###################################### ASINCRONÍA ################################################
import asyncio #Módulo para poder programar tareas recurrentes

#async def async_task(name: str, execution_time: int = 1):
#    """Tarea asíncrona que ejecuta un bloque de código durante un tiempo determinado"""
#    print(f"Esta tarea tendrá una duración de {execution_time} segundos")
#    print(f"Comenzando la tarea {name}...")
#    await asyncio.sleep(execution_time) #Pausa la ejecución durante el tiempo especificado
#    print(f"Tarea {name} finalizada.")
#
#asyncio.run(async_task("Formating SSD", 5))

###################################  EXTRA  ##############################################################
async def proccess_data(name: str, execution_time: int = 1):
    print(f"Inicio de ejecución de tarea {name}")
    await asyncio.sleep(execution_time)
    print(f"Fin de ejecución de tarea {name}")

# Ejecución asíncrona del módulo main
async def main():
    
    # Ejecutamos varias tareas en paralelo
    await asyncio.gather(
        proccess_data("Tarea C", 3),
        proccess_data("Tarea B", 2),
        proccess_data("Tarea A", 1),
    )    
    
    # Ejecución última
    final_task = asyncio.create_task(proccess_data("Tarea D", 1))
    await final_task
    

asyncio.run(main=main())
###################################  FIN EXTRA  ##############################################################
###################################### FIN ASINCRONÍA ################################################