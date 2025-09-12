"""
* EJERCICIO:
* Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
* - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
* - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
* Calcula cuántos años han transcurrido entre ambas fechas.
*
* DIFICULTAD EXTRA (opcional):
* Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
* 10 maneras diferentes. Por ejemplo:
* - Día, mes y año.
* - Hora, minuto y segundo.
* - Día de año.
* - Día de la semana.
* - Nombre del mes.
* (lo que se te ocurra...)
"""

from datetime import datetime

date_now = datetime.now()
birth_date = datetime(1994, 8, 1, 18, 33, 45)

difference = date_now - birth_date

print("Fecha actual:",date_now)
print("Fecha de nacimiento:",birth_date)

print("Años transcurridos entre las dos fechas:", difference.days // 365, "años")


################# --------------------- EXTRA ------------------------------- ###################

birth_date = datetime(1994, 8, 1, 18, 33, 45)

print(f'1. Dia, mes y año: {birth_date.strftime("%d de %B de %Y")}')

print(f'2. Hora, minutos, segundos: {birth_date.strftime("%H:%M:%S")}')

print(f"3. Dia del año: {birth_date.timetuple().tm_yday}")

print(f"4. Dia de la semana: {birth_date.strftime('%A')}")

print(f"5. Nombre del mes: {birth_date.strftime('%B')}")

print(f"6. Semana del año: {birth_date.strftime('%U')}")

print(f"7. Formato mes en letras cortas: {birth_date.strftime('%b')}")

print(f"8. Formato mm-dd-YYYY: {birth_date.strftime('%m-%d-%Y')}")

print(f"9. Formato personalizado: {birth_date.strftime('Born on %A, %dth of %B %Y at %I:%M:%S %p')}")

def obtener_estacion(fecha):
    mes = fecha.month

    if 3 <= mes <= 5:
        return "Otoño"
    elif 6 <= mes <= 8:
        return "Invierno"
    elif 9 <= mes <= 11:
        return "Primavera"
    else:
        return "Verano"

estacion_nacimiento = obtener_estacion(birth_date)
print(f"10. Estacion del año: Naciste en la estación de {estacion_nacimiento}")