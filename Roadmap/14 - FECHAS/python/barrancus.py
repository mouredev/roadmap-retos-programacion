#
#EJERCICIO:
#Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#- Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#- Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#Calcula cuántos años han transcurrido entre ambas fechas.
#
#DIFICULTAD EXTRA (opcional):
#Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#10 maneras diferentes. Por ejemplo:
#- Día, mes y año.
#- Hora, minuto y segundo.
#- Día de año.
#- Día de la semana.
#- Nombre del mes.
#(lo que se te ocurra...)
#
from datetime import datetime, date

now = datetime.now()
birth = datetime.strptime("25/05/1978 09:13:27", "%d/%m/%Y %H:%M:%S")
time_elapsed = now.year - birth.year
print(f"Desde {birth} hasta {now} han pasado {time_elapsed} años.")
print(f"{datetime.strftime(birth, "%d/%m/%Y")}")
print(f"{datetime.strftime(birth, "%H/%M/%S")}")
print(f"{datetime.isocalendar(birth)}")
print(f"{datetime.timestamp(birth)}")
print(f"{datetime.timetz(birth)}")
print(f"{datetime.timetuple(birth)}")
print(f'{datetime.astimezone(birth)}')
print(f'{datetime.dst(birth)}')
print(f'{datetime.isoformat(birth, "H", 'minutes')}')
print(f'{datetime.toordinal(birth)}')
print(f'{datetime.weekday(birth)}')
