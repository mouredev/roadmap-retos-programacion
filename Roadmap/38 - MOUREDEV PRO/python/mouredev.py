import os
import csv
import random


def read_csv_data() -> list:

    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = f"{file_dir}/subs.csv"

    data = []

    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "activo":
                data.append(row)

    return data


def select_winners(data: list) -> list:

    if len(data) < 3:
        raise ValueError("El número de elementos debe ser mínimo 3.")

    return random.sample(data, 3)


def display_winners(winners):
    prizes = ["Suscripción", "Descuento", "Libro"]
    for winner, prize in zip(winners, prizes):
        print(f"{prize}: {winner["email"]} (ID: {winner["id"]})")


try:
    data = read_csv_data()
    winners = select_winners(data)
    display_winners(winners)
except Exception as e:
    print(e)
