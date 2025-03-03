from datetime import datetime

current_date = datetime.now()
born_date = datetime(1990, 2, 7, 5, 30, 00)

#Calcular los años que han pasado entre ambas fechas
days_passed = current_date - born_date
years_passed = days_passed.days // 365

print(f"Entre ambas fechas han transcurrido {years_passed} años")

#EXTRA
print("---------------------")
print("\nDía, mes y año")
print(born_date.strftime('%d-%m-%Y'))
print("\nHora, minuto y segundo")
print(born_date.strftime('%H:%M:%S'))
print("\nDía de la semana (versión corta)")
print(born_date.strftime('%a'))
print("\nDía de la semana (versión larga)")
print(born_date.strftime('%A'))
print("\nDía del mes (0-6) donde el 0 es Domingo")
print(born_date.strftime('%w'))
print("\nHora local AM o PM")
print(born_date.strftime('%H:%M:%S %p'))
print("\nFecha con hora en formato 12 horas")
print(born_date.strftime('%x %I %p'))
print("\nDía de la semana y minuto")
print(born_date.strftime('%A - Minuto: %M'))
print("\nDía de la semana y año (versión corta)")
print(born_date.strftime('%A - Año: %y'))
print("\nDía del mes")
print(born_date.strftime('%d'))