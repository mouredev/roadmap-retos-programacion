from datetime import datetime
import calendar

ahora = datetime.now()
nac = datetime(1994, 3, 27, 11, 32, 16)
print(f"han pasado {(ahora.year - nac.year)} años")

#!Extra

print(f"{nac.year}/{nac.month}/{nac.day}")
print(f"{nac.day}/{nac.month}/{nac.year}")
print(f"{nac.year}/{nac.month}")
print(f"{nac.hour}:{nac.minute}")
print(f"{nac.minute}:{nac.second}")
print(f"{nac.day}/{nac.month}")
print(nac.strftime("%H:%M %d/%b/%Y"))
print(nac.strftime("%d/%b"))
print(f"son las: {ahora.strftime('%H:%M')}")
print(f"naci el: {calendar.day_name[calendar.weekday(nac.year, nac.month, nac.day)]} {nac.day} de {calendar.month_name[nac.month]} de {nac.year}")