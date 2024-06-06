#14 - Fechas
"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""

from datetime import datetime, date

today = datetime.today()
todayDatef = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
print(todayDatef)

birthdayDate = datetime(2012, 12, 22,13,22,5)
birthdayDatef = birthdayDate.strftime('%d/%m/%Y %H:%M:%S')
print(birthdayDatef)

diffYears = today - birthdayDate

print(f"Diff of dates: {int((diffYears.days/365))} years.")


#EXTRA
print("EXTRA, more formats:")
print(birthdayDate.strftime('%H:%M:%S'))
print(birthdayDate.strftime('%a'))
print(birthdayDate.strftime('%A'))
print(birthdayDate.strftime('%b'))
print(birthdayDate.strftime('%B'))
print(birthdayDate.strftime('%w'))
print(birthdayDate.strftime('%H:%M:%S %p'))
print(birthdayDate.strftime('%j'))
print(birthdayDate.strftime('%U'))
print(birthdayDate.strftime('%c'))


