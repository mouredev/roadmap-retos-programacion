import datetime
fecha_actual= datetime.datetime.now()
fecha_nacimiento = datetime.datetime(2002, 4, 2, 10, 24)  
diferencia = fecha_actual-fecha_nacimiento
print(f"La fech actual es:{fecha_actual}")
print(f"Mi fecha de nacimiento es: {fecha_nacimiento}")
print(f"He vivido: {diferencia.days//365} años")


"""Dificultad extra
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 """

print(f"De mi fecha de nacimiento, el dia es el dia {fecha_nacimiento.day}, del mes {fecha_nacimiento.hour}, y el año fue {fecha_nacimiento.year} ")
print(f"La hora fue a las {fecha_nacimiento.hour} : {fecha_nacimiento.minute} con {fecha_nacimiento.minute} minutos")
print (f"Horario de nacimiento {datetime.datetime.strftime(fecha_nacimiento,'%H : %M : %S')} hs. ") 
print(f"Día de nacimiento: {fecha_nacimiento.strftime('%A')}")
print (f"Día número {datetime.datetime.strftime(fecha_nacimiento, '%j')}")
print (f"Nací en la semana {datetime.datetime.strftime(fecha_nacimiento, '%W')} del año {fecha_nacimiento.year}")
print (f"Mes de nacimiento {datetime.datetime.strftime(fecha_nacimiento, '%B')}")