"""
* EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()
print(now)
my_birth_date = datetime.strptime("23-02-1985 3:00:00","%d-%m-%Y %H:%M:%S")
print(my_birth_date)

age =relativedelta(now, my_birth_date)
print(f"Años: {age.years}")
print(f"Meses: {age.months}")
print(f"Días: {age.days}")
print(f"Horas: {age.hours}")
print(f"Minutos: {age.minutes}")
print(f"Segundos: {age.seconds}")
