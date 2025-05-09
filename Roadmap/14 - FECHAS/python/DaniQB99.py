'''
EJERCICIO:
Crea dos variables utilizando los objetos fecha(date, o semejante) de
tu lenguaje:
- Una primera que represente la fecha (día, mes, año, hora, minuto, 
segundo) actual.
- Una segunda que represente tu fecha de nacimiento (te puedes 
inventar la hora).
Calcula cuántos años han transcurrido entre ambas fechas.
'''
from datetime import datetime

now = datetime.now()
birthday = datetime(1999, 7, 26, 9, 00, 00)

print(now)
print(birthday)

difference = now - birthday
print(type(difference))

print(f"Tengo {difference.days // 365} años")



'''
DIFICULTAD EXTRA (opcional):
Utilizando la fecha de tu cumpleaños, formatéala y muestra su 
resultado de 10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
(lo que se te ocurra...)
'''

print("\n\nDIFICULTAD EXTRA\n")

# Dia, mes y año

print(birthday.strftime("%d/%m/%y"))
print(birthday.strftime("%d/%m/%Y"))
print(birthday.strftime("%d %B %Y\n"))

# Hora, minuto y segundo
print(birthday.strftime("%H:%M:%S\n"))


# Dia del año
print(birthday.strftime("%j\n"))

# Dia de la semana
print(birthday.strftime("%A"))
print(birthday.strftime("%a\n"))

# Nombre del mes
print(birthday.strftime("%B"))  
print(birthday.strftime("%b\n"))    

# Representación de la fecha en formato de texto
print(birthday.strftime("%c"))      # Día, mes, día de la semana, día del mes, día del año, hora, minuto y segundo
print(birthday.strftime("%x"))      # Día de la semana, día del mes, día del año
print(birthday.strftime("%X\n"))    # Hora, minuto y segundo

# AM/PM
print(birthday.strftime("%p\n"))    # AM/PM