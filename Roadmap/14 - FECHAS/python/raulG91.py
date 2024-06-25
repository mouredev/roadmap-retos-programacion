from datetime import datetime as d

today = d.today()
birth_day = d(1991,9,11,15,00,00)
print(today.isoformat(sep=' ',timespec='seconds'))
print(birth_day.isoformat(sep=' ',timespec='seconds'))

diff = today -birth_day
print(diff)

#Extra
print("Extra")
#Format DD-MM-YYYY
print(f'{birth_day.day}-{birth_day.month}-{birth_day.year}')

#Format HH:mm:ss
print(f'{birth_day.hour}:{birth_day.minute}:{birth_day.second}')

#Week of the month
calendar_data = birth_day.isocalendar()
print(f'{calendar_data[1]}')

#Day of the week
day_week = birth_day.weekday()
if day_week == 0:
    day_week ="Monday"
elif day_week == 1:
    day_week = "Tuesday"
elif day_week == 2:
    day_week = "Wednesday"
elif day_week == 3:
    day_week = "Thursday"
elif day_week == 4:
    day_week = "Friday" 
elif day_week == 5:
    day_week = "Satruday" 
elif day_week == 6:
    day_week = "Sunday"

print(day_week)                      

#Month name 
print(birth_day.strftime("%B"))

#Day name + month name
print(birth_day.strftime("%A %d. %B %Y"))

#Extract day of the month 
tuple = birth_day.timetuple()
print(tuple[7])