# 19 ENUMERACIONES

"""SOLUCIÓN - PROBLEMA DÍAS DE LA SEMANA """

from enum import Enum

# Definición del Enum


class DiaSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

# Función


def nombre_dia():
    try:
        numero = int(input("Ingrese el número del día (1 al 7): "))
        dia = DiaSemana(numero)
        return dia.name.capitalize()
    except ValueError:
        return "Número de día inválido"


# Salida:
print(nombre_dia())
