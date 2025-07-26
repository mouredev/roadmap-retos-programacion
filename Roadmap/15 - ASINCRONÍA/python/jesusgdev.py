'''
EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
   asíncrona una función que tardará en finalizar un número concreto de
   segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
   su ejecución y cuando finaliza.
  
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
   el siguiente programa que ejecuta en este orden:
   - Una función C que dura 3 segundos.
   - Una función B que dura 2 segundos.
   - Una función A que dura 1 segundo.
   - Una función D que dura 1 segundo.
   - Las funciones C, B y A se ejecutan en paralelo.
   - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
'''

import asyncio  # ⏱️ Módulo para trabajar con funciones asíncronas
from datetime import datetime

# 🔁 Función asíncrona que recibe un nombre y una duración (en segundos)
async def async_task(task_name: str, duration: int):
    print(f"🔧 Tarea: [{task_name}] |🏁 Inicio: {datetime.now().strftime('%H:%M:%S')} |⏳ Duración de Ejecución: {duration} segundos")

    await asyncio.sleep(duration)  # 💤 Espera sin bloquear

    print(f"✅ Finalización {task_name}: {datetime.now().strftime('%H:%M:%S')}\n")

asyncio.run(async_task("Tarea Asíncrona", 5))


# 🚀 Función principal para ejecutar múltiples tareas
async def asyn_multi_tasks():
    # 🧪 Creamos varias tareas con diferentes nombres y tiempos
    await asyncio.gather(
        async_task("Tarea Asíncrona C", 3),
        async_task("Tarea Asíncrona B", 2),
        async_task("Tarea Asíncrona A", 1)
    )

    await async_task("Tarea Asincrona D", 1)


asyncio.run(asyn_multi_tasks())


