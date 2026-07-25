# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

import time
import datetime
import os
import threading

# Función para la cuenta atrás
def countdown(target_datetime):
    while True:
        now = datetime.datetime.utcnow()
        remaining = target_datetime - now

        # Si el tiempo restante es menor o igual a cero, finalizamos
        if remaining.total_seconds() <= 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("¡Cuenta atrás finalizada!")
            break

        # Desglosamos días, horas, minutos y segundos
        days = remaining.days
        seconds = remaining.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        os.system("cls" if os.name == "nt" else "clear")
        print(f"Tiempo restante: {days} días, {hours} horas, {minutes} minutos, {seconds} segundos")
        time.sleep(1)

# Entrada de usuario
def main():
    day = int(input("Día: "))
    month = int(input("Mes: "))
    year = int(input("Año: "))
    hour = int(input("Hora: "))
    minute = int(input("Minuto: "))
    second = int(input("Segundo: "))

    # Convertimos la fecha local a UTC
    local_time = datetime.datetime(year, month, day, hour, minute, second)
    target_utc = local_time - datetime.timedelta(seconds=time.timezone)

    print(f"Fecha objetivo (UTC): {target_utc}")

    # Lanzamos el hilo
    threading.Thread(target=countdown, args=(target_utc,), daemon=True).start()

if __name__ == "__main__":
    main()
