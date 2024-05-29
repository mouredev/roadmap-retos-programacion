#  * EJERCICIO:
#  * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
#  * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
#  * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
#  * Calcula cuántos años han transcurrido entre ambas fechas.

from datetime import datetime

current_date = datetime.now()
birthday_date = datetime(1997,5,10,16,30,0)

print(current_date)
print(birthday_date)

difference = current_date - birthday_date
print(difference.days)

years = (difference.days // 365)
print(f"I´m {years} old ")


#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
#  * 10 maneras diferentes. Por ejemplo:
#  * - Día, mes y año.
#  * - Hora, minuto y segundo.
#  * - Día de año.
#  * - Día de la semana.
#  * - Nombre del mes.
#  * (lo que se te ocurra...)


format1 = birthday_date.strftime("%d-%m-%y")
print(format1)
format2 = birthday_date.strftime("%d-%m-%Y")
print(format2)
format3 = birthday_date.strftime("%a-%B-%Y")
print(format3)
format4 = birthday_date.strftime("%Y-%m-%d")
print(format4)
format5 = birthday_date.strftime("%d-%m-%Y T%H:%M:%S")
print(format5)
format6 = birthday_date.strftime("%A-%B-%Y")
print(format6)
format7 = birthday_date.strftime("%d-%m-%Y %H:%M:%S %p")
print(format7)
format8 = birthday_date.strftime("%A-%B-%Y %p")
print(format8)
format9 = birthday_date.strftime("%f")
print(format9)
format10 = birthday_date.strftime("%j")
print(format10)
