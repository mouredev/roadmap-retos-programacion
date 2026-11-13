"""
/*
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
 */
"""

from datetime import datetime

now = datetime.now()

print(f" ahora es {now}")

birth_date = datetime(year=1987,month=9,day=1,hour=12,minute=30,second=10)

diff_years= now-birth_date

print(f" mi edad es {diff_years.days // 365} años")


print("mi fecha de cumpleaños es " + birth_date.strftime("%d/%m/%y"))
print(birth_date.strftime("mi fecha de cumpleaños es %D/%m/%y"))
print(birth_date.strftime("mi fecha de cumpleaños es %d/%m/%y"))
print(birth_date.strftime("mi fecha de cumpleaños es %D/%m/%Y"))
print(birth_date.strftime("la hora en que naci es %H/%M/%S"))
print(birth_date.strftime("día del año es %j"))
print(birth_date.strftime("día de la semana es %A"))
print(birth_date.strftime("mes de nacimiento es %h"))
print(birth_date.strftime("mes de nacimiento es %B"))
print(birth_date.strftime("fecha de nacimiento es %c"))
print(birth_date.strftime("fecha de nacimiento es %x"))
print(birth_date.strftime("hora de nacimiento formateada es %X"))

print(birth_date.strftime("hora en am/pm %p"))




