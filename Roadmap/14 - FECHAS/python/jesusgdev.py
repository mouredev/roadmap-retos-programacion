'''
EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
   - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
   - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
  
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
   10 maneras diferentes. Por ejemplo:
   - Día, mes y año.
   - Hora, minuto y segundo.
   - Día de año.
   - Día de la semana.
   - Nombre del mes.
   (lo que se te ocurra...)
'''

from datetime import datetime

actual_date = datetime.now()
print("Fecha actual: ", actual_date)

birth_date = datetime(1984, 3, 25, 14, 30, 0)
print("Fecha de nacimiento: ", birth_date)

years = actual_date.year - birth_date.year

if (actual_date.month, actual_date.day) < (birth_date.month, birth_date.day):
    years -= 1

print(f"Han pasado {years} años desde tu nacimiento")

'''
Extra
'''

from datetime import datetime

# 🎂 Tu cumpleaños con fecha y hora completa
birth_date = datetime(1984, 3, 25, 14, 30, 0)

print("🎉 Mostrando la fecha de cumpleaños en 10 formatos distintos:\n")

# 1️⃣ Día, mes y año (formato corto)
print("📆 Día-Mes-Año: ", birth_date.strftime("%d-%m-%Y"))

# 2️⃣ Día, mes y año (formato largo)
print("📆 Día de Mes de Año: ", birth_date.strftime("%d de %B de %Y"))

# 3️⃣ Hora, minuto y segundo
print("⏰ Hora-Minuto-Segundo: ", birth_date.strftime("%H:%M:%S"))

# 4️⃣ Día de la semana (nombre completo)
print("📅 Día de la semana: ", birth_date.strftime("%A"))

# 5️⃣ Día del año (1 al 366)
print("📅 Día del año: ", birth_date.strftime("%j"))

# 6️⃣ Semana del año (número de semana)
print("🗓️ Semana del año: ", birth_date.strftime("%U"))

# 7️⃣ Nombre del mes
print("🗓️ Mes (nombre): ", birth_date.strftime("%B"))

# 8️⃣ Día con nombre corto del mes
print("📆 Día/Mes corto: ", birth_date.strftime("%d/%b"))

# 9️⃣ Fecha y hora juntas (formato completo)
print("🕰️ Fecha y hora completas: ", birth_date.strftime("%c"))

# 🔟 Formato ISO (internacional)
print("🌐 Formato ISO 8601: ", birth_date.isoformat())
