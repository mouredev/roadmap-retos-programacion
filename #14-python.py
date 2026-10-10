''' EJERCICIO:
* Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
* - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
* - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
* Calcula cuántos años han transcurrido entre ambas fechas.
*
'''

from datetime import datetime, date

Hoy = datetime.now()
print(type(Hoy))
print(Hoy)

Nacimiento = datetime(1966, 6, 3, 12, 0, 0)
print(type(Nacimiento))
print(Nacimiento)

Periodo = Hoy - Nacimiento
print(type(Periodo))
edad = Periodo.days//365
print(f"Mi edad {edad}")

print ("*" * 60)










''' 
* DIFICULTAD EXTRA (opcional):
* Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
* 10 maneras diferentes. Por ejemplo:
* - Día, mes y año.
* - Hora, minuto y segundo.
* - Día de año.
* - Día de la semana.
* - Nombre del mes.
* (lo que se te ocurra...)
'''
Nacimiento = datetime.strptime("03--06--1966","%d--%m--%Y").date()
print(type(Nacimiento))
print(Nacimiento)

Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%D-%M-%Y")
print(type(Nacimiento))
print(Nacimiento)

Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%H:%M:%S")
print(Nacimiento)
Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%A")
print(Nacimiento)
Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%c")
print(Nacimiento)
Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%x")
print(Nacimiento)
Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%X")
print(Nacimiento)
Nacimiento = datetime(1966, 6, 3, 12, 0, 0).strftime("%p")
print(Nacimiento)
Nacimiento = datetime(1966, 6, 3, 12, 0, 0).
print(type(Nacimiento))
print(Nacimiento)