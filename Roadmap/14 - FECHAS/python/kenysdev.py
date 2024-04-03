# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------
# * FECHAS
# -----------------------------------
# Mas info: https://docs.python.org/3/library/datetime.html

"""
# EJERCICIO 1
* Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
* - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
* - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
* Calcula cuántos años han transcurrido entre ambas fechas.
"""

import datetime
current_date_time = datetime.datetime.now()
birth_date = datetime.datetime.strptime(
    "1995-10-20 02:30:00", "%Y-%m-%d %H:%M:%S")

difference = current_date_time - birth_date
years = difference.days // 365
months = (difference.days % 365) // 30
days = (difference.days % 365) % 30

print(f"""
Juanito tiene:
{years} años,
{months} meses y
{days} dias.
""")

# ___________________________________
"""
# EJERCICIO 2
* Utilizando la fecha de tu cumpleaños, formatéala y muestra su 
  resultado de 10 maneras diferentes.
"""

print(f"""
1. Predeterminado -> {birth_date}
2. dd/mm/yyyy     -> {birth_date.strftime("%d/%m/%Y")}
3. dd-mm-yyyy     -> {birth_date.strftime("%d-%m-%Y")}
4. Nombre del mes -> {birth_date.strftime("%B")}
5. Mes abreviado  -> {birth_date.strftime("%b")}
6. Nombre dia     -> {birth_date.strftime("%A")}
7. Dia abreviado  -> {birth_date.strftime("%a")}
8. Hora(12 horas) -> {birth_date.strftime("%I:%M:%S %p")}
9. Hora(24 horas) -> {birth_date.strftime("%H:%M:%S")}
0. personalizado  -> {birth_date.strftime(
    "Born on %A, %dth of %B %Y at %I:%M:%S %p")}
""")
