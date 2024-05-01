# 14 FECHAS
# Monica Vaquerano
# https://monicavaquerano.dev


"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
"""
from datetime import datetime

# Now
now = datetime.now()

# Day of Birth
dob = datetime(1988, 10, 9, 19, 59, 59)

# Difference
dif = now - dob

# Date Output
# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

print("Now: year =>", now.year)
print("Now: weekday, full version =>", now.strftime("%A"))  # Weekday, full version

print("DOB: day =>", dob.day)
print("DOB: year =>", dob.year)
print(
    "DOB: month name, full version =>", dob.strftime("%B")
)  # Month name, full version

print("Difference (Age) =>", dif.days // 365)

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
# - Día, mes y año.
print("Día, mes y año =>\t", dob.strftime("%d %B %Y"))
print("Día, mes y año =>\t", dob.strftime("%d/%m/%y"))
print("Día, mes y año =>\t", dob.strftime("%d/%m/%Y"))

# - Hora, minuto y segundo.
print("Hora, minuto y segundo =>\t", dob.strftime("%H: %M: %S"))
print("Hora, minuto y segundo =>\t", dob.strftime("%I: %M: %S %p"))

# - Día de año.
print("Día del año =>\t", dob.strftime("%A, %d %B %Y. Day %jth of that year"))
print("Día del año =>\t", dob.strftime("Day %jth of that year"))

# - Día de la semana.
print("Día de la semana =>\t", dob.strftime("%a"))
print("Día de la semana =>\t", dob.strftime("%A"))
print("Día de la semana =>\t", dob.strftime("%w"))

# - Nombre del mes.
print("Nombre del mes =>\t", dob.strftime("%b"))
print("Nombre del mes =>\t", dob.strftime("%B"))
print("Nombre del mes =>\t", dob.strftime("%m"))

# - (lo que se te ocurra...)
print("Local version of date and time =>\t", dob.strftime("%c"))
print("Century =>\t", dob.strftime("%C"))
print("Local version of date =>\t", dob.strftime("%x"))
print("Local version of time =>\t", dob.strftime("%X"))
