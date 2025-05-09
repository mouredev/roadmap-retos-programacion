from datetime import datetime, timedelta, timezone
import time, os, threading

detener_evento = threading.Event()

def cuenta_regresiva(fecha_dada_utc, fecha_limite_utc):
    # Inicializar el tiempo de inicio como la fecha dada
    start = fecha_dada_utc

    while not detener_evento.is_set():
        # Calcular tiempo restante desde la fecha dada
        tiempo_restante = fecha_limite_utc - start

        if tiempo_restante <= timedelta(0):  # Si el tiempo restante es cero o negativo, se termina
            os.system("cls" if os.name == "nt" else "clear")
            print("\u00a1La cuenta regresiva ha terminado!")
            break

        # Descomponer el tiempo restante
        dias = tiempo_restante.days
        horas, resto = divmod(tiempo_restante.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        # Limpiar la consola y mostrar el tiempo restante
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Tiempo restante desde la fecha dada: {dias}d - {horas}h - {minutos}m - {segundos}s")
        print("Presiona Enter para detener el contador ¡Ctrl + C no funciona!...")

        # Incrementar la fecha de inicio en un segundo
        start += timedelta(seconds=1)

        time.sleep(1)

year = input("Año: ")
mes = input("Mes: ")
dia = input("Día: ")
hora = input("Hora: ")
minuto = input("Minuto: ")
segundos = input("Segundos: ")

fecha_dada = f"{year}-{mes}-{dia} {hora}:{minuto}:{segundos}"
fecha_dada = datetime.strptime(fecha_dada, "%Y-%m-%d %H:%M:%S")
fecha_dada_utc = fecha_dada.replace(tzinfo=timezone.utc)

fecha_limite = "2024-12-31 23:59:00"
fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d %H:%M:%S")
fecha_limite_utc = fecha_limite.replace(tzinfo=timezone.utc)

def esperar_input():
    input()
    detener_evento.set()

hilo_cuenta_regresiva = threading.Thread(target=cuenta_regresiva, args=(fecha_dada_utc, fecha_limite_utc))
hilo_cuenta_regresiva.start()

hilo_esperar_input = threading.Thread(target=esperar_input)
hilo_esperar_input.start()

# Esperar a que ambos hilos terminen
hilo_cuenta_regresiva.join()
hilo_esperar_input.join()

print("Programa terminado.")
