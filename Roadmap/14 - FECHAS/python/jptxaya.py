#14 FECHAS

"""
/*
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
 */
 """
from datetime import datetime
date_actual = datetime.now()
print(f"Fecha actual:{date_actual}")
birth_date = datetime(1979,3,10,17,15,00,00)
print(f"Fecha Nacimiento:{birth_date}")
diference_days = date_actual - birth_date
diference_years = diference_days // 365
print(f"Años transcurridos {diference_years.days}")


#Dificultad Extra
print("\nDificultad Extra\n")
print(f"Year: {birth_date.strftime("%Y")}")
print(f"Month: {birth_date.strftime("%m")}")
print(f"Month Name: {birth_date.strftime("%B")}")
print(f"Day: {birth_date.strftime("%d")}")
print(f"Week Day: {birth_date.strftime("%A")}")
print(f"Time: {birth_date.strftime("%H:%M:%S")}")
print(f"Time AM/PM: {birth_date.strftime("%I:%M %p")}")
print(f"Days of year: {birth_date.strftime("%-j")}")
print(f"Week Number of year: {birth_date.strftime("%-W")}")
print(f"Locale Date: {birth_date.strftime("%c")}")