"""
* EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

from datetime import date, datetime

current_date = datetime.now()

birth_date = datetime(1992, 4, 29, 13, 0, 0)

date_result =current_date - birth_date

print(date_result.days / 365)

"""
DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)

"""


print(f"formato 1: {birth_date}")
print(f"formato 2: {birth_date.strftime('%x-%X')}")
print(f"formato 3: {birth_date.strftime('%d-%m-%y')}")
print(f"formato 4: {birth_date.strftime('%H-%M-%S')}")
print(f"formato 5: {birth_date.strftime('%A')}")
print(f"formato 6: {birth_date.strftime('%B')}")
print(f"formato 7: {birth_date.strftime('%d-%B')}")
print(f"formato 8: {birth_date.strftime('%j')}")
print(f"formato 9: {birth_date.strftime('%C')}")
print(f"formato 10: {birth_date.strftime('%c')}")

