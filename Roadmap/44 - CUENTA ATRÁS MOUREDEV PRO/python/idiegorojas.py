"""
44 - Cuneta regresiva Mouredev Pro
"""
# Crea un programa que funcione como una cuenta atrás.
    # Al iniciarlo tendrás que indicarle el día, mes, año, hora, minuto y segundo en el que quieres que finalice.
    # Deberás transformar esa fecha local a UTC.
    # La cuenta atrás comenzará y mostrará los días, horas, minutos y segundos que faltan.
    # Se actualizará cada segundo y borrará la terminal en cada nueva representación del tiempo restante.
    # Una vez finalice, mostrará un mensaje.
    # Realiza la ejecución, si el lenguaje lo soporta, en un hilo independiente.


from datetime import datetime
import pytz
import time
import os
import threading

# Diccionario de zonas horarias
time_zones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "ES": "Europe/Madrid",
    "US": "America/New_York",
}

def clear_terminal():
    """Limpia la terminal según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_target_datetime():
    """Solicita al usuario la fecha y hora objetivo"""
    print("Ingresa la fecha y hora objetivo para la cuenta regresiva")
    
    try:
        year = int(input("Año (ej. 2025): "))
        month = int(input("Mes (1-12): "))
        day = int(input("Día (1-31): "))
        hour = int(input("Hora (0-23): "))
        minute = int(input("Minuto (0-59): "))
        second = int(input("Segundo (0-59): "))
        
        # Solicitar zona horaria
        print("\nSelecciona tu zona horaria:")
        for code, zone in time_zones.items():
            print(f"{code}: {zone}")
        
        zone_code = input("Código de zona horaria: ").upper()
        if zone_code not in time_zones:
            print("Zona horaria no válida, usando UTC")
            timezone = pytz.UTC
        else:
            timezone = pytz.timezone(time_zones[zone_code])
        
        # Crear datetime y aplicar zona horaria
        local_datetime = timezone.localize(datetime(year, month, day, hour, minute, second))
        # Convertir a UTC
        utc_datetime = local_datetime.astimezone(pytz.UTC)
        
        return utc_datetime
        
    except ValueError:
        print("Valores incorrectos, usando fecha por defecto")
        return pytz.UTC.localize(datetime(2025, 4, 21, 6, 30, 0))

def countdown(target_datetime):
    """Ejecuta la cuenta regresiva hasta la fecha objetivo"""
    while True:
        # Obtener la hora actual en UTC
        now = datetime.now(pytz.UTC)
        
        # Calcular diferencia
        diff = target_datetime - now
        total_seconds = diff.total_seconds()
        
        if total_seconds <= 0:
            clear_terminal()
            print("¡La cuenta regresiva ha terminado!")
            break
        
        # Calcular días, horas, minutos y segundos
        days = int(total_seconds // (24 * 3600))
        total_seconds %= (24 * 3600)
        hours = int(total_seconds // 3600)
        total_seconds %= 3600
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        
        # Limpiar terminal y mostrar cuenta regresiva
        clear_terminal()
        print(f"Tiempo restante: {days} días, {hours} horas, {minutes} minutos, {seconds} segundos")
        
        # Esperar un segundo
        time.sleep(1)

def main():
    """Función principal del programa"""
    print("=== CUENTA REGRESIVA ===")
    target_datetime = get_target_datetime()
    
    print(f"\nFecha objetivo (UTC): {target_datetime}")
    print("Iniciando cuenta regresiva en 3 segundos...")
    time.sleep(3)
    
    # Iniciar la cuenta regresiva en un hilo separado
    countdown_thread = threading.Thread(target=countdown, args=(target_datetime,))
    countdown_thread.start()
    
    # El hilo principal puede hacer otras cosas mientras la cuenta regresiva se ejecuta
    # Para este ejemplo simplemente esperamos a que termine
    countdown_thread.join()
    
    print("Programa finalizado")

if __name__ == "__main__":
    main()