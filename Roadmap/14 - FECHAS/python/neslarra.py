"""
 EJERCICIO:
 Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 - Calcular el tiempo transcurrido en segundos entre el comienzo y fin de una tarea.
 Calcula cuántos años han transcurrido entre ambas fechas.

 DIFICULTAD EXTRA (opcional):
 - Me salgo del ejercicio propuesto y muestro un manejo de fechas real hecho para organizar backups.
"""
import locale
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from random import randint
locale.setlocale(locale.LC_TIME, 'es_ES')


print(f"""## Explicación {'#' * 30}""")

print("""
Voy a usar "time" cuando necesite saber tiempos pero NO necesariamente fechas (por ejemplo: calcular el tiempo de ejecución).
Voy a usar "datetime" cuando necesite operar con fechas concretas (por ejemplo: en que día cae la primavera).

from datetime import datetime, timedelta
import time
import locale
locale.setlocale(locale.LC_TIME, 'es_ES')


t1 = time.time()

time.sleep(3)

print(f"La operación tardó {(time.time() - t1).__round__(4)} segundos.")

for m in range(1, 13):
    dia_uno_este_anio = datetime(2024, m, 1)
    dia_uno_anio_anterior = (dia_uno_este_anio - timedelta(days=364)).replace(day=1)
    dia_uno_anio_proximo = (dia_uno_este_anio + timedelta(days=367)).replace(day=1)

    print(f"El primero de {dia_uno_este_anio.strftime('%B')} de {dia_uno_este_anio.strftime('%Y')} cae en {dia_uno_este_anio.strftime('%A')}")
    print(f"El primero de {dia_uno_anio_anterior.strftime('%B')} de {dia_uno_anio_anterior.strftime('%Y')} cae en {dia_uno_anio_anterior.strftime('%A')}")
    print(f"El primero de {dia_uno_anio_proximo.strftime('%B')} de {dia_uno_anio_proximo.strftime('%Y')} cae en {dia_uno_anio_proximo.strftime('%A')}")

    if m == 9:
        primavera_este_anio = dia_uno_este_anio.replace(day=21, month=9)
        print(f"La PRIMAVERA de {primavera_este_anio.strftime('%Y')} empieza en {primavera_este_anio.strftime('%A')}")

        primavera_anio_anterior = dia_uno_anio_anterior.replace(day=21, month=9)
        print(f"La PRIMAVERA de {primavera_anio_anterior.strftime('%Y')} empieza en {primavera_anio_anterior.strftime('%A')}")

        primavera_anio_proximo = dia_uno_anio_proximo.replace(day=21, month=9)
        print(f"La PRIMAVERA de {primavera_anio_proximo.strftime('%Y')} empieza en {primavera_anio_proximo.strftime('%A')}")

Va a mostrar:

""")
t1 = time.time()

time.sleep(3)

print(f"La operación tardó {(time.time() - t1).__round__(4)} segundos.")

for m in range(1, 13):
    dia_uno_este_anio = datetime(2024, m, 1)
    dia_uno_anio_anterior = (dia_uno_este_anio - timedelta(days=364)).replace(day=1)
    dia_uno_anio_proximo = (dia_uno_este_anio + timedelta(days=367)).replace(day=1)

    print(f"El primero de {dia_uno_este_anio.strftime('%B')} de {dia_uno_este_anio.strftime('%Y')} cae en {dia_uno_este_anio.strftime('%A')}")
    print(f"El primero de {dia_uno_anio_anterior.strftime('%B')} de {dia_uno_anio_anterior.strftime('%Y')} cae en {dia_uno_anio_anterior.strftime('%A')}")
    print(f"El primero de {dia_uno_anio_proximo.strftime('%B')} de {dia_uno_anio_proximo.strftime('%Y')} cae en {dia_uno_anio_proximo.strftime('%A')}")

    if m == 9:
        primavera_este_anio = dia_uno_este_anio.replace(day=21, month=9)
        print(f"La PRIMAVERA de {primavera_este_anio.strftime('%Y')} empieza en {primavera_este_anio.strftime('%A')}")

        primavera_anio_anterior = dia_uno_anio_anterior.replace(day=21, month=9)
        print(f"La PRIMAVERA de {primavera_anio_anterior.strftime('%Y')} empieza en {primavera_anio_anterior.strftime('%A')}")

        primavera_anio_proximo = dia_uno_anio_proximo.replace(day=21, month=9)
        print(f"La PRIMAVERA de {primavera_anio_proximo.strftime('%Y')} empieza en {primavera_anio_proximo.strftime('%A')}")

