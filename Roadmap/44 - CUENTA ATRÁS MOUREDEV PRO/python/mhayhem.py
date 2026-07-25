# @Author Daniel Grande  (Mhayhem)


# ¡El 12 de noviembre lanzo mouredev pro!
# El campus de la comunidad para estudiar programación de
# una manera diferente: https://mouredev.pro
#
# Crea un programa que funcione como una cuenta atrás.
#
# - Al iniciarlo tendrás que indicarle el día, mes, año,
#   hora, minuto y segundo en el que quieres que finalice.
# - Deberás transformar esa fecha local a UTC.
# - La cuenta atrás comenzará y mostrará los días, horas,
#   minutos y segundos que faltan.
# - Se actualizará cada segundo y borrará la terminal en
#   cada nueva representación del tiempo restante.
# - Una vez finalice, mostrará un mensaje.
# - Realiza la ejecución, si el lenguaje lo soporta, en
#   un hilo independiente.

from datetime import timedelta, timezone, date, datetime
import os
from time import sleep
import threading

def countdown(finally_date):
    
    
    while True:
        os.system("cls" if os.name == "nt" else ("clear"))
        final_countdown = finally_date - datetime.now()
        
        if final_countdown.total_seconds() <= 0:
            print("La cuenta final ha terminado.")
            break
        
        seconds = int(final_countdown.total_seconds())
        
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        print(f"Dias: {days}, horas: {hours:02}, minutos: {minutes:02}, segundos: {secs:02}.")
        sleep(1)

def main():
    days, month, year = input("Diganos una fecha de finalizacion de la cuenta atras: (dd/mm/aaaa)").split("/")
    optional = input("¿Quieres añadir una hora específica?").lower()
    match optional:
        case "si":
            hour, minutes, seconds = input("Indique la hora: (hh:mm:ss)").split(":")
            finally_date = datetime(int(year), int(month), int(days), int(hour), int(minutes), int(seconds))
        case "no":
            finally_date = datetime(int(year), int(month), int(days))
        case _:
            print("La opción no es valida.")
    
    thread = threading.Thread(target=countdown, args=(finally_date,))
    thread.start()
    print("La cuenta atras se esta ejecutando en otro hilo.")


if __name__=="__main__":
    main()
