"""
 EJERCICIO:
 Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 asíncrona una función que tardará en finalizar un número concreto de
 segundos parametrizables. También debes poder asignarle un nombre.
 La función imprime su nombre, cuándo empieza, el tiempo que durará
 su ejecución y cuando finaliza.

 DIFICULTAD EXTRA (opcional):
 Utilizando el concepto de asincronía y la función anterior, crea
 el siguiente programa que ejecuta en este orden:
 - Una función C que dura 3 segundos.
 - Una función B que dura 2 segundos.
 - Una función A que dura 1 segundo.
 - Una función D que dura 1 segundo.
 - Las funciones C, B y A se ejecutan en paralelo.
 - La función D comienza su ejecución cuando las 3 anteriores han
   finalizado.
"""

import datetime
import asyncio

print(f"== Explicación {'=' * 30}\n")

print(f"""
Tomado de https://eiposgrados.com/blog-python/programacion-asincronica-en-python/  <= muy buen artículo.

En esencia, la programación asincrónica es una técnica que permite a las aplicaciones realizar múltiples tareas simultáneamente, sin
bloquear la ejecución del programa. A diferencia de la programación síncrona tradicional, donde las operaciones se realizan en orden secuencial,
la programación asincrónica aprovecha la capacidad de ejecutar tareas en segundo plano mientras el programa principal sigue funcionando.
Esto se logra mediante el uso de dos palabras clave fundamentales en Python: `async` y `await`. 

Con `async`, puedes declarar funciones asincrónicas que pueden ejecutar múltiples tareas sin bloquear el flujo principal del programa. Por otro lado,
`await` permite que una función espere el resultado de una operación asíncrona sin bloquear la ejecución. Esta combinación permite que las
aplicaciones realicen operaciones en paralelo, mejorando drásticamente su capacidad de respuesta y rendimiento. 
""")

print(f"== Dificultad Extra {'=' * 30}\n")


def log_task(funcion):
    async def wrapper(*args, **kwargs):
        inicio = datetime.datetime.now()
        print(f"BEGIN {funcion.__name__} - Nombre: {args[0]} - ejecutar por {args[1]} segundos - Lanzado a las {datetime.datetime.now().strftime('%H:%M:%S')}")
        await funcion(*args, **kwargs)
        duracion = datetime.datetime.now() - inicio
        print(f"END {funcion.__name__} - Nombre: {args[0]} / duró: {duracion.seconds} segundo - Terminó a las {datetime.datetime.now().strftime('%H:%M:%S')}")

    return wrapper


@log_task
async def task(tarea: str, tiempo: int):
    return await asyncio.sleep(tiempo)


async def disparo_paralelo():
    # gather lanza simultáneamente todas las funciones que se pasen como argumento.
    await asyncio.gather(task("tarea_C", 3), task("tarea_B", 2), task("tarea_A", 1))


# Solo asíncrono
asyncio.run(task("tarea_C", 3))

# Asíncrono y paralelo
asyncio.run(disparo_paralelo())
