from datetime import datetime, timedelta

#Exercise

now = datetime.now()

birth_date = datetime(1991, 12, 21, 9, 30, 46)
print(now)
print(birth_date)

years = now - birth_date
print(f"I am {years.days // 365} years old")

#Extra exercise

#Day, month, year

print(birth_date.strftime("%d-%m-%y"))
print(birth_date.strftime("%d %m %Y"))

#Hours, minutes, seconds
print(birth_date.strftime("%H:%M:%S"))

#Day of the week name
print(birth_date.strftime("%A"))

#Month name
print(birth_date.strftime("%B"))

#My birthday + 10 days
print(birth_date + timedelta(days=10))

#My birthday - 9 hours
print(birth_date - timedelta(hours=9))

#Abbreviated month name
print(birth_date.strftime("%h"))

#Full month name
print(birth_date.strftime("%B"))

#Formatted according to your system’s locale.
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

#AM/PM
print(birth_date.strftime("%p"))
