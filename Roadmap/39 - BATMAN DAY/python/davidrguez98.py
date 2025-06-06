""" /*
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
 */ """

#RETO 1

from datetime import datetime, timedelta

year_of_creation = 1939
anniversary_year = year_of_creation + 85

batman_day_anniversary_dates = []

while anniversary_year <= year_of_creation + 100:

    september = datetime(anniversary_year, 9, 1)

    first_saturday = 5 - september.weekday() if september.weekday() <= 5 else 12 - september.weekday()

    third_saturday = september + timedelta(days=first_saturday + 14)
    
    batman_day_anniversary_dates.append((anniversary_year, anniversary_year - year_of_creation, third_saturday.strftime("%d-%m-%Y")))

    anniversary_year += 1

for year, anniversary, batman_day in batman_day_anniversary_dates:
    print(f"Batman day {year} ({anniversary} aniversario): {batman_day}")

#RETO 2

def sum_subgrid_alerts(sensors, x, y) -> int:

    total = 0

    for x in range(x - 1, x + 2):
        for y in range(y - 1, y + 2):
            for sensor in sensors:
                if sensor[0] == x and sensor[1] == y:
                    total += sensor[2]

    return total


def batcave_security_system(sensors):

    max_alert_level = 0
    max_alert_coordinate = (0,0)
    
    for x in range(1, 19):
        for y in range(1, 19):
            alert_level = sum_subgrid_alerts(sensors, x, y)
            if alert_level > max_alert_level:
                max_alert_level = alert_level
                max_alert_coordinate = (x, y)
    
    distance = abs(max_alert_coordinate[0]) + abs(max_alert_coordinate[1])
    activate_protocol = max_alert_level > 20
    

    return max_alert_coordinate, max_alert_level, distance, activate_protocol

sensors = [
    (1, 5, 9),
    (3, 8, 2),
    (6, 1, 7),
    (9, 4, 5),
    (12, 7, 6),
    (14, 10, 3),
    (17, 13, 9),
    (16, 13, 9),
    (15, 13, 9),
    (19, 15, 4),
    (21, 18, 7),
    (25, 20, 6)
]

result = batcave_security_system(sensors)
print(f"Centro cuadrícula más amenazada: {result[0]}.")
print(f"Máximo nivel de alerta: {result[1]}.")
print(f"Distancia a la Batcueva: {result[2]}.")
print(f"Activar protocolo de seguridad: {result[3]}.")