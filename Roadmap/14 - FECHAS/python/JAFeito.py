
"""
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
"""
from datetime import datetime
import locale
ahora = datetime.now()
nacido = datetime(1979,3,1,12,50,15)

diferencia = ahora - nacido
años = diferencia.days // 365
print (f"Tengo {int(años)} años")

#EXTRA

print(nacido.strftime("%d/%m/%y"))# Dia, mes y año
print(nacido.strftime("%d/%m/%Y"))# Dia, mes y año con 4 digitos
print(nacido.strftime("%j"))#Dia del año
print(nacido.strftime("%A"))#Dia de la semana en ingles
print(nacido.strftime("%c"))#Formato ingles
locale.setlocale(locale.LC_TIME, 'es_ES')
print(nacido.strftime("%A"))#Dia de la semana en español
print(nacido.strftime("%d/%h/%y"))# Dia, mes abreviado y año
print(nacido.strftime("%d/%B/%y"))# Dia, mes completo y año
print(nacido.strftime("%c"))#Formato español
print(nacido.strftime("%B/%d/%Y"))# Mes completo, dia y año