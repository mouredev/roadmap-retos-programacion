from datetime import datetime, timedelta

"""
/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""

now = datetime.now()
print(now) # 2025-01-25 11:53:25.911556

my_birthdate = datetime(1998, 6, 19, 12, 0, 0)
difference = now - my_birthdate
years = difference.days / 365

print("La diferencia en años es de: %.2f" %years) # La diferencia en años es de: 26.62

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */
"""

# Dia, mes y año
print(my_birthdate)
print("Dia, mes y año:", my_birthdate.strftime("%d, %m, %Y"))
# Hora, minuto y segundo
print("Hora, minuto y segundo:", my_birthdate.strftime("%H - %M - %S"))
# Dia de año
print("Dia de año:", my_birthdate.strftime("%j")) # 170
# Dia de la semana
print("Dia de la semana:", my_birthdate.strftime("%A")) # Friday
print("Dia de la semana:" , my_birthdate.strftime("%w")) # 5
# Nombre del mes
print("Nombre del mes:", my_birthdate.strftime("%B")) # June

# Hora
print("Hora:", my_birthdate.strftime("%I:%M:%S %p")) # 12:00 PM

# Semana del año
print("Semana del año:", my_birthdate.strftime("%U")) # 24

# Fecha-Hora local
print("Hora local:", my_birthdate.strftime("%c")) # Fri Jun 19 12:00:00 1998

# Fecha local
print("Fecha local:", my_birthdate.strftime("%x")) # 06/19/98