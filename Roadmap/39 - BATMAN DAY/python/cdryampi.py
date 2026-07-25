# /*
#  * EJERCICIO:
#  * Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
#  * ¡Y este año cumple 85 años! Te propongo un reto doble:
#  *
#  * RETO 1:
#  * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
#  * su 100 aniversario.
#  *
#  * RETO 2:
#  * Crea un programa que implemente el sistema de seguridad de la Batcueva. 
#  * Este sistema está diseñado para monitorear múltiples sensores distribuidos
#  * por Gotham, detectar intrusos y activar respuestas automatizadas. 
#  * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
#  * que procese estos datos para tomar decisiones estratégicas.
#  * Requisitos:
#  * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
#  * - Cada sensor se identifica con una coordenada (x, y) y un nivel
#  *   de amenaza entre 0 a 10 (número entero).
#  * - Batman debe concentrar recursos en el área más crítica de Gotham.
#  * - El programa recibe un listado de tuplas representando coordenadas de los 
#  *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
#  *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
#  * Acciones: 
#  * - Identifica el área con mayor concentración de amenazas
#  *   (sumatorio de amenazas en una cuadrícula 3x3).
#  * - Si el sumatorio de amenazas es mayor al umbral, activa el 
#  *   protocolo de seguridad.
#  * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
#  *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
#  * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
#  *   sus amenazas, la distancia a la Batcueva y si se debe activar el
#  *   protocolo de seguridad.
#  */
from datetime import date, timedelta
import locale
import random


class Coordenada():

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y



class Sensor():

    def __init__(self, coordenada: Coordenada, amenaza: int, neutralizado :bool = False, total_amenaza :int = 0) -> None:

        self.amenaza = 0 if amenaza < 0 else amenaza
        self.amenaza = 10 if amenaza > 10 else amenaza
        self.coordenada = coordenada
        self.neutralizado = neutralizado

    def __str__(self) -> str:
        return '📡'

class Gotham():
    # suma absoluta = ∣3−1∣+∣4−1∣=2+3=5
    __superficie = [["🏢" for _ in range(20)] for _ in range(20)]
    __amenazas = []
    __problemas = [
        "El Joker ha colocado bombas en la ciudad",
        "Dos Caras está planeando un ataque en el banco central",
        "El Acertijo ha dejado pistas encriptadas en los edificios",
        "Bane está reclutando mercenarios para controlar Gotham",
        "El Pingüino está traficando armas en los muelles",
        "Hiedra Venenosa ha liberado toxinas en el parque central",
        "Mr. Freeze está congelando zonas de la ciudad",
        "El Espantapájaros está extendiendo su gas del miedo por los barrios",
        "Harley Quinn está preparando una emboscada en el circo",
        "Ra's al Ghul está atacando con la Liga de las Sombras",
        "Man-Bat está atacando desde los cielos",
        "Hush ha infiltrado a sus secuaces entre la policía",
        "El Sombrerero Loco está controlando las mentes de los ciudadanos",
        "Clayface está causando caos en las calles con su transformación",
        "El Tribunal de los Búhos está moviendo sus piezas en la sombra",
    ]

    
    def __init__(self, sensores: list[Sensor]) -> None:
        
        for sensor in sensores:
            self.__superficie[sensor.coordenada.x][sensor.coordenada.y] = sensor
        # por las dudas sí me envían una coordenada 0,0 y nos quedamos sin el Batman.
        self.batman_pos = Coordenada(0,0)
        self.__superficie[self.batman_pos.x][self.batman_pos.y] = '🦇'

    def print_gotham(self) -> None:
        print("Ciudad de Gotham:")
        for barrio in self.__superficie:
            barrio_group = ' '.join([str(calle) for calle in barrio])
            print(barrio_group)


    def cal_amenaza(self) -> None:
        self.__amenazas = []
        for index_x, x in enumerate(self.__superficie):
            for index_y, y in enumerate(x):
                if self.__superficie[index_x][index_y].__str__() == '📡':
                    amenaza = 0
                    
                    # Recorremos los vecinos en un área de 3x3 alrededor del sensor
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            vecino_x = index_x + i
                            vecino_y = index_y + j
                            
                            if 0 <= vecino_x < 20 and 0 <= vecino_y < 20:
                                if self.__superficie[vecino_x][vecino_y].__str__() == '📡' and self.__superficie[vecino_x][vecino_y].neutralizado == False:
                                    try:
                                        amenaza += self.__superficie[vecino_x][vecino_y].amenaza
                                    except AttributeError:
                                        pass
                    if amenaza >= 20 and self.__superficie[index_x][index_y].neutralizado == False:
                        self.__amenazas.append(self.__superficie[index_x][index_y])
                        self.__superficie[index_x][index_y].total_amenaza = amenaza
        
        if len(self.__amenazas) > 0:
            self.neutralizar_amenaza()
        else:
            print("Sin anemazas cercanas...")
            self.print_gotham()

    def neutralizar_amenaza(self) -> None:
        # Neutralizar cada amenaza en la lista de amenazas
        self.__amenazas = sorted(self.__amenazas, key=lambda x: x.total_amenaza, reverse=True)
        print(f"amenazas: {len(self.__amenazas)}")
        while len(self.__amenazas) > 0:
            amenaza = self.__amenazas.pop(0)
            # Neutralizar la amenaza en la superficie
            self.__superficie[amenaza.coordenada.x][amenaza.coordenada.y].amenaza = 0
            self.__superficie[amenaza.coordenada.x][amenaza.coordenada.y].neutralizado = True
            # Guardamos el símbolo actual en la nueva posición (sensor o edificio)
            simbolo_anterior = self.__superficie[amenaza.coordenada.x][amenaza.coordenada.y]

            # Cambiamos la posición actual de Batman a '🏢' (donde estaba antes)
            self.__superficie[self.batman_pos.x][self.batman_pos.y] = '🏢'

            # Temporalmente colocamos el símbolo de Batman en la nueva posición
            self.__superficie[amenaza.coordenada.x][amenaza.coordenada.y] = '🦇'

            # Imprimimos el mapa con Batman en su nueva posición
            
            distancia = abs(amenaza.coordenada.x - 1) + abs(amenaza.coordenada.y - 1)

            problema = random.choice(self.__problemas)
            print(f"Amenaza detectada lv {amenaza.total_amenaza}: {problema} en la coordenada ({amenaza.coordenada.x}, {amenaza.coordenada.y})")

            print(f"Batman se ha movido {distancia} cuadrados para poder neutralizar la amenaza del sensor ({amenaza.coordenada.x}, {amenaza.coordenada.y})....")
            
            self.print_gotham()

            # Restauramos el símbolo anterior del sensor o el edificio
            self.__superficie[amenaza.coordenada.x][amenaza.coordenada.y] = simbolo_anterior
            self.__superficie[self.batman_pos.x][self.batman_pos.y] = '🦇'
            # Recalcular las amenazas después de neutralizarlas
            self.cal_amenaza()


    def agregar_sensor(self, sensor: Sensor) -> None:
        """Agrega un nuevo sensor a la superficie y recalcula las amenazas."""
        # Añadimos el sensor a la superficie
        self.__superficie[sensor.coordenada.x][sensor.coordenada.y] = sensor
        print(f"Sensor añadido en la coordenada ({sensor.coordenada.x}, {sensor.coordenada.y}) con nivel de amenaza {sensor.amenaza}.")
        # Recalculamos las amenazas después de agregar el sensor
        self.cal_amenaza()

