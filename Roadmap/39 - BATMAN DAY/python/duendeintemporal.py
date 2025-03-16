#39 { Retos para Programadores } BATMAN DAY

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
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

"""

log = print

import datetime
import time

# First Challenge

def calculate_batman_day():
    start_year = 1939  # Year Batman was created
    end_year = 2039    # 100th anniversary
    batman_days = []

    for year in range(start_year, end_year + 1):
        batman_days.append(datetime.date(year, 9, 15))  # 9 represents September
    return batman_days

bat_days = calculate_batman_day()
for bd in bat_days:
    log(bd)

# Second Challenge

def security_system(sensors):
    threshold = 20
    grid_size = 20
    max_threat = 0
    best_coordinate = None

    # Function to calculate the sum of threats in a 3x3 grid
    def calculate_threat_sum(x, y):
        sum_threat = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx = x + i
                ny = y + j
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    sensor = next((s for s in sensors if s['x'] == nx and s['y'] == ny), None)
                    if sensor:
                        sum_threat += sensor['threatLevel']
        return sum_threat

    # Evaluate each sensor
    for sensor in sensors:
        threat_sum = calculate_threat_sum(sensor['x'], sensor['y'])
        if threat_sum > max_threat:
            max_threat = threat_sum
            best_coordinate = {'x': sensor['x'], 'y': sensor['y']}

    # Calculate distance to the Batcave
    distance = abs(best_coordinate['x']) + abs(best_coordinate['y']) if best_coordinate else 0
    activate_protocol = max_threat > threshold

    if activate_protocol:
        log(f"There's a potential risk level at X: {best_coordinate['x']} and Y: {best_coordinate['y']} coords, "
              f"at {distance} meters of the Batcave. The Secure System Protocol is activated. "
              "It could be dangerous for any intruder.\n")
        log("Speakers Sound in the Batcave: You'll be wishing to better not disturb the Bat rest!")
    else:
        log(f"The biggest risk is at {best_coordinate}, at {distance} meters of the Batcave. "
              "It isn't considered too high to activate the Secure System Protocol.")

    log(f'coordinate: {best_coordinate}, threatSum: {max_threat}, distance: {distance}, activateProtocol: {activate_protocol}')

    return {
        'coordinate': best_coordinate,
        'threatSum': max_threat,
        'distance': distance,
        'activateProtocol': activate_protocol
    }

# Example usage
sensors = [
    {'x': 0, 'y': 0, 'threatLevel': 7},
    {'x': 0, 'y': 1, 'threatLevel': 2},
    {'x': 1, 'y': 0, 'threatLevel': 8},
    {'x': 1, 'y': 1, 'threatLevel': 3},
    {'x': 2, 'y': 2, 'threatLevel': 4},
    {'x': 1, 'y': 2, 'threatLevel': 6},
    {'x': 2, 'y': 1, 'threatLevel': 4},
    {'x': 2, 'y': 3, 'threatLevel': 5},
    {'x': 3, 'y': 2, 'threatLevel': 7},
    {'x': 3, 'y': 3, 'threatLevel': 9},
    # Add more sensors as needed
]

log(security_system(sensors))

# Simulate the alert after 2 seconds
time.sleep(2)
log('Retosparaprogramadores #39.')

"""
Output:

Dates from: 1939-09-15 to 2039-09-15

There's a potential risk level at X: 2 and Y: 2 coords, at 4 meters of the Batcave. The Secure System Protocol is activated. It could be dangerous for any intruder.

Speakers Sound in the Batcave: You'll be wishing to better not disturb the Bat rest!
coordinate: {'x': 2, 'y': 2}, threatSum: 38, distance: 4, activateProtocol: True
{'coordinate': {'x': 2, 'y': 2}, 'threatSum': 38, 'distance': 4, 'activateProtocol': True}

"""
