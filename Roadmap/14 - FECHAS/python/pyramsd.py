import datetime

current_date = datetime.datetime.now()
birthday = datetime.datetime(day=12, month=7, year=2005, hour=15, minute=30, second=0)

print(current_date.year - birthday.year)

'''
EXTRA
'''

print(birthday.strftime('%a / %b / %y'))
print(birthday.strftime('%A / %B / %Y'))
print(birthday.strftime('Semana %w / %B /%Y'))
print(birthday.strftime('Semana %W del %Y'))
print(birthday.strftime('%y / %b / %a'))
print(birthday.strftime('Semana %W a las %H horas'))
print(birthday.strftime('Semana %w a las %H:%S de %B del %Y'))
print(birthday.strftime('%d de %B del %Y'))
print(birthday.strftime('El día %d de la semana %w de %B del %Y'))
print(birthday.strftime('%D'))
