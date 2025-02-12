""" /*
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
 */ """

import datetime
import time
import os
import threading

def countdown(target_date):

    while True:

        now_date_utc = datetime.datetime.now(datetime.timezone.utc) 

        remaining_time = target_date_utc - now_date_utc

        if remaining_time.total_seconds() <= 0:
            print("\nCuenta atrás finalizada.")
            break

        days, seconds = divmod(remaining_time.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        os.system("cls")

        print(f"Tiempo restante: {int(days)} días, {int(hours)} horas, {int(minutes)} minutos y {int(seconds)} segundos.")

        time.sleep(1)

local_date = datetime.datetime(2025, 2, 10, 17, 28, 00)
local_date = local_date.replace(tzinfo=datetime.datetime.now().astimezone().tzinfo)

target_date_utc = local_date.astimezone(datetime.timezone.utc)

countdown_thread = threading.Thread(target=countdown, args=(target_date_utc,))
countdown_thread.start()
countdown_thread.join()