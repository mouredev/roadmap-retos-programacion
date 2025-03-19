"""
EJERCICIO:
Crea dos variables utilizando los objetos fecha(date, o semejante) de
tu lenguaje:
- Una primera que represente la fecha (día, mes, año, hora, minuto, 
segundo) actual.
- Una segunda que represente tu fecha de nacimiento (te puedes 
inventar la hora).
Calcula cuántos años han transcurrido entre ambas fechas.

DIFICULTAD EXTRA (opcional):
Utilizando la fecha de tu cumpleaños, formatéala y muestra su 
resultado de 10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
(lo que se te ocurra...)

by adra-dev
"""

"""
Ejercicio
"""
 
"""
Fechas:
Una fecha en python no es un tipo de dato por si solo, pero podemos 
importar un modulo llamado datetime para trabajar con fechas como 
objetos tipo fecha. El modulo date tiem tiene muchos metehodos para 
devolver informaicon acerca del objeto fecha. puedes consultarlos en
la documentacion https://docs.python.org/3/library/datetime.html o
en https://www.w3schools.com/python/python_datetime.asp
"""
import datetime 

today = datetime.datetime.now()
birthday_day = datetime.datetime(1998, 2, 12, 12, 00, 00)

def years():
    return today.year - birthday_day.year


interval = years()

print(interval)


"""
Extra
"""

"""
Los objetos datetime cuentan con un metodo para otorgarles el formato
string de una manera legible. el metodo se llama strftime() y toma un
parametro, format, para especificar el formato en el que se devuelve
dicho string.

Tip:
Esto es epecialmente util conocerlo en el Analisis de Datos ya que 
muchas veces se trabaja con este formato, librerias como pandas o 
polars incluyen sus propios estandares para representar y trabajar 
con fechas pero suelen ser muy similares a los objetos datetime.
"""

print()
print("Extra")
print("Dia de la semana version corta: ", birthday_day.strftime( "%a"))      
print("Dia de la semana completa: ", birthday_day.strftime("%A"))      
print("Dia de la semana como numero: ",birthday_day.strftime("%w"))
print("Dia del mes: ", birthday_day.strftime("%d")) 
print("Nombre del mes corto: ", birthday_day.strftime("%b"))
print("Nombre del mes completo: ", birthday_day.strftime("%B"))
print("Mes como numero: ", birthday_day.strftime("%m"))
print("Año version corta sin siglo: ", birthday_day.strftime("%y"))
print("Año version completa: ", birthday_day.strftime("%Y"))
print("Hora: ", birthday_day.strftime("%H"))
