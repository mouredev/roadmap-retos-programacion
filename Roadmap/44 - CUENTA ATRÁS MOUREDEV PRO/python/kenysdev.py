# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 44 CUENTA ATRÁS MOUREDEV PRO
# ------------------------------------

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

from datetime import datetime, timezone, timedelta
import threading
import os
import time

class ReverseTimer:
    def __init__(self, end_date: str) -> None:
        self.__end_date = datetime.fromisoformat(
            end_date
        ).replace(tzinfo=timezone.utc)

    def __time_remaining(self) -> timedelta:
        now = datetime.now(timezone.utc)
        delta = self.__end_date - now
        return max(delta, timedelta(0))
    
    def __has_finished(self) -> bool:
        return self.__time_remaining() == timedelta(0)

    def __str__(self) -> str:
        delta = self.__time_remaining()
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        min_sec: str = f"{minutes} minutos, {seconds} segundos"
        return f"{delta.days} dias, {hours} horas, {min_sec}."
        
    def print_remaining(self) -> None:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Tiempo restante:")
            print(self.__str__())

            if self.__has_finished():
                print("¡Cuenta atrás finalizada!")
                return
            time.sleep(1)

if __name__ == "__main__":
    end_date:str = "2024-12-31T23:59:59.999999"
    timer = ReverseTimer(end_date)
    reverse_timer_thread = threading.Thread(target=timer.print_remaining)
    reverse_timer_thread.start()
    reverse_timer_thread.join()

