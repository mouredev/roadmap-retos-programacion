# RETO 14 FECHAS

from datetime import datetime

"""
CREA DOS VARIABLES CON LOS OBJETOS FECHA
(año, mes, día, hora, minutos, segundos)
1: FECHA ACTUAL 
2: FECHA DE NACIMIENTO
= AÑOS TRANSCURRIDOS ENTRE AMBAS FECHAS
"""

now = datetime.now()
birth_date = datetime(1992, 12, 3, 16, 30, 0)

print(now)
print(birth_date)

diferrence = now - birth_date
print(type(diferrence))

print(f"I have {diferrence.days // 365} years.")


# Extra

print("🧩 DIFICULTAD EXTRA - 10 MANERAS DE MOSTRAR LA FECHA 🧩")

# Día, mes y año
print(birth_date.strftime("%d/%m/%y"))

# Hora, minutos y segundos
print(birth_date.strftime("%H:%M:%S"))

# Día del año
print(birth_date.strftime("%j"))

# Día de la semana
print(birth_date.strftime("%A"))

# Nombre del mes
print(birth_date.strftime("%B"))

# Locale
print(birth_date.strftime("%c"))

# AM/PM
print(birth_date.strftime("%p"))