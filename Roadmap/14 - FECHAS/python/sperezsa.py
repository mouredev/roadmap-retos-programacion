from datetime import datetime

now = datetime.now()

# Me quedo con la parte de la fecha sin los milisegundos
now_format = datetime.strptime(str(now).split(".")[0], "%Y-%m-%d %H:%M:%S")

print(f"Fecha actual en formato '%Y-%m-%d %H:%M:%S': {now_format}")

birth_date = datetime(1979, 9, 8, 12, 23, 59)
print(f"Fecha de nacimiento: {birth_date}")

print(f"Resta de fechas en años: {(now - birth_date).days / 365.25}")

"""
Extra
"""

print("EXTRA")

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Dia, mes, año
print("Día, mes, año:", birth_date.strftime("%d-%m-%Y"))

# hora, min, segundo
print("Hora, min, segundo:", birth_date.strftime("%H:%M:%S"))

# día del año desde 01-ene
print("Día del año desde 01-ene:", birth_date.strftime("%j"))

# día de la semana, en Inglés y en Castellano
print("Día de la semana, en Inglés y en Castellano:", birth_date.strftime("%A"), dias_semana[birth_date.weekday()])

#Nombre del mes, en Inglés y en Castellano
print("Nombre del mes, en Inglés y en Castellano:", birth_date.strftime("%B"),meses[birth_date.month-1])



