"""
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
"""

# Reto 1
"""
    * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
* su 100 aniversario.
"""
import datetime

class Batday:
    def __init__(self):
        self.aniversario_actual = 85
        self.year = datetime.datetime.now().year 

    def get_batday(self,aniversario):
        print("Batman Weeks")
        print("Aniversario - Dias de la Batman Weeks")
        for year in range(self.aniversario_actual, aniversario+1):
            print(f"{year} - {self.get_days_week(self.year + (year - self.aniversario_actual))}")
            
    def get_days_week(self, year):
        first_day_september = datetime.date(year, 9, 1)
        first_monday_september = first_day_september - datetime.timedelta(days=(7 - first_day_september.weekday()) % 7)
        threerd_week = first_monday_september + datetime.timedelta(days=21)
        batweek_list = [threerd_week + datetime.timedelta(days=i) for i in range(7)]
        batweek_format = [i.strftime("%d/%m/%Y") for i in batweek_list]
        batweek = ", ".join(batweek_format)
        return batweek

# Prueba
reto_1 = Batday()
reto_1.get_batday(100)
print()
# Reto 2
class Batcueva:
    mapa = {}
    sectores_control = {}
    def __init__(self,matriz) -> None:
        mapa = {}
        for sensor in matriz:
            mapa[sensor.x, sensor.y] = sensor
        Batcueva.mapa = mapa

        for x in range(1,19,3):
            for y in range(1,19,3):
                Batcueva.sectores_control[(x,y)] = [
                    (x-1, y-1), (x, y-1), (x+1, y-1),
                    (x-1, y), (x, y), (x+1, y),
                    (x-1, y+1), (x, y+1), (x+1, y+1)
                ]
        
        
    def scan_sectors(self,printeable=False) -> list:
        sectores_criticos = []
        for name, sector in Batcueva.sectores_control.items():
            level = 0
            sub_sections = []
            for sensor_area in sector:
                sensor = Batcueva.mapa[sensor_area]
                area_level = sensor.get_level()
                sub_sections.append((sensor_area, area_level))
                level += area_level

                """
                * - Si el sumatorio de amenazas es mayor al umbral, activa el 
                *   protocolo de seguridad.
                """
                if level >= 20:
                    if (name, level,sub_sections) not in sectores_criticos:
                        sectores_criticos.append((name, level,sub_sections))
            if printeable:
                print(f"Area: {name} sensores: {sector} - Amenaza: {level}")
        return sectores_criticos
    def scan_map(self) -> None:
        """
        * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
        *   sus amenazas, la distancia a la Batcueva y si se debe activar el
        *   protocolo de seguridad.
        """
        print("Iniciando Analisis de Sectores Criticos")
        check = 0
        sectores_criticos = self.scan_sectors()
        sectores_criticos.sort(key=lambda x: x[1], reverse=True)
        
        """
        * - Identifica el área con mayor concentración de amenazas
        *   (sumatorio de amenazas en una cuadrícula 3x3)."""
        if len(sectores_criticos) > 0:
            print("-"*10)
            print(f"Areas Criticas Encontradas: {len(sectores_criticos)}")
            print(f"Area más critica:\nArea:{sectores_criticos[0][0]} - Nivel de amenaza: {sectores_criticos[0][1]}")
            print("-"*10)
            for number, sector in enumerate(sectores_criticos):
                print("-"*5)
                print(f"Activando Medidas de Emergencia {number+1} de {len(sectores_criticos)}")
                print(f"Sector central del area: {sector[0]}")

                """
                * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
                *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada
                """
                print(f"Distancia desde la batcueva: {sector[0][0] + sector[0][1]} cuadrantes")

                print(f"Nivel de amenaza general: {sector[1]}")
                print(f"Sectores amenazados del area {sector[0]}:")
                for num,area in enumerate(sector[2]):
                    print("-"*2)
                    print(f" Sub-area {num+1} : Sensor del sector: {area[0]} - Nivel de amenaza: {area[1]}")
                print(f"Batman esta de camino a {sector[0]}")
        else:
            print("No hay sectores criticos")
            print("Niveles actuales de amenaza:")
            for sector in Batcueva.mapa:
                print(f"Coordenadas: {sector.x}, {sector.y} - {sector.get_level()}")

# Para poder probar el reto he creado esta clase
"""
* - Cada sensor se identifica con una coordenada (x, y) y un nivel
*   de amenaza entre 0 a 10 (número entero).
"""
class Sensor:
    def __init__(self, x, y, level) -> None:
        self.x = x
        self.y = y
        self.__level = level
    def get_level(self):
        return self.__level
    # Para poder cambiar el nivel de amenaza
    def set_level(self, level):
        self.__level = level
    

# Prueba

"""El mapa de Gotham y los sensores se representa con una cuadrícula 20x20"""
matriz = [Sensor(fila, columna, 0) for fila in range(20) for columna in range(20)]

reto_2 = Batcueva(matriz)
x = 1
y = 5
for sensor in Batcueva.mapa.values():
    if sensor.x == x and sensor.y == y:
        sensor.set_level(10)
    if sensor.x == x and sensor.y == y + 1:
        sensor.set_level(10)
    if sensor.x == x - 1 and sensor.y == y:
        sensor.set_level(5)
    if sensor.x == x + 1 and sensor.y == y:
        sensor.set_level(5)
x = 8
y = 3
for sensor in Batcueva.mapa.values():
    if sensor.x == x and sensor.y == y:
        sensor.set_level(10)
    if sensor.x == x and sensor.y == y + 1:
        sensor.set_level(10)
    if sensor.x == x - 1 and sensor.y == y:
        sensor.set_level(5)
    if sensor.x == x + 1 and sensor.y == y:
        sensor.set_level(5)

reto_2.scan_map()