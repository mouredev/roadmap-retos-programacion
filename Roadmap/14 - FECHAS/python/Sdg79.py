
from datetime import datetime

fecha_actual = datetime.now()
print(fecha_actual)

fecha_cumpleaños = datetime.strptime("04/10/1979, 16:15", "%d/%m/%Y, %H:%M")
print(fecha_cumpleaños)

años = ((fecha_actual - fecha_cumpleaños) // 365)
print(f"Han transcurrido {años.days} años desde mi nacimiento")



# DIFICULTAD EXTRA:

print(fecha_cumpleaños.strftime("Fecha de Nacimiento: %d de %B de %Y"))
print(fecha_cumpleaños.strftime("Hora de Nacimiento: %H:%M"))
print(fecha_cumpleaños.strftime("Dia del mes de Nacimiento: %d"))
print(fecha_cumpleaños.strftime("Dia de la semana de Nacimiento: %A"))
print(fecha_cumpleaños.strftime("Mes de Nacimiento: %B"))
print(fecha_cumpleaños.strftime("Año de Nacimiento: %Y"))
print(fecha_cumpleaños.strftime("Mes y año de Nacimiento: %B de %Y"))
print(fecha_cumpleaños.strftime("Fecha de Nacimiento: %d de %B de %Y, %H:%M"))
print(fecha_cumpleaños.strftime("Semana del año de Nacimiento: %U"))
print(fecha_cumpleaños.strftime("Dia del año de Nacimiento: %j"))
print(fecha_cumpleaños.strftime("Fecha de Nacimiento: %c"))