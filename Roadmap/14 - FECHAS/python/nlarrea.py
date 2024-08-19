"""
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
"""

from datetime import datetime, date

current_date = datetime.now().date()
bday_date = datetime.strptime("1998-06-29 09:25:00", "%Y-%m-%d %H:%M:%S")


def diffYears(date_one: date, date_two: date):
    return abs(date_one.year - date_two.year)


print(diffYears(current_date, bday_date))


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

WEEK_DAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(f"1. {bday_date.ctime()}")
print(f"2. {bday_date.date()}")
print(f"3. {bday_date.isoformat()}")
print(f"4. {bday_date.hour}:{bday_date.minute}:{bday_date.second}")
print(f"5. {bday_date.isocalendar()}")
print(f"6. {bday_date.day}")
print(f"7. {WEEK_DAYS[bday_date.weekday()]}")
print(f"8. {bday_date.month}")
print(f"9. {MONTH_NAMES[bday_date.month]}")
print(f"10. {bday_date.time()}")
