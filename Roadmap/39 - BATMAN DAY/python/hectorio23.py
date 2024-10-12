# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

#################################################3
##################### RETO 1 #####################
##################################################

from datetime import datetime, timedelta

def calculate_batman_day():
    current_year = datetime.now().year
    for year in range(current_year, 2039):  # Desde el año actual hasta el 100 aniversario
        september_first = datetime(year, 9, 1)
        third_saturday = september_first + timedelta(days=(5 - september_first.weekday()) % 7 + 14)
        print(f"Batman Day {year}: {third_saturday.strftime('%Y-%m-%d')}")

calculate_batman_day()


#################################################3
##################### RETO 2 #####################
##################################################

import math

def batcave_security_system(sensors):
    grid_size = 20
    threshold = 20
    max_threat = 0
    critical_area = None

    # Analizar todas las áreas de 3x3 en la cuadrícula
    for i in range(grid_size - 2):
        for j in range(grid_size - 2):
            threat_sum = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    threat_sum += sensors.get((x, y), 0)
            
            if threat_sum > max_threat:
                max_threat = threat_sum
                critical_area = (i + 1, j + 1)  # Centro de la cuadrícula

    # Calcular distancia desde la Batcueva (0, 0)
    if critical_area:
        distance = abs(critical_area[0]) + abs(critical_area[1])
        print(f"Área más amenazada: {critical_area}, Amenazas: {max_threat}, Distancia a la Batcueva: {distance}")
        if max_threat > threshold:
            print("Protocolo de seguridad activado.")

# Ejemplo de sensores
sensors = {
    (5, 5): 8, (5, 6): 7, (5, 7): 6,
    (6, 5): 9, (6, 6): 5, (6, 7): 4,
    (7, 5): 3, (7, 6): 2, (7, 7): 10,
}
batcave_security_system(sensors)
