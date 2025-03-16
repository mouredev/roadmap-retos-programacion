#14 { Retos para Programadores } FECHAS

# Bibliography reference
# Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
#Python Notes for Professionals. 800+ pages of professional hints and tricks (GoalKicker.com) (Z-Library)
# Additionally, I use GPT as a reference and sometimes to correct or generate proper comments.

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

from datetime import datetime, timedelta

# Short for print
log = print

# Simulating the window load event
def on_load():
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = 'Retosparaprogramadores #14.'
    title_style = {
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    # Simulating setting styles (not applicable in console)
    log(f"Body styles: {body_style}")
    log(f"Title: {title} with styles: {title_style}")
    
    # Simulating alert after 2 seconds
    log("Retosparaprogramadores #14")

# Call the on_load function to simulate the window load event
on_load()

# Current date
today = datetime.now()
log(today)  # Current date and time // 2024-12-25 06:22:05.153585
log(today.date())  # Current date // 2024-12-25
my_birthday = datetime(1983, 8, 8, 8, 30)  # Birthday
log(my_birthday)  # Birthday date and time // 1983-08-08 08:30:00
log(my_birthday.date())  # Birthday date // 1983-08-08 
log(my_birthday.strftime("%Y-%m-%d %I:%M:%S %p"))  # Birthday in a specific format // 1983-08-08 08:30:00 AM

def calc_years_between(date1, date2):
    """Calculate the years between two dates."""
    if date1 < date2:
        date1, date2 = date2, date1  # Swap if date1 is earlier

    difference_in_days = (date1 - date2).days
    years = difference_in_days / 365.25  # Using 365.25 for leap years
    full_years = int(years)

    # Check if the anniversary has not yet occurred this year
    if (date1.month < date2.month) or (date1.month == date2.month and date1.day < date2.day):
        full_years -= 1

    return years

years_between = calc_years_between(today, my_birthday)
log(f"Years between: {years_between:.2f}")  # Display years with two decimal places // Years between: 41.38

def calc_years_between_simple(date1, date2):
    """Calculate the simple year difference between two dates."""
    if date1 < date2:
        date1, date2 = date2, date1  # Swap if date1 is earlier

    years = date1.year - date2.year
    if (date1.month < date2.month) or (date1.month == date2.month and date1.day < date2.day):
        years -= 1

    return years

log(calc_years_between_simple(today, my_birthday))  # Simple year difference // 41

def calc_date_difference(date1, date2):
    """Calculate the difference between two dates."""
    if date1 < date2:
        date1, date2 = date2, date1  # Swap if date1 is earlier

    difference = date1 - date2

    # Calculate total seconds
    total_seconds = difference.total_seconds()
    
    # Calculate total days, weeks, months, and years
    total_days = difference.days
    years = date1.year - date2.year
    months = (date1.month - date2.month) + (years * 12)
    weeks = total_days // 7
    days = total_days % 7

    # Calculate remaining hours, minutes, and seconds
    remaining_hours = (total_seconds // 3600) % 24
    remaining_minutes = (total_seconds // 60) % 60
    remaining_seconds = total_seconds % 60

    return {
        'years': years,
        'months': months,
        'weeks': weeks,
        'days': days,
        'hours': remaining_hours,
        'minutes': remaining_minutes,
        'seconds': remaining_seconds
    }

difference = calc_date_difference(today, my_birthday)
log(f"Difference: \n{difference['years']} years, \n{difference['months']} months, \n{difference['weeks']} weeks, \n{difference['days']} days, \n{difference['hours']} hours, \n{difference['minutes']} minutes, \n{difference['seconds']} seconds")
"""  
Difference:
41 years,
496 months,
2159 weeks,
1 days,
21.0 hours,
52.0 minutes,
5.153584957122803 seconds

"""

def format_birthday(birthday):
    """Format birthday information."""
    day_month_year = birthday.strftime("%B %d, %Y")
    time = birthday.strftime("%I:%M:%S %p")
    day_of_year = (birthday - datetime(birthday.year, 1, 1)).days + 1
    day_of_week = birthday.strftime("%A")
    month_name = birthday.strftime("%B")
    iso_format = birthday.isoformat()
    short_format = birthday.strftime("%m/%d/%Y")
    long_format = birthday.strftime("%A, %B %d, %Y")
    time_12_hour = birthday.strftime("%I:%M:%S %p")
    time_with_timezone = birthday.strftime("%m/%d/%Y, %I:%M:%S %p")  # Simulating timezone display

    log("1. I was born on:", day_month_year) # 1. I was born on: August 08, 1983
    log("2. at:", time) # 2. at: 08:30:00 AM
    log("3. the day:", day_of_year, "of the year", birthday.year) # 3. the day: 220 of the year 1983
    log("4. on:", day_of_week) #  4. on: Monday
    log("5. one special day of:", month_name) # 5. one special day of: August
    log("6. isoFormat:", iso_format) # 6. isoFormat: 1983-08-08T08:30:00
    log("7. shortFormat:", short_format) # 7. shortFormat: 08/08/1983
    log("8. longFormat:", long_format) # 8. longFormat: Monday, August 08, 1983
    log("9. time12hour:", time_12_hour) # 9. time12hour: 08:30:00 AM
    log("10. timeWithTimezone:", time_with_timezone) # 10. timeWithTimezone: 08/08/1983, 08:30:00 AM

# Call the format_birthday function with my_birthday
format_birthday(my_birthday)

# Note: The timezone information is not directly available in the datetime object without additional libraries.
# The time_with_timezone output is simulated for demonstration purposes.
