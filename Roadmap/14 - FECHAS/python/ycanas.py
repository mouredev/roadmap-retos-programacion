import datetime

# ------ 1. Ejercicio

actual = datetime.datetime.now()
birth = datetime.datetime(2000, 1, 3, 6, 0, 0, 0)

difference = actual - birth
years = int(difference.days / 365)
days = difference.days % 365

print(f"Desde mi nacimiento han pasado: {years} años y {days} días.")


# ------ 2. Extra

print("Día mes y año →", birth.strftime("%d/%m/%Y"))
print("Hora minuto y segundo →", birth.strftime("%H:%M:%S"))
print("Día del año →", birth.strftime("%j"))
print("Día de la semana →", birth.strftime("%w"))
print("Nombre del mes →", birth.strftime("%B"))
print("Nombre del día de la semana →", birth.strftime("%A"))
print("Número de semana del año →", birth.strftime("%W"))
print("¿AM o PM? →", birth.strftime("%p"))
print("Nombre del día, día, nombre del mes y año →", birth.strftime("%A %d %B %Y"))
print("Número del mes", birth.strftime("%m"))
