from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, "es_ES")


#EJERCICIO

now = datetime.now().replace(microsecond=0)
birth_date = datetime(1969, 2, 27, 20, 10, 5)

years_lived = now.year - birth_date.year
if(now.month, now.day) < (birth_date.month, birth_date.day):
    years_lived -= 1


print(now)
print(birth_date)
print(years_lived)


# EXTRA


# Día, Mes, Año
print(birth_date.strftime("%d / %m / %y"))
print(birth_date.strftime("%d / %m / %Y"))
print(birth_date.strftime("%d de %B de %Y, %U semana del año, %I:%M %p en 12 h"))

# Horas, minutos segundos
print(birth_date.strftime("%H:%M:%S"))

# Día del año de mi nacimiento
print(f"El día del año de mi nac es : {birth_date.strftime("%j")}")

# Día de la semana de  mi nacimiento
print(birth_date.strftime("%A"))

# Nombre del mes
print(birth_date.strftime("%b"))
print(birth_date.strftime("%B"))

# representación por defecto del horario local
print(birth_date.strftime("%c")) # fecha y hora
print(birth_date.strftime("%x")) # solo fecha
print(birth_date.strftime("%X")) # solo h, m y seg

# HORA AM/PM
sufijo = "AM" if birth_date.hour <12 else "PM"
print(f"nací a las : {birth_date.strftime("%I:%M:%S")} {sufijo}")

print("*******************")

# ALTERNATIVA FOR
formatos = {
    "Día, Mes, Año": "%d/%m/%Y",
    "Horas, min y seg" : "%H:%M:%S",
    "Día del año de mi nacimiento" : "%j",
    "Día de la semana de  mi nacimiento" : "%A",
    "Nombre del mes abreviado": "%b",
    "Nombre del mes completo": "%B",
    "Mostrar por defect local fecha y hora": "%c",
    "Mostrar por defect local solo fecha": "%x",
    "Mostrar por defect local solo h,m y s " : "%X",
    "Hora nacimiento am/pm" : "%I:%M:%S %p"
}

for key, formato in formatos.items():
    print(f"{key} :  {birth_date.strftime(formato)} ")
0