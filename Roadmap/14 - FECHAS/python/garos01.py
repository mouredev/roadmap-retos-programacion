from datetime import datetime

# Fecha actual
fecha_actual = datetime.now()

# Tu fecha de nacimiento (puedes modificar los valores)
fecha_nacimiento = datetime(year=1994, month=9, day=11, hour=13, minute=40, second=3)

# Calculando la diferencia de años
diferencia = fecha_actual.year - fecha_nacimiento.year

# Ajustando la diferencia si aún no ha pasado tu cumpleaños este año
if (fecha_actual.month, fecha_actual.day) < (
    fecha_nacimiento.month,
    fecha_nacimiento.day,
):
    diferencia -= 1

print("Han transcurrido {} años desde tu fecha de nacimiento.".format(diferencia))

# Ejercicio extra


formatos = [
    "%d/%m/%Y",  # Día, mes y año
    "%H:%M:%S",  # Hora, minuto y segundo
    "%j",  # Día de año
    "%A",  # Día de la semana
    "%B",  # Nombre del mes
    "%d de %B del %Y",  # Día de la semana completo
    "%m/%d/%y",  # Fecha en formato corto
    "%Y-%m-%d %H:%M:%S",  # Fecha y hora en formato ISO
    "%d/%m/%Y %H:%M:%S",  # Fecha y hora en formato personalizado
    "%I:%M %p",  # Hora en formato 12 horas con AM/PM
]

# Mostrar la fecha de nacimiento en los diferentes formatos
print("Fecha de nacimiento:")
for formato in formatos:
    print(fecha_nacimiento.strftime(formato))
