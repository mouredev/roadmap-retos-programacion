from datetime import datetime

'''
Ejercicio
'''
# Fecha (día, mes, año, hora, minuto, segundo) actual
current_date = datetime.now()
current_date_formatted = current_date.strftime("%d-%m-%Y %H:%M:%S")  # datetime to str
print(current_date_formatted)
print(type(current_date_formatted)) 

birth_date = datetime.strptime("10-10-1993 04:02:03", "%d-%m-%Y %H:%M:%S")  # str to datetime
print(birth_date)
print(type(birth_date))


'''
Ejercicio extra
'''
# Día, mes y año
print("Día, mes y año: " + birth_date.strftime("%d-%m-%Y"))
# Hora, minuto y segundo
print("Hora, minuto y segundo: " + birth_date.strftime("%H:%M:%S"))
# Día de año
print("Día del año: " + str(birth_date.timetuple().tm_yday))  #timetuple() para acceder a distintos datos: año, mes, día, hora, etc.
# Día de la semana
print("Día de la semana: " + str(birth_date.timetuple().tm_wday) + ", " + str(birth_date.strftime("%A")))
# Nombre del mes
print("Nombre del mes: " + str(birth_date.strftime("%B")))

