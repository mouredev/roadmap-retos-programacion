# Ejercicio:
"""
    Crea dos variables utilizando los objetos fecha (date o semejante) de tu lenguaje:
        *La primera que represente la fecha (dia, mes, año, hora, minuto, segundo)
        *La segunda que represente tu fecha de nacimiento 
    Calcular cuántod años han transcurrido entre ambas fechas
"""

import datetime

today = datetime.datetime.now()
born_date = datetime.datetime.strptime(
    "1983-09-24 06:26:00", "%Y-%m-%d %H:%M:%S")


print(f"\n Today is: {today}")
print(f"\n Aldroide was born in: {born_date}")

year = today.year - born_date.year
print(f"\n Aldroide is {year} years old")


# Dificultad Extra
"""
    Utilizando la fecha de cumpleaños formateala y muestra su resulado 
    de 10 maneras distintas:
        - Día, mes y año.
        - Hora, minuto y segundo.
        - Día de año.
        - Día de la semana.
        - Nombre del mes.
        - (lo que se te ocurra...)
"""
print("\nDificultad Extra")
print(f"""\n
Diffents date formats
1. Year-Month-Day Hrs:Min:Sec   =   {born_date}
2. Day/Month/Year               =   {born_date.strftime("%d/%m/%Y")}
3. Month/Day/Year               =   {born_date.strftime("%m/%d/%Y")}
4. Day/MonthName/Year           =   {born_date.strftime("%d/%B/%Y")}
5. DayName-Dat/MonthName/Year   =   {born_date.strftime("%A-%d/%B/%Y")}
6. Abbreviated                  =   {born_date.strftime("%a-%d-%b-%Y")}
7. DayName-Day-MonthName        =   {born_date.strftime("%a-%d-%b")}
8. Day of the year              =   {born_date.strftime("%j")}
9. Hour(12 format)              =   {born_date.strftime("%I:%M:%S %p")}
10. Hour(24 format)             =   {born_date.strftime("%H:%M:%S")}
11. {born_date.strftime("%A, %dth of %B %Y at %I:%M:%S %p")}
""")
