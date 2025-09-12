# 39 - Batman Day
from datetime import datetime
import calendar
import random

"""
Ejercicio 1
"""
# Regresa el 
def set_batman_date(year = 2025):
    start = datetime(year=2024,month=9,day=21).date()
    start_aniversary = 85
    target = datetime(year,9,get_weekday(year)).date()
    target_aniversary = start_aniversary + (target.year - start.year)
    print(f"El {target_aniversary}º aniversario es el sábado, {target.strftime("%d/%m/%Y")}")
    return target_aniversary

# Buscador de el puesto(position) de dia buscado (desired_day)(5 es sabado) pero seteado para los valores que estoy buscando
def get_weekday(year, month = 9, position = 3, desired_day = 5):
    calendar_month = calendar.monthcalendar(year, month)
    days = [week[desired_day] for week in calendar_month if week[desired_day] != 0]
    return days[position-1]

# Recuperar todos los aniversarios dando un inicio y el numero de aniversario final
def get_date_to(number = 2024, year_to = 100):
    while True:
        number += 1
        aniversary = set_batman_date(number)
        if aniversary == year_to:
            break

#Ejecutando el codigo
# get_date_to()

"""
Ejercicio 2
"""

values = list(range(0,10))

# Ponderacion cuadratica inversa: peso alto al inicio y bajo al final

weight = [(10 - v)**2 for v in values]

gotham = [[(random.choices(values,weights=weight,k=1))[0] for i in range(20)] for i in range(20)]

for row in gotham:
    print(row)

def is_center(coord: tuple, matrix: list, size = 3):
    offset = size // 2
    if coord[0] in range(0+offset, (len(matrix)-offset)):
        if coord[1] in range(0+offset, (len(matrix[0])-offset)):
            return True
    return False

def get_center_zone(matrix, size = 3):
    zone = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_center((i,j), matrix, size):
                zone.append((i,j))
    
    return zone

center_zone = get_center_zone(gotham,3)

def get_threat_level(mini_matrix):
    threat_level = 0
    for row in mini_matrix:
        threat_level += sum(row)
    return threat_level


def get_submatrix(matrix, center_x, center_y, size = 3):
    offset = size // 2
    submatrix = []
    for i in range(center_x - offset, center_x + offset + 1):
        row = []
        for j in range(center_y - offset, center_y + offset + 1):
            row.append(matrix[i][j])
        submatrix.append(row)
    return submatrix


def threat_to_city(matrix):
    center_zone = get_center_zone(matrix,3)
    emergency_zones = []
    for zone in center_zone:
        submatrix = get_submatrix(matrix,zone[0],zone[1])
        threat_level = get_threat_level(submatrix)
        x,y = zone
        z = threat_level
        emergency_zones.append((x,y,z))
    
    return emergency_zones

def dist_to_baticueva(baticueva: list, zone: list):
    dist = (zone[1] - baticueva[1])+(zone[0] - baticueva[0])
    return dist

def defense_system(x,y,threat_level):
    baticueva = [0,0]
    print(f"Tenemos una situacion en las coordenadas: {x}, {y}")
    print(f"Nivel de peligro: {threat_level}")
    print(f"Distancia de la baticueva a la zona: {dist_to_baticueva(baticueva,[x,y])}")
    print(f"Activar el protocolo de seguridad: {"SI" if threat_level>20 else "NO"}")

zones_levels = threat_to_city(gotham)
top_priority = max(zones_levels,key=lambda x: x[2])
x,y,threat_level = top_priority
defense_system(x,y,threat_level)