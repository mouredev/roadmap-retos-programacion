# #14 FECHAS
# #### Dificultad: Fácil | Publicación: 01/04/24 | Corrección: 08/04/24

## Ejercicio



''' * EJERCICIO:
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
 */'''

from datetime import date, datetime

fecha_actual = datetime.today()

fecha_nacimiento = datetime(1990, 11, 19, 23, 30)

print(fecha_actual)
print(fecha_nacimiento)

diferecia_fechas = fecha_actual - fecha_nacimiento
print(diferecia_fechas)
anios = diferecia_fechas.days / 365
print(f'Tengo {anios}')
print()

#***********EXTRA***********


print(f'Dia, mes y anio: {fecha_nacimiento.strftime('%d-%m-%Y')}')
print(f'Horas, min, y seg: {fecha_nacimiento.strftime('%H:%M:%S')}')
print(f'Dia del anio: {fecha_nacimiento.strftime('%j')}')
print(f'Dia de la semana: {fecha_nacimiento.strftime('%A')}')
print(f'Nobre corto del mes: {fecha_nacimiento.strftime('"%h"')}')
print(f'Nobre completo del mes: {fecha_nacimiento.strftime('%B')}')
print(f'Fecha completa por defecto: {fecha_nacimiento.strftime('%c')}')
print(f'Fecha corta por defecto: {fecha_nacimiento.strftime('%x')}')
print(f'Hora por defecto: {fecha_nacimiento.strftime('%X')}')
print(f'AM/PM: {fecha_nacimiento.strftime('%p')}')