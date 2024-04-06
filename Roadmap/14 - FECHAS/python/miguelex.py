from datetime import datetime

now = datetime.now()

birth = datetime.strptime("03/09/1975 09:40:25", "%d/%m/%Y %H:%M:%S")

diff = now - birth

years = diff.days // 365
months = (diff.days % 365) // 30
days = diff.days % 30
hours = diff.seconds // 3600
minutes = (diff.seconds % 3600) // 60
seconds = diff.seconds % 60

print("Hoy es el", now.strftime("%d/%m/%Y %H:%M:%S"))
print("Nací el", birth.strftime("%d/%m/%Y %H:%M:%S"))
print("\nHan pasado", years, "años,", months, "meses,", days, "días,", hours, "horas,", minutes, "minutos y", seconds, "segundos desde que nací")

# Extras

print(birth.strftime("%d/%m/%Y"))

print(birth.strftime("%d/%m/%y"))

print(birth.strftime("%d de %B de %Y"))

print("Nací un", birth.strftime("%A"))

print("El día de mi nacimiento era el", birth.strftime("%j"), "día del año")

print("La fecha de mi nacimiento estaba en la semana", birth.strftime("%U"))

print("Mi año de nacimiento", "es" if birth.year % 4 == 0 and (birth.year % 100 != 0 or birth.year % 400 == 0) else "no es", "bisiesto")

print("Nací en", birth.strftime("%B"))

print("Nací en", birth.strftime("%b"))

print("Nací en la década de los", birth.strftime("%Y")[2], "0")

century = birth.year // 100 + 1
print("Nací en el siglo", century)

print("Nací a las", birth.strftime("%H:%M:%S"))

print("Nací a las", birth.strftime("%I:%M:%S %p"))
