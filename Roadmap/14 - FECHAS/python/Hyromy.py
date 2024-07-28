import datetime # modulo para fecha y hora

fecha_actual = datetime.datetime.now() # obtener fecha y hora actuales

print(fecha_actual)

print(f"Dia: {fecha_actual.day}")
print(f"Mes: {fecha_actual.month}")
print(f"Año: {fecha_actual.year}")
print(f"Hora: {fecha_actual.hour}")
print(f"Minutos: {fecha_actual.minute}")
print(f"Segundos: {fecha_actual.second}")
print()

import random

# construir una fecha especifica
nacimiento = datetime.datetime(year = 2004, 
                               month = 12,
                               day = 4,
                               hour = random.randint(0, 23))

print(f"fecha de nacimiento: {nacimiento}")

diferencia = fecha_actual - nacimiento # diferencia entre ambas fechas

print(f"han pasado {diferencia.days // 365} años")
print()

# ---- DIFICULTAD EXTRA ----
import calendar
nacimiento = datetime.date(year = 2004,
                           month = 12,
                           day = 4)

year_days = nacimiento - datetime.date(year = nacimiento.year,
                                        month = 1,
                                        day = 1)

bisiesto = calendar.isleap(nacimiento.year)

print(f"Año: {nacimiento.year}")
print(f"N. Mes: {nacimiento.month}")
print(f"Mes: {nacimiento.strftime("%B")}")
print(f"Dia: {nacimiento.day}")
print(f"Nombre dia: {nacimiento.strftime("%A")}")
print(f"Dia semana: {nacimiento.weekday() + 1}")
print(f"Dias del año: {year_days.days}")
print(f"Año biciesto: {bisiesto}")
print(f"Fecha (dd/mm/aaaa): {nacimiento.strftime("%d/%m/%Y")}")
print(f"Año: (yyyy/mm/dd): {nacimiento.strftime("%Y/%m/%d")}")