"""/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 */"""

# Ejercicio Base

from datetime import datetime

fecha_actual = datetime.now()
fecha_cumple = datetime.strptime("17/05/1991","%d/%m/%Y")
tiempo_pasado = fecha_actual - fecha_cumple

print(f"Fecha Actual: {fecha_actual}")
print(f"Fecha Cumpleaños: {fecha_cumple}")
print(f"Tiempo pasado: {tiempo_pasado}")

# Ejercicio Extra

'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
'''

fecha_1 = fecha_cumple.day
fecha_2 = fecha_cumple.year
fecha_3 = fecha_cumple.month
fecha_4 = fecha_cumple.second
fecha_5 = fecha_cumple.minute
fecha_6 = fecha_cumple.hour
fecha_7 = f"{fecha_cumple.day}/{fecha_cumple.month}/{fecha_cumple.year}"
fecha_8 = f"{fecha_cumple.hour}:{fecha_cumple.minute}:{fecha_cumple.second}"
fecha_9 = f"{fecha_cumple.month}/{fecha_cumple.day}/{fecha_cumple.year}"
fecha_10 = f"{fecha_cumple.day}/{fecha_cumple.month}/{fecha_cumple.year} - {fecha_cumple.hour}:{fecha_cumple.minute}:{fecha_cumple.second}"

print(fecha_1)
print(fecha_2)
print(fecha_3)
print(fecha_4)
print(fecha_5)
print(fecha_6)
print(fecha_7)
print(fecha_8)
print(fecha_9)
print(fecha_10)