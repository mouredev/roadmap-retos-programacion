"""	
14 - FECHAS
Autor de la solución: Oriaj3	
Teoría:	
Las fechas son un tipo de dato muy común en la programación, ya que permiten
representar y manipular información relacionada con el tiempo. En Python, las
fechas se pueden representar utilizando el módulo datetime, que proporciona
una serie de clases y métodos para trabajar con fechas y horas.

Para crear una fecha en Python, se puede utilizar la clase date del módulo
datetime. Esta clase permite crear objetos que representan una fecha en
formato año-mes-día. Por ejemplo, la siguiente instrucción crea un objeto
date que representa la fecha 1 de enero de 2020:

fecha = date(2020, 1, 1)

#strftime() es un método que permite formatear una fecha en una cadena de texto
#con un formato específico. Tiene los siguientes parámetros:

#%d: día del mes (01-31)
#%m: mes (01-12)
#%Y: año (cuatro dígitos)

#%H: hora (00-23)
#%M: minuto (00-59)
#%S: segundo (00-59)

#%A: nombre completo del día de la semana
#%j: día del año (001-366)
#%B: nombre completo del mes

#%W: número de la semana del año

""" 

"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

import datetime as dt

# Fecha actual
fecha_actual = dt.datetime.now()

# Fecha de nacimiento
fecha_nacimiento = dt.datetime(1993, 4, 1, 17, 30, 0)

# Cálculo de años transcurridos
diferencia = fecha_actual - fecha_nacimiento

# Mostrar años transcurridos
print(diferencia.days // 365)

"""
* DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""

# Formatear fecha de nacimiento.
# Forma 1 - Día, mes y año - hora, minuto y segundo
print(fecha_nacimiento.strftime("%d/%m/%Y %H:%M:%S"))

# Forma 2 - Día, mes y año 
print(fecha_nacimiento.strftime("%d/%m/%Y")) 

# Forma 3 - Hora, minuto y segundo
print(fecha_nacimiento.strftime("%H:%M:%S"))

# Forma 4 - Día de la semana
print(fecha_nacimiento.strftime("%A")) #%A es el día de la semana

# Forma 5 - Día de año
print(fecha_nacimiento.strftime("%j")) #%j es el día del año

# Forma 6 - Nombre del mes
print(fecha_nacimiento.strftime("%B")) #%B es el nombre del mes

# Forma 7 - Es año bisiesto 
print(fecha_nacimiento.strftime("%Y")) #%Y es el año

# Forma 8 - Semana del año
print(fecha_nacimiento.strftime("%W")) #%W es la semana del año

# Forma 9 - Día de la semana abreviado
print(fecha_nacimiento.strftime("%a")) #%a es el día de la semana abreviado

# Forma 10 - Mes abreviado
print(fecha_nacimiento.strftime("%b")) #%b es el mes abreviado