print(f"\n\n## Dificultad extra  {'#' * 30}", end="\n\n")


def log_task(funcion):
    def wrapper(*args, **kwargs):
        argumentos = ""
        for arg in args:
            argumentos += arg + " "
        print(f"BEGIN {funcion.__name__} - {argumentos} - Lanzado a las {datetime.now().strftime('%H:%M:%S')}", end="\n\t")
        inicio = time.time()
        funcion(*args, **kwargs)
        duracion = (time.time() - inicio).__round__(2)
        print(f"END {funcion.__name__} - {argumentos} / duró: {duracion} segundos - Terminó a las {datetime.now().strftime('%H:%M:%S')}", end="\n\n")

    return wrapper


@log_task
def mi_funcion(mensaje: str):
    print(mensaje)
    time.sleep(randint(1, 10))


def calcula_fechas_backup(fecha_ultima_ejecucion: datetime, tipo_backup: str):
    # Calcula las fechas de habiilitación/deshabilitación de backup de tipo MENSUAL / DIARIO

    dia_referencia = (datetime.now() + timedelta(days=1)).replace(hour=0, minute=0, second=0)

    # los backup están divididos en dos grupos: "expira jueves = 0" y "expira viernes = 1"
    grupo = 0
    if fecha_ultima_ejecucion.strftime('%a') in ['Fri', 'Vie']:
        grupo = 1

    fecha_primero_de_mes = (fecha_ultima_ejecucion.replace(day=1) + timedelta(days=32)).replace(day=1, hour=0, minute=0, second=0)
    dia_primero_de_mes = fecha_primero_de_mes.strftime('%A').capitalize()
    fecha_primero_de_mes_prox = (fecha_ultima_ejecucion.replace(day=1) + timedelta(days=64)).replace(day=1, hour=0, minute=0, second=0)
    dia_primero_de_mes_prox = fecha_primero_de_mes_prox.strftime('%A').capitalize()
    fecha_habilitar = dia_referencia
    fecha_deshabilitar = dia_referencia

    # la regla es moverse al viernes anterior al proximo primero de mes (y sumar el valor de grupo)
    # el backup DIARIO debe estar deshabilitado durante el período de corrida del MENSUAL
    # proximo primero de mes = [mensual habilita viernes anterior al primero de mes siguiente,
    #                           mensual deshabilita jueves siguiente,
    #                           diario habilita viernes post mensual,
    #                           diario deshabilita jueves anterior al primero de mes subsiguiente]
    offsets = {
        "Monday":    [-3, 3, 4, -4], "Lunes":     [-3, 3, 3, -3],
        "Tuesday":   [-4, 2, 3, -5], "Martes":    [-4, 2, 2, -4],
        "Wednesday": [-5, 1, 2, -6], "Miercoles": [-5, 1, 1, -5], "Miércoles": [-5, 1, 1, -5],
        "Thursday":  [-6, 0, 1, -7], "Jueves":    [-6, 0, 0, -6],
        "Friday":    [0, 6, 7, -1],  "Viernes":   [0, 6, 6,  0],
        "Saturday":  [-1, 5, 6, -2], "Sabado":    [-1, 5, 5, -1], "Sábado":    [-1, 5, 5, -1],
        "Sunday":    [-2, 4, 5, -3], "Domingo":   [-2, 4, 4, -2]
    }

    if tipo_backup == 'MENSUAL':
        fecha_habilitar = fecha_primero_de_mes + timedelta(days=offsets[dia_primero_de_mes][0] + grupo)
        fecha_deshabilitar = fecha_primero_de_mes + timedelta(days=offsets[dia_primero_de_mes][1] + grupo)
    elif tipo_backup == 'DIARIO':
        fecha_habilitar = fecha_primero_de_mes + timedelta(days=offsets[dia_primero_de_mes][2] + grupo)
        fecha_deshabilitar = fecha_primero_de_mes_prox + timedelta(days=offsets[dia_primero_de_mes_prox][3] + grupo)

    return fecha_habilitar, fecha_deshabilitar


