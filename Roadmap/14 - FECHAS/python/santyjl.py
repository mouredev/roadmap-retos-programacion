#14 FECHAS
"""
/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */
"""

from datetime import datetime

fecha_actual = datetime.now()
fecha_nacimiento = datetime(2010 , 1 , 20 , 20 , 17 , 24)

def calcular_diferencia_de_años(actual : datetime , nacimiento : datetime):
    año_1 = actual.year
    año_2 = nacimiento.year

    if año_2 > año_1 :
        return año_2 - año_1

    return año_1 - año_2

años_transcurridos = calcular_diferencia_de_años(fecha_actual , fecha_nacimiento)
print(f"desde tu nacimiento hasta la actualidad han transcurrido : {años_transcurridos}años")

### Extra
print("\Diferentes formas para ver una fecha")

print(datetime.strftime(fecha_nacimiento , "%d/%m/%y")) #dia/mes/año
print(datetime.strftime(fecha_nacimiento , "%H: %M: %S")) #hora:minuto:segundo
print(datetime.strftime(fecha_nacimiento , "%j")) # dia del año
print(datetime.strftime(fecha_nacimiento , "%A")) #dia de la semana
print(datetime.strftime(fecha_nacimiento , "%B")) #mes
print(datetime.strftime(fecha_nacimiento , "%B-%d-%y")) #mes-dia-año
print(datetime.strftime(fecha_nacimiento , "%y/%m/%d")) #año/mes/dia
print(datetime.strftime(fecha_nacimiento , "%A/%B/%H:%M")) #dia_nombre/mes_nombre/hora:minuto

