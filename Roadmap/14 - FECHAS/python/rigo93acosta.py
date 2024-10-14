'''
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
'''

'''
Ejercicio
'''

from datetime import datetime

now = datetime.now()
birthday = datetime(1993, 5, 25, 0, 0, 0)

if now.month < birthday.month or (now.month == birthday.month and now.day < birthday.day):
    years = now.year - birthday.year - 1
else:
    years = now.year - birthday.year

print(f"Han pasado {years} años desde mi nacimiento")

'''
Extra
'''

# Día, mes y año
print(f'{birthday.strftime("%d/%m/%y")}')
print(f'{birthday.strftime("%d/%m/%Y")}')

# Hora, minuto y segundo
print(f'{birthday.strftime("%H:%M:%S")}')

# Día de año
print(f'{birthday.strftime("%j")}')

# Día de la semana
print(f'{birthday.strftime("%A")}')

# Nombre del mes
print(f'{birthday.strftime("%B")}')
print(f'{birthday.strftime("%h")}')

# Representación por defecto del locale
print(f'{birthday.strftime("%c")}')
print(f'{birthday.strftime("%x")}')
print(f'{birthday.strftime("%X")}')

# AM/PM
print(f'{birthday.strftime("%I:%M:%S %p")}')