from os import system
import random,time
import calendar

print ("RETO 1")

year = ((100-85)+2024)

mes = 9

#calculamos el calendario de ese mes y mostramos el numero de semanas
lista_mes = calendar.monthcalendar(year,mes)

semana_aniversario = 3

dia_aniversario = lista_mes [semana_aniversario-1] [0]
print (f"EL 100 ANIVERSARIO SERA el {dia_aniversario}/{mes}/{year}" )

print("\nRETO 2")

import numpy as np

def procesar_sensores(sensores, umbral_activacion=20):
    # Crear una cuadrícula 20x20 inicializada en 0
    gotham = np.zeros((20, 20), dtype=int)
    
    # Poblar la cuadrícula con los niveles de amenaza de los sensores
    for x, y, amenaza in sensores:
        gotham[x, y] = amenaza
    
    # Variables para rastrear el área más crítica
    max_amenaza = 0
    coordenada_central = None
    
    # Recorrer la cuadrícula para calcular sumas en áreas 3x3
    for i in range(18):  # Hasta 18 para evitar desbordar el rango 3x3
        for j in range(18):
            suma_amenazas = gotham[i:i+3, j:j+3].sum()  # Suma en la subcuadrícula 3x3
            
            if suma_amenazas > max_amenaza:
                max_amenaza = suma_amenazas
                coordenada_central = (i+1, j+1)  # Centro de la cuadrícula 3x3
    
    # Calcular la distancia desde la Batcueva al centro de la cuadrícula más amenazada
    distancia_batcueva = abs(coordenada_central[0] - 0) + abs(coordenada_central[1] - 0)
    
    # Determinar si se activa el protocolo de seguridad
    activar_protocolo = max_amenaza >= umbral_activacion
    
    # Mostrar resultados
    print(f"Coordenada central del área más amenazada: {coordenada_central}")
    print(f"Suma de amenazas en el área: {max_amenaza}")
    print(f"Distancia a la Batcueva: {distancia_batcueva}")
    print(f"¿Activar protocolo de seguridad?: {'Sí' if activar_protocolo else 'No'}")

# Ejemplo de datos de sensores
sensores = [
    (2, 3, 5), (13, 4, 7), (5, 5, 3), (15, 10, 8), (10, 11, 17), (11, 11, 16),
    (15, 18, 9), (16, 15, 10), (15, 16, 18), (18, 18, 14)
]

# Ejecutar el programa con los datos de sensores
procesar_sensores(sensores)
