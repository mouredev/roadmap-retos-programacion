"""* EJERCICIO:
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
 * (lo que se te ocurra...)"""

from datetime import datetime
import locale

hoy = datetime.now()
fecha_de_nacimiento = datetime(1968,5,1,15,30,0)
anios = ((hoy - fecha_de_nacimiento).days) // 365

print(f'Hoy-> {hoy}')
print(f'Fecha de nacimiento-> {fecha_de_nacimiento}')
print(f'Tengo {anios} años')

#EXTRA

# Locale
locale.setlocale(locale.LC_ALL, 'es-ES')

# Día, mes y año
print(f'Día de mi cumpleaños: {fecha_de_nacimiento.day}/{fecha_de_nacimiento.month}/{fecha_de_nacimiento.year}')
print(fecha_de_nacimiento.strftime('%d-%m-%Y'))

# Horas, minutos y segundos
print(f'Horas, minutos y segundos: {fecha_de_nacimiento.hour}:{fecha_de_nacimiento.minute}:{fecha_de_nacimiento.second}')
print(fecha_de_nacimiento.strftime('%H:%M:%S'))
print(fecha_de_nacimiento.strftime('%H:%m %p'))

# Día del año
print(f'Día del año: {fecha_de_nacimiento.timetuple().tm_yday}')
print(fecha_de_nacimiento.strftime('%j'))

# Día de la semana
print(f'Día de la semana: {fecha_de_nacimiento.strftime("%A")}')

# Nombre del mes
print(f'Nombre del mes: {fecha_de_nacimiento.strftime("%B")}')