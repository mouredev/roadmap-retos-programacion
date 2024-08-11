"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

from datetime import datetime

# Fecha actual
fecha_actual = datetime.now()

# Fecha de nacimiento (puedes cambiarla por la tuya)
fecha_nacimiento = datetime(1990, 8, 9, 12, 0, 0)  # Año, mes, día, hora, minuto, segundo

# Cálculo de la diferencia en años
diferencia = fecha_actual.year - fecha_nacimiento.year

# Ajuste si la fecha de nacimiento aún no ha ocurrido este año
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    diferencia -= 1

print(f"Han transcurrido {diferencia} años.")


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

from datetime import datetime

# Fecha de nacimiento (puedes cambiarla por la tuya)
fecha_nacimiento = datetime(1998, 9, 24, 12, 0, 0)  # Año, mes, día, hora, minuto, segundo

# Formateos diferentes
formatos = [
    fecha_nacimiento.strftime("%d/%m/%Y"),  # Día, mes y año
    fecha_nacimiento.strftime("%H:%M:%S"),  # Hora, minuto y segundo
    fecha_nacimiento.strftime("%j"),        # Día del año
    fecha_nacimiento.strftime("%A"),        # Día de la semana
    fecha_nacimiento.strftime("%B"),        # Nombre del mes
    fecha_nacimiento.strftime("%d-%m-%Y %H:%M:%S"),  # Día, mes, año, hora, minuto y segundo
    fecha_nacimiento.strftime("%Y-%m-%d"),  # Año, mes y día
    fecha_nacimiento.strftime("%I:%M %p"),  # Hora en formato 12 horas con AM/PM
    fecha_nacimiento.strftime("%U"),        # Número de semana del año (domingo como primer día de la semana)
    fecha_nacimiento.strftime("%W")         # Número de semana del año (lunes como primer día de la semana)
]

# Mostrar los resultados
for i, formato in enumerate(formatos, 1):
    print(f"Formato {i}: {formato}")
