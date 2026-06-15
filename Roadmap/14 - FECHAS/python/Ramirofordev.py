'''
Crea dos variables los objetos fecha(date, o semejante) de tu lenguaje:
    * Una primera que represente la fecha (dia mes año hora minuto segundo) actual.
    * Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
Calcula cuando años han transcurrido entre ambas fechas'''

from datetime import datetime

actual_date = datetime.now()

birth_date = datetime(2006, 12, 22, 4, 0, 0)
print(f"La fecha actual es {actual_date}, mientras que mi fecha de nacimiento es {birth_date}")

days = actual_date - birth_date

print(f"Tengo {(days.days // 365)}\n")

'''
Dificultad extra:
Utilizando la fecha de tu cumpleaños, formateala y muestra su resultado de 10 maneras diferentes.
'''

print(birth_date.strftime("%d/%m/%y"))
print(birth_date.strftime("%d/%m/%Y"))
print(birth_date.strftime("%H: %M %S"))
print(birth_date.strftime("%j del %y"))
print(birth_date.strftime("%h del %Y"))
print(birth_date.strftime("%A"))
print(birth_date.strftime("%B del %Y"))
print(birth_date.strftime("%c"))
print(birth_date.strftime("%d de %B"))
print(birth_date.strftime("%X del dia %d"))
