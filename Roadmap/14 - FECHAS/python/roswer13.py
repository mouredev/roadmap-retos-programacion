# EJERCICIO:
# Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
# - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
# - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
# Calcula cuántos años han transcurrido entre ambas fechas.
import unittest
from datetime import datetime

def get_dates() -> tuple:
    now = datetime.now()
    birth = datetime(1993, 2, 13, 6, 36, 34)
    return now, birth

def calcuates_years_difference(now: datetime, birth: datetime) -> int:
    nowYear = now.year
    birthYear = birth.year

    if nowYear>=birthYear:
        return nowYear - birthYear
    
    return birthYear - nowYear

if __name__ == '__main__':
    now, birth = get_dates()
    print(f"Tiempo transcurrido desde el nacimiento: {calcuates_years_difference(now, birth)} años.")

# DIFICULTAD EXTRA (opcional):
# Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
# 10 maneras diferentes. Por ejemplo:
# - Día, mes y año.
# - Hora, minuto y segundo.
# - Día de año.
# - Día de la semana.
# - Nombre del mes.
def calculate_date_format(birth: datetime, format: str) -> str:
    return birth.strftime(format)

if __name__ == '__main__':
    _, birth = get_dates()
    print(f"Día, mes y año: {calculate_date_format(birth, '%d/%m/%Y')}") # 13/02/1993
    print(f"Hora, minuto y segundo: {calculate_date_format(birth, '%H:%M:%S')}") # 06:36:34
    print(f"Día de año: {calculate_date_format(birth, '%j')}") # 044
    print(f"Día de la semana: {calculate_date_format(birth, '%A')}") # Saturday
    print(f"Nombre del mes: {calculate_date_format(birth, '%B')}") # February

# TESTS

class TestDate(unittest.TestCase):
    def test_get_dates(self):
        # Arrange
        # Act
        now, birth = get_dates()
        # Assert
        self.assertTrue(type(now) == datetime)
        self.assertTrue(type(birth) == datetime)

    def test_calculates_years_difference(self):
        # Arrange
        now = datetime(2021, 6, 30, 12, 0, 0)
        birth = datetime(1993, 6, 30, 8, 0, 0)
        # Act
        result = calcuates_years_difference(now, birth)
        # Assert
        self.assertTrue(result == 28)

    def test_calculate_date_format(self):
        # Arrange
        birth = datetime(1993, 2, 13, 6, 36, 34)
        # Act
        # Assert
        self.assertTrue(calculate_date_format(birth, '%d/%m/%Y') == "13/02/1993")
        self.assertTrue(calculate_date_format(birth, '%H:%M:%S') == "06:36:34")
        self.assertTrue(calculate_date_format(birth, '%j') == "044")
        self.assertTrue(calculate_date_format(birth, '%A') == "Saturday")
        self.assertTrue(calculate_date_format(birth, '%B') == "February")

if __name__ == '__main__':
    unittest.main()