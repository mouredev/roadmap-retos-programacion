# EJERCICIO:
# Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
# - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
# - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
# Calcula cuántos años han transcurrido entre ambas fechas.
from datetime import datetime, timezone, timedelta

utc_minus_3 = timezone(timedelta(hours=-3))
ahora = datetime.now(tz=utc_minus_3)
birth_date = datetime(1987, 12, 31 , 6, 6, 10, tzinfo=utc_minus_3)

print(ahora)
print(f"birth_date: {birth_date}")

anios_transcurridos = ahora.year - birth_date.year
print(f"Años transcurridos (edad): {anios_transcurridos}")

dias = ahora - birth_date
print(f"Dias transcurridos: {dias}")

print(f"type of dias: {type(dias.days)}")
print(f"Años: {(dias.days // 365)}")


#
# DIFICULTAD EXTRA (opcional):
# Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
# 10 maneras diferentes. Por ejemplo:
# - Día, mes y año.
# - Hora, minuto y segundo.
# - Día de año.
# - Día de la semana.
# - Nombre del mes.
# (lo que se te ocurra...)


# dia, mes y año
print(f"# dia, mes y año: {birth_date.strftime(format='%d/%m/%Y')}")
print(f"# hora, minuto y segundo: {birth_date.strftime(format='%H:%M:%S')}")

# dia del año
print(f"# dia del año: {birth_date.strftime(format='%j')}")

# dia de la semana
print(f"# dia de la semana: {birth_date.strftime(format='%A')}")
print(f"# dia de la semana: {birth_date.strftime(format='%w')}")

# nombre del mes
print(f"# nombre del mes: {birth_date.strftime(format='%B')}")
print(f"# numero del mes: {birth_date.strftime(format='%m')}")

# semana del año
print(f"# semana del año: {birth_date.strftime(format='%U')}")

# hora en formato 12 horas
print(f"# hora en formato 12 horas: {birth_date.strftime(format='%I:%M:%S %p')}")

# hora en formato 24 horas
print(f"# hora en formato 24 horas: {birth_date.strftime(format='%H:%M:%S')}")

# nombre del mes abreviado
print(f"# nombre del mes abreviado: {birth_date.strftime(format='%b')}")

# nombre del dia, dia, nombre del mes y año
print(f"# nombre del dia, dia, nombre del mes y año: {birth_date.strftime(format='%A %d %B %Y')}")

# fecha completa con formato ISO
print(f"# fecha completa con formato ISO: {birth_date.isoformat()}")

# fecha y hora
print(f"# fecha y hora: {birth_date.strftime(format='%d/%m/%Y %H:%M:%S')}")

# fecha local
print(f"# fecha local: {birth_date.strftime(format='%x')}")

# hora local
print(f"# hora local: {birth_date.strftime(format='%X')}")
