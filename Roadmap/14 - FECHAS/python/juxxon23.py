from datetime import datetime

# Ejercicio 1
current_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
current_date_obj = datetime.strptime(current_date, "%d/%m/%Y, %H:%M:%S")

birth_date = "17/05/1998, 03:25:32"
birth_date_obj = datetime.strptime(birth_date, "%d/%m/%Y, %H:%M:%S")

years_passed = current_date_obj - birth_date_obj

print(f"Birth date: {birth_date_obj} \nCurrent date: {current_date_obj}")
print(f"{years_passed.days//365} years have passed.")


# Ejercicio Extra
print(f"""
Dates Formatting - 10 different ways: 
1) [day month year, hour AM/PM] -> {birth_date_obj.strftime("%A %B %Y, %-I %p")} 
2) [day-month-year] -> {birth_date_obj.strftime("%a-%b-%Y")} 
3) [day day moth, week week_year of year] -> {birth_date_obj.strftime("%A %d %B, week %W of %Y")} 
4) [day/month/year, hours:minutes:seconds AM/PM] -> {birth_date_obj.strftime("%-d/%-m/%y, %I:%-M:%-S %p")} 
5) [hour AM/PM, year/month/day] -> {birth_date_obj.strftime("%-H %p, %Y/%B/%d")} 
6) [day, day of month year] -> {birth_date_obj.strftime("%A, %-d of %B %Y")} 
7) [hour AM/PM - month day year] -> {birth_date_obj.strftime("%-H %p - %B %A %Y")} 
8) [month/day/year] -> {birth_date_obj.strftime("%b/%d/%Y")} 
9) [month.day.year] -> {birth_date_obj.strftime("%m.%d.%y")} 
10) [day, year.month.day ; hours:minutes:seconds] -> {birth_date_obj.strftime("%A, %y.%m.%d ; %H:%M:%S")}""")