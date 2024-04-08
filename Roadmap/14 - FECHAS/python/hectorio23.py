# Author: Héctor Adán
# https://github.com/hectorio23
# /bin/python3.11
import datetime

'''
EJERCICIO:
Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
- Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
- Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
Calcula cuántos años han transcurrido entre ambas fechas.
DIFICULTAD EXTRA (opcional):
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
(lo que se te ocurra...)
'''

###################################################
################## EJERCICIO 1 ####################
###################################################

current_time = datetime.datetime.now()
nacimiento = datetime.datetime(2004, 6, 28, 12, 59, 0)

delta = current_time - nacimiento

print(f"Fecha actual (dd/mm/yy): { current_time.strftime('%d - %m - %Y  %P') }")
print(f"Fecha de nacimiento (dd/mm/yy): { nacimiento.strftime('%d - %m - %Y  %P') }")

print("Delta entre la fecha de nacimiento y la fecha actual {0} -> {1:.2f} años".format(delta, delta.days / 365))

###################################################
############### EJERCICIO EXTRA ###################
###################################################

print("\n**** Formateando la fecha mi fecha de nacimiento en 10 formas distintas ******\n")
print(f"Fecha de nacimiento (dd/mm/yyyy): {nacimiento.strftime('%d/%m/%Y')}")
print(f"Fecha de nacimiento (mm-dd-yyyy): {nacimiento.strftime('%m-%d-%Y')}")
print(f"Fecha de nacimiento (dd-mm-yyyy): {nacimiento.strftime('%d-%m-%Y')}")
print(f"Fecha de nacimiento (yyyy/mm/dd): {nacimiento.strftime('%Y/%m/%d')}")
print(f"Fecha de nacimiento (dd/mm/yy): {nacimiento.strftime('%d/%m/%y')}")
print(f"Fecha de nacimiento (yy/mm/dd): {nacimiento.strftime('%y/%m/%d')}")
print(f"Fecha de nacimiento (hh:mm:ss): {nacimiento.strftime('%H:%M:%S')}")
print(f"Fecha de nacimiento (hh:mm): {nacimiento.strftime('%H:%M')}")
print(f"Fecha de nacimiento (mes dd, yyyy): {nacimiento.strftime('%B %d, %Y')}")
print(f"Fecha de nacimiento (dd de mes de yyyy): {nacimiento.strftime('%d de %B de %Y')}")

