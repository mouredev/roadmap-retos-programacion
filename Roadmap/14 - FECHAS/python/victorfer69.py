from datetime import datetime

#Ejercicio

now = datetime.now()
birth_date = datetime(2003, 9, 6, 12, 0, 0)

print(now)
print(birth_date)

difference = now - birth_date

print(type(difference))
print(f"Tengo {difference.days // 365} años")


#EJERCICIO EXTRA

años = difference.days // 365
meses = difference.days % 12
dias = difference.days % 30
print(f"Tengo {años} años, {meses} meses y {dias} días.")

# Día, mes y año
print(birth_date.strftime("%d/%m/%y"))
print(birth_date.strftime("%d/%m/%Y"))

# Horas, minutos y segundos
print(birth_date.strftime("%H:%M:%S"))

# Día del año
print(birth_date.strftime("%j"))

# Día de la semana
print(birth_date.strftime("%A"))

# Nombre del mes
print(birth_date.strftime("%h"))
print(birth_date.strftime("%B"))

# Representación por defecto del locale
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

# AM/PM
print(birth_date.strftime("%p"))