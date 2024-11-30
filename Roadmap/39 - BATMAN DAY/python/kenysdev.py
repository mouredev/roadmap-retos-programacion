# _____________________________________
# https://github.com/kenysdev
# 2024 - Python
# _____________________________________
# 39 BATMAN DAY
# ------------------------------------

"""
* RETO 1:
* Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
* su 100 aniversario.
"""

from datetime import timedelta, date

def third_saturday_of_september(year) -> str:
    d = date(year, 9, 15)
    d += timedelta(days=(5 - d.weekday() + 7) % 7)
    return d.strftime("%d-%m-%Y")

def anniversary_dates(total_anniversarys: int) -> None:
    batman_day_start = 2014
    current_year = date.today().year
    if current_year < batman_day_start:
        print("xd")
        return

    past_anniversaries = current_year - batman_day_start
    print(f"Aniversarios que ya han pasado: {past_anniversaries}")
    
    for i in range(total_anniversarys - past_anniversaries):
        num: int = past_anniversaries + i + 1
        the_date: str = third_saturday_of_september(current_year)
        print(f"- Aniversario #{num}: {the_date}")
        current_year +=1

print("Batman Day")
anniversary_dates(100)

"""
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

def create_map(size: tuple, batcave: tuple, sensors: list, threats: list) -> list:
    gotham: list = [['| '] * 20 for _ in range(20)]
    gotham[batcave[0]][batcave[1]] = '|B'

    for s in sensors:
        gotham[s[0]][s[1]] = '|S'

    for t in threats:
        gotham[t[0]][t[1]] = '|T'

    return gotham

def print_map(gotham: list) -> None:
    print("\nMapa de Gotham:")
    for row in gotham:
        print("".join(map(str, row)))

def scan_map(gotham: list, sensors: list) -> None:
    danger_list = []
    for c, s in enumerate(sensors):
        danger_counter: int = 0
        for i in range(s[0] - 1, s[0] + 2):
            for j in range(s[1] - 1, s[1] + 2):
                if gotham[i][j] == '|T':
                    danger_counter += s[2]
        danger_list.append((c, danger_counter))
    
    max_danger: tuple = max(danger_list, key=lambda x: x[1])
    location: tuple = sensors[max_danger[0]]

    print("\nInforme:")
    print(f"Cuadrícula más amenazada: '{location[0]}, {location[1]}'")
    print(f"Máximo nivel de alerta: '{max_danger[1]}'")
    if max_danger[1] >= 20:
        print("Protocolo de seguridad activado.")
        print(f"Distancia: '{location[0] + location[1]}'")
    else:
        print("No hay amenazas relevantes.")

batcave: tuple = (0, 0)
sensors: list = [(2, 2, 10), (6, 8, 9), (10, 12, 8), (17, 15, 7)]
threats: list = [(2, 3), (2, 1), (6, 9), (17, 16), (15, 4)]
gotham: list = create_map((20, 20), batcave, sensors, threats)
print_map(gotham)
scan_map(gotham, sensors)
