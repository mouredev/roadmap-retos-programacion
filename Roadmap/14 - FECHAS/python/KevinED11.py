from datetime import datetime
import random
import functools
from typing import Iterable, Final


def date_format(date: datetime, format: str = "%A, %d de %B de %Y - %I:%M %p") -> str:
    return f"{date:{format}}"


def date_formats(date: datetime, formats: Iterable[str]) -> list[str]:
    return [date_format(date=date, format=format) for format in formats]


def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date1 - date2).days) // 365


@functools.lru_cache(maxsize=25)
def available_date_formats() -> list[str]:
    return [
        "%Y-%m-%d",  # Año-Mes-Día
        "%d/%m/%Y",  # Día/Mes/Año
        "%B %d, %Y",  # Mes Nombre Día, Año
        "%A, %d %B %Y",  # Día de la semana, Día Mes Nombre Año
        "%Y-%m-%d %H:%M:%S",  # Año-Mes-Día Hora:Minuto:Segundo
        "%d-%m-%Y %H:%M",  # Día-Mes-Año Hora:Minuto
        "%Y/%m/%d %H:%M:%S",  # Año/Mes/Día Hora:Minuto:Segundo
        "%A, %d de %B de %Y",  # Día de la semana, Día de Mes Nombre Año
        "%d/%m/%Y %H:%M:%S",  # Día/Mes/Año Hora:Minuto:Segundo
        "%Y-%m-%d %H:%M:%S.%f",  # Año-Mes-Día Hora:Minuto:Segundo.Microsegundos
    ]


def choice_random_elements[T](elements: Iterable[T], quantity: int) -> list[T]:
    return random.sample(population=elements, k=quantity)


def display_formatted_date_in_various_ways(date: datetime, quantity: int = 10) -> None:
    MAXIMUM_ALLOWED_FORMATS: Final[int] = 10

    if quantity > MAXIMUM_ALLOWED_FORMATS:
        print("la cantidad maxima de fechas a imprimir es 10")

    quantity = min(quantity, MAXIMUM_ALLOWED_FORMATS)
    available_formats = available_date_formats()
    display_random_formats = choice_random_elements(
        elements=available_formats, quantity=quantity
    )

    final_representation = date_formats(date=date, formats=display_random_formats)

    print(*final_representation, sep="\n")


def main() -> None:
    current_date = datetime.now()
    BIRTH_DATE = datetime(
        year=2001, month=2, day=11, hour=5, minute=10, second=30, microsecond=0
    )
    print(date_format(date=current_date))
    print(date_format(date=BIRTH_DATE))
    print(calculate_year_difference(date1=current_date, date2=BIRTH_DATE))
    display_formatted_date_in_various_ways(date=BIRTH_DATE, quantity=20)


if __name__ == "__main__":
    main()
