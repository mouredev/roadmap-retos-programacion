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
import os

def clear_console():
    # Borra la consola. Usa "cls" para Windows o "clear" para Linux/macOS.
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(target_datetime_utc):
    while True:
        # Calculamos la diferencia entre la fecha objetivo y la fecha actual
        current_time_utc = datetime.datetime.utcnow()
        remaining_time = target_datetime_utc - current_time_utc

        # Si la cuenta regresiva ha terminado, salimos del bucle
        if remaining_time.total_seconds() <= 0:
            clear_console()
            print("¡La cuenta atrás ha finalizado!")
            break

        # Extraemos días, horas, minutos y segundos de la diferencia
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Limpiamos la consola y mostramos el tiempo restante
        clear_console()
        print(f"Tiempo restante: {days} días, {hours} horas, {minutes} minutos, {seconds} segundos")
        
        # Esperamos un segundo antes de la siguiente actualización
        time.sleep(1)

# Solicitamos la fecha y hora de finalización al usuario
day = int(input("Día de finalización: "))
month = int(input("Mes de finalización: "))
year = int(input("Año de finalización: "))
hour = int(input("Hora de finalización: "))
minute = int(input("Minuto de finalización: "))
second = int(input("Segundo de finalización: "))

# Creamos el objeto datetime en el horario local
target_datetime_local = datetime.datetime(year, month, day, hour, minute, second)

# Convertimos la fecha local a UTC
target_datetime_utc = target_datetime_local - datetime.timedelta(hours=time.localtime().tm_gmtoff // 3600)

# Ejecutamos la cuenta regresiva en un hilo independiente
countdown_thread = threading.Thread(target=countdown, args=(target_datetime_utc,))
countdown_thread.start()
