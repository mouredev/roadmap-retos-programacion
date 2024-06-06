from datetime import datetime

"""
Fechas
"""

now = datetime.now()
my_birhtday = datetime(2003,5, 30, 17,0,0)

difference = now - my_birhtday
print(f"Tengo {difference.days // 365} años")


"""
Extra
"""
# Dia,mes, año
print(my_birhtday.strftime("%d-%m-%y"))
print(my_birhtday.strftime("%d/%m/%Y"))

#Dia
print(my_birhtday.strftime("%a"))

#Dia del año
print(my_birhtday.strftime("%j"))

#Mes
print(my_birhtday.strftime("%h"))

#Mes
print(my_birhtday.strftime("%B"))

#AM/PM
print(my_birhtday.strftime("%p"))

# Representación por defecto del locale
print(my_birhtday.strftime("%x"))
print(my_birhtday.strftime("%c"))

# Numero de la semana
print(my_birhtday.strftime("%W"))