# @Author Daniel Grande (Mhayhemn)


# EJERCICIO:
# Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
# ¡Y este año cumple 85 años! Te propongo un reto doble:
#
# RETO 1:
# Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
# su 100 aniversario.
#
# RETO 2:
# Crea un programa que implemente el sistema de seguridad de la Batcueva. 
# Este sistema está diseñado para monitorear múltiples sensores distribuidos
# por Gotham, detectar intrusos y activar respuestas automatizadas. 
# Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
# que procese estos datos para tomar decisiones estratégicas.
# Requisitos:
# - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
# - Cada sensor se identifica con una coordenada (x, y) y un nivel
#   de amenaza entre 0 a 10 (número entero).
# - Batman debe concentrar recursos en el área más crítica de Gotham.
# - El programa recibe un listado de tuplas representando coordenadas de los 
#   sensores y su nivel de amenaza. El umbral de activación del protocolo de
#   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
# Acciones: 
# - Identifica el área con mayor concentración de amenazas
#   (sumatorio de amenazas en una cuadrícula 3x3).
# - Si el sumatorio de amenazas es mayor al umbral, activa el 
#   protocolo de seguridad.
# - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
#   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
# - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
#   sus amenazas, la distancia a la Batcueva y si se debe activar el
#   protocolo de seguridad.


"""    RETO BATMAN DAY     """

from datetime import date
import locale

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")


"""_summary_
    calculated which day of the week batman day will fall on over a peroid of years
    
    _args_
    None
    
    _return_
    None
"""
def batman_day_100th():
    anniversary = 85
    for year in range(2024, 2040):
        first_day_september = date(year, 9, 1).weekday()
        days_to_saturday = 5 - first_day_september
        if days_to_saturday < 0:
            days_to_saturday += 7
        first_saturday = days_to_saturday + 1
        third_saturday = first_saturday + 14
        batman_day = date(year, 9, third_saturday)
        print(f"El {anniversary} aniversario del batman day sera el {batman_day.day} {batman_day.strftime("%A")} de {batman_day.strftime("%B")} del año {batman_day.strftime("%Y")}.")
        anniversary += 1


"""    RETO BATCUEVA     """
import random

"""_summary_
    grid creation
    
    create grid with X number of row an X number of columns and initial crime rate of 0
    
    _args_
    size (int) grid size (size x size)
    
    _returns_
    crated list
"""
def create_gotham(size: int) -> list:
    gotham = [[(x, y, random.randint(0, 10)) for x in range(size)] for y in range(size)] 
    return gotham

"""_summary_
    creation of a 3x3 grid
    
    _args_ 
    gotham map (array) coordinates (center_x, center_y)
    
    _returns_
    array whit 9 elements
"""
def get_submarix(array: list, center_x: int, center_y: int) -> list:
    grid_areas = []
    for x in range(center_x - 1, center_x + 2):
        for y in range(center_y - 1, center_y + 2):
            grid_areas.append(array[y][x])
    return grid_areas

"""_summary_
    calculate crime index of a 3x3 grid
    
    _args_
    3x3 grid (array)
    
    _returns_
    total crime rate
"""
def sum_grid_areas(array: list) -> int:
    total = sum(cell[2] for cell in array)
    return total

"""_summary_
    calculate the distance between bat cave (0, 0) to center of 3x3 grid whit most crime rate
    
    _args_
    coordinates of center cell (x, y)
    
    _returns_
    absolute sum of crime rates
"""
def calculate_distance( x: int, y:int) -> int:
    return abs(x) + abs(y)


"""_summary_
    main app, obtains the data provided to the functions
    
    _args_
    number for matrix size (int)
    
    _returns_
    report whit data obtained in the each functions
"""
def main_loop(num: int) -> str:
    gotham = create_gotham(num)
    security_protocol = False
    security_protocol_index = 20
    most_dangerous_cell = None
    max_crime_index = 0
    for x in range(1, num - 1):
        for y in range(1, num - 1):
            submatrix = get_submarix(gotham, x, y)
            total = sum_grid_areas(submatrix)
            if total > max_crime_index:
                max_crime_index = total
                most_dangerous_cell = gotham[y][x]
    if max_crime_index > security_protocol_index:
        security_protocol = True
    distance = calculate_distance(most_dangerous_cell[0], most_dangerous_cell[1])
    return (f"Centro de la cuadricula mas amenazada: {most_dangerous_cell}.\n"
        f"Nivel máximo de alerta: {max_crime_index}.\n"
        f"Distancia desde la Bat cueva: {distance}.\n"
        f"Activar protocolo de seguridad: {security_protocol}.")