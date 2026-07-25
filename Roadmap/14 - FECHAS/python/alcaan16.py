"""/*
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
 */"""
from datetime import datetime
#from datetime import timedelta

now = datetime.now()# momento actual

print(now)

birth_date = datetime(1989,11,16,16,21) #indicamos una fecha en concreto

print(birth_date)

diferencia = now-birth_date #diferencia entre fechas en dias 

print(diferencia)

print(f"tengo {diferencia.days // 365} años")#IMPORTANTE!! ponemos doble // para poner valor absoluto sin decimales


# EXTRA

print(birth_date.strftime("%d %m %y")) #formato español de fecha
print(birth_date.strftime("%d %m %Y")) #formato año 4 digitos
print(birth_date.strftime("%a")) #formato dia de la semana
print(birth_date.strftime("%j")) #formato dia del año
print(birth_date.strftime("%B")) #formato del mes
print(birth_date.strftime("%c")) #formato completo ingles
print(birth_date.strftime("%x")) #formato local
print(birth_date.strftime("%X")) #formato local