###############################################################################
## EJERCICIO
###############################################################################
import datetime as dt

actual_date = dt.datetime.now()
format_actual_date = actual_date.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha Actual:", format_actual_date)

birth_date = dt.datetime(1989, 4, 4, 18, 30, 00)
format_birth_date = birth_date.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha nacimiento:",format_birth_date)

time_elapsed = actual_date - birth_date
print("Tiempo transcurrido: ", time_elapsed)



###############################################################################
## DIFICULTAD EXTRA
###############################################################################
b_format1 = birth_date.strftime("%d, %m, %Y")
b_format2 = birth_date.strftime("%H, %M, %S")
b_format3 = birth_date.strftime("%j")
b_format4 = birth_date.strftime("%A")
b_format5 = birth_date.strftime("%B")
b_format6 = birth_date.strftime("%A,%B,%Y")

fechas = [b_format1, b_format2, b_format3, b_format4, b_format5, b_format6]

for fecha in fechas:
    print(fecha)
