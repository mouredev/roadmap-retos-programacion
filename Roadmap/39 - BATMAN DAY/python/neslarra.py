"""
 EJERCICIO:
 Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
 ¡Y este año cumple 85 años! Te propongo un reto doble:

 RETO 1:
 Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
 su 100 aniversario.

 RETO 2:
 Crea un programa que implemente el sistema de seguridad de la Batcueva. 
 Este sistema está diseñado para monitorear múltiples sensores distribuidos
 por Gotham, detectar intrusos y activar respuestas automatizadas. 
 Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
 que procese estos datos para tomar decisiones estratégicas.
 Requisitos:
 - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 - Cada sensor se identifica con una coordenada (x, y) y un nivel
   de amenaza entre 0 a 10 (número entero).
 - Batman debe concentrar recursos en el área más crítica de Gotham.
 - El programa recibe un listado de tuplas representando coordenadas de los 
   sensores y su nivel de amenaza. El umbral de activación del protocolo de
   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 Acciones: 
 - Identifica el área con mayor concentración de amenazas
   (sumatorio de amenazas en una cuadrícula 3x3).
 - Si el sumatorio de amenazas es mayor al umbral, activa el 
   protocolo de seguridad.
 - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
   sus amenazas, la distancia a la Batcueva y si se debe activar el
   protocolo de seguridad.
"""
from datetime import datetime as dt, timedelta as td
from random import randint


def batman_day() -> None:
    anniversary = 75
    for year in range(2024, 2050):
        sep_fst = dt.strptime(str(year) + "-09-01", "%Y-%m-%d")
        # Batman's day is celebrated every 3rd Saturday of September
        days = 20 - int(sep_fst.strftime("%w"))
        bat_day = sep_fst + td(days=days)
        print(f"Batman celebrates its {anniversary}th anniversary on  {bat_day.strftime('%A %B %d, %Y')}")
        anniversary += 1


def gotham_map() -> list:
    map_ = []
    for x in range(0, 20, 3):
        for y in range(0, 20, 3):
            # The 20x20 map is divided in 3x3 blocks (and the block's center is the fourth pos)
            map_.append(((x, y), (x, y + 1), (x, y + 2), (x + 1, y), (x + 1, y + 1), (x + 1, y + 2), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)))
    return map_


def gotham_sensors() -> list:
    menaces_map = []
    for x in range(0, 49):
        menaces_map.append((randint(0, 10), [randint(0, 19), randint(0, 19)]))
    return menaces_map


def system_monitor(map_, sensors) -> list:

    def get_block(coord: tuple) -> int:
        # look for the block containing the alerted coord
        for ind, block in enumerate(map_):
            if tuple(coord) in block:
                return ind
        return -1

    level_alert = dict()
    for sensor in sensors:
        block = get_block(sensor[1])
        level_alert[block] = sensor[0] if block not in level_alert.keys() else level_alert[block] + sensor[0]
    return [(block, level) for block, level in level_alert.items() if level >= 20]


def calculate_distance(coord: tuple) -> float:
    return pow(pow(coord[0], 2) + pow(coord[1], 2), 0.5).__round__(2)


def max_alert(alerted_blocks: list) -> list:
    if alerted_blocks.__len__() == 1:
        return alerted_blocks
    maximal_alert = max([y for y in alerted_blocks[1]])
    return [x for x in alerted_blocks if x[1] == maximal_alert]


def activate_protocol(alerted_blocks: list) -> bool:
    activated = False
    for alert in max_alert(alerted_blocks):
        print(f"\nAlert Level: {alert[1]} / Distance from batcave to coord {gotham[alert[0]][4]} = {calculate_distance(gotham[alert[0]][4])}")
        activated = True
        break
    return activated


batman_day()
gotham = gotham_map()
while True:
    sensors = gotham_sensors()
    alerted_blocks = system_monitor(gotham, sensors)
    if alerted_blocks:
        if activate_protocol(alerted_blocks):
            print("To the Batmobile, Robin.")
            break
        else:
            print("\nNo alert rises over the minimal level of risk => police can be in charge.")
    else:
        print("\nAll quiet on Gotham.")
    print("Keep tracking.")
