import datetime

# Variable para fecha actual
current_datetime = datetime.datetime.now()

datebirth_str = "30-07-2004 02:28:00 AM"
format_str = "%d-%m-%Y %I:%M:%S %p"

# Variable para mi fecha de nacimiento
birth_datetime = datetime.datetime.strptime(datebirth_str, format_str)

# Cálculo de tiempo entre fechas
difference_datetime = current_datetime - birth_datetime
years = difference_datetime.days // 365
remaining_days = difference_datetime.days % 365
months = remaining_days // 30
remaining_days %= 30
days = remaining_days
hours = difference_datetime.seconds // 3600
minutes =(difference_datetime.seconds % 3600) // 60
seconds = difference_datetime.seconds % 60

print(f'''Hi, I'm César and i have:
  {years} years, {months} months, {days} days, with
  {hours} hours, {minutes} minutes and {seconds} seconds 
''')

print(f"""
1. Year-Month-Day Hrs:Min:Sec = {birth_datetime}
2. Day/Month/Year = {birth_datetime.strftime("%d/%m/%Y")}
3. Month/Day/Year = {birth_datetime.strftime("%m/%d/%Y")}
4. Day/MonthName/Year = {birth_datetime.strftime("%d/%B/%Y")}
5. DayName-Dat/MonthName/Year = {birth_datetime.strftime("%A-%d/%B/%Y")}
6. Abbreviated = {birth_datetime.strftime("%a-%d-%b-%Y")}
7. DayName-Day-MonthNameAbbr = {birth_datetime.strftime("%a-%d-%b")}
8. Day of the year = {birth_datetime.strftime("%j")}
9. Hour(12 format) = {birth_datetime.strftime("%I:%M:%S %p")}
10. Hour(24 format) = {birth_datetime.strftime("%H:%M:%S")}
11. {birth_datetime.strftime("%A, %dth of %B %Y at %I:%M:%S %p")}
""")