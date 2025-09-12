from datetime import datetime
hoy = datetime.now()
print(hoy)
fecha_nacimiento = datetime(1982, 2, 20, 20, 30, 23)

años = hoy - fecha_nacimiento

print(f"Tengo {años.days // 365} años.")

"""
DIFICULTAD EXTRA (opcional):
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
10 maneras diferentes. Por ejemplo:
- Día, mes y año.
- Hora, minuto y segundo.
- Día de año.
- Día de la semana.
- Nombre del mes.
(lo que se te ocurra...)
"""

print(fecha_nacimiento.strftime("%d/%m/%y")) # 20/02/82
print(fecha_nacimiento.strftime("%d/%m/%Y")) # 20/02/1982
print(fecha_nacimiento.strftime("%d/%B/%Y")) # 20/February/1982
print(fecha_nacimiento.strftime("%H:%M:%S")) # 20:30:23
print(fecha_nacimiento.strftime("%j")) # 051 (día del año)
print(fecha_nacimiento.strftime("%A")) # Saturday (nombre del día de la semana)
print(fecha_nacimiento.strftime("%h")) # Feb (nombre del mes)
print(fecha_nacimiento.strftime("%B")) # February (nombre del mes)
print(fecha_nacimiento.strftime("%p")) # February (nombre del mes)
