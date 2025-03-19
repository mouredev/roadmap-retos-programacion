import unittest
from datetime import date, datetime

# Ejercicio


def sum(a: float, b: float):
    if not isinstance(a, (float)) or not isinstance(b, (float)):
        raise ValueError("Los argumentos deben ser decimales.")
    return a + b


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(3.7686, 9.10866), 12.87726)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("3.767", 3.0)
        with self.assertRaises(ValueError):
            sum(6.456, "1.23")
        with self.assertRaises(ValueError):
            sum("2.894", "5.369")
        with self.assertRaises(ValueError):
            sum("a", 3.657)
        with self.assertRaises(ValueError):
            sum(None, 2.879)


# Dificultad extra (opcional)


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        self.professional_data = {
            "name": "Miguel Angel López Monroy",
            "age": 51,
            "birth_date": datetime.strptime("28-09-1972", "%d-%m-%Y").date(),
            "programming_languages": ["Python", "JavaScript", "C"],
        }

    def test_fields_exist(self):
        self.assertIn("name", self.professional_data)
        self.assertIn("age", self.professional_data)
        self.assertIn("birth_date", self.professional_data)
        self.assertIn("programming_languages", self.professional_data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.professional_data["name"], str)
        self.assertIsInstance(self.professional_data["age"], int)
        self.assertIsInstance(self.professional_data["birth_date"], date)
        self.assertIsInstance(self.professional_data["programming_languages"], list)


if __name__ == "__main__":
    unittest.main()
