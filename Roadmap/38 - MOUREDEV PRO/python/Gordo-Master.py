# 38 - Mouredev pro
import os
import csv
import random


def read_csv() -> list:
    # Variable que almacena los datos del csv
    data = []
    # Variable que almacena los valores que estan activos
    active_list = list()

    # Obtener la ruta
    file_dir = os.path.dirname(os.path.abspath(__file__))
    file_dir += "\\lista.csv"

    # Trabajando con el archivo csv
    with open(file=file_dir,encoding="utf-8", mode= "r") as archivo:
        data = csv.reader(archivo)

        # Tomando solo los valores que son activos
        for fila in data:
            if fila[2] == "activo":
                active_list.append(fila)

    return active_list    

def select_winners(active_list: list) -> list:
    if len(active_list) < 3:
        raise ValueError("El numero de elementos debe ser mínimo 3.")
    # Crea una lista con 3 secciones aleatorias (toma el nombre como referencia). Sample que no toma repetidos
    winners = random.sample([element[1] for element in active_list],3)
    # Crea la nueva lista usando los resultados de winners como referencia
    winners_list = [element for element in active_list if element[1] in winners]
    # Reordena todos los valores
    random.shuffle(winners_list)
    return winners_list

def display_winners(winners_list):
    # Imprimir los ganadores
    print("Ganadores del concurso:")
    print()
    print(f"1er premio: Una suscripción a MouredevPro!!!") 
    print(f"Ganador: {winners_list[0][1]} (ID: {winners_list[0][0]})") 
    print()
    print(f"2do premio: Una descuento a MouredevPro!!!") 
    print(f"Ganador: {winners_list[1][1]} (ID: {winners_list[1][0]})")
    print()
    print(f"3er premio: Una libro!!!") 
    print(f"Ganador: {winners_list[2][1]} (ID: {winners_list[2][0]})") 

try:
    data = read_csv()
    winners = select_winners(data)
    display_winners(winners)
except Exception as e:
    print(e)