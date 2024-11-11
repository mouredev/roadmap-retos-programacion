import os, platform
from random import randint
from datetime import date 
if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" * EJERCICIO:
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
 *   protocolo de seguridad."""

#### RETO 1 ####
batman_day_2024 = '{} / {} / {}'.format(date(2024,9,21).day, date(2024,9,21).month, date(2024,9,21).year)
print(f"El Batman Day de 2024 se celebró el {batman_day_2024} , este evento se celebra cada 3º Sábado de Septiembre,")
print("este año 2024 se celebra el 85º aniversario, estas serán las próximas fechas en las que se celebre este evento ")
print("hasta llegar al centenario que será en 2039:")
for year in range(2025, 2040):
    week:int = 0
    batman_day = date(year, 9, 1)
    for day in range(1, 31):
        batman_day = date(year, 9, day)
        if batman_day.weekday() == 5:
            week += 1
            if week == 3:
                print('{} / {} / {}'.format(batman_day.day, batman_day.month, batman_day.year))

#### RETO 2 ####
sensor1, sensor2, sensor3, sensor4 = (5, 5), (5, 16), (16, 5), (16, 16)

def create_map(map:list)->list:
    map, batcave, sensor  = [], '▓', '⌺'
    for i in range(20):
        map.append([])
        for j in range(20): 
            if i == 0 and j == 0:
                map[i].append(batcave)
            elif (i == sensor1[0]-1 and j == sensor1[1]-1 ) or (i == sensor2[0]-1 and j == sensor2[1]-1):
                map[i].append(sensor)
            elif (i == sensor3[0]-1 and j == sensor3[1]-1) or (i == sensor4[0]-1 and j == sensor4[1]-1):
                map[i].append(sensor)
            else:
                map[i].append(randint(0,9))
    return map

gotham_map = create_map(map)

def print_map(map:list):
    print("\n--------------------  MAPA DE GOTHAM  --------------------")
    for row in map:
        print()
        for column in row:
            print('{:<2}'.format(column), end=' ')
    print("\n")

def threat_level(map:list)->tuple:
    threat, threat_area = 0, []
    for i , row in enumerate(map):
        for j, column in enumerate(row):
            if column == '⌺':
                threat = sum([map[i-1][j-1], map[i-1][j],
                              map[i-1][j+1], map[i][j-1],                             
                              map[i][j+1], map[i+1][j-1],                            
                              map[i+1][j], map[i+1][j+1]])                                                
                threat_area.append(threat)        
    return tuple(threat_area)

def max_threat(threats:tuple)->tuple:
    hight_threat = max(threats)
    hight_index = threats.index(hight_threat) + 1
    return hight_index, hight_threat

def create_report(s1:tuple,s2:tuple,s3:tuple,s4:tuple)->list:
    report_list = []
    sensor1 = threat_level(gotham_map)[0], s1
    sensor2 = threat_level(gotham_map)[1], s2
    sensor3 = threat_level(gotham_map)[2], s3
    sensor4 = threat_level(gotham_map)[3], s4
    report_list.append(sensor1)
    report_list.append(sensor2)
    report_list.append(sensor3)
    report_list.append(sensor4)
    return report_list

def print_report(report:list):
    print_map(gotham_map)
    [print(f"Nivel de amenaza del sensor {i} : {threat_level(gotham_map)[i-1]}") for i in range(1,5)]     
    index, threat = max_threat(threat_level(gotham_map))
    print(f"\nNivel de la amenaza máxima: {threat} y sus coordenadas son: x={report[index-1][1][0]} y={report[index-1][1][1]}")
    print(f"\nEl sensor {index} está en la zona más amenazada y la distancia desde la batcueva es de {report[index-1][1][0] + report[index-1][1][1]}")
    if threat>20:
        print("\nLa zona más amenazada supera el umbral del protocolo de seguridad de 20")
        print("\n¡¡ACTIVAR PROTOCOLO DE SEGURIDAD!! ")

print_report(create_report(sensor1, sensor2, sensor3, sensor4))
















               
#print('◈') # █ ▓ ■ ░ ▒ ╬ ⌧ ⌺ ↂ ◈ 〓 ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⑩ Ⓑ ☠ ⚫ ◯ 𝐁 ❶ ⑴ 𝐀

#web special chars: https://www.caracteresespeciales.com/n%C3%BAmero-caracteres-especiales.html