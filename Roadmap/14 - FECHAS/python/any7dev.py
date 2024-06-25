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
import datetime 

fecha_actual = datetime.datetime.now()
fecha_nacimiento = datetime.datetime(1988, 3, 11, 15, 0, 0)
print(fecha_actual.year - fecha_nacimiento.year)

#DIFICULTAD EXTRA
print(fecha_nacimiento.strftime("%d-%m-%y")) #1
print(fecha_nacimiento.strftime("%H:%M:%S")) #2
print(fecha_nacimiento.timetuple()[7])#3
print(fecha_nacimiento.isoweekday())#4
print(fecha_nacimiento.strftime("%B"))#5
print(fecha_nacimiento.ctime())#6
print(fecha_nacimiento.strftime("%A, %d. %B %Y %I:%M%p"))#7
print(fecha_nacimiento.isocalendar()[1]) #8 Número de la semana
print(fecha_nacimiento.strftime("%d %m %Y")) #9
print(fecha_nacimiento.toordinal())#10 Ordinal gregoriano proléptico de la fecha

