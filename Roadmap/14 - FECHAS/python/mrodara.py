#################################  FECHAS  ####################################################

from datetime import datetime, timedelta, date, time

time_now = datetime.now()

my_birthdate = datetime(year=1980, month=1, day=3, hour=8, minute=0, second=0)

difference = time_now - my_birthdate

print(difference.days // 365)

#########################################  EXTRA  #######################################################

print(my_birthdate.day)
print(my_birthdate.month)
print(my_birthdate.year)
print(my_birthdate.hour)
print(my_birthdate.minute)
print(my_birthdate.second)
print(my_birthdate.weekday())  # 0 = Monday, 1 = Tuesday,
print(my_birthdate.isoweekday())  # 1 = Monday, 2 = Tuesday
print(my_birthdate.strftime("%A"))  # Full weekday name
print(my_birthdate.strftime("%a"))  # Abbreviated weekday name
print(my_birthdate.strftime("%B"))  # Full month name
print(my_birthdate.strftime("%b"))  # Abbreviated month name
print(my_birthdate.strftime("%Y"))  # Year with century as a decimal number
print(my_birthdate.strftime("%y"))  # Year without century as a zero-padded decimal number
print(my_birthdate.strftime("%m"))  # Month as a zero-padded decimal number
print(my_birthdate.strftime("%d"))  # Day of the month as a zero-padded decimal
print(my_birthdate.strftime("%H"))  # Hour (24-hour clock) as a zero-p
print(my_birthdate.strftime("%I"))  # Hour (12-hour clock) as a zero-p
print(my_birthdate.strftime("%M"))  # Minute as a zero-padded decimal number
print(my_birthdate.strftime("%S"))  # Second as a zero-padded decimal number
print(my_birthdate.strftime("%f"))  # Microsecond as a decimal number, zero-padded
print(my_birthdate.strftime("%p"))  # Locale’s equivalent of either AM or PM
print(my_birthdate.strftime("%j"))  # Day of the year as a zero-padded decimal



#########################################  FIN EXTRA  #######################################################

#################################  FIN FECHAS  ####################################################