from datetime import datetime

# Variables de tipo date
current_date = datetime.now()
birth_date = datetime(1993, 10, 13, 23, 00, 00)

# Cálculo del tiempo transcurrido entre ambas fechas
difference = current_date - birth_date
years_elapsed = difference.days // 365
print(f'Los años transcurridos desde tu nacimiento hasta hoy son un total de: {years_elapsed}')

# ------------------
## DIFICULTAD EXTRA
# ------------------

formatting = [
    "%d/%m/%Y",                # Día, mes y año
    "%H:%M:%S",                # Hora, minuto y segundo
    "%j",                      # Día de año
    "%A",                      # Día de la semana
    "%B",                      # Nombre del mes
    "%Y-%m-%d",                # Año-mes-día
    "%I:%M %p",                # Hora en formato 12 horas con AM/PM
    "%Y-%m-%d %H:%M:%S",       # Año-mes-día Hora:minuto:segundo
    "%b %d, %Y",               # Abreviatura del mes, día, año (May 25, 2000)
    "%A, %d %B %Y %I:%M %p"    # Día de la semana, día, nombre del mes, año, hora en formato 12 horas con AM/PM
]

for format in formatting:
  print(birth_date.strftime(format))
