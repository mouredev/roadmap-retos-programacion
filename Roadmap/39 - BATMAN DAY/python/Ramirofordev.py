'''
Ejercicio:

RETO 1:
Crea un programa que calcule cuando se va a celebrar el Batman Day hasta su 100 aniversario.

RETO 2:
Crea un programa que implemente el sistema de seguridad de la Baticueva.

Este sistema esta diseñado para monitorear mutiples sensores distribuidos por Gotham, detectar instrusos y activar respuestas automatizadas.

Cada sensor reporta su estado en tiempo real, y Batman necesita un programa que procese estos datos para tomar decisiones estatregicas.

Requitistos:
    1. El mapa de Gotham y los sensores se representa con una cuadricula 20x20.
    2. Cada sensor se identifica con una coordenada (x, y) y un nivel de amenaza entre 0 a 10 (numero entero).
    3. Batman debe concentrar recursos en el area mas critica de Gotham.
    4. El programa recibe un listado de tuplas representando coordenadas de los sensores y su nivel de amenaza. El umbral de activacion del protocolo de seguridad es 20 (sumatorio de amenazas en una cuadricula 3x3).

Acciones:
    1. Identifica el area con mayor concentracion de amenazas (sumatorio de amenazas en una cuadricula 3x3).
    2. Si el sumatorio de amenazas es mayor al umbral, activa el protocolo de seguridad.
    3. Calcula la distancia desde la Baticueva, situada en (0, 0). La distancia es la suma absoluta de las coordenadas al centro de la cuadricula amenazada.
    4. Muestra la coordenada al centro de la cuadricula mas amenazada, la suma de sus amenazas, la distancia a la Baticueva y si debe activar el protocolo de seguridad.
'''

# Reto 1

import calendar

# La primera celebracion del Batman Day fue en el año 2014 y fue la 75
aniversario = 75
year = 2014

while aniversario  <= 100:
    mes = calendar.monthcalendar(year, 9)
    sabados = []

    for semana in mes:
        if semana[5] != 0:
            sabados.append(semana[5])

    print(f"El Batman Day de {year} se realizo el {sabados[2]}.")
    aniversario += 1
    year += 1


# Reto 2

gotham = [[0] * 20 for _ in range(20)]
print(gotham)

def colocar_sensores(sensores):
    for x, y, nivel in sensores:
        fila = x
        columna = y
        n = nivel

        # Agregamos el sensor a gotham
        gotham[fila][columna] = n
    
    

def danger_zones():

    centro_max = None
    suma_maxima = 0

    for filas in range(1, 19):
        for columnas in range(1, 19):
            # Aqui fila y columnas sera el centro de un cuadrado 3x3
            suma = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    suma += gotham[filas + dx][columnas + dy]

            if suma > suma_maxima:
                suma_maxima = suma
                centro_max = (filas, columnas)

     # obtenemos al distancia sumando las diferencias absolutas de las cooredenadas
    distancia = abs(centro_max[0] - 0) + abs(centro_max[1] - 0)

    return distancia, suma_maxima, centro_max

def activar_protocolo(d, y, centro):
    print(f"Zona de mayor amenaza: {centro}")
    print(f"Suma de amenazas: {y}")
    print(f"Distancia desde la Baticueva {d}")


    if y > 20:
        print(f"Activando protocolo de seguridad, Batman! Estas a {d} de la zona de peligro.")
        print(gotham)

# Codigo de prueba

sensores = [(5, 5, 8), (6, 6, 7), (10, 10, 5)]
colocar_sensores(sensores)

distancia, suma, centro_max = danger_zones()
activar_protocolo(distancia, suma, centro_max)