def print_batman_day(dias_de_batman_day: list) -> None:

    for i in dias_de_batman_day:
        print(i.strftime("%A, %d de %B de %Y"))
    print("\n")


def get_batman_day(limit:int = 30)-> list:

    days = []


    today = date.today()
    for i in range(0,limit):
        year = today.year + i
        #formatear y setear al principio de mes
        primer_dia_septiembre = date(year, 9, 1)
        # primer sábado de septiembre
        primer_sabado = primer_dia_septiembre + timedelta(days= (5 - primer_dia_septiembre.weekday()) % 7)
        # sumamos dos semana para poder cuadrar las semanas
        next_batman_day = primer_sabado + timedelta(weeks=2)
        # comprobar si ya pasó el dia de batman.
        if i == 0:
            if next_batman_day.year == today.year and next_batman_day.month == today.month and next_batman_day.day== today.day:
                days.append(next_batman_day)
        else:
            days.append(next_batman_day)

    return days





if __name__ == '__main__':

    locale.setlocale(locale.LC_TIME, 'es_ES')

    # dias_de_batman_day = get_batman_day()
    # print("Las próximas fechas de los batmandays:")
    # print_batman_day(dias_de_batman_day)
    sesores = [
        Sensor(Coordenada(10,10), 2),
        Sensor(Coordenada(8,10), 10),
        Sensor(Coordenada(9,11), 8),
        Sensor(Coordenada(10,12), 6),
        Sensor(Coordenada(7,8), 3),
        Sensor(Coordenada(15,8), 10),
        Sensor(Coordenada(5,3), 5),
        Sensor(Coordenada(1,7), 9),
        Sensor(Coordenada(19,13), 1),
        Sensor(Coordenada(3, 4), 7),
        Sensor(Coordenada(12, 14), 4),
        Sensor(Coordenada(18, 6), 6),
        Sensor(Coordenada(14, 16), 9),
        Sensor(Coordenada(16, 19), 10),
        Sensor(Coordenada(13, 14), 5),
        Sensor(Coordenada(19, 19), 8),
        Sensor(Coordenada(6, 6), 10),
        Sensor(Coordenada(3, 17), 3),
        Sensor(Coordenada(13, 9), 6),
        Sensor(Coordenada(5, 5), 9),
        Sensor(Coordenada(6, 5), 10),
        Sensor(Coordenada(5, 6), 8),

    ]


    ciudad = Gotham(sensores=sesores)

    #ciudad.print_gotham()

    ciudad.cal_amenaza()
    # nuevos_sensores = [
    #     Sensor(Coordenada(15, 15), 10),
    #     Sensor(Coordenada(15, 16), 9),
    #     Sensor(Coordenada(16, 16), 8),
    #     Sensor(Coordenada(1, 1), 2),
    #     Sensor(Coordenada(3, 3), 1),
    #     Sensor(Coordenada(17, 18), 1),
    #     Sensor(Coordenada(19, 19), 1)
    # ]
    # for nuevo in nuevos_sensores:
    #     ciudad.agregar_sensor(nuevo)
    # ciudad.cal_amenaza()
