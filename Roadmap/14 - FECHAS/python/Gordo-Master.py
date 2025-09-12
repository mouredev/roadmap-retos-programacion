# 14 - Fechas

from datetime import datetime, date, time

now = datetime.now()
birthday = datetime(1995,5,8,12,35,17)

age = (now - birthday).days // 365

print(now)
print(birthday)
print(f"Pasaron : {age} años")

"""
Ejercicio extra
"""

print(birthday.strftime(f"%A, %d de %B de %Y"))
print(birthday.strftime(f"%c"))
print(birthday.strftime(f"%x"))
print(birthday.strftime(f"%X"))
print(birthday.strftime(f"%d / %m / %Y"))
print(birthday.strftime(f"%Y / %m / %d"))
print(birthday.strftime(f"%H horas, %M minutos, %S segundos, %p"))
print(birthday.strftime(f"%j día del año %Y"))
print(birthday.strftime(f"%Uº semana del año %Y"))
print(birthday.strftime(f"%Wº semana del año %Y"))
print(birthday.strftime(f"%Vº semana del año %Y"))