import time
import datetime
import threading
import os
import pytz

def countdown(target_date_utc):
    while True:
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        time_diff = target_date_utc - now_utc

        if time_diff.total_seconds() <= 0:
            print("¡La cuenta atrás ha finalizado!")
            break

        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Limpia la terminal para mostrar la cuenta atrás actualizada
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Tiempo restante: {days} días, {hours} horas, {minutes} minutos, {seconds} segundos")

        time.sleep(1)

print("Introduce la fecha y hora de finalización en formato de 24 horas.")
year = int(input("Año (YYYY): "))
month = int(input("Mes (MM): "))
day = int(input("Día (DD): "))
hour = int(input("Hora (HH): "))
minute = int(input("Minuto (MM): "))
second = int(input("Segundo (SS): "))

local_time = datetime.datetime(year, month, day, hour, minute, second)
local_timezone = datetime.datetime.now().astimezone().tzinfo
target_date_utc = local_time.astimezone(pytz.utc)

countdown_thread = threading.Thread(target=countdown, args=(target_date_utc,))
countdown_thread.start()
countdown_thread.join()
