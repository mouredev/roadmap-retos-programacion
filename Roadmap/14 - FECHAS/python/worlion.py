import datetime
import dateutil.relativedelta

"""
* EJERCICIO: Fechas
"""

now = datetime.datetime.now()
print(f"Today is: {now.strftime('%x')}")

my_birthday = datetime.datetime(1984, 4, 20)
print(f"born in {my_birthday.strftime('%x')}")

delta = dateutil.relativedelta.relativedelta(now, my_birthday)
print(f"Tienes {delta.years} años, 'chaval'... 🤨")



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

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")


print(f"1.- Fecha simple: {my_birthday.strftime('%x')}")
# my_birthday.hour = 23
# my_birthday.minute = 30

print(f"2.- Hora: {my_birthday.strftime('%X')}")
print(f"3.- Hora (AM/PM): {my_birthday.strftime('%I:%M %p')}")
print(f"4.- Fecha simple completa: {my_birthday}")
print(f"5.- Fecha con día sem: {my_birthday.strftime('%A %Y/%m/%d')}")
print(f"6.- Día del año: {my_birthday.strftime('%j')} - semana número: {my_birthday.strftime('%W')}")
print(f"7.- Fecha local: {my_birthday.strftime('%c')}")
print(f"8.- Fecha larga: {my_birthday.strftime('%A %B %d of %Y')}")
print(f"9.- Siglo: {int(my_birthday.strftime('%C'))+1}") #Sale el 19 🤔
print(f"10.- Mes: {my_birthday.strftime('%B (%h)')}")


