"""
* EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import calendar
import pytz

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


"""
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
week_days = list(calendar.day_name)
month_names = list(calendar.month_name)
my_birth_date = datetime.strptime("27-08-2000 13:01:05","%d-%m-%Y %H:%M:%S")
time_tuple = my_birth_date.timetuple() # Crea una especie de tupla con toda la info de una fecha en concreto

# Se puede acceder a la tupla de info o formatear directamente el datetime:
print(f"1: DD-MM-YYYY: {my_birth_date.strftime("%d-%m-%Y")}")
print(f"2: HH:MM:SS: {my_birth_date.strftime("%H:%M:%S")}")
print(f"3: Formated defined by country: {my_birth_date.ctime()}")
print(f"3: Formated defined by country: {my_birth_date.strftime("%c")}")
print(f"3: Formated defined by country. Only date: {my_birth_date.strftime("%x")}")
print(f"3: Formated defined by country. Only time: {my_birth_date.strftime("%X")}")
print(f"4: Day of the year: {time_tuple.tm_yday}")
print(f"4: Day of the year: {my_birth_date.strftime("%j")}")
print(f"5: Day of the week: {week_days[time_tuple.tm_wday]}")
print(f"5: Day of the week. Normal name: {my_birth_date.strftime("%A")}")
print(f"5: Day of the week. Short name: {my_birth_date.strftime("%a")}")
print(f"6: Day of month: {time_tuple.tm_mday}")
print(f"7: Name of month: {month_names[time_tuple.tm_mon]}")
print(f"7: Name of month: {my_birth_date.strftime("%h")}")
print(f"7: Name of month. Normal name: {my_birth_date.strftime("%B")}")
print(f"7: Name of month. Short name: {my_birth_date.strftime("%b")}")
print(f"8: Year: {time_tuple.tm_year}")
print(f"9: {time_tuple.tm_year} was leap? : {calendar.isleap(time_tuple.tm_year)}")
print(f"10: Hour: {time_tuple.tm_hour}")
print(f"10: Hour 24h format: {my_birth_date.strftime("%H")}")
print(f"10: Hour 12h format: {my_birth_date.strftime("%I")}")
print(f"11: Minute: {time_tuple.tm_min}")
print(f"11: Minute 2 digits: {my_birth_date.strftime("%M")}")
print(f"12: Seconds: {time_tuple.tm_sec}")
print(f"12: Seconds 2 digits: {my_birth_date.strftime("%S")}")
print(f"13: Microseconds: {my_birth_date.strftime("%f")}")
print(f"14: AM / PM: {my_birth_date.strftime("%p")}")


# Definir un huso horario (por ejemplo, UTC+2)
timezone = pytz.timezone("Europe/Madrid")
# Obtener la hora local con ese huso horario
now = datetime.now(timezone)
# Mostrar el desplazamiento y el nombre del huso horario
print("Con huso horario (Madrid):", now.strftime("%X %z"), now.strftime("%Z"))