"""EJERCICIO:
Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
- Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
- Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
Calcula cuántos años han transcurrido entre ambas fechas."""

import datetime
from dateutil.relativedelta import relativedelta


def calculate_how_many_years_since_dob():
    print(f'**** Current Date ****\n'
          f'Date: {current_date.date()}\n'
          f'Time: {current_date.time()}\n')

    print(f'**** My birthday ****\n'
          f'Date: {dob_date.date()}\n'
          f'Time: {dob_date.time()}\n')

    total_years = relativedelta(current_date, dob_date)
    print(f'Years that has passed: {total_years.years} years\n')


""" DIFICULTAD EXTRA (opcional):
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de 10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
- Otros"""


def formatting_dob():
    print(f'1. YYYY/DD/MM: {dob_date.strftime("%Y/%d/%m")}')
    print(f'2. YYYY/MM/DD: {dob_date.strftime("%Y/%m/%d")}')
    print(f'3. DD/MM/YY: {dob_date.strftime("%d/%m/%y")}')
    print(f'4. MM/DD/YY: {dob_date.strftime("%m/%d/%y")}')
    print(f'5. Month day, year: {dob_date.strftime("%B %d, %Y")}')
    print(f'6. Month DD, HH:MM : {dob_date.strftime("%B %d, %H:%M")}')
    print(f'7. Day of the year YYYY: {dob_date.strftime("Day %j of %Y")}')
    print(f'8. HH hours and MM minutes of MM the DD: {dob_date.strftime("%H hours and %M minutes of %B the %d")}')
    print(f'9. DD-MM-YY HH:MM:SS: {dob_date.strftime("%d-%m-%y %H:%M:%S")}')
    print(f'10. --Day and Time--\n'
          f'{dob_date.strftime("Date: %A, %d")}\n'
          f'{dob_date.strftime("Time: %H:%M:%S")}')


current_date = datetime.datetime.now().replace(microsecond=0)
dob_date = datetime.datetime(year=1994, month=5, day=20, hour=10, minute=30, second=15, microsecond=0)

calculate_how_many_years_since_dob()
print('****************')
formatting_dob()
