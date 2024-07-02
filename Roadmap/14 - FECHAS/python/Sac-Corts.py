### Ejercicio ###
from datetime import datetime

now = datetime.now()
print(now)

my_birthday = datetime(2001, 10, 21, 5, 30, 15)
print(my_birthday)

difference = now - my_birthday
print(difference)

### Ejercicio Extra ###

print(my_birthday.strftime("%d/%m/%Y"))
print(my_birthday.strftime("%d-%m-%Y"))
print(my_birthday.strftime("%B %d, %Y"))
print(my_birthday.strftime("%H:%M:%S %p"))
print(my_birthday.strftime("%X %p"))
print(my_birthday.strftime("%c"))
print(my_birthday.strftime("%x"))
print(my_birthday.strftime("%A"))
print(my_birthday.strftime("%j"))

my_next_birthday = datetime(2024, 10, 21)
time_left = my_next_birthday - now
days = time_left.days
print(f"¡Faltan {days} días para mi cumpleaños!")