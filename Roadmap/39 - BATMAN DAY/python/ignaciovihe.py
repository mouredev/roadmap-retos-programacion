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

#Reto 1 Calcular semana Batmanday

import calendar


def get_batman_weeks():
    edition = 85
    for  year in range(2024,2040):
        september = calendar.monthcalendar(year, 9)
        batman_day = september[2][5]
        print(f"En {year}, la {edition} BatmanWeek es día {batman_day} de septiembre.")
        edition += 1

get_batman_weeks()

print("##########################################")
# Reto 2 

from abc import ABC, abstractmethod
from typing import Tuple, Set, Optional

threats = [
    ((5,17),3),
    ((4,7),6),
    ((19,5),8),
    ((8,14),5),
    ((9,13),2),
    ((2,0),9),
    ((15,1),10),
    ((13,14),5),
    ((10,10),7),
    ((2,16),9),
    ((9,19),2),
    ((5,8),9),
    ((9,4),10),
    ((15,16),6),
    ((17,8),6),
    ((2, 3), 7),
    ((4, 3), 8),
    ((2, 2), 7),
    ((10, 12), 8),
    ((11, 11), 8),
    ((10, 11), 8),
    ((15, 18), 4),
    ((12, 11), 1),
]

class IGothamMap(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def get_sensor(self, x: int, y: int):
        pass

    @abstractmethod
    def get_max_threats(self) -> Set[Tuple[int, int]]:
        pass

    @abstractmethod
    def clear_max_threats(self):
        pass

    @abstractmethod
    def add_max_threat(self, coord: Tuple[int,int]):
        pass


class Sensor:
    def __init__(self, local_threat = 0, area_threat = 0, batcave = False) -> None:
        self.local_threat = local_threat
        self.area_threat = area_threat
        self.batcave = batcave


class GothamMap(IGothamMap):
    def __init__(self, gotham_size = 20) -> None:
        self.gotham_size = gotham_size
        self.map = [[Sensor() for _ in range(gotham_size)] for _ in range(gotham_size)]
        self.max_threats = set()
        self.map[0][0].batcave = True

    def get_size(self) -> int:
        return self.gotham_size
    
    def get_sensor(self, x: int, y: int) -> Optional[Sensor]:
        if 0 <= x < self.gotham_size and 0 <= y < self.gotham_size:
            return self.map[x][y]
        return None
    
    def get_max_threats(self) -> Set[Tuple[int, int]]:
        return self.max_threats
    
    def clear_max_threats(self):
        self.max_threats.clear()

    def add_max_threat(self, coord: Tuple[int, int]):
        self.max_threats.add(coord)

    def print_local_threats(self):
        for line in self.map:
            for sensor in line:
                valor = "B" if sensor.batcave else str(sensor.local_threat)
                print(f"{valor:>3}", end=" ")
            print()

    def print_area_threats(self):
        for line in self.map:
            for sensor in line:
                valor = "B" if sensor.batcave else str(sensor.area_threat)
                print(f"{valor:>3}", end=" ")
            print()


class ThreatsManager:
    def __init__(self, gotham_map: IGothamMap) -> None:
        self.gotham_map = gotham_map

    def update_local_threats(self, threats):
        for threat in threats:
            x, y = threat[0]
            sensor = self.gotham_map.get_sensor(x, y)
            if sensor:
                sensor.local_threat = threat[1]
            else:
                print(f"Advertencia: coordenadas inválidas ({x}, {y})")

    def update_area_threats(self):
        max_threat = 0
        size = self.gotham_map.get_size()
        for line_index in range(size):
            for sensor_index in range(size):
                sensor = self.gotham_map.get_sensor(line_index, sensor_index)
                if sensor:
                    sensor.area_threat = 0
                    for x in range(-1,2):
                        for y in range(-1,2):
                            neighbour_x = line_index + x
                            neighbour_y = sensor_index + y
                            if (0 <= (neighbour_x) < size) and (0 <= (neighbour_y) < size):
                                neighbour_sensor = gotham_map.get_sensor(neighbour_x,neighbour_y)
                                if neighbour_sensor:
                                    sensor.area_threat += neighbour_sensor.local_threat

                    if sensor.area_threat >= max_threat:
                        if sensor.area_threat > max_threat:
                            self.gotham_map.clear_max_threats()
                        self.gotham_map.add_max_threat((line_index, sensor_index))
                        max_threat = sensor.area_threat


class SecurityProtocolChecker:
    def __init__(self, gotham_map: IGothamMap) -> None:
        self.gotham_map = gotham_map

    def calculate_distance(self, coordinate):
        return abs(coordinate[0]) + abs(coordinate[1])

    def activate_protocol(self):
        for threat in self.gotham_map.get_max_threats():
            x, y = threat
            sensor = self.gotham_map.get_sensor(x, y)
            if sensor:
                area_threat = sensor.area_threat
                print(f"Centro cuadrícula más amenazada: {threat}.")
                print(f"Máximo nivel de alerta: {area_threat}")
                print(f"Distancia a la Batcueva: {self.calculate_distance(threat)}")
                print(f"Activar protocolo de seguridad: {"Si." if area_threat >= 20 else "No."}")
                print()



gotham_map = GothamMap()
threats_manager = ThreatsManager(gotham_map)
security_protocol_checker = SecurityProtocolChecker(gotham_map)

threats_manager.update_local_threats(threats)
threats_manager.update_area_threats()

gotham_map.print_local_threats()
print()
gotham_map.print_area_threats()
print()

security_protocol_checker.activate_protocol()
