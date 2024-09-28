"""
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
"""
import datetime

# EJERCICIO:
fecha_actual = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
fecha_formateada_datetime = datetime.datetime.strptime(
    fecha_actual, '%d-%m-%Y %H:%M:%S')

fecha_nacimiento = datetime.datetime(2000, 8, 3, 7, 30)

# Calcular la diferencia
diferencia = fecha_formateada_datetime - fecha_nacimiento

# Obtener la diferencia en años
dias = diferencia.days
print(f'Años transcurridos: {dias // 365}')

# DIFICULTAD EXTRA:
print('Día, mes y año:', fecha_nacimiento.strftime('%d-%m-%Y'))
print('Hora, minuto y segundo:', fecha_nacimiento.strftime('%H:%M:%S'))
print('Día de año:', fecha_nacimiento.timetuple().tm_yday)
print('Día de la semana:', fecha_nacimiento.strftime('%A'))
print('Nombre del mes:', fecha_nacimiento.strftime('%B'))
print('Semana del año:', fecha_nacimiento.strftime('%U'))
print('Hora completa:', fecha_nacimiento.strftime('%T'))
print('Año:', fecha_nacimiento.strftime('%Y'))
print('Año-mes-dia hora-minuto-segundos-milisegundos:',
      fecha_nacimiento.strftime('%Y-%m-%d %H:%M:%S.%f'))
print('Hora, minuto, segundos, am/pm:',
      fecha_nacimiento.strftime('%H:%M:%S %p'))
