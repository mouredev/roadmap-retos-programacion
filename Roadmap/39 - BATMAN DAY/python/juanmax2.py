"""
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
 * su 100 aniversario.
"""

from datetime import datetime, timedelta ,time

año_creacion = 1939

año_aniversario = año_creacion + 86

dia_aniversario_fechas = []

while año_aniversario <= año_creacion + 100:
    
    septiembre = datetime(año_aniversario, 9, 1)
    
    primer_sabado = 5 - septiembre.weekday() if septiembre.weekday() <= 5 else 12 - septiembre.weekday()
    
    tercer_sabado = septiembre + timedelta(days=primer_sabado + 14)
    
    
    dia_aniversario_fechas.append(
        (
            año_aniversario,
            año_aniversario - año_creacion,
            tercer_sabado.strftime("%d-%m-%Y")
        )
        
    )
    año_aniversario += 1
for year, aniversario, batman_day in dia_aniversario_fechas:
    print(f"Batman day {year} ({aniversario} aniversario): {batman_day}")
    


"""
Reto 2 - Sistema seguridad batcueva

"""

def sum_subgrid(sensores, x, y):
    
    total = 0
    
    for x in range(x - 1, x + 2):
        for y in range(y - 1, y + 2):
            for sensor in sensores:
                if sensor[0] == x and sensor[1] == y:
                    total += sensor[2]
    return total

def sistema_seguridad(sensores):
    
    mayor_nivel_alerta = 0
    mayor_alerta_cordenada = (0, 0)
    
    for x in range(1, 19):
        for y in range(1, 19):
            nivel_alerta = sum_subgrid(sensores, x, y)
            if nivel_alerta > mayor_nivel_alerta:
                mayor_nivel_alerta = nivel_alerta
                mayor_alerta_cordenada = (x, y)
    activar_protocolo = mayor_nivel_alerta > 20
    distancia = abs(mayor_alerta_cordenada[0]) + abs(mayor_alerta_cordenada[1])
    return mayor_nivel_alerta, mayor_alerta_cordenada, activar_protocolo, distancia
                


sensores = [
    (2, 3, 6),
    (4, 3, 5),
    (2, 2, 7),
    (10, 12, 8),
    (15, 16, 4),
    (14, 16, 6),
    (2, 4, 10)
]

resultado = sistema_seguridad(sensores)
print(f"Maximo nivel de alaerta: {resultado[0]}")
print(f"Cordenadas de la alerta: {resultado[1]}")
print(f"Activar protocolo: {resultado[2]}")
print(f"Distancia hasta las cordenadas: {resultado[3]}")