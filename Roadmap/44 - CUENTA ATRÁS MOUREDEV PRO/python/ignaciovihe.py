""" * EJERCICIO:
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
 *   un hilo independiente."""


from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
import threading
import time
import os

def print_resting_time(final_date: datetime, now: datetime):

    diff = relativedelta(final_date, now)

    print(f"{diff.years} años - {diff.months} meses - {diff.days} días - {diff.hours} horas - {diff.minutes} minutos - {diff.seconds} segundos.")


def counter(final_date_utc , now_utc):
    os.system('cls' if os.name == 'nt' else 'clear')

    while (final_date_utc - now_utc) > timedelta(0):
        os.system('cls' if os.name == 'nt' else 'clear')
        now_utc = datetime.now(timezone.utc).replace(microsecond=0)
        print_resting_time(final_date_utc, now_utc)

        time.sleep(1)

    print("Temporizador terminado!!!")


date = input("Introduce una fecha con el siguiente formato. ej: '30-07-2025 15:45:00'")
# Se obtiene un datetime de un str, pasandole el formato que tendrá la entrada.
final_date = datetime.strptime(date, "%d-%m-%Y %H:%M:%S")

# Como el datetime no tiene uso horario, lo reemplazamos (propiedad tzinfo) por el uso horario,
# de un datenime.now con uso horario.
final_date = final_date.replace(tzinfo=datetime.now().astimezone().tzinfo)

# Una vez que nuestra fecha ya tiene uso horario, usamos astimezone para cambiarlo a utc.
final_date_utc = final_date.astimezone(timezone.utc).replace(microsecond=0)

# CVuando usamos now, no hace falta hacer lo anterior, podemos pedirlo como parametro directamente.
now_utc = datetime.now(timezone.utc).replace(microsecond=0)

# Lanzamos un hilo para que se ejecute en segundo plano. daemon indica si debe parar cuando termine el resto de la ejecución.
# en este caso pongo false porque como el programa no hace otra cosa, terminaria de inmediato si hacer la cuenta atras.
thread = threading.Thread(target=counter,args=(final_date_utc ,now_utc,), daemon=False)
thread.start()






