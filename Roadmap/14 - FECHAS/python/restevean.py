"""
Ejercicio
"""
from datetime import datetime

current_date = datetime.now()
birthdate = datetime(1990, 4, 15, 0, 0, 0)


def calculate_age(current, birth):
    age = current.year - birth.year - ((current.month, current.day) < (birth.month, birth.day))
    return age


"""
Extra
"""
formats = {
    "1. Día, mes y año": birthdate.strftime("%d/%m/%Y"),
    "2. Hora, minuto y segundo": birthdate.strftime("%H:%M:%S"),
    "3. Día del año": birthdate.strftime("%j"),
    "4. Día de la semana": birthdate.strftime("%A"),
    "5. Nombre del mes": birthdate.strftime("%B"),
    "6. Fecha en formato ISO": birthdate.isoformat(),
    "7. Fecha larga con nombre del día": birthdate.strftime("%A, %d de %B de %Y"),
    "8. Fecha corta": birthdate.strftime("%d/%m/%y"),
    "9. Fecha con nombre del mes y día de la semana": birthdate.strftime("%A, %d de %B"),
    "10. Tiempo UNIX": int(birthdate.timestamp())
}


if __name__ == "__main__":
    print( "La edad es:", calculate_age(current_date, birthdate))
    for name, format_example in formats.items():
        print(f"{name}: {format_example}")

