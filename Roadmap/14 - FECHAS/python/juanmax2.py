"""
Fechas
"""

from datetime import datetime, date

now = datetime.now()

print(now)

birthdate = datetime(1992, 11, 13, 5, 45, 0)

print(birthdate)

resultado = now - birthdate

print(f"Tengo {resultado.days // 365} años")

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
 */
"""

# Dia, mes, año
print(birthdate.strftime("%d - %m - %y"))
print(birthdate.strftime("%d - %m - %Y"))

# Horas, minutos y segundos
print(birthdate.strftime("%H : %M : %S"))

# Dia del año
print(birthdate.strftime("%j"))

# Dia de la semana
print(birthdate.strftime("%A"))

# Nombre del mes
print(birthdate.strftime("%B"))

# Nombre del mes abreviado
print(birthdate.strftime("%h"))

# Representación por defecto del locale
print(birthdate.strftime("%c"))
print(birthdate.strftime("%x"))
print(birthdate.strftime("%X"))

# AP/PM
print(birthdate.strftime("%p"))
