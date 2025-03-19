import re

"""
Ejercicio
"""

def find_numbers(cadena:str)->list:
    return re.findall(r"\d+", cadena)

print(find_numbers("papa1hermano2si1no2"))
