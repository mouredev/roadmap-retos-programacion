"""
    #14 FECHAS
"""

from datetime import datetime

fecha_actual = datetime.now()
print(fecha_actual.strftime("%d/%m/%Y %H:%M:%S"))

fecha_nacimiento = datetime(year=2005, month=4, day=15, hour=12, minute=00, second=00)

diferencia_dias = fecha_actual - fecha_nacimiento

años_transcurridos = diferencia_dias.days // 365.25

print(f"Han transcurrido {años_transcurridos} años.")

"""
    DIFICULTAD EXTRA
"""

# 1. Día, mes y año
day_month_year = fecha_nacimiento.strftime("%d/%m/%Y")
print(f"1. Día, mes y año: {day_month_year}")

# 2. Hora, minuto y segundo
hora_minuto_segundo = fecha_nacimiento.strftime("%H:%M:%S")
print(f"2. Hora, minuto y segundo: {hora_minuto_segundo}")

# 3. Día del año
day_year = fecha_nacimiento.strftime("%j")
print(f"3. Día del año: {day_year}")

# 4. Día de la semana
dia_semana = fecha_nacimiento.strftime("%A")
print(f"4. Día de la semana: {dia_semana}")

# 5. Nombre del mes
nombre_mes = fecha_nacimiento.strftime("%B")
print(f"5. Nombre del mes: {nombre_mes}")

# 6. Semana del año
semana_año = fecha_nacimiento.strftime("%W")
print(f"6. Semana del año: {semana_año}")

# 7. Fecha completa con formato ISO
fecha_formateada7 = fecha_nacimiento.isoformat()
print(f"7. Fecha completa con formato ISO: {fecha_formateada7}")

# 8. Fecha y hora
fecha_formateada8 = fecha_nacimiento.strftime("%d de %B de %Y a las %H:%M:%S")
print(f"8. Fecha y hora: {fecha_formateada8}")

# 9. Hora con formato de 12 horas
fecha_formateada9 = fecha_nacimiento.strftime("%I:%M:%S %p")
print(f"9. Hora con formato de 12 horas: {fecha_formateada9}")

# 10. Fecha y hora
fecha_formateada10 = fecha_nacimiento.strftime("%d/%m/%Y %H:%M:%S")
print(f"10. Fecha y hora: {fecha_formateada10}")
