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


from datetime import datetime

now = datetime.now()
print(now)
birth_date = datetime.strptime("10-02-1997 10:00:02", "%d-%m-%Y %H:%M:%S" )
print(birth_date)

diff_dates = now - birth_date
print(diff_dates)


""" * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */  """

print(birth_date.strftime("%d-%m-%Y"))
print(birth_date.strftime("%H:%M:%S"))
print(birth_date.strftime("%-j"))
print(birth_date.strftime("%B"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%A"))
