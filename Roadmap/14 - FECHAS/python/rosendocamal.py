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

current_date = datetime.now()

print(current_date)

fecha_nacimiento = datetime(2000, 12, 25, 23, 59, 59)

diff_dates = current_date - fecha_nacimiento
print(diff_dates); print()

# 01
print(fecha_nacimiento.strftime("%d%m%y"))
# 02
print(fecha_nacimiento.strftime("%I%M%S"))
# 03
print(fecha_nacimiento.strftime("%j"))
# 04
print(fecha_nacimiento.strftime("%A"))
# 05
print(fecha_nacimiento.strftime("%B"))
# 06
print(fecha_nacimiento.strftime("%a%A%w%d%b%y%m%Y%H%I%p%M%S%f%z%Z%j%U%W%c%C%x%X%%"))
# 07
print(fecha_nacimiento.strftime("%v"))
# 08
print(fecha_nacimiento.strftime("%G"))
# 09
print(fecha_nacimiento.strftime("%C"))
# 10
print(fecha_nacimiento.strftime("%U"))