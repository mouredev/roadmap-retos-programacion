""" # 39 - Batman Day"""

""" * RETO 1: """
# Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta su 100 aniversario.

""" * RETO 2: """
# Crea un programa que implemente el sistema de seguridad de la Batcueva.
# Este sistema está diseñado para monitorear múltiples sensores distribuidos por Gotham, detectar intrusos y activar respuestas automatizadas.
# Cada sensor reporta su estado en tiempo real, y Batman necesita un programa que procese estos datos para tomar decisiones estratégicas.

""" Requisitos: """
# El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
# Cada sensor se identifica con una coordenada (x, y) y un nivel de amenaza entre 0 a 10 (número entero).
# Batman debe concentrar recursos en el área más crítica de Gotham.
# El programa recibe un listado de tuplas representando coordenadas de los sensores y su nivel de amenaza. El umbral de activación del protocolo de seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).

""" Acciones: """
# Identifica el área con mayor concentración de amenazas (sumatorio de amenazas en una cuadrícula 3x3).
# Si el sumatorio de amenazas es mayor al umbral, activa el protocolo de seguridad.
# Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
# la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
# Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de sus amenazas, la distancia a la Batcueva y si se debe activar el protocolo de seguridad.


""" Reto #1 """
from datetime import datetime, timedelta

year_of_creation = 1939
anniversary_year = year_of_creation + 85

batman_day_anniversary_dates = []

while anniversary_year <= year_of_creation + 100:

    september = datetime(anniversary_year, 9, 1)

    first_saturday = 5 - september.weekday() if september.weekday() <= 5 else 12 - \
        september.weekday()

    third_saturday = september + timedelta(days=first_saturday + 14)

    batman_day_anniversary_dates.append(
        (
            anniversary_year,
            anniversary_year - year_of_creation,
            third_saturday.strftime("%d-%m-%Y")
        )
    )

    anniversary_year += 1

for year, anniversary, batman_day in batman_day_anniversary_dates:
    print(f"Batman day {year} ({anniversary} aniversario): {batman_day}")



""" Reto #2 """
def sistema_seguridad_batcueva(sensores):
    # Inicializar la cuadrícula 20x20 con ceros
    cuadricula_gotham = [[0 for _ in range(20)] for _ in range(20)]
    
    # Poblar la cuadrícula con niveles de amenaza de los sensores
    for x, y, nivel_amenaza in sensores:
        if 0 <= x < 20 and 0 <= y < 20:
            cuadricula_gotham[y][x] = nivel_amenaza
    
    suma_amenazas_maxima = 0
    centro_amenaza_maxima = (0, 0)
    
    # Comprobar cada posible cuadrícula 3x3
    for centro_y in range(1, 19):
        for centro_x in range(1, 19):
            suma_amenazas = 0
            
            # Sumar amenazas en la cuadrícula 3x3 alrededor del centro
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    suma_amenazas += cuadricula_gotham[centro_y + dy][centro_x + dx]
            
            # Actualizar si esta es el área con mayor amenaza
            if suma_amenazas > suma_amenazas_maxima:
                suma_amenazas_maxima = suma_amenazas
                centro_amenaza_maxima = (centro_x, centro_y)
    
    # Calcular distancia desde la Batcueva (0,0) hasta el centro de amenaza
    distancia_a_batcueva = abs(centro_amenaza_maxima[0]) + abs(centro_amenaza_maxima[1])
    
    # Determinar si se debe activar el protocolo de seguridad
    activar_protocolo = suma_amenazas_maxima >= 20
    
    return {
        "centro_amenaza": centro_amenaza_maxima,
        "suma_amenazas": suma_amenazas_maxima,
        "distancia": distancia_a_batcueva,
        "activar_protocolo": activar_protocolo
    }

# Ejemplo de uso:
if __name__ == "__main__":
    # Lista de ejemplo de sensores: (x, y, nivel_amenaza)
    sensores_ejemplo = [
        (5, 5, 8),
        (6, 5, 7),
        (7, 5, 6),
        (5, 6, 5),
        (6, 6, 9),
        (7, 6, 4),
        (5, 7, 3),
        (6, 7, 2),
        (7, 7, 1),
        (10, 15, 10),
        (2, 3, 6)
    ]
    
    resultado = sistema_seguridad_batcueva(sensores_ejemplo)
    
    print("\nInforme del Sistema de Seguridad de la Batcueva:")
    print(f"Área más amenazada: {resultado['centro_amenaza']}")
    print(f"Suma de nivel de amenaza: {resultado['suma_amenazas']}")
    print(f"Distancia desde la Batcueva: {resultado['distancia']}")
    print(f"Protocolo de seguridad activado: {'SÍ' if resultado['activar_protocolo'] else 'NO'}")