r"""
 EJERCICIO:
 ¡El 12 de noviembre lanzo mouredev pro!
 El campus de la comunidad para estudiar programación de
 una manera diferente: https://mouredev.pro

 Crea un programa que funcione como una cuenta atrás.

 - Al iniciarlo tendrás que indicarle el día, mes, año,
   hora, minuto y segundo en el que quieres que finalice.
 - Deberás transformar esa fecha local a UTC.
 - La cuenta atrás comenzará y mostrará los días, horas,
   minutos y segundos que faltan.
 - Se actualizará cada segundo y borrará la terminal en
   cada nueva representación del tiempo restante.
 - Una vez finalice, mostrará un mensaje.
 - Realiza la ejecución, si el lenguaje lo soporta, en
   un hilo independiente.
"""
from datetime import datetime as dt, timedelta as td
from threading import Thread
from os import system
from time import sleep

END_TIME = dt.strptime('20241105111925', '%Y%m%d%H%M%S')


class Clock(Thread):
    def run(self):
        while dt.now() < END_TIME:
            system("cls")
            current_time = END_TIME - dt.now()
            days_left = current_time.days
            hours_left = current_time.seconds // 3600
            minutes_left = current_time.seconds // 60
            seconds_left = current_time.seconds - hours_left * 3600 - minutes_left * 60
            print(f"Faltan: {days_left} días, {hours_left} horas, {minutes_left} minutos, {seconds_left} segundos")
            sleep(1)
        print(f"TERMINADO: {END_TIME} {dt.now()}")


class Counter(Thread):
    def run(self):
        count = 0
        while dt.now() < END_TIME:
            count += 1
            print(f"Vamos contando {count}")
            sleep(1)
        print(f"Terminé de contar en {count}")


Clock().start()
sleep(0.3)
Counter().start()
