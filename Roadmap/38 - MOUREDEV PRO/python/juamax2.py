import os
import csv
import random

def read_csv() -> list:
    
    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_dir}/subs.csv"
    
    data = []
    
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row["status"] == "Activo":
                data.append(row)
    return data

def seleccionar_ganadores(data):
    
    if len(data) < 3:
        raise ValueError("El número de elementos debe ser mínimo 3.")
    return random.sample(data, 3)
    

def mostrar_ganadores(winners):
    premios = ["Suscripción", "Descuento", "Libro"]
    for winner, premio in zip(winners, premios):
        print(f"{winner["email"]} ID: {winner["id"]}. Premio: {premio}")
    
try:   
    data = read_csv()
    winners = seleccionar_ganadores(data)
    mostrar_ganadores(winners)
except Exception as e:
    print({e})