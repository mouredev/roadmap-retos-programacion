# Fechas

# Crear una fecha
from datetime import date

hoy = date.today()
print(f'Hoy es: {hoy}')

# Crear una fecha especifica
fecha = date(2024, 2, 18)
print(f'La fecha es: {fecha}')

# Obtener partes de una fecha
hoy = date.today()
print('Año: ', hoy.year)
print('Mes: ', hoy.month)
print('Dia: ', hoy.day)

# Manejar fechas con timedelta
from datetime import timedelta

hoy = date.today()
mañana = hoy + timedelta(days=1)
print(f'Mañana sera: {mañana}')

# Fecha y hora con datetime
from datetime import datetime

ahora = datetime.now()
print(f'Ahora es: {ahora}')

# Fortmatear fechas
from datetime import datetime
ahora = datetime.now()
formato = ahora.strftime('%d-%m-%y %H:%M:%S')
print(f'Fecha y hora formateada: {formato}')


# Convertir una cadena de texto en un objeto datetime
from datetime import datetime
cadena = '2024-2-18 19:50:00'
formato = "%Y-%m-%d %H:%M:%S"
fecha = datetime.strptime(cadena, formato)
print(f'Fecha convertida: {fecha}')


# Ejercicio
from datetime import datetime
from datetime import timedelta

hoy = datetime.now()

cadena_nacimiento = '1996-11-8 20:00:00'
formato_nacimiento = '%Y-%m-%d %H:%M:%S'
nacimiento = datetime.strptime(cadena_nacimiento, formato_nacimiento)

ano_actual = hoy.year
ano_nacimiento = nacimiento.year

tiempo_transcurrido = ano_actual - ano_nacimiento
print(f'Han transcurrido: {tiempo_transcurrido} años.')



# Extra

print(f'Dia: {nacimiento.day}, Mes: {nacimiento.month}, Año: {nacimiento.year}')
print(f'Hora: {nacimiento.hour}, Minuto: {nacimiento.minute}, Segundo: {nacimiento.second}')
print(f'Dia {nacimiento.day} del año {nacimiento.year}')
nombre_mes = nacimiento.strftime('%B')
print(f'Mes de nacimiento: {nombre_mes}')
nombre_dia = nacimiento.strftime('%A')
print(f'Naci el {nombre_dia} {nacimiento.day} de {nombre_mes} de {nacimiento.year}')