# -- exercice
import datetime


def calculate_age(birth_date: datetime, current_date: datetime) -> int:
    age: int = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
        current_date.month == birth_date.month and current_date.day < birth_date.day
    ):
        age -= 1
    return age


current_date: datetime = datetime.datetime.now()
birth_date: datetime = datetime.datetime(2002, 11, 9, 8, 20, 0)

print(f"Current date: {current_date}")
print(f"Binary date: {birth_date}")
print(f"Years: {calculate_age(birth_date, current_date)}")


# -- extra challenge
def format_date(date: datetime) -> None:
    print(f"Date: {date}")
    print(f"Date: {date.strftime('%d/%m/%Y')}")
    print(f"Date: {date.strftime('%H:%M:%S')}")
    print(f"Date: {date.strftime('%j')}")
    print(f"Date: {date.strftime('%A')}")
    print(f"Date: {date.strftime('%B')}")
    print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S %j')}")
    print(f"Date: {date.strftime('%A %B')}")
    print(f"Date: {date.strftime('%A %B %d')}")
    print(f"Date: {date.strftime('%A %B %d %H:%M:%S')}")


format_date(birth_date)
