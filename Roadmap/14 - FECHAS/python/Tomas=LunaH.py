#  * EJERCICIO:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.

from datetime import datetime

now = datetime.now()
mi_fecha = datetime(2006,7,19,3,0,0)

print(now)
print(mi_fecha)

rest = now - mi_fecha
print(type(rest))
print(f"tengo {rest.days // 365} anos")


# DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)

print(mi_fecha.strftime("%d/%m/%y"))
print(mi_fecha.strftime("%m/%d/%y"))
print(mi_fecha.strftime("%d/%m/%Y"))
print(mi_fecha.strftime("%j"))
print(mi_fecha.strftime("%H:%M:%S"))
print(mi_fecha.strftime("%A"))
print(mi_fecha.strftime("%a"))
print(mi_fecha.strftime("%B"))
print(mi_fecha.strftime("%b"))
print(mi_fecha.strftime("%A %d/%m/%Y"))
