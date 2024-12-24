""" /*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */ """

#EJERCICIO

from datetime import datetime

now = datetime.now()
birth_date = datetime(1998, 3, 10, 12, 0, 0)

i = now - birth_date

print(f"Tengo {int(i.days / 365)} años.")

#DIFICULTAD EXTRA

print(birth_date.day, birth_date.month, birth_date.year)
print(birth_date.strftime("%d %m %y"))
print(birth_date.hour, birth_date.minute, birth_date.second)
print(birth_date.strftime("%j"))
print(birth_date.strftime("%A"))
print(birth_date.strftime("%h"))
print(birth_date.strftime("%B"))
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))
