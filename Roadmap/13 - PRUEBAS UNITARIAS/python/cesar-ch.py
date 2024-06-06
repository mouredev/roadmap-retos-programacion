import unittest
from datetime import datetime, date

"""
  #13 PRUEBAS UNITARIAS
"""


def sumar_numeros(a, b):
    return a + b


class TestSumarNumeros(unittest.TestCase):

    def test_suma_numeros(self):
        resultado = sumar_numeros(2, 3)
        self.assertEqual(resultado, 5)
        resultado2 = sumar_numeros(-2, -3)
        self.assertEqual(resultado2, -5)
        resultado3 = sumar_numeros(2, -3)
        self.assertEqual(resultado3, -1)


"""
  DIFICULTAD EXTRA
"""

personal_info = {
    "name": "cesar-ch",
    "age": 3,
    "birth_date": datetime.strptime("2021-02-03", "%Y-%m-%d").date(),
    "programming_languages": ["Javascript", "Python", "Java"],
}


class TestInformacionPersonal(unittest.TestCase):

    # Test para verificar la existencia de las claves:
    def test_claves(self):

        claves_esperadas = ["name", "age", "birth_date", "programming_languages"]
        for campo in claves_esperadas:
            self.assertIn(campo, personal_info)

    # Test para verificar la corrección de los datos (ejemplo):
    def test_datos_correctos(self):
        self.assertIsInstance(personal_info["name"], str)
        self.assertIsInstance(personal_info["age"], int)
        self.assertIsInstance(personal_info["birth_date"], date)
        self.assertIsInstance(personal_info["programming_languages"], list)


if __name__ == "__main__":
    unittest.main()
