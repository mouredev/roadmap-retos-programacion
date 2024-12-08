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

# Reto 1
from datetime import datetime, timedelta

def calcular_batman_day(anio_inicio, anios):
    batman_days = []
    for i in range(anios):
        anio = anio_inicio + i
        # Encuentra el primer día de la tercera semana de septiembre
        primer_dia_septiembre = datetime(anio, 9, 1)
        tercer_lunes = primer_dia_septiembre + timedelta(days=(14 - primer_dia_septiembre.weekday() + 7) % 7)
        batman_days.append(tercer_lunes)
    return batman_days

# Ejemplo de uso
anio_inicio = 2024
anios = 100 - 85  # Hasta el 100 aniversario
batman_days = calcular_batman_day(anio_inicio, anios)
for dia in batman_days:
    print(dia.strftime("%Y-%m-%d"))


# Reto 2
def calcular_amenaza(sensor_data):
    max_amenaza = 0
    coordenada_max = (0, 0)
    activar_protocolo = False

    for i in range(18):  # 20x20 grid, 3x3 subgrid
        for j in range(18):
            suma_amenaza = sum(sensor_data[x][y] for x in range(i, i+3) for y in range(j, j+3))
            if suma_amenaza > max_amenaza:
                max_amenaza = suma_amenaza
                coordenada_max = (i+1, j+1)
                activar_protocolo = suma_amenaza > 20

    distancia_batcueva = abs(coordenada_max[0] - 1) + abs(coordenada_max[1] - 1)
    return coordenada_max, max_amenaza, distancia_batcueva, activar_protocolo

# Ejemplo de uso
sensor_data = [[0]*20 for _ in range(20)]
# Añadir datos de sensores (coordenada x, y, nivel de amenaza)
sensores = [(5, 5, 8), (6, 6, 7), (7, 7, 6), (8, 8, 9), (9, 9, 10)]
for x, y, amenaza in sensores:
    sensor_data[x][y] = amenaza

coordenada_max, max_amenaza, distancia_batcueva, activar_protocolo = calcular_amenaza(sensor_data)
print(f"Coordenada más amenazada: {coordenada_max}")
print(f"Suma de amenazas: {max_amenaza}")
print(f"Distancia a la Batcueva: {distancia_batcueva}")
print(f"Activar protocolo de seguridad: {'Sí' if activar_protocolo else 'No'}")
