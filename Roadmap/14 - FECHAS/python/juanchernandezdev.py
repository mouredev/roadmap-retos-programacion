### Python Dates ###
from datetime import datetime

current_time = datetime.now()
birth_time = datetime(1987, 12, 23, 4, 45, 8)
print(current_time, birth_time)

years_passed = current_time - birth_time
print(years_passed)

#! Optional Challenge
format_one = birth_time.strftime('%Y/%d/%m')
print(format_one)
format_two = birth_time.strftime('%B-%d-%Y')
print(format_two)
format_three = birth_time.strftime('%a-%d-%B-%y')
print(format_three)
format_four = birth_time.strftime('%a-%d-%B-%y')
print(format_three)
format_five= birth_time.strftime('%d-%B-%y-%H')
print(format_five)
format_six = birth_time.strftime('%d-%a-%B-%Y-%H')
print(format_six)
format_seven = birth_time.strftime('%d-%a-%B-%Y-%I%p')
print(format_seven)
format_eighth = birth_time.strftime('%d-%a-%B-%y-%I%p-00:%M')
print(format_eighth)
format_nine = birth_time.strftime('%d-%a-%B-%y-%I%p-00:%M-00:%S')
print(format_nine)
format_ten = birth_time.strftime('%d-%a/%B/%y/ %I:%M:%S %p')
print(format_ten)
