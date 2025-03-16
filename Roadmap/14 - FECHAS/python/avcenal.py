"""
EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
"""
from datetime import datetime,date

now = datetime.now()
birthdate = datetime(day=19,month=12,year=1984,hour=23,minute=50,second=00)#también se puede hacer datetime(1984,12,19,23,50,00)
diff = abs(now-birthdate)
print(f"La diferencia entre la fecha actual y mi compleaños es: {diff}")

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
"""
weekdays = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
months = ["none","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

print(f"FECHA: {birthdate.day}/{birthdate.month}/{birthdate.year}")
print(f"HORA: {birthdate.timetz()}")
print(f"DÍA DEL AÑO: {birthdate.timetuple()[7]}")
print(f"DÍA DE LA SEMANA: {weekdays[birthdate.weekday()]}")
print(f"MES: {months[birthdate.month]}")
print(f"EN MILISEGUNDOS: {birthdate.timestamp()}")
print(f"INDICANDO LA ZONA HORARIA LOCAL(+1:00 H EN MADRID): {birthdate.astimezone()}")
print(f"EN FORMATO ISO: {birthdate.isoformat()}")
print(f"CADENBA EN LOCAL TIME: {birthdate.ctime()}")
print(f"ORDINAL DESDE EL 1 DE ENERO DEL AÑO 1: {birthdate.toordinal()}")
