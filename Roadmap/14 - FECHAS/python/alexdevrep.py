'''
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
'''
#Importamos las librerías necesarias
from datetime import datetime


#Variable con la fecha actual
hoy = datetime.now()
print(hoy)

#Variable con la fecha de mi cumpleaños
fecha_nacimiento= datetime(1999,7,22,10,30,22,00000)
print(fecha_nacimiento)

#Comprobamos cuanto tiempo ha transcurrido
edad= hoy - fecha_nacimiento
print(edad)

#Dificultad EXTRA
formato1=fecha_nacimiento.strftime('%d/%m/%Y') #Día mes año
formato2=fecha_nacimiento.strftime('%H/%M/%S') #Horas minutos segundos
formato3=fecha_nacimiento.strftime('%j') #Día del año
formato4=fecha_nacimiento.strftime('%A') #Nombre del día de la semana
formato5=fecha_nacimiento.strftime('%B') #Nombre completo del mes
formato6=fecha_nacimiento.strftime('%p') #AM o PM
formato7=fecha_nacimiento.strftime('%U') #Semana del año
formato8=fecha_nacimiento.strftime('%w') #Día de la semana en número
formato9=fecha_nacimiento.strftime('%a') #Nombre abreviado del día de la semana 
formato10=fecha_nacimiento.strftime('%y') #Año con dos dígitos

print(formato1)
print(formato2)
print(formato3)
print(formato4)
print(formato5)
print(formato6)
print(formato7)
print(formato8)
print(formato9)
print(formato10)



