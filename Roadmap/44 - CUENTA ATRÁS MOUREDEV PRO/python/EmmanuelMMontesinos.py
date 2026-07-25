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
from datetime import datetime, timezone
import os
import time
import threading

class CuentaAtras:
    def __init__(self, dia: int, mes: int, ano: int, hora: int, minutos: int, segundos: int):
        self.fecha_final = datetime(ano, mes, dia, hora, minutos, segundos, tzinfo=timezone.utc)
        
    def limpiar_pantalla(self):
        os.system("cls")

    def bucle(self):
        while True:
            self.diferencia = self.fecha_final - datetime.now(timezone.utc)
            if self.diferencia.total_seconds() <= 0:
                self.limpiar_pantalla()
                print("¡Hemos llegado!")
                break

            dias = self.diferencia.days
            horas, resto = divmod(self.diferencia.seconds, 3600)
            minutos, segundos = divmod(resto, 60)
            

            self.limpiar_pantalla()
            print(f"Quedan: {dias} días, {horas} horas, {minutos} minutos, {segundos} segundos")
            

            time.sleep(1)

# Prueba
cuenta = CuentaAtras(7, 11, 2024, 20, 41, 0)
proceso = threading.Thread(target=cuenta.bucle)
proceso.start()
