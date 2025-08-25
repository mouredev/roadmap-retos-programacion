from datetime import datetime, date, time, timedelta, tzinfo

# EJERCICIO:
# Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
# - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
# - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
# Calcula cuántos años han transcurrido entre ambas fechas.

current_date = datetime.today()

my_birthday = datetime(1983, 7, 15, 18, 32, 12)

passed_time = current_date - my_birthday

print(f"Fecha actual: {current_date}.")

print(f"Fecha de nacimiento: {my_birthday}.")

print(f"Tiempo transcurrido entre esas fechas: {passed_time.days // 365} años.")


# DIFICULTAD EXTRA (opcional):
# Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
# 10 maneras diferentes. Por ejemplo:
# - Día, mes y año.
# - Hora, minuto y segundo.
# - Día de año.
# - Día de la semana.
# - Nombre del mes.
# (lo que se te ocurra...)

day_name = my_birthday.strftime("%A")
month_name = my_birthday.strftime("%B")
print(f"fecha completa: {my_birthday.ctime()}.")
print(f"Día: {my_birthday.day}")
print(f"Mes: {my_birthday.month}")
print(f"Año: {my_birthday.year}")
print(f"Número de dia de la semana: {my_birthday.isoweekday()}")
print(f"Fecha solo en sin hora: {my_birthday.date()}")
print(f"Segundos que llevo viviendo: {int(my_birthday.timestamp())}")
print(f"Fecha: {my_birthday.date()}")
print(f"Fecha formateada: {my_birthday.strftime("")}")
print(f"nombre del día de nacimiento: {day_name}")
print(f"Nombre del mes: {month_name}")