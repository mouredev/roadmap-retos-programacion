import datetime

# Ejercicio
current_date = datetime.datetime.now()
birth_date = datetime.datetime(1972, 9, 28, 10, 20, 0)


def calculate_age(birth_date: datetime, current_date: datetime) -> int:
    age: int = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
        current_date.month == birth_date.month and current_date.day < birth_date.day
    ):
        age -= 1
    return age


# Dificultad Extra
# mostrar de 10 maneras distintas
def show_formats_of_birth_date() -> None:
    print(birth_date.strftime("%d/%m/%Y, %H:%M:%S"))
    print(birth_date.strftime("%a-%b-%Y"))
    print(birth_date.strftime("%A, %d of %B %Y"))
    print(birth_date.strftime("%-d/%-m/%y, %I:%-M:%-S %p"))
    print(birth_date.strftime("%-H %p, %Y/%B/%d"))
    print(birth_date.strftime("%A, %-d of %B %Y"))
    print(birth_date.strftime("%-H %p - %B %A %Y"))
    print(birth_date.strftime("%b/%d/%Y"))
    print(birth_date.strftime("%m.%d.%y"))
    print(birth_date.strftime("%A, %y.%m.%d ; %H:%M:%S"))


if __name__ == "__main__":
    print(f"Current date: {current_date}")
    print(f"Binary date: {birth_date}")
    print(f"Years: {calculate_age(birth_date, current_date)}")

    print("Muestra mi fecha de nacimiento de 10 maneras distintas")
    show_formats_of_birth_date()
