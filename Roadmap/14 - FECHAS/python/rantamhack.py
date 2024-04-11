'''
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (dia, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuantos años han transcurrido entre ambas fechas.
'''

print("\n\n=======================================EJERCICIO=======================================\n\n")

from datetime import datetime

now = datetime.now()
print(f"\nLa fecha en el momento actual es: {now}")

birth_date = datetime(1962, 7, 9, 19, 15, 00)
print(f"\nLa fecha de nacimiento de Rantam fue: {birth_date}")

def edad():
    age = now.year - birth_date.year
    print(f"\n La edad actual de rantam es: {age}")
    
edad() 


 
'''
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formateala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Dia, mes y año.
 * - Hora, minuto y segundo.
 * - Dia de año.
 * - Dia de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
'''

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


print(f"\nLa fecha de nacimiento de Rantam fue:")

print(f"\n\t 1.- Usando el formato por defecto de  ('AÑO-MES-DIA  HORA-MINUTO-SEGUNDO'): {birth_date}")
print(f"\n\t 2.- usando formato con textos: {birth_date.ctime()}")
print(f"\n\t 3.- Usando dia, mes y año: {birth_date.strftime('%d/%m/%Y')}")
print(f"\n\t 4.- Usando hora, minuto y segundo: {birth_date.strftime('%H:%M:%S')}")
print(f"\n\t 5.- Dia del año: {birth_date.strftime('%j')}")
print(f"\n\t 6.- Dia de la semana: {birth_date.strftime('%A')}")
print(f"\n\t 7.- Mes de nacimiento: {birth_date.strftime('%B')}")
print(f"\n\t 8.- Numero de semana del año: {birth_date.strftime('%U')}")
print(f"\n\t 9.- Dia de la semana, mes, dia,  numero de semana y año en texto: {birth_date.strftime('%A, %B %d, week %U of the year %Y')}")
print(f"\n\t10.- Hora de nacimiento en formato 12 horas: {birth_date.strftime('%I:%M:%S%p')}")











