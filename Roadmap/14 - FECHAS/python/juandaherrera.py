"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

from datetime import datetime

current_date = datetime.now()
birth_date = datetime(1999, 12, 5, 19, 34, 16)

print("Fecha actual:", current_date)
print("Fecha de nacimiento: ", birth_date)

print("Tiempo transcurrido entre ambas fechas:", current_date - birth_date)


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
print(f"{'Formatos':-^80}")
date_formats = [
    "%d-%m-%Y",  # día, mes y año
    "%H-%M-%S",  # Hora, minuto, segundo
    "%j",  # Día del año (de 001 a 366)
    "%w",  # Dow. 0 es domingo y 6 es sábado
    "%B",  # Nombre completo del mes
    "%a, %d %b %Y",
    "%Y-%m-%d",
    "%c",  # Representación apropiada de fecha y hora localmente
    "%X",
    "%A, %d %B %Y",
]

for index, date_format in enumerate(date_formats):
    print(f"{index + 1}. ", birth_date.strftime(date_format))
