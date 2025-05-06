# 44 - Cuenta atrás Mouredev Pro
import datetime
import time
import os
import threading

# Formatear el timedelta para mostrar en dias, horas, min, seg.
def format_timedelta(td: datetime.timedelta) -> str:
    total_seconds = td.total_seconds()
    days = td.days
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if days:
        return f"{days} dias {hours % 24:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
    else:
        return f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}"
    
def count_down(target_date):
    # Hacer el bucle de impresion infinita hasta llegar el momento
    while True:
        os.system("cls")
        # Imprimir hora del evento
        print("Fecha del evento: ")
        print(target_date.astimezone().strftime("%d/%m/%Y, %H:%M:%S"))
        print("El evento sera en: ")
        now_date_utc = datetime.datetime.now().astimezone(datetime.timezone.utc)
        remaining_time = target_date - now_date_utc
        formated_time = format_timedelta(remaining_time)

        if remaining_time.total_seconds() <= 0:
            print("La cuenta atras ha terminado")
            break
        
        print("Cuenta regresiva: ")
        print(formated_time)
        time.sleep(1)
    

# Definir la fecha del evento
local_date = datetime.datetime(2025,5,5,19,36,20)
local_date = local_date.replace(tzinfo=datetime.datetime.now().astimezone().tzinfo)

# Ejecucion con hilos
target_date_utc = local_date.astimezone(datetime.timezone.utc)
countdown_treath = threading.Thread(target=count_down, args=(target_date_utc,))
countdown_treath.start()
countdown_treath.join()