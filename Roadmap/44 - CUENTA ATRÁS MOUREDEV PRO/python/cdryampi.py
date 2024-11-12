# /*
#  * EJERCICIO:
#  * ¡El 12 de noviembre lanzo mouredev pro!
#  * El campus de la comunidad para estudiar programación de
#  * una manera diferente: https://mouredev.pro
#  *
#  * Crea un programa que funcione como una cuenta atrás.
#  *
#  * - Al iniciarlo tendrás que indicarle el día, mes, año,
#  *   hora, minuto y segundo en el que quieres que finalice.
#  * - Deberás transformar esa fecha local a UTC.
#  * - La cuenta atrás comenzará y mostrará los días, horas,
#  *   minutos y segundos que faltan.
#  * - Se actualizará cada segundo y borrará la terminal en
#  *   cada nueva representación del tiempo restante.
#  * - Una vez finalice, mostrará un mensaje.
#  * - Realiza la ejecución, si el lenguaje lo soporta, en
#  *   un hilo independiente.
#  */
from datetime import datetime, timezone, timedelta
import threading
import time
import os

class CuentaAtras:
    """Clase que representa una cuenta atrás"""
    __END_COUNTER = None
    __RUNING = True

    def __init__(self, dia: int, mes: int, any: int, hora: int, minuto: int, segundo: int):
        self.__END_COUNTER = datetime(
            year=any,
            month=mes,
            day=dia,
            hour=hora,
            minute=minuto,
            second=segundo,
            tzinfo=timezone.utc
        )

    def time_remaining(self) -> timedelta:
        """Devuelve el tiempo restante como un timedelta"""
        return self.__END_COUNTER - datetime.now(timezone.utc)

    def time_to_seconds(self) -> bool:
        """Verifica si el tiempo restante ha terminado"""
        remaining = self.time_remaining()
        if remaining.total_seconds() <= 0:
            print("¡MoureDev Pro ha comenzado! Disfruta del programa.")
            return True
        return False

    def time_str(self) -> str:
        """Devuelve una cadena con el tiempo restante en días, horas, minutos y segundos"""
        remaining = self.time_remaining()
        
        # Obtener días, horas, minutos y segundos restantes
        dias = remaining.days
        horas, resto_segundos = divmod(remaining.seconds, 3600)
        minutos, segundos = divmod(resto_segundos, 60)

        return f"Encara falta {dias} dies, {horas} hores, {minutos} minuts i {segundos} segons.\nPresiona Enter para detener el contador...\n"
    
    def safe_execute_clear_from_cmd(self) -> None:
        """Limpia la consola dependiendo del sistema operativo"""
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        except Exception as e:
            print(f"Error al limpiar la consola: {e}")

    def print_next_second(self):
        """Imprime el tiempo restante cada segundo"""
        print(self.time_str())

    def run_to_end_counter_threat(self):
        """Inicia el contador en un hilo y lo detiene con la entrada del usuario"""
        def countdown():
            while not self.time_to_seconds() and self.__RUNING:
                self.safe_execute_clear_from_cmd()
                self.print_next_second()
                time.sleep(1)
            print("Contador detenido.")

        threat = threading.Thread(target=countdown)
        threat.start()

        input_thread = threading.Thread(target=self.stop)
        input_thread.start()

        threat.join()
        input_thread.join()
        
    def stop(self):
        input("Presiona Enter para detener el contador...\n")
        self.__RUNING = False


def main():
    compte_enrrere = CuentaAtras(
        dia=12,
        mes=11,
        any=2024,
        hora=0,
        minuto=0,
        segundo=0
    )

    compte_enrrere.run_to_end_counter_threat()

if __name__ == '__main__':
    main()