print("Calculo mi edad al día de hoy:")
dia_nacimiento = datetime.strptime("23031965141547", "%d%m%Y%H%M%S")
print(f"Nací un {dia_nacimiento.strftime('%A %d de %B de %Y a las %H:%M:%S')}", end=". ")
print(f"Tengo {((datetime.now() - dia_nacimiento).days/365).__trunc__()} años.")
print(f"Si me jubilo a los 70 años será {(dia_nacimiento + relativedelta(years=70)).strftime('%A %d de %B de %Y')}", end="\n\n")

print("Calculo el tiempo de ejecución de un par de tareas:")
mi_funcion("Mandando algo primero")
mi_funcion("Mandando otra cosa después")

print("Calculo los días de habilitación/deshabilitación de backups:")
tipo_backup = "MENSUAL"
fecha_expiracion_anterior = datetime.strptime("20240404", "%Y%m%d")
fechas_backup = calcula_fechas_backup(fecha_expiracion_anterior, tipo_backup)
print(f"Expiración anterior del {tipo_backup}: {fecha_expiracion_anterior.strftime('%A %d-%m-%Y')}")
print(f"Habilito el {tipo_backup} {fechas_backup[0].strftime('%A %c')}  -  Deshabilito el día {fechas_backup[1].strftime('%A %d de %B del %y a las %H:%M:%S')}")

tipo_backup = "DIARIO"
fecha_expiracion_anterior -= timedelta(days=7)
fechas_backup = calcula_fechas_backup(fecha_expiracion_anterior, tipo_backup)
print(f"Expiración anterior del {tipo_backup}: {fecha_expiracion_anterior.strftime('%A %d-%m-%Y')}")
print(f"Habilito el {tipo_backup} {fechas_backup[0].strftime('%A %c')}  -  Deshabilito el día {fechas_backup[1].strftime('%A %d de %B del %y a las %H:%M:%S')}", end="\n\n")

tipo_backup = "MENSUAL"
fecha_expiracion_anterior = datetime.strptime("20240502", "%Y%m%d")
fechas_backup = calcula_fechas_backup(fecha_expiracion_anterior, tipo_backup)
print(f"Expiración anterior del {tipo_backup}: {fecha_expiracion_anterior.strftime('%A %d-%m-%Y')}")
print(f"Habilito el {tipo_backup} {fechas_backup[0].strftime('%A %c')}  -  Deshabilito el día {fechas_backup[1].strftime('%A %d de %B del %y a las %H:%M:%S')}")

tipo_backup = "DIARIO"
fecha_expiracion_anterior -= timedelta(days=7)
fechas_backup = calcula_fechas_backup(fecha_expiracion_anterior, tipo_backup)
print(f"Expiración anterior del {tipo_backup}: {fecha_expiracion_anterior.strftime('%A %d-%m-%Y')}")
print(f"Habilito el {tipo_backup} {fechas_backup[0].strftime('%A %c')}  -  Deshabilito el día {fechas_backup[1].strftime('%A %d de %B del %y a las %H:%M:%S')}")
