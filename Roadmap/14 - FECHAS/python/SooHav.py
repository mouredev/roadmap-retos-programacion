# 14 - Fechas

# Ejercicio

from datetime import datetime, date
import locale
# print(locale.locale_alias)

# Día actual
print("Fecha actual:")
today = date.today()
# Fecha actual
now = datetime.now()
print(today)
print(now)

print()
print("Fecha de mi cumpleaños:")
# Fecha cumpleaños
fecha_cumpleaños = date(1978, 2, 26)
fecha_cumpleaños_hora = datetime(1978, 2, 26, 12, 10)
print(fecha_cumpleaños)
print(fecha_cumpleaños_hora)
print(fecha_cumpleaños_hora.isoformat())
print(fecha_cumpleaños_hora.strftime("%Y-%m-%d %H:%M:%S"))

# Ejercicio Extra
print()
print("Otras variantes de mi cumpleaños:")
print(fecha_cumpleaños_hora.strftime("%d-%m-%Y"))
print(fecha_cumpleaños_hora.strftime("%d/%m/%Y"))
print(fecha_cumpleaños_hora.strftime("%d-%m-%Y %I:%M %p"))
print(fecha_cumpleaños_hora.strftime("%Y/%m/%d %H:%M:%S"))
print(fecha_cumpleaños_hora.strftime("%d %B %Y"))
print(fecha_cumpleaños_hora.strftime("%A %d %B %Y %I:%M"))
print(fecha_cumpleaños_hora.strftime("%A %d %B %Y"))
print(fecha_cumpleaños_hora.strftime("%a, %d %b %Y"))
print(fecha_cumpleaños_hora.strftime("%A, %d %b %Y %H:%M:%S"))
print(fecha_cumpleaños_hora.strftime("Fecha: %d-%m-%Y, Hora: %H:%M:%S"))
# Cambiar a configuración regional española
locale.setlocale(locale.LC_ALL, 'es_AR.utf8')
print(fecha_cumpleaños_hora.strftime("%A %d %B %Y %I:%M"))
print(fecha_cumpleaños_hora.strftime("%A %d de %B de %Y - %H:%M"))
print(fecha_cumpleaños_hora.strftime("%A, %d de %B de %Y"))
print()
print("Otros formatos de la fecha cumpleaños:")
# Calcular el día juliano
dia_juliano = fecha_cumpleaños_hora.timetuple().tm_yday
# Mostrar la fecha en días julianos
print(f"Mi cumple en días Juliano es el: {dia_juliano}")
print("¿Cuándo es tu cumpleaños?")
print(f"Cumplo el {fecha_cumpleaños_hora.strftime('%d de %B')}")

"""
Ayuda:
%a	Día de la semana abreviado:	lu., ma., …
%A	Día de la semana completo:	lunes, martes, …
%w	Día de la semana como número decimal:	0, 1, … 6
%d	Día del mes como número decimal con cero:	01, 02, …, 31
%b	Mes abreviado:	ene., feb., …
%B	Mes completo:	enero, febrero, …
%m	Mes como número decimal con cero:	01, 02, …12
%Y	Año en formato de cuatro dígitos:	0001, 0002, …, 2020, 2021, …
%H	Hora en formato 24h. con dos dígitos:	00, 01, …, 23
%I	Hora en formato 12h. con dos dígitos:	01, 02, …, 12
%M	Minutos en formato de dos dígitos:	00, 01, …, 59
%S	Segundos en formato de dos dígitos:	00, 01, …, 59
"""
