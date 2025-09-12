"""
Ejercicio
"""
import unittest


def my_sum(a: int, b: int) -> int:
    return a + b


class TestSumFunction(unittest.TestCase):
    def test_sum_two_positives(self):
        self.assertEqual(my_sum(3, 2), 5, "Should be 5")

    def test_sum_two_negatives(self):
        self.assertEqual(my_sum(-1, -1), -2, "Should be -2")

    def test_sum_positive_and_negative(self):
        self.assertEqual(my_sum(-5, 5), 0, "Should be 0")

    def test_sum_with_zero(self):
        self.assertEqual(my_sum(0, 5), 5, "Should be 5")
        self.assertEqual(my_sum(0, -5), -5, "Should be -5")


"""
Extra
"""


# Define el diccionario con los datos personales
personal_info = {
    "name": "John",
    "age": "35",
    "birth_date": "20/05/1990",
    "programming_languages": ["Python", "Clipper 5.2"]
}


# Clase para los tests unitarios
class TestPersonalInfo(unittest.TestCase):
    # Test para verificar la existencia de todos los campos
    def test_fields_existence(self):
        self.assertIn("name", personal_info)
        self.assertIn("age", personal_info)
        self.assertIn("birth_date", personal_info)
        self.assertIn("programming_languages", personal_info)

    # Test para verificar que los datos son correctos
    def test_data_correctness(self):
        self.assertEqual(personal_info["name"], "John")
        self.assertEqual(personal_info["age"], "35")
        self.assertEqual(personal_info["birth_date"], "20/05/1990")
        self.assertListEqual(personal_info["programming_languages"], ["Python", "Clipper 5.2"])


# Ejecutar los tests si se ejecuta el script directamente
if __name__ == "__main__":
    unittest.main()
