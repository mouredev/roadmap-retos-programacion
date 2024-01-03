# Script para calcular el % de uso de cada lenguaje

import os
import operator
import re

CHALLENGE_PATTERN = r'^\d{2} - '


def scan_dir(dir_path, challenges={}, languages={}, total=0, challenge_name=None, path_name=None) -> tuple:
    for path in os.scandir(dir_path):
        if path.is_dir():

            match = re.match(CHALLENGE_PATTERN, path.name)

            if match and path.name not in challenges:
                challenges[path.name] = 0
                challenge_name = path.name
            elif not match and path.name not in languages:
                languages[path.name] = 0

            _, _, total = scan_dir(
                path.path, challenges,
                languages, total, challenge_name, path.name)
        else:
            if path_name in languages:
                total += 1
                if challenge_name is not None:
                    challenges[challenge_name] += 1
                languages[path_name] += 1

    return (challenges, languages, total)


# Directorio de retos a analizar
dir_path = os.path.dirname(__file__)

# Directorio de un reto específico
# dir_path += "/00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO"

# Función recursiva para recorrer el directorio y almacenar el número de archivos por reto y lenguaje
challenges, languajes, total = scan_dir(dir_path)

# Ordenación por uso
challenges = dict(
    sorted(challenges.items(), key=operator.itemgetter(1), reverse=True))
languajes = dict(
    sorted(languajes.items(), key=operator.itemgetter(1), reverse=True))

# Estadísticas
print(
    f"\nESTADÍSTICAS ROADMAP RETOS DE PROGRAMACIÓN:\n> {len(languajes.keys())} LENGUAJES ({total} CORRECCIONES)")
for challenge in challenges:
    print(
        f"> {challenge.upper()} ({challenges[challenge]}): {round(challenges[challenge] / total * 100, 2)}%")
print()
for languaje in languajes:
    print(
        f"> {languaje.upper()} ({languajes[languaje]}): {round(languajes[languaje] / total * 100, 2)}%")
