from  datetime  import datetime
from datetime import timezone 
import zoneinfo

"""
Ejercicio
"""

#argentina=zoneinfo.ZoneInfo("America/BuenosAires")
#argentina= timezone.tzname()
ahora= datetime.now()
print(ahora.strftime("%c"))


cumpleaños= datetime(1981, 6, 9, 4, 30)
print(cumpleaños)

edad= ahora - cumpleaños

print(f"Tengo {edad.days //365} años")

"""
extra
"""

#Dia, mes, año
print(cumpleaños.strftime("%d %m %y"))
print(cumpleaños.strftime("%d %m %Y"))

#Hora, minutos, segundos
print(cumpleaños.strftime("%H %M %S"))

#dia del año
print(cumpleaños.strftime("%j"))

#dia del año
print(cumpleaños.strftime("%A "))

print(cumpleaños.strftime("%c"))