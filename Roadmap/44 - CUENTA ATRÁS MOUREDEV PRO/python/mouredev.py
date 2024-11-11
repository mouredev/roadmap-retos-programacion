import datetime
import time
import os
import threading


def countdown(target_date):

    while True:

        now_date_utc = datetime.datetime.now(datetime.timezone.utc)

        remaining_time = target_date - now_date_utc

        if remaining_time.total_seconds() <= 0:
            print("\n¡Cuenta atrás finalizada!")
            break

        days, seconds = divmod(remaining_time.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        os.system("clear")

        print(
            f"Tiempo restante: {int(days)} días, {int(hours)} horas, {int(minutes)} minutos, {int(seconds)} segundos")

        time.sleep(1)


local_date = datetime.datetime(2024, 11, 11, 20, 47, 00)
local_date = local_date.replace(
    tzinfo=datetime.datetime.now().astimezone().tzinfo)

target_date_utc = local_date.astimezone(datetime.timezone.utc)

countdown_thread = threading.Thread(target=countdown, args=(target_date_utc,))
countdown_thread.start()
countdown_thread.join()
