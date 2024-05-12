from enum import Enum

"""
    EJERCICIO:
"""

# Enumeración de los días de la semana
class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def dia_semana(numero):
    if numero < 1 or numero > 7:
        return "Día no válido"
    return DiaSemana(numero).name

print(f"Dia 1 : {dia_semana(1)} ") # LUNES
print(f"Dia 7 : {dia_semana(7)} ") # DOMINGO
print(f"Dia 8 : {dia_semana(8)} ") # Día no válido
print(f"Dia 0 : {dia_semana(0)} ") # Día no válido
