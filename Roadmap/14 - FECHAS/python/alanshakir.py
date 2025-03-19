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
now = datetime.now()
birth_date = datetime(1985, 1, 20, 15, 10, 33)
print(now)
print(birth_date)

year = now - birth_date
print(f"Han transcurrido {year.days//365} años")

#Extra

#1 Día, mes y año.
print(birth_date.strftime("%d/%m/%Y"))
#2 Hora, minuto y segundo.
print(birth_date.strftime("%H:%M:%S"))
#3 Día de año.
print(birth_date.strftime("%j"))
#4 Día de la semana.
print(birth_date.strftime("%A"))
#5 Nombre del mes.
print(birth_date.strftime("%B"))
#6 semana del año
print(birth_date.strftime("%U"))
#7 nombre del mes abreviado
print(birth_date.strftime("%a"))
#8 hora en formato 00-12
print(birth_date.strftime("%I"))
#9 Nombre del mes (corto)
print(birth_date.strftime("%b"))
#10 AM/PM
print(birth_date.strftime("%p"))
