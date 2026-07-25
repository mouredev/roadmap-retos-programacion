import csv
import random
import sys
from pathlib import Path

PRIZES = ["suscripción", "descuento", "libro"]
CSV_PATH = Path("~/Descargas/participants.csv").expanduser()


def load_participants(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(
            f, fieldnames=["id", "email", "estado"], skipinitialspace=True
        )
        return list(reader)


def select_winners(participants):
    active = [p for p in participants if p["estado"].strip().lower() == "activo"]
    if len(active) < len(PRIZES):
        raise ValueError(
            f"Se necesitan ≥{len(PRIZES)} activos, solo hay {len(active)}."
        )
    winners = random.sample(active, k=len(PRIZES))
    return {prize: winner for prize, winner in zip(PRIZES, winners)}


def display_results(prize_map):
    print(f"\n{'Premio':<15} {'ID':<6} {'Email'}")

    for prize, p in prize_map.items():
        print(f"{prize:<15} {p['id']:<6} {p['email']}")


if not CSV_PATH.is_file():
    print(f"[ERROR] No se encontró el archivo: {CSV_PATH}")
    sys.exit(1)

participants = load_participants(CSV_PATH)

try:
    prize_map = select_winners(participants)
except ValueError as e:
    print(f"[ERROR] {e}")
    sys.exit(1)

display_results(prize_map)
