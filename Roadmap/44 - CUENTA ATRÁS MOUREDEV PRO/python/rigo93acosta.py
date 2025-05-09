"""
 * EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
"""

import datetime
import time
import threading

def countdown(end):
    target_end = end.astimezone(datetime.timezone.utc)

    while True:
        now = datetime.datetime.now().astimezone(datetime.timezone.utc)
        diff = target_end - now

        if diff.total_seconds() <= 0:
            print("\nCuenta atrás finalizada!!!\n")
            break
        else:
            print(f"Tiempo restante {diff.days:02} days " +
                  f"{diff.seconds//3600:02} hours " +
                  f"{diff.seconds//60%60:02} minutes " +
                  f"{diff.seconds%60:02} seconds", end='\r')
            time.sleep(1)

if __name__ == '__main__':
    end = datetime.datetime(2024, 11, 23, 11, 24, 00)
    end = end.replace(
        tzinfo=datetime.datetime.now().astimezone().tzinfo
        )
 
    thread = threading.Thread(target=countdown, args=(end,))
    thread.start()
    thread.join()
    
    # while True:
    #     now = datetime.datetime.now().astimezone(datetime.timezone.utc)
    #     diff = target_end - now

    #     if diff.total_seconds() <= 0:
    #         print("\nCuenta atrás finalizada!!!\n")
    #         break
    #     else:
    #         print(f"Tiempo restante {diff.days:02} days " +
    #               f"{diff.seconds//3600:02} hours " +
    #               f"{diff.seconds//60%60:02} minutes " +
    #               f"{diff.seconds%60:02} seconds", end='\r')
    #         time.sleep(1)
