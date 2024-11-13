import datetime
import random

# RETO 1: Cálculo de Batman Day hasta su 100 aniversario
def calcular_batman_day(anio_inicio, anio_final):
    print("Fechas del Batman Day hasta su 100 aniversario:")
    for anio in range(anio_inicio, anio_final + 1):
        tercer_sabado = datetime.datetime(anio, 9, 1) + datetime.timedelta((5 - datetime.datetime(anio, 9, 1).weekday()) % 7 + 14)
        print(f"Batman Day en el año {anio}: {tercer_sabado.strftime('%d-%m-%Y')}")

# RETO 2: Sistema de seguridad de la Batcueva
def activar_sistema_seguridad(sensores):
    tamano_mapa = 20
    umbral_seguridad = 20
    mejor_suma_amenazas = 0
    mejor_centro = None

    for i in range(tamano_mapa - 2):
        for j in range(tamano_mapa - 2):
            suma_amenazas = sum(sensores[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
            if suma_amenazas > mejor_suma_amenazas:
                mejor_suma_amenazas = suma_amenazas
                mejor_centro = (i + 1, j + 1)

    if mejor_centro:
        distancia_batcueva = abs(mejor_centro[0]) + abs(mejor_centro[1])
        print(f"\nÁrea más amenazada en coordenadas {mejor_centro}")
        print(f"Suma de amenazas: {mejor_suma_amenazas}")
        print(f"Distancia a la Batcueva: {distancia_batcueva}")

        if mejor_suma_amenazas > umbral_seguridad:
            print("¡Protocolo de seguridad activado!")
        else:
            print("Protocolo de seguridad NO activado.")

# Ejecutar el reto 1
anio_inicio = 2024
anio_final = 2024 + (100 - 85)
calcular_batman_day(anio_inicio, anio_final)

# Ejecutar el reto 2
sensores = [[random.randint(0, 10) for _ in range(20)] for _ in range(20)]
activar_sistema_seguridad(sensores)
