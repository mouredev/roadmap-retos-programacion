# /*
#  * EJERCICIO:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.
#  *

import datetime

now_date = datetime.datetime.now()
bith_date = datetime.datetime(1979,10,26,19,00,00,00)
print(now_date)
print(bith_date)
dif = now_date.year - bith_date.year

print(f"Han pasado {dif} annos" )







#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)
#  */

print(f" Date {bith_date.date()}")
print(f" Date {bith_date.strftime("%d %m %y")}")
print(f" Time {bith_date.strftime("%H %M %S")}")
print(f" Time {bith_date.time()}")
print(f" Day of the week  {bith_date.strftime("%A")}")
print(f" Name of Month {bith_date.strftime("%B")}")
print(f" day of the years {bith_date.strftime("%j")}")