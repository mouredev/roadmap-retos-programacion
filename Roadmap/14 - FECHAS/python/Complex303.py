"""
FECHAS
"""

# Importamos la clase datetime del módulo datetime
from datetime import datetime

# Obtenemos la fecha y hora actual del sistema
now = datetime.now()

# Creamos un objeto datetime con una fecha y hora específica: 16 de febrero de 2001 a la 1:34:00 AM
birth_date = datetime(2001, 2, 16, 1, 34, 0)

# Mostramos en pantalla la fecha y hora actual
print(f"Fecha actual: {now}")

# Mostramos en pantalla la fecha y hora de nacimiento
print(f"Fecha de cumpleaños:  {birth_date}")

# Calculamos la diferencia entre la fecha actual y la fecha de nacimiento
differencia = now - birth_date

# Imprimimos el tipo de dato que devuelve esa resta (es un objeto 'timedelta')
print(type(differencia))  # <class 'datetime.timedelta'>

# Mostramos los años cumplidos dividiendo los días transcurridos entre 365
# (Nota: esto es una aproximación porque no toma en cuenta los años bisiestos)
print(f"Tengo {differencia.days // 365} años")


#Para bases de datos y programación: YYYY-MM-DD
#Para mostrar a usuarios hispanohablantes: DD/MM/YYYY

""" * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)"""

# Día-Mes-Año (año en dos dígitos)
print(birth_date.strftime("%d-%m-%y"))  # Ej: 16-02-01

# Día-Mes-Año (año en cuatro dígitos)
print(birth_date.strftime("%d-%m-%Y"))  # Ej: 16-02-2001

# Horas, minutos y segundos en formato de 24 horas
print(birth_date.strftime("%H:%M:%S"))  # Ej: 01:34:00

# Día del año (número de 001 a 366)
print(birth_date.strftime("%j"))        # Ej: 047 (porque 16 de febrero es el día 47 del año)

# Día de la semana completo
print(birth_date.strftime("%A"))        # Ej: Friday

# Día de la semana abreviado
print(birth_date.strftime("%a"))        # Ej: Fri

# Nombre del mes abreviado
print(birth_date.strftime("%h"))        # Ej: Feb

# Nombre completo del mes
print(birth_date.strftime("%B"))        # Ej: February

# Representación local por defecto (fecha y hora completa en formato regional)
print(now.strftime("%c"))               # Ej: Thu May 15 22:30:00 2025

# Solo la fecha en formato local
print(birth_date.strftime("%x"))        # Ej: 02/16/01 (depende de la configuración regional)

# Solo la hora en formato local
print(now.strftime("%X"))               # Ej: 22:30:00

# AM o PM
print(now.strftime("%p"))               # Ej: PM


# Año solo (dos dígitos)
print(birth_date.strftime("%y"))  # Ej: 01

# Año solo (cuatro dígitos)
print(birth_date.strftime("%Y"))  # Ej: 2001

# Mes solo (número)
print(birth_date.strftime("%m"))  # Ej: 02

# Día del mes (número)
print(birth_date.strftime("%d"))  # Ej: 16

# Hora en formato 12 horas
print(birth_date.strftime("%I:%M %p"))  # Ej: 01:34 AM

# Hora en formato 24 horas
print(birth_date.strftime("%H:%M"))     # Ej: 01:34

# Nombre corto del mes
print(birth_date.strftime("%b"))        # Ej: Feb

# Número de la semana del año (domingo como primer día de la semana)
print(birth_date.strftime("%U"))        # Ej: 06

# Número de la semana del año (lunes como primer día de la semana)
print(birth_date.strftime("%W"))        # Ej: 07


#strftime (string format time) convierte un objeto datetime a un string con el formato que tú le indiques.
#strptime (string parse time) convierte un string con una fecha y hora a un objeto datetime, usando el formato que tú le indiques
