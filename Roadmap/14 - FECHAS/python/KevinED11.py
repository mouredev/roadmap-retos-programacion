from datetime import datetime
import random
import functools
from typing import Iterable, Final


def format_date(date: datetime) -> str:
    return f"{date:%A, %d de %B de %Y - %I:%M %p}"


def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date1 - date2).days) // 365


@functools.lru_cache
def date_formats(date: datetime) -> list[str]:
    return [
        f"{date:%Y-%m-%d}",  # Año-Mes-Día
        f"{date:%d/%m/%Y}",  # Día/Mes/Año
        f"{date:%B %d, %Y}",  # Mes Nombre Día, Año
        f"{date:%A, %d %B %Y}",  # Día de la semana, Día Mes Nombre Año
        f"{date:%Y-%m-%d %H:%M:%S}",  # Año-Mes-Día Hora:Minuto:Segundo
        f"{date:%d-%m-%Y %H:%M}",  # Día-Mes-Año Hora:Minuto
        f"{date:%Y/%m/%d %H:%M:%S}",  # Año/Mes/Día Hora:Minuto:Segundo
        f"{date:%A, %d de %B de %Y}",  # Día de la semana, Día de Mes Nombre Año
        f"{date:%d/%m/%Y %H:%M:%S}",  # Día/Mes/Año Hora:Minuto:Segundo
        f"{date:%Y-%m-%d %H:%M:%S.%f}",  # Año-Mes-Día Hora:Minuto:Segundo.Microsegundos
    ]


def choice_random_elements[T](elements: Iterable[T], quantity: int) -> list[T]:
    return random.sample(population=elements, k=quantity)


def display_formatted_date_in_various_ways(date: datetime, quantity: int = 10) -> None:
    MAXIMUM_ALLOWED_FORMATS: Final = 10

    if quantity > MAXIMUM_ALLOWED_FORMATS:
        print("la cantidad maxima de fechas a imprimir es 10")

    quantity = min(quantity, MAXIMUM_ALLOWED_FORMATS)
    available_formats = date_formats(date=date)
    display_random_formats = choice_random_elements(
        elements=available_formats, quantity=quantity
    )

    print(*display_random_formats, sep="\n")


def main() -> None:
    current_date = datetime.now()
    BIRTH_DATE = datetime(
        year=2001, month=2, day=11, hour=5, minute=10, second=30, microsecond=0
    )

    print(format_date(date=current_date))
    print(format_date(date=BIRTH_DATE))
    print(calculate_year_difference(date1=current_date, date2=BIRTH_DATE))
    display_formatted_date_in_various_ways(date=BIRTH_DATE, quantity=20)


if __name__ == "__main__":
    main()
