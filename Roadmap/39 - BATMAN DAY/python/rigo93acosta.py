'''
/*
 * EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
 * su 100 aniversario.
 *
 * RETO 2:
 * Crea un programa que implemente el sistema de seguridad de la Batcueva. 
 * Este sistema está diseñado para monitorear múltiples sensores distribuidos
 * por Gotham, detectar intrusos y activar respuestas automatizadas. 
 * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
 * que procese estos datos para tomar decisiones estratégicas.
 * Requisitos:
 * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
 * - Cada sensor se identifica con una coordenada (x, y) y un nivel
 *   de amenaza entre 0 a 10 (número entero).
 * - Batman debe concentrar recursos en el área más crítica de Gotham.
 * - El programa recibe un listado de tuplas representando coordenadas de los 
 *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
 *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
 * Acciones: 
 * - Identifica el área con mayor concentración de amenazas
 *   (sumatorio de amenazas en una cuadrícula 3x3).
 * - Si el sumatorio de amenazas es mayor al umbral, activa el 
 *   protocolo de seguridad.
 * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
 *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
 * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
 *   sus amenazas, la distancia a la Batcueva y si se debe activar el
 *   protocolo de seguridad.
 */
'''

# When Saturday 3th Week September
from datetime import datetime, timedelta
import math

## Reto 1
year_of_creation: int = 1939
anniversary: int = year_of_creation + 85
batman_day_ann_dates = []
while anniversary <= year_of_creation + 100:
    september = datetime(anniversary, 9, 1)
    first_saturday = 5 - september.weekday() \
                        if september.weekday() <= 5 \
                        else 12 - september.weekday()
    third_saturday = september + timedelta(days=first_saturday + 14)

    batman_day_ann_dates.append(
        (
            anniversary, 
            anniversary - year_of_creation, 
            third_saturday.strftime("%d-%m-%Y")
        )
    )
    anniversary += 1

for year, anniversary, date in batman_day_ann_dates:
    print(f"Batman Day {anniversary}º Aniversario: {date}")

## Reto 2
sensors = [
    (2, 3, 7),
    (4, 3, 8),
    (2, 2, 7),
    (10, 12, 8),
    (11, 12, 8),
    (10, 11, 8),
    (15, 18, 4)
]

map_gotham = [[0 for _ in range(20)] for _ in range(20)]
threshold = 20
all_alarm = []

def update_map(map_gotham, sensors):
    map_gotham_tmp = map_gotham.copy()
    for x, y, threat in sensors:
        map_gotham_tmp[x][y] = threat
    
    return map_gotham_tmp

def print_map(map_gotham):
    for row in map_gotham:
        print(row)

def sum_subgrid(values):
    values = [value for sublist in values for value in sublist]
    return sum(values)

def select_alarm(alarms):
    alarm = max(alarms, key=lambda x: x[2])
    return alarm

def batcave_security(map_gotham):
    for y in range(1, 19):
        for x in range(1, 19):
            values = [
                map_gotham[y-1][x-1:x+2],
                map_gotham[y][x-1:x+2],
                map_gotham[y+1][x-1:x+2]
            ]
            
            all_alarm.append((y, x, sum_subgrid(values)))
                
    alarm = select_alarm(all_alarm)
    if not alarm:
        print("No hay amenazas.")
    else:
        center_coor = (alarm[0], alarm[1])
        distance = abs(alarm[0]) + abs(alarm[1])
        protocol = "activar" \
                    if alarm[2] > threshold \
                    else "no activar"
             
        print(f"Máxima ameneza en {center_coor}" +\
            f" con {alarm[2]} de amenaza," +\
                f" distancia {distance:.2f} u.a," +\
                f" {protocol} protocolo de seguridad.")

map_gotham = update_map(map_gotham, sensors)   
print_map(map_gotham)
batcave_security(map_gotham)