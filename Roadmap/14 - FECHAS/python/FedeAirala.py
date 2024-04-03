# Reto 14 - FECHAS

"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

import datetime

current_day = datetime.datetime.now()
birthdate = datetime.datetime (1980,6,25,9,30,25)

print (f"La fecha actual es: {current_day}")
print (f"La fecha de mi nacimiento es: {birthdate} ")

time_elapsed_year = current_day.year - birthdate.year
time_elapsed_day = current_day - birthdate

print (f"Entre la fecha actual y mi fecha de nacimiento pasaron {time_elapsed_year} años")
print (f"Que son nada más y nada menos que {time_elapsed_day.days} días")

"""
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
print ("\n")
print ("-"*60)

print ("DATOS CON MI FECHA DE NACIMIENTO")
print ("")
print (f"La fecha de mi nacimiento es el {birthdate.day} del {birthdate.month} de {birthdate.year}")
print (f"Día, mes y año de nacimiento:  {datetime.datetime.strftime(birthdate,'%d / %m / %Y')}")
print (f"Horario de nacimiento {datetime.datetime.strftime(birthdate,'%H : %M : %S')} hs. ")
print (f"Año de Nacimiento {birthdate.year}")
print (f"Mes de nacimiento {datetime.datetime.strftime(birthdate, '%B')}")
print (f"Día de nacimiento  {datetime.datetime.strftime(birthdate, '%a')}")
print (f"Nací en la semana {datetime.datetime.strftime(birthdate, '%W')} del año {birthdate.year}")
print (f"Día número {datetime.datetime.strftime(birthdate, '%j')}")


