from datetime import datetime

# EJERCICIO:
# Crea dos variables utilizando los objetos fecha (data, o semejante) de tu lenguaje:
# - Una primera que representa la fecha (día, mes, año, hora, minuto, segundo) actual.
# - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
# Calcula cuántos años han transcurrido entre ambas fechas.

fecha_actual = datetime.now()
fecha_nac = datetime(2000, 9, 19, 12, 0, 0)

print(f"Fecha actual: {fecha_actual}")
print(f"Mi fecha de nacimiento: {fecha_nac}")
print(f"Han transcurrido {(fecha_actual - fecha_nac).days // 365} años entre ambas fechas.")

# DIFICULTAD EXTRA (opcional):
# Utilizando la fecha de tu cumpleaños, formateála y muestra su resultado de
# 10 maneras diferentes. Por ejemplo:
# - Día, mes y año.
# - Hora, minuto y segundo.
# - Día de año.
# - Día de la semana.
# - Nombre del mes
# (lo que se te ocurra....)

print(f"\nMi fecha de nacimiento: {fecha_nac}")

'''(Día) de (mes) del (año)'''
print(datetime.strftime(fecha_nac, '%d de %m del %Y'))

'''(Día) de (Nombre del mes) del (año)'''
print(datetime.strftime(fecha_nac, '%d de %B del %Y'))

'''(Nombre del día)'''
print(datetime.strftime(fecha_nac, '%A'))

'''(Nombre del mes)'''
print(datetime.strftime(fecha_nac, '%B'))

'''(Día)/(Mes)/(Año)'''
print(datetime.strftime(fecha_nac, '%d/%m/%Y'))

'''(Día)/(Mes)/(Año) (Horas):(Minutos):(Segundos)'''
print(datetime.strftime(fecha_nac, '%d/%m/%Y %H:%M:%S'))

'''(Horas):(Minutos) (AM/PM)'''
print(datetime.strftime(fecha_nac, '%H:%M %p'))

'''Día: (Nombre del día), Mes: (Nombre del mes), Año: (Año)'''
print(datetime.strftime(fecha_nac, 'Día: %A, Mes: %B, Año: %Y'))

'''(Nombre del día) (Día) de (Nombre del mes) del (Año)'''
print(datetime.strftime(fecha_nac, '%A %d de %B del %Y'))

'''(Nombre del día) (Día) de (Nombre del mes) del (Año) a las (Horas):(Minutos) (AM/PM)'''
print(datetime.strftime(fecha_nac, '%A %d de %B del %Y a las %H:%M %p'))